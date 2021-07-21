##
```
actions.py，用来自定义actions的文件
config.yml *，NLU和Core模型的配置文件
credentials.yml，用来连接到其他服务(services)
data/nlu.md *，用于NLU训练的数据
data/stories.md *，用于训练Core模型的故事数据集
domain.yml *，assistant的领域（assistant's domain）配置文件
endpoints.yml，连接到类似于Facebook的messenger的详细配置(即可以配置到其他类似Facebook的平台)
models/.tar.gz，初始化模型
stories.yml:表示用户和AI助手之间的对话，用户输入被表示成意图(和实体)，助手响应和动作被表示成action name
```
```
1.自定义action
    需要在endpoints.yml中设置 url

2.命令
    rasa train
    #启动自定义action
    rasa run actions 
    rasa shell

```

```
 pip install transformers

LanguageModelTokenizer 不支持中文  ==>JiebaTokenizer

```
```
交互式学习
python3 -m rasa interactive -m models/20201127-144757.tar.gz --endpoints endpoints.yml --config config.yml
```

```
任务一：天气助手
1.nlu 中定义好 intent examples,具体见文件
2.domain文件： 中定义好intents,entities,slots,responses 中utter_ask_city，utter_ask_date_time :ask后面的词语solt里面的名称对应
    forms 中定义表单，必须的槽位值
3.stories文件中：定义故事,激活表单，会自动进入表单检查槽位是否被填充，如果没有，会发出utter_ask_city 或 utter_ask_date_time消息
任务二：问诊助手
```
```
stories 可视化
rasa visualize
```
