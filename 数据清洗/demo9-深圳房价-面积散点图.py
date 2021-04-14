import pandas as pd
from pyecharts.charts import Scatter
from pyecharts.faker import Faker
from pyecharts import options as opts

# 1.读取csv文件内容
df = pd.read_csv("lianjia_data.csv")
# print(df)

# 2.获取面积 房价
# print(df['hourseSize'])
# print(df['total_price'])
# # 3.把面积和价格拼接成散点图所需要的格式数据
# print(Faker.choose())

# 4.绘图
c=(
    Scatter()
            .add_xaxis(df['hourseSize'])    # x轴 面积
            .add_yaxis("房价",df['total_price'])  # y轴 价格
            # 全局配置项
            .set_global_opts(
                # 标题配置项
                title_opts=opts.TitleOpts(title="房价-面积"),
                # 视觉配置项
                visualmap_opts=opts.VisualMapOpts(max_=150),
                # 坐标轴配置项
                xaxis_opts=opts.AxisOpts(
                    type_="value",
                    name="m²"
                ),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    name="万/元"

                )

    )
            .set_series_opts(
                # 去掉数值显示
                label_opts=opts.LabelOpts(
                    is_show=False
                ),
                # 标记点配置项，配置最大值最小值
                # markpoint_opts=opts.MarkLineOpts(
                #     data=[
                #         opts.MarkPointItem(
                #             type="max",
                #             name="最贵的房子"
                #          ),
                #         opts.MarkPointItem(
                #             type="min",
                #             name="最便宜的房子"
                #         )
                #     ]
                # )
    )


            .render("深圳二手房面积-房价散点图.html")
)