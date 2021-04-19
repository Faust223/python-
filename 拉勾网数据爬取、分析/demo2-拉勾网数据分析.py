import requests
import pandas as pd
import numpy

# 1.读取内容
df = pd.read_csv("lagou_date.cvs", names=['title', 'address', 'company', 'salary', 'exp', 'edu', 'type'])

# 2.筛选标题中带有数据分析的 contains()
temp = df[df['title'].str.contains("数据分析")]

# 3.筛选标题中不包含实习的
temp1 = df[df['title'].str.contains("实习")]
# print(temp1)

# 4.筛选标题中不包含实习的
# temp1 = df [~df['title'].str.contains("实习")]
# print(temp1)

# 5.同时满足

# 6.工资的处理 10k-20k
# lower()
result = df['salary'].str.lower()

# extract():根据工资正则提取数值
result = result.str.extract(r'(\d+)k-(\d+)k')

# 求均值
# applymap():可以对，每个单元格做操作


result = result.applymap(lambda x: int(x)).mean(axis=1).astype(int)

print(result)
