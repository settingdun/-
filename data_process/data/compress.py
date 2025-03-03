import json

# 读取原始 JSON 文件
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 将每条数据压缩为一行，并删除所有空格
compressed_data = [json.dumps(item, ensure_ascii=False).replace(" ", "") for item in data]

# 将结果写入新文件
with open('data1.json', 'w', encoding='utf-8') as f:
    for line in compressed_data:
        f.write(line + '\n')