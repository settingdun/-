import thulac
import sys
import csv
import os

sys.path.append("..")

from Model.neo4j_models import Neo4j_Handle


#预加载Neo4j图数据库
neo4jconn = Neo4j_Handle()
neo4jconn.connectDB()
print('-------数据库已连接,点击下方链接开始-------\n')