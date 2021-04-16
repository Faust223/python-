import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Bar3D

# 1.读取内容(添加列名)

df = pd.read_csv("./data/video.csv", names=['title', 'type', 'time', 'count', 'start', 'date', 'author', 'url'])
# 2.目标数据格式 [[1,2,3]]
# 查看学科类型和对应的个数
# print(df['type'].value_counts())
# #3.根据年份和学科进行统计
# 获取年份： 2019/3/1
# expand=True:将一列拆分成多列(分列效果)
year = df['date'].str.split("/", expand=True)[0]
# 4.将年份添加到df中
df['year'] = year
# 5.按照学科和年份分组，统计播放量的和
result = df.groupby(['type', 'year'])['count'].sum().reset_index()
# 6.数据处理
temp = [[value['type'], value['year'], value['count']] for key, value in result.iterrows()]
# 7.绘图
(Bar3D(init_opts=opts.InitOpts(width="1200px", height="600px"))
 .add(series_name="不同学科不同年份视频播放量", data=temp, zaxis3d_opts=opts.Axis3DOpts(type_="value"), )
 .set_global_opts(visualmap_opts=opts.VisualMapOpts(
    max_=1000000,
    range_color=["#313695", "#4575b4", "#74add1", "#abd9e9", "#e0f3f8", "#ffffbf", "#fee090", "#fdae61", "#f46d43",
                 "#d73027", "#a50026", ], ))
 .render("不同学科不同年份播放量3D柱状图.html"))
