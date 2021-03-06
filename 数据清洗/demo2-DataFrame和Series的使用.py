from pandas import DataFrame

# 1.自定义DataFrame数据
x = DataFrame(
    data={
        "name": ['xxx', 'juice', 'lil peep'],
        "age": [20, 23, 22]
    },
    index=["first", 'second', 'third']

)
#
# print(x)

#2.获取所有的列名
#print(x.cloumns)
#3.直接向DataFrame中传如列表，列表中的元素是字典
df = DataFrame(
    data=[
        {"name": "xxx", "age": 20, "hobby": "basketball"},
        {"name": "xxx", "age": 20, "hobby": "basketball"},
        {"name": "xxx", "age": 20, "hobby": "basketball"}

    ],
    index=['first', 'second','third']
)

print(df)

# 4.去除name列所有数据，获取是Series类型
print(df['name'],type(df['name']))

# 5.切片使用
print(df[0:])  # 切片从0开始，切到末尾（包含）
