# coding:utf-8
"""
增强版图表预设配置
包含通用的reload功能和图表管理
"""

from typing import List, Dict, Any

# 导入图表管理器
from ..chart_manager import get_chart_manager


# 增强版预设函数，自动注册到管理器
def managed_basic_line_chart(chart_id: str, x_data: List[str], y_data: List[float], 
                        title: str = "基础折线图", 
                        color: str = "#5470c6") -> Dict[str, Any]:
    """
    管理版基础折线图
    
    Args:
        chart_id: 图表唯一标识
        x_data: x轴数据
        y_data: y轴数据  
        title: 图表标题
        color: 线条颜色
        
    Returns:
        ECharts配置字典
    """
    config = {
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
            'type': 'line',
            'itemStyle': {
                'color': color
            }
        }]
    }
    
    # 存储到管理器
    manager = get_chart_manager()
    manager._configs[chart_id] = config
    return config


def managed_basic_bar_chart(chart_id: str, x_data: List[str], y_data: List[float],
                      title: str = "基础柱状图",
                      color: str = "#5470c6") -> Dict[str, Any]:
    """
    管理版基础柱状图
    
    Args:
        chart_id: 图表唯一标识
        x_data: x轴数据
        y_data: y轴数据
        title: 图表标题
        color: 柱子颜色
        
    Returns:
        ECharts配置字典
    """
    config = {
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
    
    # 存储到管理器
    manager = get_chart_manager()
    manager._configs[chart_id] = config
    return config


def managed_donut_chart(chart_id: str, data: List[Dict[str, Any]],
                    title: str = "环形图") -> Dict[str, Any]:
    """
    管理版环形图
    
    Args:
        chart_id: 图表唯一标识
        data: 数据列表，每个元素包含name和value
        title: 图表标题
        
    Returns:
        ECharts配置字典
    """
    config = {
        'title': {
            'text': title,
            'left': 'center'
        },
        'tooltip': {
            'trigger': 'item',
            'formatter': '{a} <br/>{b}: {c} ({d}%)'
        },
        'legend': {
            'orient': 'vertical',
            'left': 'left'
        },
        'series': [{
            'name': title,
            'type': 'pie',
            'radius': ['40%', '70%'],
            'center': ['50%', '50%'],
            'data': data,
            'emphasis': {
                'itemStyle': {
                    'shadowBlur': 10,
                    'shadowOffsetX': 0,
                    'shadowColor': 'rgba(0, 0, 0, 0.5)'
                }
            }
        }]
    }
    
    # 存储到管理器
    manager = get_chart_manager()
    manager._configs[chart_id] = config
    return config


def managed_gauge_chart(chart_id: str, value: float,
                     title: str = "基础仪表盘",
                     min_value: float = 0,
                     max_value: float = 100) -> Dict[str, Any]:
    """
    管理版基础仪表盘
    
    Args:
        chart_id: 图表唯一标识
        value: 当前值
        title: 图表标题
        min_value: 最小值
        max_value: 最大值
        
    Returns:
        ECharts配置字典
    """
    config = {
        'title': {
            'text': title,
            'left': 'center'
        },
        'series': [{
            'type': 'gauge',
            'data': [{'value': value, 'name': '当前值'}],
            'min': min_value,
            'max': max_value,
            'detail': {
                'formatter': '{value}%'
            }
        }]
    }
    
    # 存储到管理器
    manager = get_chart_manager()
    manager._configs[chart_id] = config
    return config
