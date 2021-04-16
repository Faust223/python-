import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType

df = pd.read_csv("lianjia_data.csv")
# 2.户型分布
# 根据房子户型分组，并依据个数排序
data = df.groupby("hourseType")['area'].count().reset_index()

# 3.数据处理二维列表
temp = [[value['hourseType'],value['area']] for key,value in data.iterrows()]

# 4.排序
result = sorted(temp,key=lambda x:x[1],reverse=True)[0:10]

# 5.绘图

(
    Pie(init_opts=opts.InitOpts(theme=ThemeType.DARK))
  .add(
        "",
       result,
        radius=["30%","75%"],
       center=["50%", "50%"],
       rosetype="area"
    )
    # 全局配置项
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="户型分布",
            pos_left="center",
            pos_top="20v",
            title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
        ),
        legend_opts=opts.LegendOpts(is_show=False),
    )
    # 系列配置项
    .set_series_opts(
        label_opts=opts.LabelOpts(
            formatter="{b}:{d}%"
        ),
    )
    .render("户型分布.html")

)


