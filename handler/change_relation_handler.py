from toolkit.pre_load import neo4jconn
import os
import json


def change_relation(entity1, relation1, entity2, relation2):
	db = neo4jconn
	entity1 = entity1.strip()
	relation1 = relation1.strip()
	entity2 = entity2.strip()
	relation2 = relation2.strip()
	if len(entity1) != 0 and len(relation1) != 0 and len(entity2) != 0 and len(relation2) != 0:
		searchResult = db.ChangeRelationByEntities(entity1, relation1, entity2)
		print(searchResult)
		if len(searchResult) > 0:
			return {'ctx': '', 'searchResult': json.dumps(searchResult, ensure_ascii=False)}

	return {'ctx': 'padding', 'searchResult': ''}






