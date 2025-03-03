import json
import csv

# 定义实体类型编号
KIND_MAPPING = {
    "疾病名称": 1,
    "药物名称": 2,
    "检查项目": 3,
    "症状": 4,
    "推荐药物": 5,
    "推荐食物": 6,
    "推荐食谱": 7,
    "禁忌食物": 8,
    "并发症": 9,
    "治疗科室":10,
    "治疗方式":11,
    "常规药物":12,
    "药物品牌":13
}

# 读取JSON数据
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# 提取实体
entities = set()  # 使用集合去重

for item in data:
    # 提取疾病名称
    entities.add((item["name"], KIND_MAPPING["疾病名称"]))
    
    # 提取药物名称
    for drug in item.get("common_drug", []):
        entities.add((drug, KIND_MAPPING["药物名称"]))
    
    # 提取检查项目
    for check in item.get("check", []):
        entities.add((check, KIND_MAPPING["检查项目"]))
    
    # 提取症状
    for symptom in item.get("symptom", []):
        entities.add((symptom, KIND_MAPPING["症状"]))
    
    # 提取推荐药物
    for drug in item.get("recommand_drug", []):
        entities.add((drug, KIND_MAPPING["推荐药物"]))
    
    # 提取推荐食物
    for food in item.get("do_eat",[]):
        entities.add((food,KIND_MAPPING["推荐食物"]))
    
    # 提取推荐食谱
    for food in item.get("recommand_eat", []):
        entities.add((food, KIND_MAPPING["推荐食谱"]))
    
    # 提取禁忌食物
    for food in item.get("not_eat", []):
        entities.add((food, KIND_MAPPING["禁忌食物"]))

    # 提取并发症
    for acompany in item.get("acompany", []):
        entities.add((acompany, KIND_MAPPING["并发症"]))

    #提取治疗科室
    for cure_department in item.get("cure_department", []):
        entities.add((cure_department, KIND_MAPPING["治疗科室"]))

    #提取治疗方式
    for cure_way in item.get("cure_way", []):
        entities.add((cure_way, KIND_MAPPING["治疗方式"]))
    
    #提取常规药物
    for common_drug in item.get("common_drug", []):
        entities.add((common_drug,KIND_MAPPING["常规药物"]))
    
    #提取药物品牌
    for drug_detail in item.get("drug_detail",[]):
        entities.add((drug_detail, KIND_MAPPING["药物品牌"]))
    

# 转换为列表并分配ID
entities = [{"id": idx + 1, "name": name, "kind": kind, "state": "0"} 
            for idx, (name, kind) in enumerate(entities)]

# 保存到CSV文件
with open("entity.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["id", "name", "kind", "state"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for entity in entities:
        writer.writerow(entity)

print("实体已保存到 entity.csv 文件中。")