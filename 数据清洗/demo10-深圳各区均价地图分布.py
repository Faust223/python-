import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
from pyecharts.globals import ChartType

# 1.读取数据
df = pd.read_csv("lianjia_data.csv")

# 2.根据地区进行分组，求单价的均值
temp = df.groupby('area')['unit_price'].mean().reset_index()

# 3.把result处理为目标数据格式
result = [[value['area'], round(value['unit_price'] / 10000, 1)] for key, value in temp.iterrows()]

# 4.绘图
c = (
    Map()
        .add(
        "深圳各区均价", result, "深圳"

    )

        .set_global_opts(title_opts=opts.TitleOpts(title="深圳各区均价"),
                         visualmap_opts=opts.VisualMapOpts(max_=10, min_=0, is_piecewise=True, is_show=True),
                         tooltip_opts=opts.TooltipOpts(
                             is_show=True, formatter="{b}:{c}万元"

                         )
                         )

        .render("深圳各区均价地图展示.html")
)