# coding:utf-8
"""
Vispy 组件模块

提供基于 Vispy 的高性能 2D/3D 可视化组件，支持：
- 2D/3D 场景渲染
- 实时数据可视化
- 交互式相机控制
- 丰富的图形元素
- 交互式绘图框架
"""

from .vispy_canvas import VispyCanvas2D, VispyCanvas3D, VISPY_AVAILABLE, initialize_vispy
from .vispy_widget import VispyWidget2D, VispyWidget3D
from .vispy_visuals import VisualEntry, MarkersEntry, LineEntry, MeshEntry
from .drawing_view import DrawingView
from .drawing import (
    InteractiveDrawingWidget,
    InteractionMode,
    StyleData,
    PrimitiveData,
    LineData,
    BezierData,
    ArcData,
    CircleData,
    RectangleData,
    PolygonData,
    MarkersData,
    ImageData,
    Primitive,
    PrimitiveGroup,
    Layer,
    LayerManager
)

__all__ = [
    # Canvas 层
    'VispyCanvas2D',
    'VispyCanvas3D', 
    'VISPY_AVAILABLE',
    'initialize_vispy',
    
    # Widget 层
    'VispyWidget2D',
    'VispyWidget3D',
    'DrawingView',
    
    # Visual 元素
    'VisualEntry',
    'MarkersEntry', 
    'LineEntry',
    'MeshEntry',
    
    # 交互式绘图
    'InteractiveDrawingWidget',
    'InteractionMode',
    
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
    
    # 层级管理
    'Primitive',
    'PrimitiveGroup',
    'Layer',
    'LayerManager',
]
