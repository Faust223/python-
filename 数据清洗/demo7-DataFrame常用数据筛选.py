import pandas as pd
# 1.读取数据
# df = pd.read_csv("data/data.csv")
# print(df)
# print("-------------------")
#
# # 2.去除重复的数据
# df = df.drop_duplicates()
# print(df)
#
# # 3.空值处理
# df = pd.read_csv("data/data1.csv")
# print(df)
#
# # 3.1去除空值
# print(df.dropna())
#
# # 给空值填充数据
# print(df.fillna("Not null"))
#
# # 4.列值的替换
# df = pd.read_csv("data/data2.csv")
# print(df)
#
# # 将所有的name列的值为JIMI改为Nacy
# # 将Series类型转为str类型
# df = df['name'].str.replace('JIMI', 'Nacy')
# print(df)
#
# # 5.读取excel
# # excel文件读取必须安装库：pip install xlrd
# df = pd.read_excel("data/3.xlsx",sheet_name=['data2', 'data'])

# 6.data4数据
df = pd.read_csv("data/data4.csv",sep="|")
#print(df)

# 6.1筛选所有的comments大于等于10000的数据
print(df['comments']>=10000)
