# coding:utf-8
"""
散点图预设配置
包含：基础散点图、数据聚合、线性回归（使用统计插件）
"""

from typing import List, Dict, Any


def basic_scatter_chart(data: List[List[float]],
                      title: str = "基础散点图",
                      color: str = "#5470c6") -> Dict[str, Any]:
    """
    基础散点图
    
    Args:
        data: 散点数据，每个元素是[x, y]坐标
        title: 图表标题
        color: 散点颜色
        
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
            'formatter': function_formatter
        },
        'xAxis': {
            'type': 'value',
            'scale': True
        },
        'yAxis': {
            'type': 'value',
            'scale': True
        },
        'series': [{
            'data': data,
            'type': 'scatter',
            'symbolSize': 8,
            'itemStyle': {
                'color': color
            }
        }]
    }


def aggregated_scatter_chart(data: List[List[float]],
                           title: str = "数据聚合散点图") -> Dict[str, Any]:
    """
    数据聚合散点图
    
    Args:
        data: 散点数据，每个元素是[x, y]坐标
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
            'trigger': 'item',
            'formatter': function_formatter
        },
        'xAxis': {
            'type': 'value',
            'scale': True
        },
        'yAxis': {
            'type': 'value',
            'scale': True
        },
        'series': [{
            'data': data,
            'type': 'scatter',
            'symbolSize': function_symbol_size,
            'itemStyle': {
                'color': '#5470c6'
            }
        }]
    }


def regression_scatter_chart(data: List[List[float]],
                           regression_data: List[List[float]],
                           title: str = "线性回归散点图") -> Dict[str, Any]:
    """
    线性回归散点图（使用统计插件）
    
    Args:
        data: 散点数据，每个元素是[x, y]坐标
        regression_data: 回归线数据，每个元素是[x, y]坐标
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
            'trigger': 'item',
            'formatter': function_formatter
        },
        'xAxis': {
            'type': 'value',
            'scale': True
        },
        'yAxis': {
            'type': 'value',
            'scale': True
        },
        'series': [
            {
                'name': '数据点',
                'data': data,
                'type': 'scatter',
                'symbolSize': 8,
                'itemStyle': {
                    'color': '#5470c6'
                }
            },
            {
                'name': '回归线',
                'data': regression_data,
                'type': 'line',
                'smooth': True,
                'lineStyle': {
                    'color': '#ee6666',
                    'width': 2
                },
                'itemStyle': {
                    'color': '#ee6666'
                }
            }
        ]
    }


# JavaScript 函数定义
function_formatter = """
function(params) {
    return 'X: ' + params.value[0] + '<br/>Y: ' + params.value[1];
}
"""

function_symbol_size = """
function(data) {
    return Math.sqrt(data[2]) * 2;
}
"""
