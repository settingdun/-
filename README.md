# -本项目旨在构建肺炎支原体感染相关知识图谱

通过以下技术路线进行实现，具体分为数据获取、知识图谱构建和前后端搭建三个部分。

# -数据获取部分

第一阶段，我们将从相关医学教材、专业文献及数据库中，筛选出与肺炎和支原体感染相关的关键专业词汇。这些词汇包括疾病名称、症状、诊断方法、治疗手段、常见药物等，作为知识图谱中的实体。
第二阶段，我们将使用爬虫技术从公开的医学百科网站、专业研究论文及临床数据中抓取相关的非结构化信息，进一步提取出与肺炎支原体感染相关的知识语句。这些信息经过自然语言处理技术的筛选后，将被转化为结构化数据，挖掘出实体之间的关系，如“肺炎”的症状关联以及治疗方法、治疗药物的推荐。

# -知识图谱构建

对不同类别的医学词汇进行分类整理，确保知识图谱结构清晰、层次分明，便于用户查询与该领域相关的各类信息。
知识图谱将具备增、删、改、查等功能，支持动态更新，以应对可能由于本项目所采用的数据集较小所带来的信息缺失问题。

# -前后端搭建

前端

使用了Flask框架基于Web浏览器设计用户界面，前端界面支持关键字搜索、疾病概述、症状查询等功能。

后端

采用了Neo4j图数据库与Py2neo库相结合，构建知识图谱的数据存储和处理模块。支持实体的增、删、改、查等操作以及对大量医学数据的快速查询与实时更新。
