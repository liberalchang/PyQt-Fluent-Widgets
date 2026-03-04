# 图表预设配置

本模块提供了各种常见图表的快捷配置接口，方便外部快速使用。

## 目录结构

```
presets/
├── __init__.py          # 导出所有预设函数
├── examples.py          # 使用示例
├── README.md            # 说明文档
├── line_charts.py       # 折线图预设
├── bar_charts.py        # 柱状图预设
├── pie_charts.py        # 环形图预设
├── scatter_charts.py    # 散点图预设
├── map_charts.py        # 地图预设
├── candlestick_charts.py # K线图预设
├── radar_charts.py      # 雷达图预设
├── tree_charts.py       # 树状图预设
├── gauge_charts.py      # 仪表盘预设
└── charts_3d.py        # 3D图表预设
```

## 快速开始

### 1. 导入预设函数

```python
from qfluentwidgets.components.charts.presets import (
    basic_line_chart,
    basic_bar_chart,
    donut_chart,
    basic_gauge_chart
)
```

### 2. 创建EChartsWidget并设置配置

```python
from qfluentwidgets.components.charts import EChartsWidget

# 创建图表组件
chart = EChartsWidget()

# 使用预设配置
x_data = ['1月', '2月', '3月', '4月', '5月', '6月']
y_data = [120, 200, 150, 80, 70, 110]

config = basic_line_chart(
    x_data=x_data,
    y_data=y_data,
    title="月度销售数据"
)

chart.setOption(config)
```

## 图表类型

### 折线图
- `basic_line_chart`: 基础折线图
- `smooth_line_chart`: 基础平滑折线图
- `area_chart`: 基础面积图
- `stacked_line_chart`: 堆叠折线图

### 柱状图
- `basic_bar_chart`: 基础柱状图
- `aligned_bar_chart`: 坐标轴刻度与标签对齐
- `custom_color_bar_chart`: 自定义单个柱子颜色

### 环形图
- `rounded_pie_chart`: 圆角环形图
- `donut_chart`: 环形图
- `semi_donut_chart`: 半环形图

### 散点图
- `basic_scatter_chart`: 基础散点图
- `aggregated_scatter_chart`: 数据聚合
- `regression_scatter_chart`: 线性回归（使用统计插件）

### 地图
- `svg_map_chart`: 地图（SVG）
- `geo_scatter_chart`: 地理散点图

### K线图
- `basic_candlestick_chart`: 基础K线图
- `brush_candlestick_chart`: K线图刷选
- `broken_axis_candlestick_chart`: 断轴上的日内走势图

### 雷达图
- `basic_radar_chart`: 基础雷达图
- `aqi_radar_chart`: AQI雷达图

### 树状图
- `left_to_right_tree_chart`: 从左到右树状图
- `treemap_chart`: 矩形树图
- `sunburst_transition_chart`: 矩形树图和旭日图的动画过渡

### 仪表盘
- `basic_gauge_chart`: 基础仪表盘
- `animated_gauge_chart`: 带标签数字动画的基础仪表盘
- `speed_gauge_chart`: 速度仪表盘
- `level_gauge_chart`: 等级仪表盘

### 3D图表
- `earth_3d_chart`: 3D地球（大气层显示）
- `bar_3d_chart`: 3D柱状图
- `scatter_3d_chart`: 3D散点图
- `surface_3d_chart`: 3D曲面
- `line_3d_chart`: 3D折线图
- `gl_scatter_chart`: GL散点图
- `gl_path_chart`: GL路径图
- `gl_vector_field_chart`: GL矢量场图

## 使用示例

### 基础折线图

```python
from qfluentwidgets.components.charts.presets.line_charts import basic_line_chart

config = basic_line_chart(
    x_data=['1月', '2月', '3月', '4月', '5月', '6月'],
    y_data=[120, 200, 150, 80, 70, 110],
    title="月度销售数据",
    color="#5470c6"
)
```

### 基础柱状图

```python
from qfluentwidgets.components.charts.presets.bar_charts import basic_bar_chart

config = basic_bar_chart(
    x_data=['产品A', '产品B', '产品C', '产品D', '产品E'],
    y_data=[120, 200, 150, 80, 70],
    title="产品销量对比",
    color="#91cc75"
)
```

### 环形图

```python
from qfluentwidgets.components.charts.presets.pie_charts import donut_chart

data = [
    {'name': '直接访问', 'value': 335},
    {'name': '邮件营销', 'value': 310},
    {'name': '联盟广告', 'value': 234},
    {'name': '视频广告', 'value': 135},
    {'name': '搜索引擎', 'value': 1548}
]

config = donut_chart(
    data=data,
    title="流量来源分析"
)
```

### 仪表盘

```python
from qfluentwidgets.components.charts.presets.gauge_charts import basic_gauge_chart

config = basic_gauge_chart(
    value=75.5,
    title="CPU使用率",
    min_value=0,
    max_value=100
)
```

## 快速获取配置

使用 `examples.py` 中的 `get_chart_config` 函数快速获取预设配置：

```python
from qfluentwidgets.components.charts.presets.examples import get_chart_config

# 获取基础折线图配置
line_config = get_chart_config('line')

# 获取环形图配置
donut_config = get_chart_config('donut')

# 获取速度仪表盘配置
speed_config = get_chart_config('speed_gauge')
```

## 注意事项

1. 所有预设函数返回的都是 ECharts 配置字典，可以直接传递给 `EChartsWidget.setOption()`
2. 部分高级图表（如3D图表、地图等）需要额外的 ECharts 插件支持
3. 可以根据需要修改预设配置中的参数来定制图表样式
4. JavaScript 函数字符串会自动注入到页面中，无需额外处理

## 扩展

如果需要添加新的预设图表，可以：

1. 在对应的文件中添加新的函数
2. 在 `__init__.py` 中导出新函数
3. 在 `examples.py` 中添加使用示例
4. 更新此 README 文档

## 完整示例

```python
import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PySide6.QtCore import Qt

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from qfluentwidgets.components.charts import EChartsWidget
from qfluentwidgets.components.charts.presets import basic_line_chart

class DemoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("图表预设演示")
        self.resize(800, 600)
        
        layout = QVBoxLayout(self)
        
        # 创建图表
        chart = EChartsWidget(self)
        layout.addWidget(chart)
        
        # 使用预设配置
        config = basic_line_chart(
            x_data=['1月', '2月', '3月', '4月', '5月', '6月'],
            y_data=[120, 200, 150, 80, 70, 110],
            title="月度销售数据"
        )
        
        chart.setOption(config)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DemoWindow()
    window.show()
    sys.exit(app.exec())
```
