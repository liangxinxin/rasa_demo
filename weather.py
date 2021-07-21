"""
@Time    : 2020/7/2 5:38 下午
@Author  : Haibei
@Site: http://www.haibei.online
@Software: PyCharm
@File: weather.py
@Describe:
"""
import typing
import requests
from pypinyin import lazy_pinyin
from xml.etree import ElementTree as ET
import json
import os
from knowledge_base.neo4j import  Neo4j
neo4j = Neo4j()



class Weather(object):
    url = 'http://flash.weather.com.cn/wmaps/xml/{0}.xml'

    def __init__(self):
        self._city_list = []
        print(os.getcwd())
        with open("api/address.json", "r", encoding="utf-8") as file:
            self.city_mapping = json.load(file)

    def list_city(self, city):
        """
        返回城市包含区的列表
        :param city: 城市名称
        :return:
        """
        return [i.attrib['cityname'] for i in self._analysis(city)]

    def _analysis(self, city):
        """
        xml解析
        :param city:
        :return:
        """
        city = "".join(lazy_pinyin(city))
        xml = self.request(city)
        return ET.fromstring(xml)

    def say(self, city: typing.Union[tuple, list, dict]):
        """
        格式化请求结果
        :param city: {城市名称:地区名称}
        :return:
        """
        if isinstance(city, dict):
            city = list(city.items())[0]
        elif isinstance(city, (tuple, list)):
            pass
        else:
            raise AttributeError("格式有误，请传入tuple, list, dict")
        c, p = city
        root = self._analysis(c)
        info = None
        province = []
        for i in root:
            province.append(i.attrib['cityname'])
            if i.attrib['cityname'] == p:
                info = i.attrib
        print(province)
        if info is None:
            return None
        return info

    def request(self, city):
        url = self.url.format(city)
        r = requests.get(url)
        r.encoding = 'utf-8'
        return r.text

    def test(self):
        """测试脚本"""
        city_list = [['沈阳', '沈阳市'], ('北京', '大兴'), {"辽宁": "鞍山"}]
        for i in city_list:
            result = self.say(i)
            print(result)

    def __call__(self, address: str, date_time: str = "今天"):
        '''
        __call__ 使得实例对象变成可调用的对象，Weather(address,date_time)
        :param address:
        :param date_time:
        :return:
        '''
        print("查询信息：", address, date_time)
        if address in ["北京", "天津", "上海"]:
            province, address = address, "市中心"
            address_name = province
        elif address not in self.city_mapping:
            print(f"{address}不是城市名称。")
            return None
        else:
            province = self.city_mapping[address]
            print(province, address)
            address_name = address
        info = self.say({province: address})
        return f"{date_time}{address_name}地区{info['stateDetailed']}，{info['windState']}。\n" \
               f"最高气温{info['tem1']}℃，最低气温{info['tem2']}℃。\n" \
               f"当前气温{info['temNow']}℃，湿度{info['humidity']}。"
