import pandas as pd
from pandas import DataFrame,Series

#1.读取csv文件内容
df = pd.read_csv("data1.csv")
print(df)
print("-----------------------")

# 缺失数据：NaN
# df = df.dropna()
#print(df)

# 筛选行和列
# 3.使用loc筛选前5行，前两列
# print(df.loc[0:4,"id":"key"])
# 使用iloc筛选前5行，前两列
print(df.iloc[0:5,0:1])



