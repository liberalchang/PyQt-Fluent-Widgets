# coding:utf-8
"""
地理坐标/地图预设配置
包含：地图（SVG）
"""

from typing import List, Dict, Any


def svg_map_chart(svg_data: str,
                 title: str = "SVG地图") -> Dict[str, Any]:
    """
    SVG地图
    
    Args:
        svg_data: SVG地图数据
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
        'geo': {
            'map': 'custom_map',
            'roam': True,
            'itemStyle': {
                'color': '#eee'
            },
            'emphasis': {
                'itemStyle': {
                    'color': '#5470c6'
                }
            }
        },
        'series': [{
            'type': 'custom',
            'coordinateSystem': 'geo',
            'data': [],
            'renderItem': render_item_function
        }]
    }


def geo_scatter_chart(geo_data: List[Dict[str, Any]],
                    title: str = "地理散点图") -> Dict[str, Any]:
    """
    地理散点图
    
    Args:
        geo_data: 地理数据，每个元素包含name、value、coords
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
        'geo': {
            'map': 'china',
            'roam': True,
            'itemStyle': {
                'color': '#eee'
            },
            'emphasis': {
                'itemStyle': {
                    'color': '#5470c6'
                }
            }
        },
        'series': [{
            'name': '地理数据',
            'type': 'scatter',
            'coordinateSystem': 'geo',
            'data': geo_data,
            'symbolSize': function_symbol_size,
            'itemStyle': {
                'color': '#ee6666'
            }
        }]
    }


# JavaScript 函数定义
render_item_function = """
function(params, api) {
    return {
        type: 'path',
        shape: {
            pathData: params.pathData
        },
        style: api.style({
            stroke: '#5470c6',
            lineWidth: 1
        })
    };
}
"""

function_symbol_size = """
function(val) {
    return val[2] / 10;
}
"""
