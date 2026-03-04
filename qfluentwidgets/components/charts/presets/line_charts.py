# coding:utf-8
"""
折线图预设配置
包含：基础折线图、基础平滑折线图、基础面积图、堆叠折线图
"""

from typing import List, Dict, Any


def basic_line_chart(x_data: List[str], y_data: List[float], 
                    title: str = "基础折线图", 
                    color: str = "#5470c6") -> Dict[str, Any]:
    """
    基础折线图
    
    Args:
        x_data: x轴数据
        y_data: y轴数据  
        title: 图表标题
        color: 线条颜色
        
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
            'type': 'line',
            'itemStyle': {
                'color': color
            }
        }]
    }


def smooth_line_chart(x_data: List[str], y_data: List[float],
                    title: str = "基础平滑折线图",
                    color: str = "#91cc75") -> Dict[str, Any]:
    """
    基础平滑折线图
    
    Args:
        x_data: x轴数据
        y_data: y轴数据
        title: 图表标题
        color: 线条颜色
        
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
            'type': 'line',
            'smooth': True,
            'itemStyle': {
                'color': color
            }
        }]
    }


def area_chart(x_data: List[str], y_data: List[float],
              title: str = "基础面积图",
              color: str = "#fac858") -> Dict[str, Any]:
    """
    基础面积图
    
    Args:
        x_data: x轴数据
        y_data: y轴数据
        title: 图表标题
        color: 填充颜色
        
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
            'type': 'line',
            'areaStyle': {
                'color': color + '33'  # 添加透明度
            },
            'itemStyle': {
                'color': color
            }
        }]
    }


def stacked_line_chart(x_data: List[str], series_data: List[Dict[str, Any]],
                     title: str = "堆叠折线图") -> Dict[str, Any]:
    """
    堆叠折线图
    
    Args:
        x_data: x轴数据
        series_data: 系列数据列表，每个元素包含name和data
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
            'trigger': 'axis'
        },
        'legend': {
            'data': [series['name'] for series in series_data],
            'top': 'bottom'
        },
        'xAxis': {
            'type': 'category',
            'data': x_data
        },
        'yAxis': {
            'type': 'value'
        },
        'series': [
            {
                'name': series['name'],
                'data': series['data'],
                'type': 'line',
                'stack': 'total',
                'areaStyle': {},
                'itemStyle': {
                    'color': series.get('color', '#5470c6')
                }
            }
            for series in series_data
        ]
    }
