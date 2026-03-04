# coding:utf-8
"""
图表预设使用示例
演示如何快速创建各种常见图表
"""

from .line_charts import basic_line_chart, smooth_line_chart, area_chart
from .bar_charts import basic_bar_chart, custom_color_bar_chart
from .pie_charts import donut_chart, semi_donut_chart
from .scatter_charts import basic_scatter_chart
from .gauge_charts import basic_gauge_chart, speed_gauge_chart
from .radar_charts import basic_radar_chart


def demo_basic_line_chart():
    """基础折线图示例"""
    x_data = ['1月', '2月', '3月', '4月', '5月', '6月']
    y_data = [120, 200, 150, 80, 70, 110]
    
    return basic_line_chart(
        x_data=x_data,
        y_data=y_data,
        title="月度销售数据"
    )


def demo_smooth_line_chart():
    """平滑折线图示例"""
    x_data = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    y_data = [820, 932, 901, 934, 1290, 1330, 1320]
    
    return smooth_line_chart(
        x_data=x_data,
        y_data=y_data,
        title="网站访问量趋势"
    )


def demo_area_chart():
    """面积图示例"""
    x_data = ['2010', '2011', '2012', '2013', '2014', '2015']
    y_data = [56, 58, 62, 69, 73, 78]
    
    return area_chart(
        x_data=x_data,
        y_data=y_data,
        title="市场份额变化"
    )


def demo_basic_bar_chart():
    """基础柱状图示例"""
    x_data = ['产品A', '产品B', '产品C', '产品D', '产品E']
    y_data = [120, 200, 150, 80, 70]
    
    return basic_bar_chart(
        x_data=x_data,
        y_data=y_data,
        title="产品销量对比"
    )


def demo_custom_color_bar_chart():
    """自定义颜色柱状图示例"""
    x_data = ['Q1', 'Q2', 'Q3', 'Q4']
    y_data = [120, 200, 150, 80]
    colors = ['#5470c6', '#91cc75', '#fac858', '#ee6666']
    
    return custom_color_bar_chart(
        x_data=x_data,
        y_data=y_data,
        colors=colors,
        title="季度营收"
    )


def demo_donut_chart():
    """环形图示例"""
    data = [
        {'name': '直接访问', 'value': 335},
        {'name': '邮件营销', 'value': 310},
        {'name': '联盟广告', 'value': 234},
        {'name': '视频广告', 'value': 135},
        {'name': '搜索引擎', 'value': 1548}
    ]
    
    return donut_chart(
        data=data,
        title="流量来源分析"
    )


def demo_semi_donut_chart():
    """半环形图示例"""
    data = [
        {'name': '已完成', 'value': 75},
        {'name': '进行中', 'value': 20},
        {'name': '待开始', 'value': 5}
    ]
    
    return semi_donut_chart(
        data=data,
        title="项目进度"
    )


def demo_scatter_chart():
    """散点图示例"""
    data = [
        [10.0, 8.04],
        [8.0, 6.95],
        [13.0, 7.58],
        [9.0, 8.81],
        [11.0, 8.33],
        [14.0, 9.96],
        [6.0, 7.24],
        [4.0, 4.26],
        [12.0, 10.84],
        [7.0, 4.82],
        [5.0, 5.68]
    ]
    
    return basic_scatter_chart(
        data=data,
        title="身高体重关系"
    )


def demo_basic_gauge():
    """基础仪表盘示例"""
    return basic_gauge_chart(
        value=75.5,
        title="CPU使用率",
        min_value=0,
        max_value=100
    )


def demo_speed_gauge():
    """速度仪表盘示例"""
    return speed_gauge_chart(
        value=120,
        title="车速监控",
        max_speed=200
    )


def demo_radar_chart():
    """雷达图示例"""
    indicators = [
        {'name': '销售', 'max': 6500},
        {'name': '管理', 'max': 16000},
        {'name': '信息技术', 'max': 30000},
        {'name': '客服', 'max': 38000},
        {'name': '研发', 'max': 52000},
        {'name': '市场', 'max': 25000}
    ]
    
    data = [
        {
            'value': [4200, 3000, 20000, 35000, 50000, 18000],
            'name': '预算分配'
        },
        {
            'value': [5000, 14000, 28000, 26000, 42000, 21000],
            'name': '实际开销'
        }
    ]
    
    return basic_radar_chart(
        data=data,
        indicators=indicators,
        title="部门预算分析"
    )


# 快速使用函数
def get_chart_config(chart_type: str, **kwargs):
    """
    根据图表类型快速获取配置
    
    Args:
        chart_type: 图表类型
        **kwargs: 图表参数
        
    Returns:
        ECharts配置字典
    """
    chart_map = {
        'line': demo_basic_line_chart,
        'smooth_line': demo_smooth_line_chart,
        'area': demo_area_chart,
        'bar': demo_basic_bar_chart,
        'custom_bar': demo_custom_color_bar_chart,
        'donut': demo_donut_chart,
        'semi_donut': demo_semi_donut_chart,
        'scatter': demo_scatter_chart,
        'gauge': demo_basic_gauge,
        'speed_gauge': demo_speed_gauge,
        'radar': demo_radar_chart
    }
    
    if chart_type in chart_map:
        return chart_map[chart_type]()
    else:
        raise ValueError(f"不支持的图表类型: {chart_type}")


# 使用示例
if __name__ == "__main__":
    # 获取基础折线图配置
    line_config = get_chart_config('line')
    print("基础折线图配置:", line_config)
    
    # 获取环形图配置
    donut_config = get_chart_config('donut')
    print("环形图配置:", donut_config)
