import pandas as pd
from pandas import DataFrame, Series

# 1.读取数据
df=pd.read_csv("data/groupby.csv")
print(df)

# 2.统计各地区的总人数
# 先根据address分组,求个数,会显示所有列
data = df.groupby("address")['name'].count()

# 3.统计各地区的score列平均分
avg = df.groupby("address")['score'].mean().reset_index()

# 4.统计各地区score列的平均分和最大值、最小值、分数总和
# agg():aggregate 合计
result=df.groupby('address')['score'].agg(['mean','max','min','sum']).reset_index()

# 5.统计各地区年龄的平均值score成绩的总和，最大值
da = df.groupby('address').agg({"age":'mean','score':['sum','max']})
print(da)

# 6.排序
print(df)

# 根据score进行排序
# by:根据什么进行排序
# ascending=False:降序

print(df.sort_values(by='score',ascending=False))
# 根据score降序排序，如果score一样，根据年龄降序
print(df.sort_values(by=['score','age'],ascending=False))

# 7.求重复出现的频率
print(df['address'].value_counts())

# 8.读取豆瓣影评
df = pd.read_csv("豆瓣影评.csv",names=['author','title','commentText'])

# 计算豆瓣影评打分的个数
print(df['title'].value_counts())