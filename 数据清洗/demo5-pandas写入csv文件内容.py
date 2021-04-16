from pandas import DataFrame,Series
import pandas as pd

# 1.自定义DataFrame数据
df = DataFrame(

    data=[

        {"name": "Playboy Carty", "age": 25,"hobby": "melodic rap"},
        {"name": "YoungThug", "age": 28, "hobby": "trap"},
        {"name": "Travis Scott", "age": 24, "hobby": "auto-tune"}


    ]

)
print(df)
print("---------------------------")
# 2.写入csv文件中
# index=False 只写入列，不写入索引
# header=True 不写入表头
df.to_csv("rappers.csv",index=False,header=False)

# 3.读取csv文件内容
data= pd.read_csv("rappers.csv",names=["name","age","hobby"])
print(data)

# 作业
# 豆瓣影评数据爬取，进行词云分析
