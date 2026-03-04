# coding:utf-8
"""
环形图预设配置
包含：圆角环形图、环形图、半环形图
"""

from typing import List, Dict, Any


def rounded_pie_chart(data: List[Dict[str, Any]], 
                    title: str = "圆角环形图",
                    radius: str = "50%") -> Dict[str, Any]:
    """
    圆角环形图
    
    Args:
        data: 数据列表，每个元素包含name和value
        title: 图表标题
        radius: 半径
        
    Returns:
        ECharts配置字典
    """
    return {
        'title': {
            'text': title,
            'left': 'center'
        },
        'tooltip': {
            'trigger': 'item',
            'formatter': '{a} <br/>{b}: {c} ({d}%)'
        },
        'series': [{
            'name': title,
            'type': 'pie',
            'radius': radius,
            'center': ['50%', '50%'],
            'data': data,
            'itemStyle': {
                'borderRadius': 10,
                'borderColor': '#fff',
                'borderWidth': 2
            },
            'emphasis': {
                'itemStyle': {
                    'borderRadius': 15,
                    'shadowBlur': 10,
                    'shadowOffsetX': 0,
                    'shadowColor': 'rgba(0, 0, 0, 0.5)'
                }
            }
        }]
    }


def donut_chart(data: List[Dict[str, Any]],
              title: str = "环形图",
              inner_radius: str = "40%",
              outer_radius: str = "70%") -> Dict[str, Any]:
    """
    环形图
    
    Args:
        data: 数据列表，每个元素包含name和value
        title: 图表标题
        inner_radius: 内半径
        outer_radius: 外半径
        
    Returns:
        ECharts配置字典
    """
    return {
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
            'radius': [inner_radius, outer_radius],
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


def semi_donut_chart(data: List[Dict[str, Any]],
                    title: str = "半环形图",
                    radius: List[str] = ["50%", "70%"]) -> Dict[str, Any]:
    """
    半环形图
    
    Args:
        data: 数据列表，每个元素包含name和value
        title: 图表标题
        radius: 半径范围
        
    Returns:
        ECharts配置字典
    """
    return {
        'title': {
            'text': title,
            'left': 'center'
        },
        'tooltip': {
            'trigger': 'item',
            'formatter': '{a} <br/>{b}: {c} ({d}%)'
        },
        'series': [{
            'name': title,
            'type': 'pie',
            'radius': radius,
            'center': ['50%', '50%'],
            'startAngle': 180,
            'endAngle': 360,
            'data': data,
            'label': {
                'show': True,
                'formatter': '{b}: {c}'
            },
            'emphasis': {
                'itemStyle': {
                    'shadowBlur': 10,
                    'shadowOffsetX': 0,
                    'shadowColor': 'rgba(0, 0, 0, 0.5)'
                }
            }
        }]
    }
