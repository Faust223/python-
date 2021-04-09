
# pip install pandas
# 1.dataframe
# 2.series
import pandas as pd

df = pd.DataFrame()
print(df)

from pandas import Series
# 1.自定义Series数据
# data：数据
# index：索引（可以是字符串）默认是0，1，2...
# 索引可以重复，但一般不这样用
x = Series(
    data=["xxx","juice","lil peep"],
    index=['a','b','c']

)

print(x)

# 2.传入列表中的字典元素生成Series对象
y = Series(
    data=[
        {"name":"xxx","age":20,"hobby":"basketball"},
        {"name":"xxx","age":20,"hobby":"basketball"},
        {"name":"xxx","age":20,"hobby":"basketball"}
    ]

)
print(y)
# 3.根据索引查找数据
print(x["a"],x['b'])

#4.根据a取到b的值
print(x['a':'b'])

# 5.Series添加元素
x = x.append(Series(data=['shawty'],index=['d']))
print(x)

# 根据索引删除元素
x = x.drop('d')

# 查看所有的索引，对应的值
print(x.index,x.values)

