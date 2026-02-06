Vispy Drawing 交互式绘图模块
==================================

Vispy Drawing 模块提供基于 Vispy 的交互式 2D 绘图功能，支持多种图元和交互模式。
该模块提供现代化的绘图界面，支持丰富的图形元素和交互功能。

主要功能
--------

- **多种图元** - 支持线条、贝塞尔曲线、圆弧、矩形、多边形等基础图元
- **样式控制** - 提供线宽、颜色、填充等样式控制功能
- **交互管理** - 支持绘制、选择、移动等交互模式
- **图层管理** - 提供三级层级结构的图层管理功能
- **坐标系统** - 支持屏幕坐标与世界坐标的转换

核心组件
--------

StyleData
~~~~~~~~~

样式数据类，提供图形元素的样式信息。

.. code-block:: python

   from qfluentwidgets.components.vispy import StyleData
   
   # 创建样式数据
   style = StyleData(
       color='red',
       line_width=2.0,
       fill_color='lightblue',
       alpha=1.0
   )

PrimitiveData
~~~~~~~~~~~~

基础图元数据类，提供图形元素的基本信息。

.. code-block:: python

   from qfluentwidgets.components.vispy import PrimitiveData
   
   # 创建基础图元数据
   primitive = PrimitiveData(
       style=style_data,
       visible=True,
       selectable=True
   )

LineData
~~~~~~~~~~

线条数据类，提供线条图元的信息。

.. code-block:: python

   from qfluentwidgets.components.vispy import LineData
   
   # 创建线条数据
   line_data = LineData(
       points=[[0, 0], [1, 1], [2, 0]],
       style=line_style
   )

BezierData
~~~~~~~~~~~~

贝塞尔曲线数据类，提供贝塞尔曲线图元的信息。

.. code-block:: python

   from qfluentwidgets.components.vispy import BezierData
   
   # 创建贝塞尔曲线数据
   bezier_data = BezierData(
       control_points=[[0, 0], [1, 1], [2, 0]],
       style=line_style
   )

ArcData
~~~~~~~~~~

圆弧数据类，提供圆弧图元的信息。

.. code-block:: python

   from qfluentwidgets.components.vispy import ArcData
   
   # 创建圆弧数据
   arc_data = ArcData(
       center=[0, 0],
       radius=10,
       start_angle=0,
       end_angle=180,
       style=line_style
   )

CircleData
~~~~~~~~~~

圆形数据类，提供圆形图元的信息。

.. code-block:: python

   from qfluentwidgets.components.vispy import CircleData
   
   # 创建圆形数据
   circle_data = CircleData(
       center=[0, 0],
       radius=10,
       style=fill_style
   )

RectangleData
~~~~~~~~~~~~

矩形数据类，提供矩形图元的信息。

.. code-block:: python

   from qfluentwidgets.components.vispy import RectangleData
   
   # 创建矩形数据
   rect_data = RectangleData(
       position=[0, 0],
       size=[100, 50],
       style=fill_style
   )

PolygonData
~~~~~~~~~~

多边形数据类，提供多边形图元的信息。

.. code-block:: python

   from qfluentwidgets.components.vispy import PolygonData
   
   # 创建多边形数据
   polygon_data = PolygonData(
       points=[[0, 0], [1, 1], [0, 1]],
       style=fill_style
   )

MarkersData
~~~~~~~~~~

标记数据类，提供标记图元的信息。

.. code-block:: python

   from qfluentwidgets.components.vispy import MarkersData
   
   # 创建标记数据
   markers_data = MarkersData(
       positions=[[0, 0], [1, 1], [2, 0]],
       style=marker_style
   )

ImageData
~~~~~~~~~~

图像数据类，提供图像图元的信息。

.. code-block:: python

   from qfluentwidgets.components.vispy import ImageData
   
   # 创建图像数据
   image_data = ImageData(
       position=[0, 0],
       size=[100, 100],
       image_path='path/to/image.png'
   )

InteractiveDrawingWidget
~~~~~~~~~~~~~~~~~~~~

交互式绘图控件，提供完整的绘图功能。

.. code-block:: python

   from qfluentwidgets.components.vispy import InteractiveDrawingWidget
   
   # 创建交互式绘图控件
   drawing_widget = InteractiveDrawingWidget(parent=parent)
   
   # 设置交互模式
   drawing_widget.set_interaction_mode(InteractionMode.DRAW)

实际应用
--------

基本绘图应用
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy import InteractiveDrawingWidget
   from qfluentwidgets.components.vispy import StyleData, LineData, CircleData
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   
   class BasicDrawingWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_drawing()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("基本绘图应用")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建交互式绘图控件
           self.drawing_widget = InteractiveDrawingWidget(parent=self)
           
           # 显示当前状态
           self.status_label = Label("状态: 绘图模式")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.drawing_widget)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_drawing(self):
           """设置绘图内容"""
           # 创建样式
           line_style = StyleData(color='blue', line_width=2.0)
           fill_style = StyleData(color='lightblue', alpha=0.5)
           
           # 添加线条
           line_data = LineData(
               points=[[0, 0], [100, 0], [100, 100], [0, 100]],
               style=line_style
           )
           
           # 添加圆形
           circle_data = CircleData(
               center=[50, 50],
               radius=20,
               style=fill_style
           )
           
           # 添加到绘图控件
           self.drawing_widget.add_primitive(line_data)
           self.drawing_widget.add_primitive(circle_data)
           
           # 设置交互模式
           self.drawing_widget.set_interaction_mode(InteractionMode.DRAW)

高级绘图应用
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy import InteractiveDrawingWidget
   from qfluentwidgets.components.vispy import StyleData, BezierData, RectangleData, PolygonData
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   
   class AdvancedDrawingWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_drawing()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("高级绘图应用")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.draw_btn = PushButton("绘制模式")
           self.select_btn = PushButton("选择模式")
           self.clear_btn = PushButton("清空画布")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.draw_btn)
           header_layout.addWidget(self.select_btn)
           header_layout.addWidget(self.clear_btn)
           
           # 创建交互式绘图控件
           self.drawing_widget = InteractiveDrawingWidget(parent=self)
           
           # 显示当前状态
           self.status_label = Label("状态: 绘图模式")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.drawing_widget)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_drawing(self):
           """设置高级绘图内容"""
           # 创建样式
           line_style = StyleData(color='red', line_width=3.0)
           fill_style = StyleData(color='green', alpha=0.7)
           
           # 添加贝塞尔曲线
           bezier_data = BezierData(
               control_points=[[0, 0], [50, 100], [100, 50]],
               style=line_style
           )
           
           # 添加矩形
           rect_data = RectangleData(
               position=[150, 0],
               size=[80, 60],
               style=fill_style
           )
           
           # 添加多边形
           polygon_data = PolygonData(
               points=[[250, 0], [300, 50], [280, 100], [220, 100]],
               style=fill_style
           )
           
           # 添加到绘图控件
           self.drawing_widget.add_primitive(bezier_data)
           self.drawing_widget.add_primitive(rect_data)
           self.drawing_widget.add_primitive(polygon_data)
           
           # 设置交互模式
           self.drawing_widget.set_interaction_mode(InteractionMode.DRAW)
       
       def setup_connections(self):
           """设置连接"""
           self.draw_btn.clicked.connect(self.enable_draw_mode)
           self.select_btn.clicked.connect(self.enable_select_mode)
           self.clear_btn.clicked.connect(self.clear_canvas)
       
       def enable_draw_mode(self):
           """启用绘制模式"""
           self.drawing_widget.set_interaction_mode(InteractionMode.DRAW)
           self.status_label.setText("状态: 绘图模式")
       
       def enable_select_mode(self):
           """启用选择模式"""
           self.drawing_widget.set_interaction_mode(InteractionMode.SELECT)
           self.status_label.setText("状态: 选择模式")
       
       def clear_canvas(self):
           """清空画布"""
           self.drawing_widget.clear_all()
           self.status_label.setText("状态: 画布已清空")

最佳实践
--------

1. **性能优化** - 合理使用批量更新和缓存机制
2. **内存管理** - 及时清理不需要的图形元素
3. **交互设计** - 提供直观的用户交互体验
4. **样式管理** - 统一管理图形元素的样式
5. **图层组织** - 合理组织和管理图形元素的层级

注意事项
--------

- 绘图模块需要安装 vispy 库才能正常工作
- 大量图形元素可能影响性能，需要合理控制数量
- 交互模式需要正确设置事件处理
- 样式数据需要正确设置颜色和透明度
- 图元数据需要正确设置坐标和尺寸
- 需要正确管理图形元素的生命周期

相关模块
--------

- :doc:`components.vispy.vispy_canvas` - Vispy 画布
- :doc:`components.vispy.vispy_widget` - Vispy 控件
- :doc:`components.vispy.vispy_visuals` - Vispy 可视化元素
- :doc:`common.color` - 颜色管理
