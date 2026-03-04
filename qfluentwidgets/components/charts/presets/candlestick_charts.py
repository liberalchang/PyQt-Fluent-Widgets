# coding:utf-8
"""
K线图预设配置
包含：基础K线图、K线图刷选、断轴上的日内走势图
"""

from typing import List, Dict, Any


def basic_candlestick_chart(data: List[List[float]],
                          title: str = "基础K线图") -> Dict[str, Any]:
    """
    基础K线图
    
    Args:
        data: K线数据，每个元素是[开盘, 收盘, 最低, 最高]
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
                'type': 'cross'
            }
        },
        'legend': {
            'data': ['K线'],
            'top': 'bottom'
        },
        'grid': {
            'left': '10%',
            'right': '10%',
            'bottom': '15%'
        },
        'xAxis': {
            'type': 'category',
            'data': list(range(len(data))),
            'scale': True,
            'boundaryGap': False,
            'axisLine': {'onZero': False},
            'splitLine': {'show': False},
            'min': 'dataMin',
            'max': 'dataMax'
        },
        'yAxis': {
            'scale': True,
            'splitArea': {
                'show': True
            }
        },
        'dataZoom': [
            {
                'type': 'inside',
                'start': 50,
                'end': 100
            },
            {
                'show': True,
                'type': 'slider',
                'top': '90%',
                'start': 50,
                'end': 100
            }
        ],
        'series': [{
            'name': 'K线',
            'type': 'candlestick',
            'data': data,
            'itemStyle': {
                'color': '#ec0000',
                'color0': '#00da3c',
                'borderColor': '#8A0000',
                'borderColor0': '#008F28'
            }
        }]
    }


def brush_candlestick_chart(data: List[List[float]],
                          title: str = "K线图刷选") -> Dict[str, Any]:
    """
    K线图刷选
    
    Args:
        data: K线数据，每个元素是[开盘, 收盘, 最低, 最高]
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
                'type': 'cross'
            }
        },
        'legend': {
            'data': ['K线'],
            'top': 'bottom'
        },
        'grid': {
            'left': '10%',
            'right': '10%',
            'bottom': '15%'
        },
        'xAxis': {
            'type': 'category',
            'data': list(range(len(data))),
            'scale': True,
            'boundaryGap': False,
            'axisLine': {'onZero': False},
            'splitLine': {'show': False},
            'min': 'dataMin',
            'max': 'dataMax'
        },
        'yAxis': {
            'scale': True,
            'splitArea': {
                'show': True
            }
        },
        'brush': {
            'xAxisIndex': 0,
            'brushLink': 'all'
        },
        'dataZoom': [
            {
                'type': 'inside',
                'start': 50,
                'end': 100
            },
            {
                'show': True,
                'type': 'slider',
                'top': '90%',
                'start': 50,
                'end': 100
            }
        ],
        'series': [{
            'name': 'K线',
            'type': 'candlestick',
            'data': data,
            'itemStyle': {
                'color': '#ec0000',
                'color0': '#00da3c',
                'borderColor': '#8A0000',
                'borderColor0': '#008F28'
            }
        }]
    }


def broken_axis_candlestick_chart(data: List[List[float]],
                               title: str = "断轴上的日内走势图") -> Dict[str, Any]:
    """
    断轴上的日内走势图
    
    Args:
        data: K线数据，每个元素是[开盘, 收盘, 最低, 最高]
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
                'type': 'cross'
            }
        },
        'legend': {
            'data': ['K线'],
            'top': 'bottom'
        },
        'grid': [
            {
                'left': '10%',
                'right': '8%',
                'height': '35%'
            },
            {
                'left': '10%',
                'right': '8%',
                'top': '55%',
                'height': '35%'
            }
        ],
        'xAxis': [
            {
                'type': 'category',
                'data': list(range(len(data))),
                'scale': True,
                'boundaryGap': False,
                'axisLine': {'onZero': False},
                'splitLine': {'show': False},
                'min': 'dataMin',
                'max': 'dataMax'
            },
            {
                'type': 'category',
                'gridIndex': 1,
                'data': list(range(len(data))),
                'scale': True,
                'boundaryGap': False,
                'axisLine': {'onZero': False},
                'axisTick': {'show': False},
                'splitLine': {'show': False},
                'axisLabel': {'show': False},
                'min': 'dataMin',
                'max': 'dataMax'
            }
        ],
        'yAxis': [
            {
                'scale': True,
                'splitArea': {
                    'show': True
                }
            },
            {
                'scale': True,
                'gridIndex': 1,
                'splitNumber': 2,
                'axisLabel': {'show': False},
                'axisLine': {'show': False},
                'axisTick': {'show': False},
                'splitLine': {'show': False}
            }
        ],
        'dataZoom': [
            {
                'type': 'inside',
                'xAxisIndex': [0, 1],
                'start': 50,
                'end': 100
            },
            {
                'show': True,
                'xAxisIndex': [0, 1],
                'type': 'slider',
                'top': '95%',
                'start': 50,
                'end': 100
            }
        ],
        'series': [{
            'name': 'K线',
            'type': 'candlestick',
            'data': data,
            'itemStyle': {
                'color': '#ec0000',
                'color0': '#00da3c',
                'borderColor': '#8A0000',
                'borderColor0': '#008F28'
            }
        }]
    }
