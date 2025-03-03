import pandas as pd
import numpy as np


data = pd.read_csv("ori_data/entity.csv")
data = np.array(data)

data1 = [[], [], [], [], []]

for item in data:
    if item[2] - 1 > 4:
        continue
    data1[item[2] - 1].append(item[1])

for i in range(len(data1)):
    data2 = pd.DataFrame(data=data1[i])
    data2.to_csv("ori_data/data_" + str(i) + ".csv")


