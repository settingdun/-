import json
import csv
import re

# 定义关系类型编号
RELATION_MAPPING = {
    "Disease-Symptom": 1,
    "Disease-Drug": 2,
    "Disease-Check": 3,
    "Disease-RecommandDrug": 4,
    "Disease-RecommandFood": 5,
    "Disease-RecommandRecipe": 6,
    "Disease-ForbiddenFood": 7,
    "Disease-Acompany": 8,
    "Disease-cure_department":9,
    "Disease-cure_way":10,
    "RecommandDrug-Drug_detail":11,
    "None":12
}

# 读取JSON数据
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# 定义实体关系
relations = []

for item in data:
    disease = item["name"]  # 疾病名称
    
    # 疾病与症状
    for symptom in item.get("symptom", []):
        relations.append({
            "id": len(relations) + 1,
            "entity1": disease,
            "entity2": symptom,
            "relation_id": RELATION_MAPPING["Disease-Symptom"],
            "note": "NULL"
        })
    
    # 疾病与药物
    for drug in item.get("common_drug", []):
        relations.append({
            "id": len(relations) + 1,
            "entity1": disease,
            "entity2": drug,
            "relation_id": RELATION_MAPPING["Disease-Drug"],
            "note": "NULL"
        })
    
    # 疾病与检查项目
    for check in item.get("check", []):
        relations.append({
            "id": len(relations) + 1,
            "entity1": disease,
            "entity2": check,
            "relation_id": RELATION_MAPPING["Disease-Check"],
            "note": "NULL"
        })
    
    # 疾病与推荐药物
    for drug in item.get("recommand_drug", []):
        relations.append({
            "id": len(relations) + 1,
            "entity1": disease,
            "entity2": drug,
            "relation_id": RELATION_MAPPING["Disease-RecommandDrug"],
            "note": "NULL"
        })
    
    # 疾病与推荐食物
    for food in item.get("do_eat",[]):
        relations.append({
            "id": len(relations) + 1,
            "entity1": disease,
            "entity2": food,
            "relation_id": RELATION_MAPPING["Disease-RecommandFood"],
            "note": "NULL"
        })
    
    # 疾病与推荐食谱
    for food in item.get("recommand_eat", []):
        relations.append({
            "id": len(relations) + 1,
            "entity1": disease,
            "entity2": food,
            "relation_id": RELATION_MAPPING["Disease-RecommandRecipe"],
            "note": "NULL"
        })
    
    # 疾病与禁忌食物
    for food in item.get("not_eat", []):
        relations.append({
            "id": len(relations) + 1,
            "entity1": disease,
            "entity2": food,
            "relation_id": RELATION_MAPPING["Disease-ForbiddenFood"],
            "note": "NULL"
        })
    
    # 疾病和并发症
    for acompany in item.get("acompany",[]):
        relations.append({
            "id": len(relations) + 1,
            "entity1": disease,
            "entity2": acompany,
            "relation_id": RELATION_MAPPING["Disease-Acompany"],
            "note": "NULL"
        })

    # 疾病和治疗科室
    for cure_department in item.get("cure_department",[]):
        relations.append({
            "id": len(relations) + 1,
            "entity1": disease,
            "entity2": cure_department,
            "relation_id": RELATION_MAPPING["Disease-cure_department"],
            "note": "NULL"
        })
    #疾病和治疗方式
    for cure_way in item.get("cure_way",[]):
        relations.append({
            "id": len(relations) + 1,
            "entity1": disease,
            "entity2": cure_way,
            "relation_id": RELATION_MAPPING["Disease-cure_way"],
            "note": "NULL"
        })

    
    #药物和药物品牌
    for recommand_drug in item.get("recommand_drug",[]):
    # 在 drug_detail 中查找匹配的品牌
        for drug_detail in item.get("drug_detail",[]):
        # 提取药物名称（括号内的部分）
            drug_name_in_detail = re.search(r"\((.*?)\)", drug_detail)
            if drug_name_in_detail and drug_name_in_detail.group(1) == drug:
            # 提取品牌名称（括号前的部分）
                brand_name = drug_detail.split("(")[0].strip()
                relations.append({
                    "id": len(relations) + 1,  
                    "entity1": recommand_drug,         # 推荐药物
                    "entity2": drug_detail,   # 品牌名称
                    "relation_id": RELATION_MAPPING["Disease-Drug"],
                    "note": "NULL"             
            })

# 保存到CSV文件
with open("entity_relations.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["id", "entity1", "entity2", "relation_id", "note"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for relation in relations:
        writer.writerow(relation)

print("实体关系已保存到 entity_relations.csv 文件中。")