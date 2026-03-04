# coding:utf-8
"""
柱状图预设配置
包含：基础柱状图、坐标轴刻度与标签对齐、自定义单个柱子颜色
"""

from typing import List, Dict, Any


def basic_bar_chart(x_data: List[str], y_data: List[float],
                  title: str = "基础柱状图",
                  color: str = "#5470c6") -> Dict[str, Any]:
    """
    基础柱状图
    
    Args:
        x_data: x轴数据
        y_data: y轴数据
        title: 图表标题
        color: 柱子颜色
        
    Returns:
        ECharts配置字典
    """
    return {
        'title': {
            'text': title,
            'left': 'center'
        },
        'tooltip': {
            'trigger': 'axis'
        },
        'xAxis': {
            'type': 'category',
            'data': x_data
        },
        'yAxis': {
            'type': 'value'
        },
        'series': [{
            'data': y_data,
            'type': 'bar',
            'itemStyle': {
                'color': color
            }
        }]
    }


def aligned_bar_chart(x_data: List[str], y_data: List[float],
                    title: str = "坐标轴刻度与标签对齐") -> Dict[str, Any]:
    """
    坐标轴刻度与标签对齐的柱状图
    
    Args:
        x_data: x轴数据
        y_data: y轴数据
        title: 图表标题
        
    Returns:
        ECharts配置字典
    """
    return {
        'title': {
            'text': title,
            'left': 'center'
        },
        'tooltip': {
            'trigger': 'axis',
            'axisPointer': {
                'type': 'shadow'
            }
        },
        'xAxis': {
            'type': 'category',
            'data': x_data,
            'axisTick': {
                'alignWithLabel': True
            }
        },
        'yAxis': {
            'type': 'value'
        },
        'series': [{
            'data': y_data,
            'type': 'bar',
            'barWidth': '60%'
        }]
    }


def custom_color_bar_chart(x_data: List[str], y_data: List[float],
                         colors: List[str],
                         title: str = "自定义单个柱子颜色") -> Dict[str, Any]:
    """
    自定义单个柱子颜色的柱状图
    
    Args:
        x_data: x轴数据
        y_data: y轴数据
        colors: 每个柱子的颜色列表
        title: 图表标题
        
    Returns:
        ECharts配置字典
    """
    # 为每个数据点设置颜色
    item_style_data = []
    for i, (value, color) in enumerate(zip(y_data, colors)):
        item_style_data.append({
            'value': value,
            'itemStyle': {
                'color': color
            }
        })
    
    return {
        'title': {
            'text': title,
            'left': 'center'
        },
        'tooltip': {
            'trigger': 'axis'
        },
        'xAxis': {
            'type': 'category',
            'data': x_data
        },
        'yAxis': {
            'type': 'value'
        },
        'series': [{
            'data': item_style_data,
            'type': 'bar'
        }]
    }
