# coding:utf-8
# @Time    : 2021/7/16 10:18 上午
# @Author  : liangxinxin
# @Email  : liangxinxina@enn.cn
from py2neo import Graph


class Neo4j():
    def __init__(self):
        self.graph = self.connected()

    def connected(self):
        graph = Graph('http://localhost:7474/', name='neo4j', password='123456')
        return graph

    def query(self, sql):
        return self.graph.run(sql).data()


class Neo4jGraphDatabase():
    neo4j = Neo4j()

    @staticmethod
    def symptom_sql(disease):
        sql = "MATCH (n:Disease)-[r:HAS_SYMPTOMS]-(m:Symptom)  where n.name='{disease}' RETURN collect(m.name) as res;"
        return sql.format(disease=disease)

    @staticmethod
    def recipe_sql(disease):
        sql = "MATCH (n:Disease)-[r:HAS_SYMPTOMS]-(m:Food)  where n.name='{disease}' RETURN collect(m.name) as res;"
        return sql.format(disease=disease)

    @staticmethod
    def complication_sql(disease):
        sql = "MATCH (n:Disease)-[r:ACOMPANY_WITH]-(m:Disease)  where n.name='{disease}' RETURN collect(m.name) as res;"
        return sql.format(disease=disease)

    @staticmethod
    def drug_sql(disease):
        sql = "MATCH (n:Disease)-[r:RECOMMAND_DRUG]-(m:Drug)  where n.name='{disease}' RETURN collect(m.name) as res;"
        return sql.format(disease=disease)

    @staticmethod
    def not_eat_sql(disease):
        sql = "MATCH (n:Disease)-[r:NO_EAT]-(m:Food)  where n.name='{disease}' RETURN collect(m.name) as res;"
        return sql.format(disease=disease)

    @staticmethod
    def check_sql(disease):
        sql = "MATCH (n:Disease)-[r:NEED_CHECK]-(m:Check)  where n.name='{disease}' RETURN collect(m.name) as res;"
        return sql.format(disease=disease)

    @staticmethod
    def query_attribute(en_name, attribute):
        sql = "MATCH (n:Disease)  where n.name='{disease}' RETURN n.{attribute} as attribute"
        return sql.format(disease=en_name, attribute=attribute)

    @staticmethod
    def query(sql):
        return Neo4jGraphDatabase.neo4j.query(sql)[0]


if __name__ == '__main__':
    neo4j = Neo4j()
    sql = "MATCH (n:Disease)-[r:HAS_SYMPTOMS]-(m:Symptom)  where n.name='' RETURN collect(m.name);"
    print(sql)
    print(neo4j.query(sql))
