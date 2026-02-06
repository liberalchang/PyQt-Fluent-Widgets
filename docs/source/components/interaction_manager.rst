Interaction Manager 交互管理器模块
======================================

Interaction Manager 模块实现模式化的鼠标交互管理，提供交互模式枚举和交互管理器类。
该模块管理鼠标交互模式和状态，分发事件到对应的处理逻辑。

主要功能
--------

- **交互模式** - 提供多种交互模式枚举
- **事件处理** - 处理鼠标按下、移动、释放和双击事件
- **状态管理** - 管理交互状态和拖拽状态
- **预览生成** - 生成实时预览数据
- **信号系统** - 提供图元创建和移动信号
- **样式管理** - 管理默认样式和控制端点创建

核心组件
--------

InteractionMode
~~~~~~~~~~~~~~~

交互模式枚举，定义所有支持的交互模式。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import InteractionMode
   
   # 基础模式
   DEFAULT = InteractionMode.DEFAULT            # 默认模式（光标模式：拖动平移，滚轮缩放）
   MOVE = InteractionMode.MOVE               # 移动模式（选择和移动图元）
   
   # 绘制模式
   DRAW_LINE = InteractionMode.DRAW_LINE          # 绘制多段线
   DRAW_RECTANGLE = InteractionMode.DRAW_RECTANGLE     # 绘制矩形
   DRAW_CIRCLE = InteractionMode.DRAW_CIRCLE        # 绘制圆形
   DRAW_ELLIPSE = InteractionMode.DRAW_ELLIPSE       # 绘制椭圆
   DRAW_BEZIER = InteractionMode.DRAW_BEZIER        # 绘制贝塞尔曲线
   DRAW_POLYGON = InteractionMode.DRAW_POLYGON       # 绘制多边形
   DRAW_POINT = InteractionMode.DRAW_POINT         # 绘制点
   
   # 高级模式
   EDIT_BEZIER = InteractionMode.EDIT_BEZIER        # 编辑贝塞尔曲线控制点

InteractionManager
~~~~~~~~~~~~~~~~~~

交互管理器类，管理鼠标交互模式和状态。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import InteractionManager
   from qfluentwidgets.components.vispy.drawing import CoordinateSystem, SelectionManager
   
   # 创建交互管理器
   coord_system = CoordinateSystem(view, canvas)
   selection_manager = SelectionManager(layer_manager, coord_system, view)
   
   manager = InteractionManager(coord_system, selection_manager)
   
   # 设置交互模式
   manager.setMode(InteractionMode.DRAW_LINE)
   
   # 处理鼠标事件
   result = manager.handleMousePress(100, 100)
   result = manager.handleMouseMove(110, 110)
   result = manager.handleMouseRelease(110, 110)

**主要信号：**
- ``primitiveCreated`` - 图元创建完成信号
- ``primitiveMoved`` - 图元移动信号
- ``interactionStateChanged`` - 交互状态改变信号

**主要方法：**
- ``setMode()`` - 设置交互模式
- ``getMode()`` - 获取当前交互模式
- ``setDefaultStyle()`` - 设置默认样式
- ``getDefaultStyle()`` - 获取默认样式
- ``setCreateHandles()`` - 设置是否创建控制端点
- ``handleMousePress()`` - 处理鼠标按下事件
- ``handleMouseMove()`` - 处理鼠标移动事件
- ``handleMouseRelease()`` - 处理鼠标释放事件
- ``handleDoubleClick()`` - 处理鼠标双击事件
- ``getCurrentPreview()`` - 获取当前预览数据

实际应用
--------

基本交互管理
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import InteractionManager, InteractionMode
   from qfluentwidgets.components.vispy.drawing import CoordinateSystem, SelectionManager
   from qfluentwidgets.components.vispy.drawing import StyleData
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   
   class BasicInteractionWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_interaction()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("基本交互管理")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.default_btn = PushButton("默认模式")
           self.move_btn = PushButton("移动模式")
           self.draw_btn = PushButton("绘制模式")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.default_btn)
           header_layout.addWidget(self.move_btn)
           header_layout.addWidget(self.draw_btn)
           
           # 显示当前状态
           self.status_label = Label("状态: 交互管理器已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_interaction(self):
           """设置交互管理"""
           # 这里需要实际的坐标系统和选择管理器
           # 示例代码，实际使用时需要传入正确的对象
           self.coord_system = None  # 需要传入 CoordinateSystem
           self.selection_manager = None  # 需要传入 SelectionManager
           
           if self.coord_system and self.selection_manager:
               self.manager = InteractionManager(
                   self.coord_system,
                   self.selection_manager
               )
               
               # 设置默认样式
               default_style = StyleData(
                   lineWidth=2.0,
                   lineColor=(1.0, 0.0, 0.0, 1.0),
                   filled=True,
                   fillColor=(1.0, 0.5, 0.5, 0.5)
               )
               self.manager.setDefaultStyle(default_style)
               
               # 连接信号
               self.manager.primitiveCreated.connect(self.on_primitive_created)
               self.manager.primitiveMoved.connect(self.on_primitive_moved)
               
               self.status_label.setText("状态: 交互管理器已设置")
           else:
               self.status_label.setText("状态: 需要坐标系统和选择管理器")
       
       def setup_connections(self):
           """设置连接"""
           self.default_btn.clicked.connect(self.set_default_mode)
           self.move_btn.clicked.connect(self.set_move_mode)
           self.draw_btn.clicked.connect(self.set_draw_mode)
       
       def set_default_mode(self):
           """设置默认模式"""
           if hasattr(self, 'manager'):
               self.manager.setMode(InteractionMode.DEFAULT)
               self.status_label.setText("状态: 已切换到默认模式")
       
       def set_move_mode(self):
           """设置移动模式"""
           if hasattr(self, 'manager'):
               self.manager.setMode(InteractionMode.MOVE)
               self.status_label.setText("状态: 已切换到移动模式")
       
       def set_draw_mode(self):
           """设置绘制模式"""
           if hasattr(self, 'manager'):
               self.manager.setMode(InteractionMode.DRAW_LINE)
               self.status_label.setText("状态: 已切换到绘制模式")
       
       def simulate_mouse_events(self):
           """模拟鼠标事件"""
           if hasattr(self, 'manager'):
               # 模拟鼠标按下
               result = self.manager.handleMousePress(100, 100)
               print(f"鼠标按下结果: {result}")
               
               # 模拟鼠标移动
               result = self.manager.handleMouseMove(110, 110)
               print(f"鼠标移动结果: {result}")
               
               # 模拟鼠标释放
               result = self.manager.handleMouseRelease(110, 110)
               print(f"鼠标释放结果: {result}")
       
       def on_primitive_created(self, data):
           """图元创建处理"""
           print(f"图元已创建: {data.type_name}")
           self.status_label.setText(f"状态: 已创建 {data.type_name}")
       
       def on_primitive_moved(self, primitive_ids, dx, dy):
           """图元移动处理"""
           print(f"图元已移动: {primitive_ids}, 位移: ({dx:.2f}, {dy:.2f})")
           self.status_label.setText(f"状态: 图元已移动")

高级交互管理
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import InteractionManager, InteractionMode
   from qfluentwidgets.components.vispy.drawing import StyleData
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   
   class AdvancedInteractionWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_interaction()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("高级交互管理")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.line_btn = PushButton("线条模式")
           self.rect_btn = PushButton("矩形模式")
           self.circle_btn = PushButton("圆形模式")
           self.bezier_btn = PushButton("贝塞尔模式")
           self.preview_btn = PushButton("获取预览")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.line_btn)
           header_layout.addWidget(self.rect_btn)
           header_layout.addWidget(self.circle_btn)
           header_layout.addWidget(self.bezier_btn)
           header_layout.addWidget(self.preview_btn)
           
           # 显示当前状态
           self.status_label = Label("状态: 高级交互管理器已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_interaction(self):
           """设置高级交互管理"""
           # 这里需要实际的坐标系统和选择管理器
           self.coord_system = None  # 需要传入 CoordinateSystem
           self.selection_manager = None  # 需要传入 SelectionManager
           
           if self.coord_system and self.selection_manager:
               self.manager = InteractionManager(
                   self.coord_system,
                   self.selection_manager
               )
               
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
               
               # 设置默认样式
               self.manager.setDefaultStyle(self.styles['red'])
               self.manager.setCreateHandles(True)
               
               # 连接信号
               self.manager.primitiveCreated.connect(self.on_primitive_created)
               self.manager.interactionStateChanged.connect(self.on_state_changed)
               
               self.status_label.setText("状态: 高级交互管理器已设置")
           else:
               self.status_label.setText("状态: 需要坐标系统和选择管理器")
       
       def setup_connections(self):
           """设置连接"""
           self.line_btn.clicked.connect(self.set_line_mode)
           self.rect_btn.clicked.connect(self.set_rect_mode)
           self.circle_btn.clicked.connect(self.set_circle_mode)
           self.bezier_btn.clicked.connect(self.set_bezier_mode)
           self.preview_btn.clicked.connect(self.get_preview)
       
       def set_line_mode(self):
           """设置线条模式"""
           if hasattr(self, 'manager'):
               self.manager.setMode(InteractionMode.DRAW_LINE)
               self.manager.setDefaultStyle(self.styles['red'])
               self.status_label.setText("状态: 已切换到线条模式")
       
       def set_rect_mode(self):
           """设置矩形模式"""
           if hasattr(self, 'manager'):
               self.manager.setMode(InteractionMode.DRAW_RECTANGLE)
               self.manager.setDefaultStyle(self.styles['blue'])
               self.status_label.setText("状态: 已切换到矩形模式")
       
       def set_circle_mode(self):
           """设置圆形模式"""
           if hasattr(self, 'manager'):
               self.manager.setMode(InteractionMode.DRAW_CIRCLE)
               self.manager.setDefaultStyle(self.styles['green'])
               self.status_label.setText("状态: 已切换到圆形模式")
       
       def set_bezier_mode(self):
           """设置贝塞尔模式"""
           if hasattr(self, 'manager'):
               self.manager.setMode(InteractionMode.DRAW_BEZIER)
               self.manager.setDefaultStyle(self.styles['red'])
               self.status_label.setText("状态: 已切换到贝塞尔模式")
       
       def get_preview(self):
           """获取预览数据"""
           if hasattr(self, 'manager'):
               preview = self.manager.getCurrentPreview()
               if preview:
                   preview_type = preview.get('type', 'unknown')
                   self.status_label.setText(f"状态: 当前预览类型: {preview_type}")
                   print(f"预览数据: {preview}")
               else:
                   self.status_label.setText("状态: 无预览数据")
       
       def simulate_drawing_sequence(self):
           """模拟绘制序列"""
           if hasattr(self, 'manager'):
               # 设置线条模式
               self.manager.setMode(InteractionMode.DRAW_LINE)
               
               # 模拟绘制线条的点击序列
               points = [(100, 100), (150, 120), (200, 100)]
               
               for i, (x, y) in enumerate(points):
                   result = self.manager.handleMousePress(x, y)
                   print(f"点击 {i+1} 结果: {result}")
                   
                   if i < len(points) - 1:
                       # 模拟移动到下一个点
                       next_x, next_y = points[i + 1]
                       result = self.manager.handleMouseMove(next_x, next_y)
                       print(f"移动结果: {result}")
               
               # 双击完成绘制
               result = self.manager.handleDoubleClick(200, 100)
               print(f"双击结果: {result}")
       
       def on_primitive_created(self, data):
           """图元创建处理"""
           print(f"图元已创建: {data.type_name}")
           self.status_label.setText(f"状态: 已创建 {data.type_name}")
       
       def on_state_changed(self, state):
           """交互状态改变处理"""
           print(f"交互状态改变: {state}")
           if 'box_select_end' in state:
               self.status_label.setText("状态: 框选结束")
           elif 'start_draw_drag' in state:
               self.status_label.setText("状态: 开始拖拽绘制")

最佳实践
--------

1. **模式管理** - 正确切换和管理交互模式
2. **状态重置** - 在模式切换时重置交互状态
3. **样式统一** - 使用统一的样式管理
4. **信号连接** - 正确连接和处理信号
5. **预览更新** - 及时更新预览数据

注意事项
--------

- 交互管理器需要有效的坐标系统和选择管理器
- 不同模式有不同的鼠标事件处理逻辑
- 预览数据用于实时显示绘制效果
- 信号系统用于通知上层组件
- 状态管理需要正确处理拖拽和选择状态
- 样式设置会影响新创建的图元

相关模块
--------

- :doc:`components.vispy.drawing.coordinate_system` - 坐标系统
- :doc:`components.vispy.drawing.selection_manager` - 选择管理
- :doc:`components.vispy.drawing.data_models` - 数据模型
- :doc:`components.vispy.drawing.drawing_canvas` - 绘图画布
- :doc:`common.style_sheet` - 样式表
