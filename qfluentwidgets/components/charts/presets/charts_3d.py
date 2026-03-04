# coding:utf-8
"""
3D图表预设配置
包含：3D地球、3D柱状图、3D散点图、3D曲面、3D折线图、GL散点图、GL路径图、GL矢量场图
"""

from typing import List, Dict, Any


def earth_3d_chart(title: str = "3D地球") -> Dict[str, Any]:
    """
    3D地球（大气层显示）
    
    Args:
        title: 图表标题
        
    Returns:
        ECharts配置字典
    """
    return {
        'title': {
            'text': title,
            'left': 'center'
        },
        'geo3D': {
            'map': 'world',
            'shading': 'realistic',
            'light': {
                'main': {
                    'intensity': 2,
                    'shadow': True,
                    'shadowQuality': 'high',
                    'alpha': 30
                },
                'ambient': {
                    'intensity': 0
                }
            },
            'viewControl': {
                'distance': 50,
                'alpha': 40,
                'beta': 40,
                'center': [0, 0, 0]
            },
            'postEffect': {
                'enable': True,
                'bloom': {
                    'enable': True
                }
            },
            'temporalSuperSampling': {
                'enable': True
            },
            'layerTexture': {
                'texture': 'asset/earth.jpg'
            },
            'atmosphere': {
                'show': True
            }
        },
        'series': []
    }


def bar_3d_chart(data: List[List[float]],
               title: str = "3D柱状图") -> Dict[str, Any]:
    """
    3D柱状图
    
    Args:
        data: 3D数据，每个元素是[x, y, z]坐标
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
        'visualMap': {
            'max': 100,
            'color': ['#d94e5d', '#eac736', '#50a3ba'].reverse()
        },
        'xAxis3D': {
            'type': 'category',
            'data': ['A', 'B', 'C', 'D', 'E']
        },
        'yAxis3D': {
            'type': 'category',
            'data': ['1', '2', '3', '4', '5']
        },
        'zAxis3D': {
            'type': 'value'
        },
        'grid3D': {
            'boxWidth': 200,
            'boxDepth': 80,
            'viewControl': {
                'distance': 200,
                'alpha': 20,
                'beta': 40,
                'autoRotate': True
            },
            'light': {
                'main': {
                    'intensity': 1.2,
                    'shadow': True
                },
                'ambient': {
                    'intensity': 0.3
                }
            }
        },
        'series': [{
            'type': 'bar3D',
            'data': data,
            'shading': 'lambert',
            'label': {
                'show': False
            },
            'itemStyle': {
                'opacity': 0.8
            },
            'emphasis': {
                'label': {
                    'show': True
                }
            }
        }]
    }


def scatter_3d_chart(data: List[List[float]],
                    title: str = "3D散点图") -> Dict[str, Any]:
    """
    3D散点图
    
    Args:
        data: 3D散点数据，每个元素是[x, y, z]坐标
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
        'xAxis3D': {
            'type': 'value',
            'name': 'X轴'
        },
        'yAxis3D': {
            'type': 'value',
            'name': 'Y轴'
        },
        'zAxis3D': {
            'type': 'value',
            'name': 'Z轴'
        },
        'grid3D': {
            'viewControl': {
                'distance': 200,
                'alpha': 20,
                'beta': 40,
                'autoRotate': True
            }
        },
        'series': [{
            'type': 'scatter3D',
            'data': data,
            'symbolSize': 8,
            'itemStyle': {
                'color': '#5470c6'
            }
        }]
    }


def surface_3d_chart(data: List[List[float]],
                   title: str = "3D曲面") -> Dict[str, Any]:
    """
    3D曲面
    
    Args:
        data: 曲面数据矩阵
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
        'visualMap': {
            'show': False,
            'dimension': 2,
            'min': 0,
            'max': 10,
            'inRange': {
                'color': ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
            }
        },
        'xAxis3D': {
            'type': 'value'
        },
        'yAxis3D': {
            'type': 'value'
        },
        'zAxis3D': {
            'type': 'value'
        },
        'grid3D': {
            'viewControl': {
                'distance': 100,
                'alpha': 40,
                'beta': 40
            }
        },
        'series': [{
            'type': 'surface',
            'data': data,
            'shading': 'color'
        }]
    }


def line_3d_chart(data: List[List[float]],
                title: str = "3D折线图") -> Dict[str, Any]:
    """
    3D折线图
    
    Args:
        data: 3D折线数据，每个元素是[x, y, z]坐标
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
        'xAxis3D': {
            'type': 'value',
            'name': 'X轴'
        },
        'yAxis3D': {
            'type': 'value',
            'name': 'Y轴'
        },
        'zAxis3D': {
            'type': 'value',
            'name': 'Z轴'
        },
        'grid3D': {
            'viewControl': {
                'distance': 200,
                'alpha': 20,
                'beta': 40
            }
        },
        'series': [{
            'type': 'line3D',
            'data': data,
            'lineStyle': {
                'width': 4,
                'color': '#5470c6'
            }
        }]
    }


def gl_scatter_chart(data: List[List[float]],
                   title: str = "GL散点图") -> Dict[str, Any]:
    """
    GL散点图
    
    Args:
        data: 散点数据，每个元素是[x, y, z]坐标
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
        'xAxis3D': {
            'type': 'value'
        },
        'yAxis3D': {
            'type': 'value'
        },
        'zAxis3D': {
            'type': 'value'
        },
        'grid3D': {
            'viewControl': {
                'distance': 200,
                'alpha': 20,
                'beta': 40
            }
        },
        'series': [{
            'type': 'scatterGL',
            'data': data,
            'symbolSize': 8,
            'itemStyle': {
                'color': '#5470c6'
            }
        }]
    }


def gl_path_chart(data: List[List[float]],
                title: str = "GL路径图") -> Dict[str, Any]:
    """
    GL路径图
    
    Args:
        data: 路径数据，每个元素是[x, y]坐标
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
        'xAxis': {
            'type': 'value'
        },
        'yAxis': {
            'type': 'value'
        },
        'series': [{
            'type': 'linesGL',
            'data': data,
            'lineStyle': {
                'width': 3,
                'color': '#5470c6'
            }
        }]
    }


def gl_vector_field_chart(data: List[List[float]],
                       title: str = "GL矢量场图") -> Dict[str, Any]:
    """
    GL矢量场图
    
    Args:
        data: 矢量场数据，每个元素是[x, y, vx, vy]
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
        'xAxis': {
            'type': 'value'
        },
        'yAxis': {
            'type': 'value'
        },
        'series': [{
            'type': 'flowGL',
            'data': data,
            'particleSize': 5,
            'particleSpeed': 1,
            'particleDensity': 0.8,
            'itemStyle': {
                'color': '#5470c6'
            }
        }]
    }
