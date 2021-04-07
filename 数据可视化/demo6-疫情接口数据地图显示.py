# 思路；：1.解析疫情接口数据 2.数据拼接成二维列表 3.生成地图
import requests
from pyecharts import options as opts

from pyecharts.charts import Map
from pyecharts.globals import ThemeType


def draw():
    c = (
        Map(init_opts=opts.InitOpts(theme=ThemeType.DARK))
            .add("疫情接口可视化",pageData,"china")
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                is_show=True,
                min_=0,
                max_=2000

            ), title_opts=opts.TitleOpts(
                title="疫情传染视图"
            )
        )
            .render("疫情接口可视化地图.html")
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
    print(pageData)
    draw()
    # print(len(pageData))
