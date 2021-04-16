import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map3D
from pyecharts.globals import ChartType
from pyecharts.commons.utils import JsCode

# 1.读取内容
df = pd.read_csv("./data/bigwater.csv")
# #2.目标数据 [("泸定",['102.233333’，‘29.916667’，‘ 0.76’])]
# print(df)
result = [(value['站点'], [value['经度'], value['纬度'], value['汛情(米)']]) for key, value in df.iterrows()]

# 3.绘图
c = (
    Map3D()
        .add_schema(itemstyle_opts=opts.ItemStyleOpts(
        color="rgb(5,101,123)",
        opacity=1,
        border_width=0.8,
         border_color="rgb(62,215,213)",),
                    map3d_label=opts.Map3DLabelOpts(is_show=False, formatter=JsCode(
                        "function(data){return data.name + " " + data.value[2];}"),
                                                    ),
                    emphasis_label_opts=opts.LabelOpts(
                        is_show=False,
                        color="#fff",
                        font_size=10,
                        background_color="rgba(0,23,11,0)",
                    ),
                    light_opts=opts.Map3DLightOpts(
                        main_color="#fff", main_intensity=1.2,
                        main_shadow_quality="high",
                        is_main_shadow=False,
                        main_beta=10,
                        ambient_intensity=0.3,
                    ),
                    )
        .add(
        series_name="bar3D", data_pair=result,
        type_=ChartType.BAR3D,
        bar_size=1,
        shading="lambert",
        label_opts=opts.LabelOpts(
            is_show=False,
            formatter=JsCode("function(data){return data.name + ' ' + data.value[2];}"),
        ),
    )
        .set_global_opts(title_opts=opts.TitleOpts(title="Map3D-Bar3D"))
        .render("3D地图.html")
)
