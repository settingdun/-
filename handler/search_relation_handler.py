from toolkit.pre_load import neo4jconn
import os
import json


def search_relation(entity1, relation, entity2):
	db = neo4jconn
	entity1 = entity1.strip()
	relation = relation.strip()
	entity2 = entity2.strip()
	relation_map = {1: '无限制'}
	#若只输入entity1,则输出与entity1有直接关系的实体和关系
	if len(entity1) != 0 and len(relation) == 0 and len(entity2) == 0:
		searchResult = db.findRelationByEntity1(entity1)
		if len(searchResult) > 0:
			return {'ctx': '', 'searchResult':json.dumps(searchResult, ensure_ascii=False)}

	#若只输入entity2则,则输出与entity2有直接关系的实体和关系
	if len(entity2) != 0 and len(relation) == 0 and len(entity1) == 0:
		searchResult = db.findRelationByEntity2(entity2)
		if len(searchResult) > 0:
			return {'ctx': '', 'searchResult':json.dumps(searchResult, ensure_ascii=False)}

	#若输入entity1和relation，则输出与entity1具有relation关系的其他实体
	if len(entity1) != 0 and len(relation) != 0 and len(entity2) == 0:
		# relation = relation_map[relation]
		searchResult = db.findOtherEntities(entity1, relation)
		if len(searchResult) > 0:
			return {'ctx': '', 'searchResult':json.dumps(searchResult, ensure_ascii=False)}

	#若输入entity2和relation，则输出与entity2具有relation关系的其他实体
	if len(entity2) != 0 and len(relation) != 0 and len(entity1) == 0:
		# relation = relation_map[relation]
		searchResult = db.findOtherEntities2(entity2, relation)
		if len(searchResult) > 0:
			return {'ctx': '', 'searchResult':json.dumps(searchResult, ensure_ascii=False)}

	#若输入entity1和entity2,则输出entity1和entity2之间的关系
	if len(entity1) != 0 and len(relation) == 0 and len(entity2) != 0:
		searchResult = db.findRelationByEntities(entity1, entity2)
		print(searchResult)
		if len(searchResult) > 0:
			return {'ctx': '', 'searchResult':json.dumps(searchResult, ensure_ascii=False)}

	#若输入entity1,entity2和relation,则输出entity1、entity2是否具有相应的关系
	if len(entity1) != 0 and len(entity2) != 0 and len(relation) != 0:
		# relation = relation_map[relation]
		searchResult = db.findEntityRelation(entity1, relation, entity2)
		if len(searchResult) > 0:
			return {'ctx': '', 'searchResult':json.dumps(searchResult, ensure_ascii=False)}

	return {'ctx': 'padding', 'searchResult': ''}






