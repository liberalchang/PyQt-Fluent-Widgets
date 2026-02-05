Vispy 可视化组件 (Vispy)
=======================

本节介绍 PySide6-Fluent-Widgets 中的 Vispy 可视化组件。

Canvas 层组件
--------------

VispyCanvas2D
-------------

2D 可视化画布，基于 Vispy 的 2D 渲染画布。

.. code-block:: python

   from qfluentwidgets import VispyCanvas2D, VISPY_AVAILABLE, initialize_vispy

   # 检查 Vispy 可用性
   if VISPY_AVAILABLE:
       # 初始化 Vispy
       initialize_vispy()
       
       # 创建 2D 画布
       canvas = VispyCanvas2D()
       canvas.setFixedSize(600, 400)

VispyCanvas3D
-------------

3D 可视化画布，基于 Vispy 的 3D 渲染画布。

.. code-block:: python

   from qfluentwidgets import VispyCanvas3D

   # 创建 3D 画布
   canvas = VispyCanvas3D()
   canvas.setFixedSize(600, 400)

Widget 层组件
--------------

VispyWidget2D
-------------

2D 可视化组件，基于 Vispy 的 2D 图形组件。

.. code-block:: python

   from qfluentwidgets import VispyWidget2D
   import numpy as np

   # 创建 2D 可视化组件
   vispy_2d = VispyWidget2D()
   vispy_2d.setFixedSize(600, 400)
   
   # 添加数据点
   x = np.linspace(0, 10, 100)
   y = np.sin(x)
   vispy_2d.plot(x, y, color='red', linewidth=2)

VispyWidget3D
-------------

3D 可视化组件，支持 3D 图形渲染。

.. code-block:: python

   from qfluentwidgets import VispyWidget3D
   import numpy as np

   # 创建 3D 可视化组件
   vispy_3d = VispyWidget3D()
   vispy_3d.setFixedSize(600, 400)
   
   # 添加 3D 散点图
   x = np.random.randn(100)
   y = np.random.randn(100)
   z = np.random.randn(100)
   vispy_3d.scatter(x, y, z, color='blue', size=5)

DrawingView
-----------

绘图视图，支持交互式绘图。

.. code-block:: python

   from qfluentwidgets import DrawingView

   # 创建绘图视图
   drawing_view = DrawingView()
   drawing_view.setFixedSize(800, 600)

Visual 元素
-----------

VisualEntry
-----------

可视化元素基类。

.. code-block:: python

   from qfluentwidgets import VisualEntry

   # 创建可视化元素
   visual = VisualEntry()
   visual.setData(data)

MarkersEntry
------------

标记元素，用于显示散点数据。

.. code-block:: python

   from qfluentwidgets import MarkersEntry

   # 创建标记元素
   markers = MarkersEntry()
   markers.setData(x_data, y_data, z_data)

LineEntry
---------

线条元素，用于显示线条数据。

.. code-block:: python

   from qfluentwidgets import LineEntry

   # 创建线条元素
   line = LineEntry()
   line.setData(x_data, y_data)

MeshEntry
---------

网格元素，用于显示 3D 网格数据。

.. code-block:: python

   from qfluentwidgets import MeshEntry

   # 创建网格元素
   mesh = MeshEntry()
   mesh.setMesh(vertices, faces)

交互式绘图组件
--------------

InteractiveDrawingWidget
------------------------

交互式绘图组件，支持多种绘图模式。

.. code-block:: python

   from qfluentwidgets import InteractiveDrawingWidget, InteractionMode

   # 创建交互式绘图组件
   drawing_widget = InteractiveDrawingWidget()
   drawing_widget.setInteractionMode(InteractionMode.DRAW)

InteractionMode
---------------

交互模式枚举。

.. code-block:: python

   from qfluentwidgets import InteractionMode

   # 设置交互模式
   mode = InteractionMode.SELECT  # 选择模式
   # mode = InteractionMode.DRAW   # 绘图模式
   # mode = InteractionMode.EDIT   # 编辑模式

数据模型
--------

StyleData
---------

样式数据，定义绘图样式。

.. code-block:: python

   from qfluentwidgets import StyleData

   # 创建样式数据
   style = StyleData()
   style.setColor('#0078d4')
   style.setLineWidth(2.0)

PrimitiveData
-------------

基础图元数据。

.. code-block:: python

   from qfluentwidgets import PrimitiveData

   # 创建基础图元数据
   data = PrimitiveData()
   data.setPoints(points)

LineData
--------

线条数据。

.. code-block:: python

   from qfluentwidgets import LineData

   # 创建线条数据
   line_data = LineData()
   line_data.setPoints(points)
   line_data.setSmooth(True)

BezierData
----------

贝塞尔曲线数据。

.. code-block:: python

   from qfluentwidgets import BezierData

   # 创建贝塞尔曲线数据
   bezier_data = BezierData()
   bezier_data.setControlPoints(control_points)

ArcData
-------

弧形数据。

.. code-block:: python

   from qfluentwidgets import ArcData

   # 创建弧形数据
   arc_data = ArcData()
   arc_data.setCenter(center)
   arc_data.setRadius(radius)
   arc_data.setStartAngle(start_angle)
   arc_data.setEndAngle(end_angle)

CircleData
----------

圆形数据。

.. code-block:: python

   from qfluentwidgets import CircleData

   # 创建圆形数据
   circle_data = CircleData()
   circle_data.setCenter(center)
   circle_data.setRadius(radius)

RectangleData
-------------

矩形数据。

.. code-block:: python

   from qfluentwidgets import RectangleData

   # 创建矩形数据
   rect_data = RectangleData()
   rect_data.setTopLeft(top_left)
   rect_data.setSize(width, height)

PolygonData
-----------

多边形数据。

.. code-block:: python

   from qfluentwidgets import PolygonData

   # 创建多边形数据
   polygon_data = PolygonData()
   polygon_data.setPoints(points)

MarkersData
-----------

标记数据。

.. code-block:: python

   from qfluentwidgets import MarkersData

   # 创建标记数据
   markers_data = MarkersData()
   markers_data.setPoints(points)
   markers_data.setSizes(sizes)

ImageData
---------

图像数据。

.. code-block:: python

   from qfluentwidgets import ImageData

   # 创建图像数据
   image_data = ImageData()
   image_data.setImage(image_array)

层级管理
--------

Primitive
----------

基础图元。

.. code-block:: python

   from qfluentwidgets import Primitive

   # 创建基础图元
   primitive = Primitive()
   primitive.setData(data)
   primitive.setStyle(style)

PrimitiveGroup
--------------

图元组。

.. code-block:: python

   from qfluentwidgets import PrimitiveGroup

   # 创建图元组
   group = PrimitiveGroup()
   group.addPrimitive(primitive1)
   group.addPrimitive(primitive2)

Layer
-----

图层。

.. code-block:: python

   from qfluentwidgets import Layer

   # 创建图层
   layer = Layer()
   layer.setName('图层名称')
   layer.setVisible(True)

LayerManager
------------

图层管理器。

.. code-block:: python

   from qfluentwidgets import LayerManager

   # 创建图层管理器
   layer_manager = LayerManager()
   layer_manager.addLayer(layer1)
   layer_manager.addLayer(layer2)

完整示例
--------

下面是一个完整的 Vispy 可视化组件使用示例：

.. code-block:: python

   import sys
   import numpy as np
   from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                                QWidget, QPushButton, QLabel, QTabWidget)
   from PySide6.QtCore import Qt
   from qfluentwidgets import *

   class VispyDemoWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           
           self.setWindowTitle('Vispy 可视化组件示例')
           self.resize(1000, 700)
           
           # 检查 Vispy 可用性
           if not VISPY_AVAILABLE:
               self.show_error('Vispy 未安装，请先安装: pip install vispy')
               return
           
           # 初始化 Vispy
           initialize_vispy()
           
           # 创建界面
           self.setup_ui()

       def setup_ui(self):
           """设置界面"""
           central_widget = QWidget()
           self.setCentralWidget(central_widget)
           
           layout = QVBoxLayout(central_widget)
           
           # 添加标题
           title = SubtitleLabel('Vispy 可视化组件示例')
           layout.addWidget(title)
           
           # 创建标签页
           tab_widget = QTabWidget()
           
           # 2D 可视化标签页
           self.setup_2d_tab(tab_widget)
           
           # 3D 可视化标签页
           self.setup_3d_tab(tab_widget)
           
           # 交互式绘图标签页
           self.setup_drawing_tab(tab_widget)
           
           layout.addWidget(tab_widget)

       def setup_2d_tab(self, tab_widget):
           """设置 2D 可视化标签页"""
           tab = QWidget()
           tab_layout = QVBoxLayout(tab)
           
           # 创建 2D 可视化组件
           self.vispy_2d = VispyWidget2D()
           self.vispy_2d.setFixedSize(800, 500)
           tab_layout.addWidget(self.vispy_2d)
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           sin_btn = PrimaryPushButton('绘制正弦波')
           sin_btn.clicked.connect(self.plot_sine)
           
           scatter_btn = PushButton('绘制散点图')
           scatter_btn.clicked.connect(self.plot_scatter_2d)
           
           clear_btn = PushButton('清除')
           clear_btn.clicked.connect(self.clear_2d)
           
           button_layout.addWidget(sin_btn)
           button_layout.addWidget(scatter_btn)
           button_layout.addWidget(clear_btn)
           button_layout.addStretch()
           
           tab_layout.addLayout(button_layout)
           
           tab_widget.addTab(tab, '2D 可视化')

       def setup_3d_tab(self, tab_widget):
           """设置 3D 可视化标签页"""
           tab = QWidget()
           tab_layout = QVBoxLayout(tab)
           
           # 创建 3D 可视化组件
           self.vispy_3d = VispyWidget3D()
           self.vispy_3d.setFixedSize(800, 500)
           tab_layout.addWidget(self.vispy_3d)
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           surface_btn = PrimaryPushButton('绘制曲面')
           surface_btn.clicked.connect(self.plot_surface)
           
           scatter_3d_btn = PushButton('3D 散点图')
           scatter_3d_btn.clicked.connect(self.plot_scatter_3d)
           
           clear_3d_btn = PushButton('清除')
           clear_3d_btn.clicked.connect(self.clear_3d)
           
           button_layout.addWidget(surface_btn)
           button_layout.addWidget(scatter_3d_btn)
           button_layout.addWidget(clear_3d_btn)
           button_layout.addStretch()
           
           tab_layout.addLayout(button_layout)
           
           tab_widget.addTab(tab, '3D 可视化')

       def setup_drawing_tab(self, tab_widget):
           """设置交互式绘图标签页"""
           tab = QWidget()
           tab_layout = QVBoxLayout(tab)
           
           # 创建交互式绘图组件
           self.drawing_view = DrawingView()
           self.drawing_view.setFixedSize(800, 500)
           tab_layout.addWidget(self.drawing_view)
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           draw_btn = PrimaryPushButton('绘图模式')
           draw_btn.clicked.connect(self.set_draw_mode)
           
           select_btn = PushButton('选择模式')
           select_btn.clicked.connect(self.set_select_mode)
           
           edit_btn = PushButton('编辑模式')
           edit_btn.clicked.connect(self.set_edit_mode)
           
           clear_drawing_btn = PushButton('清除绘图')
           clear_drawing_btn.clicked.connect(self.clear_drawing)
           
           button_layout.addWidget(draw_btn)
           button_layout.addWidget(select_btn)
           button_layout.addWidget(edit_btn)
           button_layout.addWidget(clear_drawing_btn)
           button_layout.addStretch()
           
           tab_layout.addLayout(button_layout)
           
           tab_widget.addTab(tab, '交互式绘图')

       def plot_sine(self):
           """绘制正弦波"""
           x = np.linspace(0, 4 * np.pi, 200)
           y = np.sin(x)
           
           self.vispy_2d.clear()
           self.vispy_2d.plot(x, y, color='blue', linewidth=2)
           self.vispy_2d.set_xlabel('X')
           self.vispy_2d.set_ylabel('Y')
           self.vispy_2d.set_title('正弦波')
           
           InfoBar.success('正弦波绘制完成', parent=self)

       def plot_scatter_2d(self):
           """绘制 2D 散点图"""
           x = np.random.randn(100)
           y = np.random.randn(100)
           colors = np.random.rand(100)
           
           self.vispy_2d.clear()
           self.vispy_2d.scatter(x, y, c=colors, s=50, cmap='viridis')
           self.vispy_2d.set_xlabel('X')
           self.vispy_2d.set_ylabel('Y')
           self.vispy_2d.set_title('2D 散点图')
           
           InfoBar.success('2D 散点图绘制完成', parent=self)

       def clear_2d(self):
           """清除 2D 图形"""
           self.vispy_2d.clear()
           InfoBar.info('2D 图形已清除', parent=self)

       def plot_surface(self):
           """绘制 3D 曲面"""
           x = np.linspace(-5, 5, 50)
           y = np.linspace(-5, 5, 50)
           X, Y = np.meshgrid(x, y)
           Z = np.sin(np.sqrt(X**2 + Y**2))
           
           self.vispy_3d.clear()
           self.vispy_3d.plot_surface(X, Y, Z, cmap='viridis')
           self.vispy_3d.set_xlabel('X')
           self.vispy_3d.set_ylabel('Y')
           self.vispy_3d.set_zlabel('Z')
           self.vispy_3d.set_title('3D 曲面')
           
           InfoBar.success('3D 曲面绘制完成', parent=self)

       def plot_scatter_3d(self):
           """绘制 3D 散点图"""
           x = np.random.randn(200)
           y = np.random.randn(200)
           z = np.random.randn(200)
           colors = np.random.rand(200)
           
           self.vispy_3d.clear()
           self.vispy_3d.scatter(x, y, z, c=colors, s=20, cmap='plasma')
           self.vispy_3d.set_xlabel('X')
           self.vispy_3d.set_ylabel('Y')
           self.vispy_3d.set_zlabel('Z')
           self.vispy_3d.set_title('3D 散点图')
           
           InfoBar.success('3D 散点图绘制完成', parent=self)

       def clear_3d(self):
           """清除 3D 图形"""
           self.vispy_3d.clear()
           InfoBar.info('3D 图形已清除', parent=self)

       def set_draw_mode(self):
           """设置绘图模式"""
           self.drawing_view.setInteractionMode(InteractionMode.DRAW)
           InfoBar.info('已切换到绘图模式', parent=self)

       def set_select_mode(self):
           """设置选择模式"""
           self.drawing_view.setInteractionMode(InteractionMode.SELECT)
           InfoBar.info('已切换到选择模式', parent=self)

       def set_edit_mode(self):
           """设置编辑模式"""
           self.drawing_view.setInteractionMode(InteractionMode.EDIT)
           InfoBar.info('已切换到编辑模式', parent=self)

       def clear_drawing(self):
           """清除绘图"""
           self.drawing_view.clear()
           InfoBar.info('绘图已清除', parent=self)

       def show_error(self, message):
           """显示错误信息"""
           InfoBar.error(message, parent=self)

   if __name__ == '__main__':
       app = QApplication(sys.argv)
       window = VispyDemoWindow()
       window.show()
       sys.exit(app.exec())

最佳实践
--------

1. **性能优化**: 
   - 大量数据时使用适当的数据采样
   - 合理设置渲染参数
   - 避免频繁更新图形

2. **数据管理**: 
   - 使用 NumPy 数组处理数据
   - 合理设置数据范围和比例
   - 处理缺失值和异常值

3. **交互功能**: 
   - 支持鼠标缩放和平移
   - 提供坐标显示
   - 添加选择和高亮功能

4. **可视化设计**: 
   - 选择合适的颜色映射
   - 设置清晰的坐标轴标签
   - 添加图例和标题

依赖要求
--------

使用 Vispy 组件需要安装以下依赖：

.. code-block:: bash

   pip install vispy numpy

组件层次
--------

.. code-block:: text

   Vispy 组件层次
   ├─ Canvas 层
   │  ├─ VispyCanvas2D
   │  └─ VispyCanvas3D
   ├─ Widget 层
   │  ├─ VispyWidget2D
   │  ├─ VispyWidget3D
   │  └─ DrawingView
   ├─ Visual 元素
   │  ├─ VisualEntry
   │  ├─ MarkersEntry
   │  ├─ LineEntry
   │  └─ MeshEntry
   ├─ 交互式绘图
   │  ├─ InteractiveDrawingWidget
   │  └─ InteractionMode
   ├─ 数据模型
   │  ├─ StyleData
   │  ├─ PrimitiveData
   │  ├─ LineData
   │  ├─ BezierData
   │  ├─ ArcData
   │  ├─ CircleData
   │  ├─ RectangleData
   │  ├─ PolygonData
   │  ├─ MarkersData
   │  └─ ImageData
   └─ 层级管理
      ├─ Primitive
      ├─ PrimitiveGroup
      ├─ Layer
      └─ LayerManager
