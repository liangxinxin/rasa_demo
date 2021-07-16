# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from api.weather import Weather
from knowledge_base.neo4j import Neo4jGraphDatabase
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase


#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
class WeatherForm(Action):

    def name(self) -> Text:
        return "action_submit_weather_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: "DomainDict") -> List[Dict[Text, Any]]:
        slots = tracker.current_slot_values()
        city = slots.get("city")
        date_time = slots.get("date_time")
        text = Weather()(city, date_time)

        dispatcher.utter_message(text)

        return [AllSlotsReset]  # 设置此次对话结


class AskSymptomAction(ActionQueryKnowledgeBase):

    def name(self) -> Text:
        return "ask_symptom_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: "DomainDict"):
        slots = tracker.current_slot_values()
        disease = slots.get('disease')
        text = Neo4jGraphDatabase.query_symptom(disease)
        dispatcher.utter_message(text)
        return [AllSlotsReset]  # 设置此次对话结


class AskDrugAction(ActionQueryKnowledgeBase):

    def name(self) -> Text:
        return "ask_drug_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: "DomainDict"):
        slots = tracker.current_slot_values()
        disease = slots.get('disease')
        text = Neo4jGraphDatabase.query_drug(disease)
        dispatcher.utter_message(text)
        return [AllSlotsReset]  # 设置此次对话结


class AskComplicationAction(ActionQueryKnowledgeBase):

    def name(self) -> Text:
        return "ask_complication_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: "DomainDict"):
        slots = tracker.current_slot_values()
        disease = slots.get('disease')
        text = Neo4jGraphDatabase.query_complication(disease)
        dispatcher.utter_message(text)
        return [AllSlotsReset]  # 设置此次对话结
