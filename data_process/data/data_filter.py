from fuzzywuzzy import fuzz
import re
import json

# 加载 JSON 数据
with open('medical.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 定义筛选关键词
keywords = ["肺炎支原体", "支原体肺炎", "Mycoplasma pneumoniae"]
patterns = [re.compile(r"肺炎支原体", re.IGNORECASE), re.compile(r"支原体肺炎", re.IGNORECASE)]

# 模糊匹配函数
def fuzzy_match(text, keyword, threshold=70):
    return fuzz.partial_ratio(text, keyword) >= threshold

# 正则匹配函数
def regex_match(text, patterns):
    return any(pattern.search(text) for pattern in patterns)

# 筛选函数
def filter_pneumonia(item):
    # 检查疾病名称
    if any(fuzzy_match(item.get("name", ""), keyword) for keyword in keywords) or regex_match(item.get("name", ""), patterns):
        return True
    # 检查描述字段
    if any(fuzzy_match(item.get("desc", ""), keyword) for keyword in keywords) or regex_match(item.get("desc", ""), patterns):
        return True
    # 检查病因字段
    if any(fuzzy_match(item.get("cause", ""), keyword) for keyword in keywords) or regex_match(item.get("cause", ""), patterns):
        return True
    # 检查症状字段
    if any(fuzzy_match(symptom, keyword) for symptom in item.get("symptom", []) for keyword in keywords) or any(regex_match(symptom, patterns) for symptom in item.get("symptom", [])):
        return True
    # 检查检查字段
    if any(fuzzy_match(check, keyword) for check in item.get("check", []) for keyword in keywords) or any(regex_match(check, patterns) for check in item.get("check", [])):
        return True
    # 检查治疗字段
    if any(fuzzy_match(treatment, keyword) for treatment in item.get("cure_way", []) for keyword in keywords) or any(regex_match(treatment, patterns) for treatment in item.get("cure_way", [])):
        return True
    return False

# 筛选数据
filtered_data = [item for item in data if filter_pneumonia(item)]

# 输出筛选结果
print(json.dumps(filtered_data, ensure_ascii=False, indent=2))
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=2)