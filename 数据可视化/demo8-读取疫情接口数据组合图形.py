# 思路；：1.解析疫情接口数据 2.数据拼接成二维列表 3.生成地图
import requests
from pyecharts import options as opts

from pyecharts.charts import Pie, Map, Grid, Bar
from pyecharts.globals import ThemeType


# 解析疫情接口数据
def getData():
    # 1.请求url地址
    result = requests.get(url).json()['data']['list']
    # a = []
    # 只要省份 感染人数
    # for item in result:
    return [[item["name"], item["value"]] for item in result]


def draw():
    # 饼图
    pie = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.DARK))
            .add("疫情接口可视化", pageData)
            .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                is_show=True,
                min_=0,
                max_=2000

            )
        )
    )
    map = (
        Map(init_opts=opts.InitOpts(theme=ThemeType.DARK))
            .add("疫情接口可视化", pageData, "china")
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                is_show=True,
                min_=0,
                max_=2000

            )
        )

    )
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
            # 只取省份
            .add_xaxis([item[0] for item in pageData])
            # 只取人数
            .add_yaxis(series_name="", y_axis=[item[1] for item in pageData])
            # 设置全局配置项
            .set_global_opts(
            # 设置视觉配置项
            visualmap_opts=opts.VisualMapOpts(
                is_show=True,
                min_=0,
                max_=10000,
                dimension=0,
                # 翻转坐标之后，视觉映射不生效可以添加dimension=0
                # pos_right=10, # pos_top=0
            ),
            # x坐标轴默认标注去除
            xaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(
                    is_show=True
                )
            ),
            # y坐标轴默认标注去除
            yaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(
                    is_show=True
                )
            )
        )
            # 去除柱状图上的数字标注
            .set_series_opts(
            label_opts=opts.LabelOpts(
                is_show=False
            )
        )
        .reversal_axis()  # x轴y轴
    )
    # grid = (
    #     # 初始化配置项，参考 `global_options.InitOpts`
    #     Grid(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    #         .add(pie, grid_opts=opts.GridOpts())
    #         .add(map, grid_opts=opts.GridOpts())
    #         .add(bar, grid_opts=opts.GridOpts())
    #         .render("疫情接口数据组合图形.html")
    # )

    # 组合图形
    grid = ( Grid(init_opts=opts.InitOpts(theme=ThemeType.DARK))
             .add(bar, grid_opts=opts.GridOpts())
             # 柱状图放在组合图形的第一个
             .add(map, grid_opts=opts.GridOpts())
             .add(pie, grid_opts=opts.GridOpts())
             .render("全国疫情数据可视化组合图形展示.html") )
if __name__ == '__main__':
    url = "https://gwpre.sina.cn/interface/fymap2020_data.json?1582011487323"
    # 解析疫情接口数据
    pageData = getData()
    pageData = sorted(pageData, key=lambda x: x[1], reverse=True)
    draw()
