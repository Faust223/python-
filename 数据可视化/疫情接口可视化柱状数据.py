# 思路；：1.解析疫情接口数据 2.数据拼接成二维列表 3.生成地图
import requests
from pyecharts import options as opts

from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

# 有点毛病，网页显示有问题
def draw():
    # 饼图
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
            # 只取省份
            .add_xaxis([item[0]] for item in pageData)
            .add_yaxis(series_name="", y_axis=[item[1] for item in pageData])
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                is_show=True,
                min_=0,
                max_=2000,
                dimension=0,

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
        .render("疫情接口可视化柱状数据.html")
    )


# 解析疫情接口数据
def getData():
    # 1.请求url地址
    result = requests.get(url).json()['data']['list']
    a = []
    # 只要省份 感染人数
    for item in result:
        return [[item["name"], item["value"]] for item in result]


if __name__ == '__main__':
    url = "https://gwpre.sina.cn/interface/fymap2020_data.json?1582011487323"
    # 解析疫情接口数据
    pageData = getData()
    pageData = sorted(pageData, key=lambda x: x[1], reverse=True)
    draw()
    # print(len(pageData))
