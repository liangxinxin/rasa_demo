# coding:utf-8
# @Time    : 2021/7/21 6:31 下午
# @Author  : liangxinxin
# @Email  : liangxinxina@enn.cn
import os
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
base = '/Users/liangxinxin/Documents/projects/Rasa/rasa_demo'
class MyKnowledgeBaseAction(ActionQueryKnowledgeBase):
    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase(os.path.join(base,"knowledge_base/knowledge_base_data.json"))
        super().__init__(knowledge_base)