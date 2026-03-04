# coding:utf-8
"""
图表预设配置模块
提供各种常见图表的快捷配置接口
"""

# 折线图
from .line_charts import (
    basic_line_chart,
    smooth_line_chart,
    area_chart,
    stacked_line_chart
)

# 柱状图
from .bar_charts import (
    basic_bar_chart,
    aligned_bar_chart,
    custom_color_bar_chart
)

# 环形图
from .pie_charts import (
    rounded_pie_chart,
    donut_chart,
    semi_donut_chart
)

# 散点图
from .scatter_charts import (
    basic_scatter_chart,
    aggregated_scatter_chart,
    regression_scatter_chart
)

# 地图
from .map_charts import (
    svg_map_chart,
    geo_scatter_chart
)

# K线图
from .candlestick_charts import (
    basic_candlestick_chart,
    brush_candlestick_chart,
    broken_axis_candlestick_chart
)

# 雷达图
from .radar_charts import (
    basic_radar_chart,
    aqi_radar_chart
)

# 树状图
from .tree_charts import (
    left_to_right_tree_chart,
    treemap_chart,
    sunburst_transition_chart
)

# 仪表盘
from .gauge_charts import (
    basic_gauge_chart,
    animated_gauge_chart,
    speed_gauge_chart,
    level_gauge_chart
)

# 3D图表
from .charts_3d import (
    earth_3d_chart,
    bar_3d_chart,
    scatter_3d_chart,
    surface_3d_chart,
    line_3d_chart,
    gl_scatter_chart,
    gl_path_chart,
    gl_vector_field_chart
)

# 增强版预设（包含通用reload功能）
from .enhanced_presets import (
    managed_basic_line_chart,
    managed_basic_bar_chart,
    managed_donut_chart,
    managed_gauge_chart
)

__all__ = [
    # 折线图
    'basic_line_chart',
    'smooth_line_chart', 
    'area_chart',
    'stacked_line_chart',
    
    # 柱状图
    'basic_bar_chart',
    'aligned_bar_chart',
    'custom_color_bar_chart',
    
    # 环形图
    'rounded_pie_chart',
    'donut_chart',
    'semi_donut_chart',
    
    # 散点图
    'basic_scatter_chart',
    'aggregated_scatter_chart',
    'regression_scatter_chart',
    
    # 地图
    'svg_map_chart',
    'geo_scatter_chart',
    
    # K线图
    'basic_candlestick_chart',
    'brush_candlestick_chart',
    'broken_axis_candlestick_chart',
    
    # 雷达图
    'basic_radar_chart',
    'aqi_radar_chart',
    
    # 树状图
    'left_to_right_tree_chart',
    'treemap_chart',
    'sunburst_transition_chart',
    
    # 仪表盘
    'basic_gauge_chart',
    'animated_gauge_chart',
    'speed_gauge_chart',
    'level_gauge_chart',
    
    # 3D图表
    'earth_3d_chart',
    'bar_3d_chart',
    'scatter_3d_chart',
    'surface_3d_chart',
    'line_3d_chart',
    'gl_scatter_chart',
    'gl_path_chart',
    'gl_vector_field_chart',
    
    # 增强版预设（包含通用reload功能）
    'managed_basic_line_chart',
    'managed_basic_bar_chart',
    'managed_donut_chart',
    'managed_gauge_chart'
]
