from toolkit.pre_load import neo4jconn
import os
import json



def add(entity):
	db = neo4jconn
	db.addEntity(entity)
	return 
	
