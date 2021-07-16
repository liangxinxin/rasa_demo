# coding:utf-8
# @Time    : 2021/7/15 4:52 下午
# @Author  : liangxinxin
# @Email  : liangxinxina@enn.cn


class Answer():

    def __init__(self):
        pass
    @staticmethod
    def query_symptom(disease):
        sql = "MATCH (n:Disease)-[r:HAS_SYMPTOMS]-(m:Symptoms)  where n.name='{disease}' RETURN m.name"
        return sql.format(disease)

    @staticmethod
    def query_recipe(disease):
        sql = "MATCH (n:Disease)-[r:HAS_SYMPTOMS]-(m:Food)  where n.name='{disease}' RETURN m.name"
        return sql.format(disease)

    @staticmethod
    def query_complication(disease):
        sql = "MATCH (n:Disease)-[r:ACOMPANY_WITH]-(m:Disease)  where n.name='{disease}' RETURN m.name"
        return sql.format(disease)

    @staticmethod
    def query_drug(disease):
        sql = "MATCH (n:Disease)-[r:RECOMMAND_DRUG]-(m:Drug)  where n.name='{disease}' RETURN m.name"
        return sql.format(disease)

    @staticmethod
    def query_not_eat(disease):
        sql = "MATCH (n:Disease)-[r:NO_EAT]-(mm:Food)  where n.name='{disease}' RETURN m.name"
        return sql.format(disease)

