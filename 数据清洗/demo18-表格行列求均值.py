import pandas as pd

# 1.自定义dataframe

df = pd.DataFrame(
    data=[
        {"a": 1, "b": 2},
        {"a": 2, "b": 4},
        {"a": 3, "b": 6}

    ]

)

# 2.对行求均值
# axis=1 跨列操作（对行求均值）
print(df.mean(axis=1))

# 2.对列求均值
# axis=0 跨行操作（对列求均值）
print(df.mean(axis=0))
