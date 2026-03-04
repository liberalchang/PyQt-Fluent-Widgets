# coding:utf-8
"""
树状图和矩形树图预设配置
包含：从左到右树状图、矩形树图和旭日图的动画过渡
"""

from typing import List, Dict, Any


def left_to_right_tree_chart(data: Dict[str, Any],
                           title: str = "从左到右树状图") -> Dict[str, Any]:
    """
    从左到右树状图
    
    Args:
        data: 树状数据，包含name、children等
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
            'triggerOn': 'mousemove'
        },
        'series': [{
            'type': 'tree',
            'data': [data],
            'top': '10%',
            'left': '8%',
            'bottom': '8%',
            'right': '20%',
            'symbolSize': 7,
            'orient': 'LR',
            'label': {
                'position': 'left',
                'verticalAlign': 'middle',
                'align': 'right',
                'fontSize': 9
            },
            'leaves': {
                'label': {
                    'position': 'right',
                    'verticalAlign': 'middle',
                    'align': 'left'
                }
            },
            'emphasis': {
                'focus': 'descendant'
            },
            'expandAndCollapse': True,
            'animationDuration': 550,
            'animationDurationUpdate': 750
        }]
    }


def treemap_chart(data: List[Dict[str, Any]],
                title: str = "矩形树图") -> Dict[str, Any]:
    """
    矩形树图
    
    Args:
        data: 树状数据列表
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
            'formatter': '{b}: {c}'
        },
        'series': [{
            'type': 'treemap',
            'data': data,
            'label': {
                'show': True,
                'formatter': '{b}'
            },
            'itemStyle': {
                'borderColor': '#fff'
            },
            'levels': [
                {
                    'itemStyle': {
                        'borderColor': '#777',
                        'borderWidth': 0,
                        'gapWidth': 1
                    }
                },
                {
                    'itemStyle': {
                        'borderColorSaturate': True,
                        'borderColor': '#555',
                        'borderWidth': 5,
                        'gapWidth': 1
                    },
                    'emphasis': {
                        'itemStyle': {
                            'borderColor': '#ddd'
                        }
                    }
                }
            ]
        }]
    }


def sunburst_transition_chart(data: Dict[str, Any],
                           title: str = "旭日图动画过渡") -> Dict[str, Any]:
    """
    矩形树图和旭日图的动画过渡
    
    Args:
        data: 旭日图数据
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
            'formatter': '{a} <br/>{b}: {c}'
        },
        'series': [{
            'type': 'sunburst',
            'data': data,
            'radius': [0, '90%'],
            'label': {
                'rotate': 'radial'
            },
            'itemStyle': {
                'borderRadius': 7,
                'borderColor': '#fff',
                'borderWidth': 2
            },
            'levels': [
                {},
                {
                    'r0': '15%',
                    'r': '35%',
                    'itemStyle': {
                        'borderWidth': 2
                    },
                    'label': {
                        'rotate': 'tangential'
                    }
                },
                {
                    'r0': '35%',
                    'r': '70%',
                    'label': {
                        'align': 'right'
                    }
                },
                {
                    'r0': '70%',
                    'r': '72%',
                    'label': {
                        'position': 'outside',
                        'padding': 3,
                        'silent': False
                    },
                    'itemStyle': {
                        'borderWidth': 3
                    }
                }
            ]
        }]
    }
