# coding:utf-8
"""
交互式绘图模块

提供基于 Vispy 的交互式 2D 绘图功能，支持：
- 多种基础图元（线条、贝塞尔曲线、圆弧、矩形、多边形等）
- 样式控制（线宽、颜色、填充）
- 交互管理（绘制、选择、移动等模式）
- 图层管理（三级层级结构）
- 坐标系统（屏幕坐标与世界坐标转换）
"""

from .data_models import (
    StyleData,
    PrimitiveData,
    LineData,
    BezierData,
    ArcData,
    CircleData,
    RectangleData,
    PolygonData,
    MarkersData,
    ImageData
)

from .drawing_widget import InteractiveDrawingWidget
from .interaction_manager import InteractionMode
from .layer_manager import Primitive, PrimitiveGroup, Layer, LayerManager

__all__ = [
    # 数据模型
    'StyleData',
    'PrimitiveData',
    'LineData',
    'BezierData',
    'ArcData',
    'CircleData',
    'RectangleData',
    'PolygonData',
    'MarkersData',
    'ImageData',
    
    # 主控件
    'InteractiveDrawingWidget',
    
    # 交互模式
    'InteractionMode',
    
    # 层级管理
    'Primitive',
    'PrimitiveGroup',
    'Layer',
    'LayerManager',
]
