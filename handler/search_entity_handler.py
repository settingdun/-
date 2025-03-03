from toolkit.pre_load import neo4jconn
import os
import json


def search_entity(entity):
	db = neo4jconn
	entityRelation = db.getEntityRelationbyEntity(entity)
	print(entityRelation)
	if len(entityRelation) == 0:
		return {'ctx': '', 'entityRelation': ''}
	else:
		return {'ctx': json.dumps(entity, ensure_ascii=False), 'entityRelation': json.dumps(entityRelation, ensure_ascii=False)}

