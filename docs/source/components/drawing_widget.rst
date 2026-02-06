Drawing Widget 交互式绘图控件模块
======================================

Drawing Widget 模块提供 InteractiveDrawingWidget 控件，封装 InteractiveDrawingCanvas，
提供高层API接口和信号，便于用户使用。该模块提供完整的2D交互式绘图功能。

主要功能
--------

- **高层API** - 提供简化的图元绘制接口
- **信号系统** - 提供丰富的事件信号支持
- **工具集成** - 支持与ToolPanel的集成
- **坐标显示** - 实时显示鼠标坐标信息
- **主题适配** - 支持明暗主题切换
- **键盘处理** - 支持键盘快捷键操作

核心组件
--------

InteractiveDrawingWidget
~~~~~~~~~~~~~~~~~~~~~~~

交互式绘图控件，提供完整的2D交互式绘图功能。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import InteractiveDrawingWidget
   from qfluentwidgets.components.vispy.drawing import StyleData
   from PySide6.QtWidgets import QVBoxLayout
   import numpy as np
   
   # 创建交互式绘图控件
   widget = InteractiveDrawingWidget(
       parent=parent,
       scale_factor=1.0,
       origin_offset=(0.0, 0.0),
       grid_size=100.0,
       grid_spacing=10.0
   )
   
   # 添加线条
   points = np.array([[0, 0], [10, 10]], dtype=np.float32)
   line_id = widget.addLine(points)
   
   # 设置交互模式
   widget.setInteractionMode(InteractionMode.DRAW_LINE)

**主要信号：**
- ``primitiveAdded`` - 图元添加信号
- ``primitiveRemoved`` - 图元移除信号
- ``selectionChanged`` - 选择改变信号
- ``interactionModeChanged`` - 交互模式改变信号
- ``primitiveMoved`` - 图元移动信号

**主要方法：**
- ``addLine()`` - 添加线条
- ``addBezierCurve()`` - 添加贝塞尔曲线
- ``addArc()`` - 添加圆弧
- ``addCircle()`` - 添加圆形
- ``addRectangle()`` - 添加矩形
- ``addPolygon()`` - 添加多边形
- ``setInteractionMode()`` - 设置交互模式
- ``clearAll()`` - 清空所有图元
- ``autoRange()`` - 自动调整视图范围

实际应用
--------

基本绘图控件
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import InteractiveDrawingWidget
   from qfluentwidgets.components.vispy.drawing import StyleData
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   import numpy as np
   
   class BasicDrawingWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_drawing()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("基本绘图控件")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.line_btn = PushButton("添加线条")
           self.circle_btn = PushButton("添加圆形")
           self.clear_btn = PushButton("清空画布")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.line_btn)
           header_layout.addWidget(self.circle_btn)
           header_layout.addWidget(self.clear_btn)
           
           # 创建交互式绘图控件
           self.drawing_widget = InteractiveDrawingWidget(parent=self)
           self.drawing_widget.setFixedSize(600, 400)
           
           # 显示当前状态
           self.status_label = Label("状态: 绘图控件已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.drawing_widget)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_drawing(self):
           """设置绘图功能"""
           # 创建默认样式
           self.default_style = StyleData(
               lineWidth=2.0,
               lineColor=(1.0, 0.0, 0.0, 1.0),  # 红色
               filled=True,
               fillColor=(1.0, 0.5, 0.5, 0.5)  # 半透明红色
           )
           
           # 连接信号
           self.drawing_widget.primitiveAdded.connect(self.on_primitive_added)
           self.drawing_widget.selectionChanged.connect(self.on_selection_changed)
           
           # 设置初始交互模式
           self.drawing_widget.setInteractionMode(InteractionMode.DEFAULT)
           
           self.status_label.setText("状态: 绘图功能已设置")
       
       def setup_connections(self):
           """设置连接"""
           self.line_btn.clicked.connect(self.add_line)
           self.circle_btn.clicked.connect(self.add_circle)
           self.clear_btn.clicked.connect(self.clear_canvas)
       
       def add_line(self):
           """添加线条"""
           import random
           
           # 随机生成线条点
           points = np.array([
               [random.randint(50, 200), random.randint(50, 200)],
               [random.randint(200, 350), random.randint(50, 200)]
           ], dtype=np.float32)
           
           # 创建随机颜色样式
           color = (random.random(), random.random(), random.random(), 1.0)
           style = StyleData(
               lineWidth=2.0,
               lineColor=color,
               filled=False
           )
           
           # 添加线条
           line_id = self.drawing_widget.addLine(points, style)
           self.status_label.setText(f"状态: 已添加线条，ID: {line_id[:8]}")
       
       def add_circle(self):
           """添加圆形"""
           import random
           
           # 随机生成圆形参数
           center = (random.randint(100, 300), random.randint(100, 250))
           radius = random.randint(20, 50)
           
           # 创建随机颜色样式
           color = (random.random(), random.random(), random.random(), 1.0)
           style = StyleData(
               lineWidth=1.0,
               lineColor=color,
               filled=True,
               fillColor=(*color[:3], 0.5)
           )
           
           # 添加圆形
           circle_id = self.drawing_widget.addCircle(center, radius, style)
           self.status_label.setText(f"状态: 已添加圆形，ID: {circle_id[:8]}")
       
       def clear_canvas(self):
           """清空画布"""
           self.drawing_widget.clearAll()
           self.status_label.setText("状态: 画布已清空")
       
       def on_primitive_added(self, primitive_id):
           """图元添加处理"""
           print(f"图元已添加: {primitive_id}")
       
       def on_selection_changed(self, selected_ids):
           """选择改变处理"""
           if selected_ids:
               self.status_label.setText(f"状态: 已选择 {len(selected_ids)} 个图元")
           else:
               self.status_label.setText("状态: 无选择")

高级绘图控件
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import InteractiveDrawingWidget
   from qfluentwidgets.components.vispy.drawing import StyleData
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   import numpy as np
   
   class AdvancedDrawingWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_drawing()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("高级绘图控件")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.bezier_btn = PushButton("贝塞尔曲线")
           self.polygon_btn = PushButton("多边形")
           self.arc_btn = PushButton("圆弧")
           self.export_btn = PushButton("导出数据")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.bezier_btn)
           header_layout.addWidget(self.polygon_btn)
           header_layout.addWidget(self.arc_btn)
           header_layout.addWidget(self.export_btn)
           
           # 创建交互式绘图控件
           self.drawing_widget = InteractiveDrawingWidget(parent=self)
           self.drawing_widget.setFixedSize(600, 400)
           
           # 显示当前状态
           self.status_label = Label("状态: 高级绘图控件已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.drawing_widget)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_drawing(self):
           """设置高级绘图功能"""
           # 创建多种样式模板
           self.styles = {
               'red': StyleData(
                   lineWidth=2.0,
                   lineColor=(1.0, 0.0, 0.0, 1.0),
                   filled=True,
                   fillColor=(1.0, 0.5, 0.5, 0.5)
               ),
               'blue': StyleData(
                   lineWidth=2.0,
                   lineColor=(0.0, 0.0, 1.0, 1.0),
                   filled=True,
                   fillColor=(0.5, 0.5, 1.0, 0.5)
               ),
               'green': StyleData(
                   lineWidth=2.0,
                   lineColor=(0.0, 1.0, 0.0, 1.0),
                   filled=True,
                   fillColor=(0.5, 1.0, 0.5, 0.5)
               )
           }
           
           # 连接信号
           self.drawing_widget.primitiveAdded.connect(self.on_primitive_added)
           self.drawing_widget.primitiveMoved.connect(self.on_primitive_moved)
           self.drawing_widget.interactionModeChanged.connect(self.on_mode_changed)
           
           self.status_label.setText("状态: 高级绘图功能已设置")
       
       def setup_connections(self):
           """设置连接"""
           self.bezier_btn.clicked.connect(self.add_bezier)
           self.polygon_btn.clicked.connect(self.add_polygon)
           self.arc_btn.clicked.connect(self.add_arc)
           self.export_btn.clicked.connect(self.export_data)
       
       def add_bezier(self):
           """添加贝塞尔曲线"""
           import random
           
           # 随机生成控制点
           control_points = np.array([
               [random.randint(50, 150), random.randint(50, 200)],
               [random.randint(150, 250), random.randint(100, 250)],
               [random.randint(250, 350), random.randint(50, 200)]
           ], dtype=np.float32)
           
           # 随机选择样式
           style_name = random.choice(list(self.styles.keys()))
           style = self.styles[style_name]
           
           # 添加贝塞尔曲线
           bezier_id = self.drawing_widget.addBezierCurve(control_points, 2, style)
           self.status_label.setText(f"状态: 已添加贝塞尔曲线，ID: {bezier_id[:8]}")
       
       def add_polygon(self):
           """添加多边形"""
           import random
           
           # 随机生成多边形顶点
           num_vertices = random.randint(3, 6)
           center_x, center_y = random.randint(150, 300), random.randint(100, 250)
           radius = random.randint(30, 60)
           
           vertices = []
           for i in range(num_vertices):
               angle = 2 * np.pi * i / num_vertices
               x = center_x + radius * np.cos(angle)
               y = center_y + radius * np.sin(angle)
               vertices.append([x, y])
           
           vertices = np.array(vertices, dtype=np.float32)
           
           # 随机选择样式
           style_name = random.choice(list(self.styles.keys()))
           style = self.styles[style_name]
           
           # 添加多边形
           polygon_id = self.drawing_widget.addPolygon(vertices, style)
           self.status_label.setText(f"状态: 已添加多边形，ID: {polygon_id[:8]}")
       
       def add_arc(self):
           """添加圆弧"""
           import random
           
           # 随机生成圆弧参数
           center = (random.randint(100, 300), random.randint(100, 250))
           radius = random.randint(20, 50)
           start_angle = random.uniform(0, 180)
           end_angle = start_angle + random.uniform(45, 180)
           
           # 随机选择样式
           style_name = random.choice(list(self.styles.keys()))
           style = StyleData(
               lineWidth=2.0,
               lineColor=style.lineColor,
               filled=False
           )
           
           # 添加圆弧
           arc_id = self.drawing_widget.addArc(center, radius, start_angle, end_angle, style)
           self.status_label.setText(f"状态: 已添加圆弧，ID: {arc_id[:8]}")
       
       def export_data(self):
           """导出数据"""
           data = self.drawing_widget.exportLayerData()
           
           # 统计信息
           total_primitives = 0
           for layer in data.get('layers', []):
               total_primitives += len(layer.get('primitives', []))
           
           self.status_label.setText(f"状态: 数据已导出，共 {total_primitives} 个图元")
           print(f"导出的数据: {data}")
       
       def on_primitive_added(self, primitive_id):
           """图元添加处理"""
           print(f"图元已添加: {primitive_id}")
       
       def on_primitive_moved(self, primitive_ids, dx, dy):
           """图元移动处理"""
           print(f"图元已移动: {primitive_ids}, 位移: ({dx:.2f}, {dy:.2f})")
       
       def on_mode_changed(self, mode):
           """交互模式改变处理"""
           mode_name = mode.name if hasattr(mode, 'name') else str(mode)
           self.status_label.setText(f"状态: 交互模式已切换到 {mode_name}")

工具集成应用
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import InteractiveDrawingWidget
   from qfluentwidgets.components.vispy.drawing import StyleData
   from qfluentwidgets import CardWidget, Label, PushButton
   from qfluentwidgets.components import ToolPanel
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   
   class ToolIntegrationWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_drawing()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("工具集成应用")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建工具面板和绘图控件的水平布局
           content_layout = QHBoxLayout()
           
           # 创建工具面板
           self.tool_panel = ToolPanel(self)
           self.tool_panel.setFixedSize(60, 400)
           
           # 创建交互式绘图控件
           self.drawing_widget = InteractiveDrawingWidget(parent=self)
           self.drawing_widget.setFixedSize(540, 400)
           
           content_layout.addWidget(self.tool_panel)
           content_layout.addWidget(self.drawing_widget)
           
           # 显示当前状态
           self.status_label = Label("状态: 工具集成已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addLayout(content_layout)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_drawing(self):
           """设置工具集成"""
           # 获取绘图工具数据
           tools_data = self.drawing_widget.createDrawingToolsData()
           
           # 设置工具面板
           self.tool_panel.setToolData(tools_data)
           
           # 连接工具面板信号
           self.tool_panel.toolChanged.connect(self.drawing_widget.onToolPanelChanged)
           
           # 连接绘图控件信号
           self.drawing_widget.interactionModeChanged.connect(self.on_mode_changed)
           self.drawing_widget.primitiveAdded.connect(self.on_primitive_added)
           
           self.status_label.setText("状态: 工具集成已完成")
       
       def on_mode_changed(self, mode):
           """交互模式改变处理"""
           mode_name = mode.name if hasattr(mode, 'name') else str(mode)
           self.status_label.setText(f"状态: 当前模式: {mode_name}")
       
       def on_primitive_added(self, primitive_id):
           """图元添加处理"""
           self.status_label.setText(f"状态: 已添加图元: {primitive_id[:8]}")

最佳实践
--------

1. **信号连接** - 正确连接和使用信号系统
2. **样式管理** - 创建样式模板以提高复用性
3. **工具集成** - 充分利用ToolPanel集成功能
4. **数据导出** - 定期导出重要的绘图数据
5. **键盘处理** - 支持常用的键盘快捷键

注意事项
--------

- 控件需要安装 vispy 库才能正常工作
- 坐标显示标签会自动跟随鼠标位置
- ESC键可以取消当前操作
- Delete键可以删除选中的图元
- 工具面板集成需要正确设置工具数据
- 大量图元可能影响性能

相关模块
--------

- :doc:`components.vispy.drawing.drawing_canvas` - 绘图画布
- :doc:`components.vispy.drawing.data_models` - 数据模型
- :doc:`components.vispy.drawing.interaction_manager` - 交互管理
- :doc:`components.tool_panel` - 工具面板
- :doc:`common.icon` - 图标管理
