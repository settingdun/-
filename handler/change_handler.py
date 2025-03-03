from toolkit.pre_load import neo4jconn
import os
import json


def change(entity1, entity2):
	db = neo4jconn
	entity1 = entity1.strip()
	entity2 = entity2.strip()
	relation_map = {1: '无限制'}

	searchResult = db.changeEntity(entity1, entity2)
	if len(searchResult) > 0:
		return {'ctx': '', 'searchResult':json.dumps(searchResult, ensure_ascii=False)}

	return {'ctx': 'padding', 'searchResult': ''}






