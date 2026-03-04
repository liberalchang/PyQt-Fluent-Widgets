# coding:utf-8
"""
雷达图预设配置
包含：基础雷达图、AQI雷达图
"""

from typing import List, Dict, Any


def basic_radar_chart(data: List[Dict[str, Any]],
                    indicators: List[Dict[str, Any]],
                    title: str = "基础雷达图") -> Dict[str, Any]:
    """
    基础雷达图
    
    Args:
        data: 数据列表，每个元素包含name和value
        indicators: 指标配置，每个元素包含name和max
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
            'trigger': 'item'
        },
        'legend': {
            'data': [item['name'] for item in data],
            'top': 'bottom'
        },
        'radar': {
            'indicator': indicators
        },
        'series': [{
            'type': 'radar',
            'data': data
        }]
    }


def aqi_radar_chart(data: List[Dict[str, Any]],
                   title: str = "AQI雷达图") -> Dict[str, Any]:
    """
    AQI雷达图
    
    Args:
        data: 数据列表，每个元素包含name和value
        title: 图表标题
        
    Returns:
        ECharts配置字典
    """
    indicators = [
        {'name': 'PM2.5', 'max': 300},
        {'name': 'PM10', 'max': 400},
        {'name': 'SO2', 'max': 200},
        {'name': 'NO2', 'max': 200},
        {'name': 'O3', 'max': 300},
        {'name': 'CO', 'max': 50}
    ]
    
    return {
        'title': {
            'text': title,
            'left': 'center'
        },
        'tooltip': {
            'trigger': 'item'
        },
        'legend': {
            'data': [item['name'] for item in data],
            'top': 'bottom'
        },
        'radar': {
            'indicator': indicators,
            'shape': 'polygon',
            'splitNumber': 5,
            'axisName': {
                'color': 'rgb(238, 197, 102)'
            },
            'splitLine': {
                'lineStyle': {
                    'color': [
                        'rgba(238, 197, 102, 0.1)',
                        'rgba(238, 197, 102, 0.2)',
                        'rgba(238, 197, 102, 0.3)',
                        'rgba(238, 197, 102, 0.4)',
                        'rgba(238, 197, 102, 0.5)'
                    ].reverse()
                }
            },
            'splitArea': {
                'show': True,
                'areaStyle': {
                    'color': [
                        'rgba(238, 197, 102, 0.1)',
                        'rgba(238, 197, 102, 0.2)',
                        'rgba(238, 197, 102, 0.3)',
                        'rgba(238, 197, 102, 0.4)',
                        'rgba(238, 197, 102, 0.5)'
                    ].reverse()
                }
            },
            'axisLine': {
                'lineStyle': {
                    'color': 'rgba(238, 197, 102, 0.5)'
                }
            }
        },
        'series': [{
            'type': 'radar',
            'data': data,
            'lineStyle': {
                'width': 2
            },
            'symbol': 'circle',
            'symbolSize': 8,
            'itemStyle': {
                'color': '#F9713C'
            },
            'areaStyle': {
                'color': 'rgba(249, 113, 60, 0.3)'
            }
        }]
    }
