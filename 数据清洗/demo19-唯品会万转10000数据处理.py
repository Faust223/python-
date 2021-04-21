import pandas as pd

from pyecharts import options as opts
from pyecharts.charts import Bar

from pyecharts.globals import ThemeType

# 1.处理数据
df = pd.read_csv("./data/唯品会万转10000数据处理.csv", names=['title', 'newPrice', 'oldPrice', 'amounts'])

# 2.销量中带万字的去掉之后，数值乘以10000，没有的就不变
# apply():任意可以执行的函数都可以通过lambda的方式传入
df['amounts'] = df['amounts'].apply(lambda x: float(x.split("万")[0]) * 10000 if x.split('万')[-1] == '' else float(x))
# print()

# 根据title分组，然后求销量的均值和newPrice的值
result = df.groupby('title').agg({"amounts": "mean", "newPrice": "mean"}).reset_index()
print(result)
c = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(list(result['title']))
    .add_yaxis("销量", list(df['amounts']), stack="stack1", category_gap="50%")
    .add_yaxis("价格", list(df['newPrice']), stack="stack1", category_gap="50%")
    .set_series_opts(
        label_opts=opts.LabelOpts(
            position="right",

        )
    )
    .render("唯品会数据分析柱状图.html")
)
