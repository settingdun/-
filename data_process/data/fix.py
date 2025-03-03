import json

# 读取原始文件内容
with open('data1.json', 'r', encoding='utf-8') as f:
    content = f.read()

# 修复 JSON 格式（假设每行是一个独立的 JSON 对象）
fixed_content = "[" + content.replace("}\n{", "},\n{") + "]"

# 保存修复后的 JSON 文件
with open('fixed_data.json', 'w', encoding='utf-8') as f:
    f.write(fixed_content)

# 加载修复后的 JSON 数据
with open('fixed_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)