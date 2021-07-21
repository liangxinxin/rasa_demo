# coding:utf-8
# @Time    : 2021/7/21 2:57 下午
# @Author  : liangxinxin
# @Email  : liangxinxina@enn.cn

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from knowledge_base.neo4j import Neo4jGraphDatabase
from rasa_sdk.events import AllSlotsReset


class AskSymptomAction(Action):

    def name(self) -> Text:
            return "action_kbqa_submit_symptom"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: "DomainDict"):
        slots = tracker.current_slot_values()
        disease = slots.get('disease')
        print("AskSymptomAction", disease)
        sql = Neo4jGraphDatabase.symptom_sql(disease)
        text = ','.join(Neo4jGraphDatabase.query(sql)['res'])
        print("action_submit_symptom:", text)
        if text:
            dispatcher.utter_message(response="utter_symptom",disease=disease, symptoms=text)
        else:
            dispatcher.utter_message(response="utter_not_find")
        return [AllSlotsReset()]  # 设置此次对话结，清空槽位


class AskDrugAction(Action):

    def name(self) -> Text:
        return "action_kbqa_submit_drug"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: "DomainDict"):
        slots = tracker.current_slot_values()
        disease = slots.get('disease')

        sql = Neo4jGraphDatabase.drug_sql(disease)
        text = ','.join(Neo4jGraphDatabase.query(sql)['res'])
        print("AskDrugAction:", text)
        if text:
            dispatcher.utter_message(response="utter_drug",disease=disease, drugs=text)
        else:
            dispatcher.utter_message(response="utter_not_find")
        return [AllSlotsReset()]  # 设置此次对话结


class AskComplicationAction(Action):

    def name(self) -> Text:
        return "action_kbqa_submit_complication"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: "DomainDict"):
        slots = tracker.current_slot_values()
        disease = slots.get('disease')
        sql = Neo4jGraphDatabase.complication_sql(disease)
        text = ','.join(Neo4jGraphDatabase.query(sql)['res'])
        print(sql)
        print("AskComplicationAction:", text)
        dispatcher.utter_message(text)
        return [AllSlotsReset()]  # 设置此次对话结

class AskCureAction(Action):

    def name(self) -> Text:
        return "action_kbqa_submit_cure"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: "DomainDict"):
        slots = tracker.current_slot_values()
        disease = slots.get('disease')
        sql = Neo4jGraphDatabase.query_attribute(disease)
        print(sql)
        text = ','.join(Neo4jGraphDatabase.query(sql)['res'])
        if text:
            dispatcher.utter_message(text)
        else:
            dispatcher.utter_message(response="utter_not_find")
        return [AllSlotsReset()]  # 设置此次对话结

class AskCheckAction(Action):

    def name(self) -> Text:
        return "action_kbqa_submit_check"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: "DomainDict"):
        slots = tracker.current_slot_values()
        disease = slots.get('disease')
        sql = Neo4jGraphDatabase.check_sql(disease)
        print(sql)
        text = ','.join(Neo4jGraphDatabase.query(sql)['res'])
        if text:
            dispatcher.utter_message(response="utter_not_find")
        else:
            dispatcher.utter_message(text)
        return [AllSlotsReset()]  # 设置此次对话结

class AskCauseAction(Action):

    def name(self) -> Text:
        return "action_kbqa_submit_cause"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: "DomainDict"):
        slots = tracker.current_slot_values()
        disease = slots.get('disease')
        sql = Neo4jGraphDatabase.query_attribute(disease,"cause")
        print(sql)
        text = Neo4jGraphDatabase.query(sql)['attribute']
        if text:
            dispatcher.utter_message(text)
        else:
            dispatcher.utter_message(response="utter_not_find")
        print("AskCauseAction:",text)

        return [AllSlotsReset()]  # 设置此次对话结
