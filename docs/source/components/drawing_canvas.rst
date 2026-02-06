Drawing Canvas 交互式绘图画布模块
======================================

Drawing Canvas 模块扩展 VispyCanvas2D，集成所有管理器，提供完整的交互式绘图功能。
该模块提供统一的绘图接口，支持图元管理、交互模式和实时预览。

主要功能
--------

- **图元管理** - 提供完整的图元 CRUD 操作接口
- **交互管理** - 集成交互管理器，支持多种绘图模式
- **图层管理** - 集成图层管理器，支持多层级组织
- **选择管理** - 集成选择管理器，支持图元选择和高亮
- **坐标系统** - 集成坐标系统，支持屏幕坐标与世界坐标转换
- **实时预览** - 提供绘图过程中的实时预览功能

核心组件
--------

InteractiveDrawingCanvas
~~~~~~~~~~~~~~~~~~~~~~~

交互式绘图画布类，扩展 VispyCanvas2D。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import InteractiveDrawingCanvas
   from qfluentwidgets.components.vispy.drawing import StyleData, LineData
   
   # 创建交互式绘图画布
   canvas = InteractiveDrawingCanvas(
       scale_factor=1.0,
       origin_offset=(0.0, 0.0),
       grid_size=100.0,
       grid_spacing=10.0
   )
   
   # 设置交互模式
   canvas.setInteractionMode(InteractionMode.DRAW_LINE)
   
   # 添加图元
   line_data = LineData(
       points=[[0, 0], [10, 10]],
       style=StyleData(lineWidth=2.0)
   )
   canvas.addPrimitive(line_data)

**主要信号：**
- ``mouseMoved`` - 鼠标移动信号

**主要方法：**
- ``addPrimitive()`` - 添加图元
- ``removePrimitive()`` - 移除图元
- ``updatePrimitive()`` - 更新图元
- ``getPrimitive()`` - 获取图元
- ``getAllPrimitives()`` - 获取所有图元
- ``clearAll()`` - 清空所有图元
- ``setInteractionMode()`` - 设置交互模式
- ``getInteractionMode()`` - 获取当前交互模式
- ``setDefaultStyle()`` - 设置默认样式
- ``getDefaultStyle()`` - 获取默认样式

实际应用
--------

基本绘图应用
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import InteractiveDrawingCanvas
   from qfluentwidgets.components.vispy.drawing import StyleData, LineData, CircleData
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   import numpy as np
   
   class BasicDrawingCanvasWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_canvas()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("基本绘图应用")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建交互式绘图画布
           self.canvas = InteractiveDrawingCanvas(parent=self)
           self.canvas.setFixedSize(600, 400)
           
           # 显示当前状态
           self.status_label = Label("状态: 画布已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.canvas)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_canvas(self):
           """设置画布内容"""
           # 创建样式
           line_style = StyleData(
               lineWidth=2.0,
               lineColor=(1.0, 0.0, 0.0, 1.0),  # 红色
               filled=False
           )
           
           circle_style = StyleData(
               lineWidth=1.0,
               lineColor=(0.0, 0.0, 1.0, 1.0),  # 蓝色
               filled=True,
               fillColor=(0.5, 0.5, 1.0, 0.5)  # 半透明蓝色
           )
           
           # 添加线条
           points = np.array([[50, 50], [150, 100], [250, 50]], dtype=np.float32)
           line_data = LineData(
               points=points,
               style=line_style,
               name="示例线条"
           )
           
           # 添加圆形
           circle_data = CircleData(
               center=(150, 150),
               radius=(30, 30),
               style=circle_style,
               name="示例圆形"
           )
           
           # 添加到画布
           self.canvas.addPrimitive(line_data)
           self.canvas.addPrimitive(circle_data)
           
           # 设置交互模式
           self.canvas.setInteractionMode(InteractionMode.DEFAULT)
           
           self.status_label.setText("状态: 图元已添加到画布")

高级绘图应用
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import InteractiveDrawingCanvas
   from qfluentwidgets.components.vispy.drawing import StyleData, RectangleData, PolygonData
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   import numpy as np
   
   class AdvancedDrawingCanvasWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_canvas()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("高级绘图应用")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.draw_btn = PushButton("绘制模式")
           self.select_btn = PushButton("选择模式")
           self.clear_btn = PushButton("清空画布")
           self.add_rect_btn = PushButton("添加矩形")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.draw_btn)
           header_layout.addWidget(self.select_btn)
           header_layout.addWidget(self.add_rect_btn)
           header_layout.addWidget(self.clear_btn)
           
           # 创建交互式绘图画布
           self.canvas = InteractiveDrawingCanvas(parent=self)
           self.canvas.setFixedSize(600, 400)
           
           # 显示当前状态
           self.status_label = Label("状态: 画布已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.canvas)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_canvas(self):
           """设置画布内容"""
           # 创建样式
           rect_style = StyleData(
               lineWidth=1.0,
               lineColor=(0.0, 1.0, 0.0, 1.0),  # 绿色
               filled=True,
               fillColor=(0.5, 1.0, 0.5, 0.3)  # 半透明绿色
           )
           
           # 添加矩形
           rect_data = RectangleData(
               pos=(100, 100),
               size=(80, 60),
               style=rect_style,
               name="示例矩形"
           )
           
           # 添加多边形
           vertices = np.array([[300, 100], [350, 120], [330, 150], [280, 150]], dtype=np.float32)
           polygon_data = PolygonData(
               vertices=vertices,
               style=rect_style,
               name="示例多边形"
           )
           
           # 添加到画布
           self.canvas.addPrimitive(rect_data)
           self.canvas.addPrimitive(polygon_data)
           
           # 设置默认样式
           default_style = StyleData(
               lineWidth=2.0,
               lineColor=(1.0, 0.0, 0.0, 1.0),
               filled=True,
               fillColor=(1.0, 0.5, 0.5, 0.5)
           )
           self.canvas.setDefaultStyle(default_style)
           
           self.status_label.setText("状态: 高级图元已添加")
       
       def setup_connections(self):
           """设置连接"""
           self.draw_btn.clicked.connect(self.enable_draw_mode)
           self.select_btn.clicked.connect(self.enable_select_mode)
           self.clear_btn.clicked.connect(self.clear_canvas)
           self.add_rect_btn.clicked.connect(self.add_random_rectangle)
       
       def enable_draw_mode(self):
           """启用绘制模式"""
           self.canvas.setInteractionMode(InteractionMode.DRAW_RECTANGLE)
           self.status_label.setText("状态: 矩形绘制模式")
       
       def enable_select_mode(self):
           """启用选择模式"""
           self.canvas.setInteractionMode(InteractionMode.SELECT)
           self.status_label.setText("状态: 选择模式")
       
       def clear_canvas(self):
           """清空画布"""
           self.canvas.clearAll()
           self.status_label.setText("状态: 画布已清空")
       
       def add_random_rectangle(self):
           """添加随机矩形"""
           import random
           
           # 随机位置和大小
           x = random.randint(50, 400)
           y = random.randint(50, 250)
           w = random.randint(30, 100)
           h = random.randint(20, 80)
           
           # 创建随机颜色
           color = (random.random(), random.random(), random.random(), 1.0)
           rect_style = StyleData(
               lineWidth=1.0,
               lineColor=color,
               filled=True,
               fillColor=(*color[:3], 0.5)
           )
           
           # 创建矩形数据
           rect_data = RectangleData(
               pos=(x, y),
               size=(w, h),
               style=rect_style,
               name=f"随机矩形_{x}_{y}"
           )
           
           # 添加到画布
           self.canvas.addPrimitive(rect_data)
           self.status_label.setText(f"状态: 已添加随机矩形 ({x}, {y})")

图元管理应用
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import InteractiveDrawingCanvas
   from qfluentwidgets.components.vispy.drawing import StyleData, LineData, CircleData
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   import numpy as np
   
   class PrimitiveManagementWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_canvas()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("图元管理应用")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.add_btn = PushButton("添加图元")
           self.remove_btn = PushButton("移除图元")
           self.update_btn = PushButton("更新图元")
           self.list_btn = PushButton("列出图元")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.add_btn)
           header_layout.addWidget(self.remove_btn)
           header_layout.addWidget(self.update_btn)
           header_layout.addWidget(self.list_btn)
           
           # 创建交互式绘图画布
           self.canvas = InteractiveDrawingCanvas(parent=self)
           self.canvas.setFixedSize(600, 400)
           
           # 显示当前状态
           self.status_label = Label("状态: 画布已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.canvas)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_canvas(self):
           """设置画布内容"""
           # 创建初始图元
           self.create_initial_primitives()
           self.status_label.setText("状态: 初始图元已创建")
       
       def create_initial_primitives(self):
           """创建初始图元"""
           # 创建样式
           line_style = StyleData(
               lineWidth=2.0,
               lineColor=(1.0, 0.0, 0.0, 1.0)
           )
           
           circle_style = StyleData(
               lineWidth=1.0,
               lineColor=(0.0, 0.0, 1.0, 1.0),
               filled=True,
               fillColor=(0.5, 0.5, 1.0, 0.5)
           )
           
           # 创建线条
           points = np.array([[50, 50], [150, 100]], dtype=np.float32)
           self.line_data = LineData(
               points=points,
               style=line_style,
               name="管理线条"
           )
           
           # 创建圆形
           self.circle_data = CircleData(
               center=(250, 150),
               radius=(30, 30),
               style=circle_style,
               name="管理圆形"
           )
           
           # 添加到画布并保存ID
           self.line_id = self.canvas.addPrimitive(self.line_data)
           self.circle_id = self.canvas.addPrimitive(self.circle_data)
       
       def setup_connections(self):
           """设置连接"""
           self.add_btn.clicked.connect(self.add_primitive)
           self.remove_btn.clicked.connect(self.remove_primitive)
           self.update_btn.clicked.connect(self.update_primitive)
           self.list_btn.clicked.connect(self.list_primitives)
       
       def add_primitive(self):
           """添加新图元"""
           import random
           
           # 创建随机线条
           points = np.array([
               [random.randint(50, 200), random.randint(50, 200)],
               [random.randint(200, 350), random.randint(50, 200)]
           ], dtype=np.float32)
           
           style = StyleData(
               lineWidth=random.uniform(1, 3),
               lineColor=(random.random(), random.random(), random.random(), 1.0)
           )
           
           line_data = LineData(
               points=points,
               style=style,
               name=f"随机线条_{random.randint(100, 999)}"
           )
           
           # 添加到画布
           primitive_id = self.canvas.addPrimitive(line_data)
           self.status_label.setText(f"状态: 已添加新图元，ID: {primitive_id[:8]}")
       
       def remove_primitive(self):
           """移除图元"""
           if self.line_id:
               success = self.canvas.removePrimitive(self.line_id)
               if success:
                   self.line_id = None
                   self.status_label.setText("状态: 线条图元已移除")
               else:
                   self.status_label.setText("状态: 移除失败")
           else:
               self.status_label.setText("状态: 没有可移除的线条图元")
       
       def update_primitive(self):
           """更新图元"""
           if self.circle_id:
               # 更新圆形位置
               import random
               new_center = (random.randint(100, 300), random.randint(100, 250))
               success = self.canvas.updatePrimitive(self.circle_id, center=new_center)
               
               if success:
                   self.status_label.setText(f"状态: 圆形已更新到 {new_center}")
               else:
                   self.status_label.setText("状态: 更新失败")
           else:
               self.status_label.setText("状态: 没有可更新的圆形图元")
       
       def list_primitives(self):
           """列出所有图元"""
           primitives = self.canvas.getAllPrimitives()
           
           if primitives:
               info_lines = [f"图元总数: {len(primitives)}"]
               for primitive in primitives:
                   info_lines.append(f"- {primitive.data.name} (ID: {primitive.id[:8]})")
               
               self.status_label.setText("\n".join(info_lines))
           else:
               self.status_label.setText("状态: 没有图元")

最佳实践
--------

1. **图元管理** - 合理组织图元的创建和管理
2. **交互模式** - 正确设置和使用交互模式
3. **样式统一** - 使用统一的样式管理
4. **性能优化** - 避免频繁的图元更新操作
5. **事件处理** - 正确处理鼠标和键盘事件

注意事项
--------

- 画布需要有效的 vispy 环境才能正常工作
- 图元操作需要正确的数据类型和格式
- 交互模式切换会清除当前操作状态
- 预览图元会在模式切换时自动清除
- 需要正确处理图元的生命周期
- 大量图元可能影响性能

相关模块
--------

- :doc:`components.vispy.vispy_canvas` - Vispy 画布
- :doc:`components.vispy.drawing` - 交互式绘图
- :doc:`components.vispy.drawing.data_models` - 数据模型
- :doc:`components.vispy.drawing.coordinate_system` - 坐标系统
- :doc:`components.vispy.drawing.interaction_manager` - 交互管理
