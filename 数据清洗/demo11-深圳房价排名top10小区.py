import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType

# 1.读取数据
df = pd.read_csv("lianjia_data.csv")

# 2.数据分组
# 根据小区进行分组，再根据个数进行筛选
# 条件：当前小区同时在3套以上的数量进行统计
temp = df.groupby('community')['unit_price'].agg(['mean','count']).reset_index()
# 先进行数据处理
result = [ [value['community'],round(value['mean']/10000,1)] if value['count']>=3  else [value['community'],0] for key,value in temp.iterrows()]

# 3.排序
# 第一个参数：被排序的数据(列表或者元组)
# key:根据什么排序
result = sorted(result,key=lambda x:x[1],reverse=True)[0:10]

# 4.绘图
list2 = [
    {"value":12,"percent":12/(12+3)},
    {"value":23,"percent":23/(23+21)},
    {"value":33,"percent":33/(33+5)},
    {"value":3,"percent":3/(3+52)},
    {"value":33,"percent":33/(33+43)}
]

c = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .add_xaxis([ item[0] for item in result[::-1]])  # x轴显示小区的 名字

    .add_yaxis("深圳房价排名Top10小区", [item[1] for item in result[::-1]],
    stack="stack1",category_gap="50%") # y轴显示均价
    .set_series_opts(
        label_opts=opts.LabelOpts(
            position="right",
            formatter="{b}:{c}万元"
        )

    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(
            is_show=True,
            max_=20,
            min_=0,
            dimension=0
        )
    )
    .reversal_axis() # 翻转xy轴
    .render("深圳房价排名Top10小区.html")

)
