from py2neo import Graph, Node, Relationship, NodeMatcher
import re


class Neo4j_Handle():
    graph = None

    # matcher = None
    def __init__(self):
        print("-----------正在初始化neo4j数据库-----------\n")
        

    def connectDB(self):
        self.graph = Graph("http://localhost:7474", auth=("neo4j", "123456"))

    def matchEntityItem(self, value):
        answer = self.graph.run("MATCH (entity1) WHERE entity1.name = \"" + value + "\" RETURN entity1").data()
        return answer

    def getEntityRelationbyEntity(self, value):
        answer = self.graph.run(
            "MATCH (entity1) - [rel] -> (entity2)  WHERE entity1.name = \"" + value + "\" RETURN entity1, rel,entity2").data()
        if len(answer) == 0:
            # 查询实体：不考虑关系方向
            answer = self.graph.run(
                "MATCH (entity1)  WHERE entity1.name = \"" + value + "\" RETURN entity1").data()
        print(answer)
        return answer

    def findRelationByEntity1(self, entity1):
        answer = self.graph.run("MATCH (n1)- [rel] -> (n2) WHERE n1.name=\"" + entity1 + "\"RETURN n1,rel,n2").data()
        return answer

    def findRelationByEntity2(self, entity1):
        answer = self.graph.run("MATCH (n1) - [rel] -> (n2) WHERE n2.name=\"" + entity1 + "\" RETURN n1,rel,n2").data()
        return answer

    def findOtherEntities(self, entity, relation):
        answer = self.graph.run(
            "MATCH (n1)- [rel] -> (n2) WHERE rel.name = \""
            + relation + "\"  AND n1.name=\"" + entity + "\" RETURN n1,rel,n2").data()
        return answer

    def findOtherEntities2(self, entity, relation):
        answer = self.graph.run(
            "MATCH (n1)- [rel] -> (n2) WHERE rel.name = \"" + relation +
            "\" AND n2.name=\"" + entity + "\" RETURN n1,rel,n2").data()
        return answer

    def findRelationByEntities(self, entity1, entity2):
        answer = self.graph.run(
            "MATCH (n1)- [rel] -> (n2) WHERE n1.name=\"" + entity1 + "\" and n2.name = \"" + entity2 + "\"RETURN n1,rel,n2").data()

        return answer

    def findEntityRelation(self, entity1, relation, entity2):
        answer = self.graph.run(
            "MATCH (n1)- [rel] -> (n2) WHERE rel.name=\"" + relation
            + "\" AND n1.name=\"" + entity1 + "\" AND n2.name=\"" + entity2 + "\" RETURN n1,rel,n2").data()
        return answer

    def deleteEntity(self, entity):
        input = entity
        self.graph.run("MATCH (n1) - [rel] - (n2) WHERE n1.name=\"" + input + "\"  DELETE n1,rel").data()
        self.graph.run("MATCH (n1) WHERE n1.name=\"" + input + "\" DELETE n1").data()
        return

    def addEntity(self, entity):
        self.graph.run("CREATE(n:my_entity{name:\"" + entity + "\"}) return n").data()
        return

    def addRelationByEntities(self, entity1, relation, entity2):
        search_entity1 = self.graph.run("MATCH(n:my_entity{name:\"" + entity1 + "\"}) return n").data()

        if len(search_entity1) == 0:
            self.graph.run("CREATE(n:my_entity{name:\"" + entity1 + "\"}) return n").data()

        search_entity2 = self.graph.run("MATCH(n:my_entity{name:\"" + entity2 + "\"}) return n").data()
        if len(search_entity2) != 0:
            answer = self.graph.run(
                "MATCH (n1),(n2) WHERE n1.name = \"" + str(entity1) + "\" AND n2.name = \""
                + str(entity2) + "\" CREATE (n1)-[rel:" + str(relation)
                + "] -> (n2) SET rel={name:\"" + str(relation) + "\"}RETURN n1, rel, n2").data()

        else:
            self.graph.run("CREATE(n:my_entity{name:\"" + entity2 + "\"}) return n").data()
            answer = self.graph.run(
                "MATCH (n1),(n2) WHERE n1.name = \"" + str(entity1) + "\" AND n2.name = \""
                + str(entity2) + "\" CREATE (n1)-[rel:" + str(relation)
                + "] -> (n2) SET rel={name:\"" + str(relation) + "\"}RETURN n1, rel, n2").data()
        return answer

    def changeEntity(self, old_name, new_name):
        self.graph.run("MATCH (n1) WHERE n1.name = \"" + old_name + "\" SET n1.name=\"" + new_name + "\"")
        answer = self.graph.run("MATCH (n1)- [rel] -> (n2) WHERE n1.name=\"" + new_name + "\"RETURN n1,rel,n2").data()
        return answer

    def deleteRelationByEntities(self, entity1, relation, entity2):
        self.graph.run("MATCH (n1) - [rel] - (n2) WHERE n1.name=\"" + entity1 + "\" AND n2.name=\"" + entity2
                       + "\" AND rel.name=\"" + relation + "\"DELETE rel").data()
        return

    def ChangeRelationByEntities(self, entity1, relation1, entity2, relation2):

        answer = self.graph.run("MATCH (n1) - [rel] - (n2) WHERE n1.name=\"" + entity1 + "\" AND n2.name=\"" + entity2
                + "\" AND rel.name=\"" + relation1 + "\" SET rel{name:\"" + relation2 + "\"} RETURN n1, rel, n2").data
        return answer


