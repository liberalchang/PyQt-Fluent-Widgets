# coding:utf-8
"""
仪表盘预设配置
包含：基础仪表盘、带标签数字动画的基础仪表盘、速度仪表盘、等级仪表盘
"""

from typing import Dict, Any


def basic_gauge_chart(value: float,
                     title: str = "基础仪表盘",
                     min_value: float = 0,
                     max_value: float = 100) -> Dict[str, Any]:
    """
    基础仪表盘
    
    Args:
        value: 当前值
        title: 图表标题
        min_value: 最小值
        max_value: 最大值
        
    Returns:
        ECharts配置字典
    """
    return {
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


def animated_gauge_chart(value: float,
                      title: str = "带标签数字动画的基础仪表盘",
                      min_value: float = 0,
                      max_value: float = 100) -> Dict[str, Any]:
    """
    带标签数字动画的基础仪表盘
    
    Args:
        value: 当前值
        title: 图表标题
        min_value: 最小值
        max_value: 最大值
        
    Returns:
        ECharts配置字典
    """
    return {
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
                'formatter': '{value}%',
                'fontSize': 20,
                'offsetCenter': [0, '70%']
            },
            'axisLine': {
                'lineStyle': {
                    'width': 20,
                    'color': [
                        [0.3, '#ff6e76'],
                        [0.7, '#fddd60'],
                        [1, '#58d9f9']
                    ]
                }
            },
            'pointer': {
                'itemStyle': {
                    'color': 'auto'
                }
            },
            'axisTick': {
                'distance': -20,
                'length': 8,
                'lineStyle': {
                    'color': '#fff',
                    'width': 2
                }
            },
            'splitLine': {
                'distance': -20,
                'length': 20,
                'lineStyle': {
                    'color': '#fff',
                    'width': 4
                }
            },
            'axisLabel': {
                'color': 'inherit',
                'distance': 30,
                'fontSize': 12
            },
            'title': {
                'fontSize': 14
            },
            'detail': {  # noqa: F601
                'fontSize': 30,
                'offsetCenter': [0, '70%'],
                'valueAnimation': True,
                'formatter': function_value_formatter,
                'color': 'inherit'
            }
        }]
    }


def speed_gauge_chart(value: float,
                    title: str = "速度仪表盘",
                    max_speed: float = 200) -> Dict[str, Any]:
    """
    速度仪表盘
    
    Args:
        value: 当前速度
        title: 图表标题
        max_speed: 最大速度
        
    Returns:
        ECharts配置字典
    """
    return {
        'title': {
            'text': title,
            'left': 'center'
        },
        'series': [{
            'type': 'gauge',
            'center': ['50%', '60%'],
            'startAngle': 200,
            'endAngle': -20,
            'min': 0,
            'max': max_speed,
            'splitNumber': 12,
            'itemStyle': {
                'color': '#FFAB91'
            },
            'progress': {
                'show': True,
                'width': 30
            },
            'pointer': {
                'show': False
            },
            'axisLine': {
                'lineStyle': {
                    'width': 30
                }
            },
            'axisTick': {
                'distance': -45,
                'splitNumber': 5,
                'lineStyle': {
                    'width': 2,
                    'color': '#999'
                }
            },
            'splitLine': {
                'distance': -52,
                'length': 14,
                'lineStyle': {
                    'width': 3,
                    'color': '#999'
                }
            },
            'axisLabel': {
                'distance': -20,
                'color': '#999',
                'fontSize': 20
            },
            'anchor': {
                'show': False
            },
            'title': {
                'show': False
            },
            'detail': {
                'valueAnimation': True,
                'width': '60%',
                'lineHeight': 40,
                'borderRadius': 8,
                'offsetCenter': [0, '-15%'],
                'fontSize': 60,
                'fontWeight': 'bolder',
                'formatter': '{value} km/h',
                'color': 'inherit'
            },
            'data': [{
                'value': value,
                'name': '速度'
            }]
        }]
    }


def level_gauge_chart(value: float,
                    title: str = "等级仪表盘") -> Dict[str, Any]:
    """
    等级仪表盘
    
    Args:
        value: 当前值
        title: 图表标题
        
    Returns:
        ECharts配置字典
    """
    return {
        'title': {
            'text': title,
            'left': 'center'
        },
        'series': [{
            'type': 'gauge',
            'data': [{'value': value, 'name': '等级'}],
            'min': 0,
            'max': 5,
            'splitNumber': 5,
            'axisLine': {
                'lineStyle': {
                    'width': 18,
                    'color': [
                        [0.2, '#ff4757'],
                        [0.4, '#ffa502'],
                        [0.6, '#fffa65'],
                        [0.8, '#32ff7e'],
                        [1, '#18dcff']
                    ]
                }
            },
            'pointer': {
                'itemStyle': {
                    'color': 'auto'
                }
            },
            'axisTick': {
                'distance': -20,
                'length': 8,
                'lineStyle': {
                    'color': '#fff',
                    'width': 2
                }
            },
            'splitLine': {
                'distance': -20,
                'length': 20,
                'lineStyle': {
                    'color': '#fff',
                    'width': 4
                }
            },
            'axisLabel': {
                'color': 'auto',
                'distance': 30,
                'fontSize': 12,
                'formatter': function_level_formatter
            },
            'title': {
                'fontSize': 14
            },
            'detail': {
                'fontSize': 20,
                'offsetCenter': [0, '70%'],
                'valueAnimation': True,
                'formatter': function_level_detail,
                'color': 'auto'
            }
        }]
    }


# JavaScript 函数定义
function_value_formatter = """
function(value) {
    return value.toFixed(1);
}
"""

function_level_formatter = """
function(value) {
    return 'Level ' + value;
}
"""

function_level_detail = """
function(value) {
    if (value < 1) {
        return 'Poor';
    } else if (value < 2) {
        return 'Fair';
    } else if (value < 3) {
        return 'Good';
    } else if (value < 4) {
        return 'Very Good';
    } else {
        return 'Excellent';
    }
}
"""
