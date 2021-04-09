# pandas筛选行和列的方法
from pandas import DataFrame,Series



# 区别：列名筛选loc 列索引iloc
df=DataFrame(
    data=[
        {"name":"xxx","age":20,"hobby":"emo rap"},
        {"name":"juice","age":20,"hobby":"emo rap"},
        {"name":"lil peep","age":20,"hobby":"emo rap"}


    ],
    index=['first','second','third']


)
print(df)
print("--------------------")

# 1.loc的用法
# (1)行默认，只针对列操作
# 筛选所有的行，name列数据
# print(df.loc[:,["name"]])

#(2)筛选first行，name列数据
# print(df.loc["first",["name"]])
# print(df.loc["second",["age"]])

# (3)行索引与列名同时筛选
# 筛选first行与second行，name数据列
# print(df.loc["first":"second",["name"]])
# 报错，loc根据索引筛选，不能根据下标筛选
#print(df.loc[0:2,["name"]])

#（4）只获取某些行
# 筛选first行和third行，name和age数据(和不是到)
# print(df.loc[["first","third"],["name","hobby"]])

# 筛选first行到third行，name到age数据(到不是和)
# print(df.loc["first":"third","name":"hobby"])

# 2.iloc方法（列索引筛选）
# 筛选first行到second行，name列到age数据
#print(df.iloc[0:2,0:2])     # 行位置不能取到2，可以取到0，前面0：2管行，后面0：2管列

# 根据行位置筛选特定行
# 筛选first行，third行，hobby列数据
# print(df.iloc[[0,2],2])

