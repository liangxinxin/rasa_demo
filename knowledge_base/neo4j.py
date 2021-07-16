# coding:utf-8
# @Time    : 2021/7/16 10:18 上午
# @Author  : liangxinxin
# @Email  : liangxinxina@enn.cn
from py2neo import Graph

class Neo4j():
    def __init__(self):
        self.graph = self.connected()

    def connected(self):
        graph = Graph('http://localhost:7474/', username='neo4j', password='123456')
        return graph
    def query(self,sql):
        return self.graph.run(sql).data()


class Neo4jGraphDatabase():


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



















if __name__ == '__main__':
    neo4j = Neo4j()
    sql = ""
    print(neo4j.query(sql))