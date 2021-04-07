import pyecharts
from pyecharts.charts import Bar    # 柱状图
from pyecharts import options as ops
from pyecharts.globals import ThemeType # 内置主题类型
bar = (
    Bar(init_opts=ops.InitOpts(theme=""))
    .add_xaxis(["xxx", "juice", "14", "ts", "drake", "young thug"])
    .add_yaxis("商家A", [100, 20, 36, 10, 75, 90])
    # 全局配置项
    .set_global_opts(
        # 标题配置项
        title_opts=ops.TitleOpts(
            # 主标题
            title="hello",
            subtitle="hhh"
        ),
        # 图例配置项
        legend_opts=ops.LegendOpts(
            is_show=True
        ),
        # 工具配置项
        toolbox_opts=ops.ToolboxOpts(
            is_show=False
        ),
        # 视觉映射配置项
        visualmap_opts=ops.VisualMapOpts(
            is_show=True,
            # type_="color"
        )


    )
)
bar.render("柱状图.html")



# 使用 options 配置项，在 pyecharts 中，一切皆 Options。

# 全局配置项可通过 set_global_opts 方法设置