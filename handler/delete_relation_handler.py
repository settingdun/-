from toolkit.pre_load import neo4jconn
import os
import json


def delete_relation(entity1, relation, entity2):
	db = neo4jconn
	entity1 = entity1.strip()
	relation = relation.strip()
	entity2 = entity2.strip()
	if len(entity1) != 0 and len(relation) != 0 and len(entity2) != 0:
		searchResult = db.deleteRelationByEntities(entity1, relation, entity2)
		return {'ctx': '', 'searchResult': json.dumps(searchResult, ensure_ascii=False)}

	return {'ctx': 'padding', 'searchResult': ''}






