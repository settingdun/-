from toolkit.pre_load import neo4jconn
import os
import json


relationCountDict = {}
filePath = os.path.abspath(os.path.join(os.getcwd(),"."))

def delete(entity):
	db = neo4jconn
	entityRelation = db.getEntityRelationbyEntity(entity)
	if len(entityRelation) == 0:
		return {'ctx': '', 'entityRelation': ''}

	db.deleteEntity(entity)
	return {'ctx': json.dumps(entity, ensure_ascii=False), 'entityRelation': json.dumps(entityRelation, ensure_ascii=False)}
	
