import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Scatter
from pyecharts.globals import ThemeType

# 1.读取数据
df = pd.read_csv("./data/bigwater.csv")
# 2. 根据汛情排序，获取前十个
result = df.sort_values(by="汛情(米)",ascending=False)[0:10]
# 使用list做了类型转换
print(list(result['站点']))
# x轴显示站点 y轴显示汛情(米)
# 根据站点与汛情绘制散点图
# print(Faker.choose())
c = (Scatter(init_opts=opts.InitOpts(theme=ThemeType.DARK))
     .add_xaxis(list(result['站点']))
     .add_yaxis("站点汛情散点图", list(result['汛情(米)']))
     .set_global_opts( title_opts=opts.TitleOpts(title="站点-汛情(米)"),
                       visualmap_opts=opts.VisualMapOpts( is_show=True, max_=5, min_=0, type_="size" ),
# x轴y轴标记
xaxis_opts=opts.AxisOpts( name="站点" ),yaxis_opts=opts.AxisOpts( name="汛情(米)" ) )
    .set_series_opts(
#去掉数值显示
label_opts=opts.LabelOpts( is_show=False ) )
     .render("站点汛情散点图.html") )







