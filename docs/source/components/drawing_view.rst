Drawing View 绘图视图模块
===============================

Drawing View 模块提供完整的绘图视图界面，集成工具面板、配置面板和交互式绘图控件。
该模块提供用户友好的绘图界面，支持多种绘图工具和样式配置。

主要功能
--------

- **工具面板** - 提供完整的绘图工具集合
- **配置面板** - 支持实时样式配置
- **交互式绘图** - 集成InteractiveDrawingWidget
- **样式管理** - 支持颜色、线宽、填充等样式配置
- **工具切换** - 支持工具和子工具的动态切换
- **键盘处理** - 支持ESC键取消操作

核心组件
--------

ColorPickerButton
~~~~~~~~~~~~~~~~

颜色选择按钮，提供颜色选择功能。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import ColorPickerButton
   
   # 创建颜色选择按钮
   color_btn = ColorPickerButton(
       color=(255, 255, 255),  # 白色
       parent=parent
   )
   
   # 连接颜色变化信号
   color_btn.colorChanged.connect(self.on_color_changed)
   
   # 设置颜色
   color_btn.setColor((255, 0, 0))  # 红色
   
   # 获取颜色
   color = color_btn.getColor()  # 返回 (r, g, b, a) 元组

**主要信号：**
- ``colorChanged`` - 颜色变化信号

**主要方法：**
- ``setColor()`` - 设置颜色
- ``getColor()`` - 获取颜色

PropertyGroup
~~~~~~~~~~~~~~

属性组控件，用于组织相关的属性控件。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import PropertyGroup
   from qfluentwidgets.components.widgets import PushButton
   
   # 创建属性组
   group = PropertyGroup("线条属性", parent)
   
   # 添加标签
   label = group.addLabel("线宽:")
   
   # 添加控件
   button = PushButton("设置", parent)
   group.addWidget(button)
   
   # 添加分隔符
   group.addSeparator()

ConfigPanel
~~~~~~~~~~~~

配置面板，提供不同工具的样式配置界面。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import ConfigPanel
   from qfluentwidgets.components.vispy.drawing import StyleData
   
   # 创建配置面板
   config_panel = ConfigPanel(parent=parent)
   
   # 连接信号
   config_panel.styleChanged.connect(self.on_style_changed)
   config_panel.handlesChanged.connect(self.on_handles_changed)
   
   # 设置样式数据
   style = StyleData(
       lineWidth=2.0,
       lineColor=(1.0, 0.0, 0.0, 1.0),
       filled=True,
       fillColor=(1.0, 0.5, 0.5, 0.5)
   )
   config_panel.setStyleData(style)

**主要信号：**
- ``styleChanged`` - 样式变化信号
- ``handlesChanged`` - 控制端点变化信号

**主要方法：**
- ``setStyleData()`` - 设置样式数据
- ``updatePageIcon()`` - 更新页面图标

DrawingView
~~~~~~~~~~~

绘图视图主控件，集成工具面板、配置面板和绘图控件。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import DrawingView
   
   # 创建绘图视图
   drawing_view = DrawingView(parent=parent)
   
   # 设置尺寸
   drawing_view.setFixedSize(800, 600)
   
   # 连接信号
   drawing_view.drawingWidget.primitiveAdded.connect(self.on_primitive_added)
   drawing_view.drawingWidget.selectionChanged.connect(self.on_selection_changed)

**主要属性：**
- ``drawingWidget`` - 交互式绘图控件
- ``toolPanel`` - 工具面板
- ``configPanel`` - 配置面板

实际应用
--------

基本绘图视图
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import DrawingView
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   
   class BasicDrawingViewWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_drawing_view()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("基本绘图视图")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.clear_btn = PushButton("清空画布")
           self.export_btn = PushButton("导出数据")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.clear_btn)
           header_layout.addWidget(self.export_btn)
           
           # 创建绘图视图
           self.drawing_view = DrawingView(parent=self)
           self.drawing_view.setFixedSize(800, 600)
           
           # 显示当前状态
           self.status_label = Label("状态: 绘图视图已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.drawing_view)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_drawing_view(self):
           """设置绘图视图"""
           # 连接信号
           self.drawing_view.drawingWidget.primitiveAdded.connect(self.on_primitive_added)
           self.drawing_view.drawingWidget.selectionChanged.connect(self.on_selection_changed)
           
           self.status_label.setText("状态: 绘图视图已设置")
       
       def setup_connections(self):
           """设置连接"""
           self.clear_btn.clicked.connect(self.clear_canvas)
           self.export_btn.clicked.connect(self.export_data)
       
       def clear_canvas(self):
           """清空画布"""
           self.drawing_view.drawingWidget.clearAll()
           self.status_label.setText("状态: 画布已清空")
       
       def export_data(self):
           """导出数据"""
           data = self.drawing_view.drawingWidget.exportLayerData()
           
           # 统计信息
           total_primitives = 0
           for layer in data.get('layers', []):
               total_primitives += len(layer.get('primitives', []))
           
           self.status_label.setText(f"状态: 数据已导出，{total_primitives} 个图元")
           print(f"导出的数据: {data}")
       
       def on_primitive_added(self, primitive_id):
           """图元添加处理"""
           print(f"图元已添加: {primitive_id}")
           self.status_label.setText(f"状态: 已添加图元 {primitive_id[:8]}")
       
       def on_selection_changed(self, selected_ids):
           """选择变化处理"""
           if selected_ids:
               self.status_label.setText(f"状态: 已选择 {len(selected_ids)} 个图元")
           else:
               self.status_label.setText("状态: 无选择")

高级绘图视图
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import DrawingView
   from qfluentwidgets.components.vispy.drawing import StyleData
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   
   class AdvancedDrawingViewWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_drawing_view()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("高级绘图视图")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.style_btn = PushButton("应用样式")
           self.mode_btn = PushButton("切换模式")
           self.info_btn = PushButton("视图信息")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.style_btn)
           header_layout.addWidget(self.mode_btn)
           header_layout.addWidget(self.info_btn)
           
           # 创建绘图视图
           self.drawing_view = DrawingView(parent=self)
           self.drawing_view.setFixedSize(800, 600)
           
           # 显示当前状态
           self.status_label = Label("状态: 高级绘图视图已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.drawing_view)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_drawing_view(self):
           """设置高级绘图视图"""
           # 连接信号
           self.drawing_view.drawingWidget.primitiveAdded.connect(self.on_primitive_added)
           self.drawing_view.drawingWidget.interactionModeChanged.connect(self.on_mode_changed)
           self.drawing_view.configPanel.styleChanged.connect(self.on_style_changed)
           
           self.status_label.setText("状态: 高级绘图视图已设置")
       
       def setup_connections(self):
           """设置连接"""
           self.style_btn.clicked.connect(self.apply_style)
           self.mode_btn.clicked.connect(self.switch_mode)
           self.info_btn.clicked.connect(self.show_info)
       
       def apply_style(self):
           """应用预设样式"""
           import random
           
           # 创建随机样式
           style = StyleData(
               lineWidth=random.uniform(1, 5),
               lineColor=(random.random(), random.random(), random.random(), 1.0),
               filled=True,
               fillColor=(random.random(), random.random(), random.random(), 0.5),
               borderColor=(random.random(), random.random(), random.random(), 1.0),
               borderWidth=random.uniform(1, 3)
           )
           
           # 应用到配置面板
           self.drawing_view.configPanel.setStyleData(style)
           
           # 设置为默认样式
           self.drawing_view.drawingWidget.setDefaultStyle(style)
           
           self.status_label.setText("状态: 已应用随机样式")
       
       def switch_mode(self):
           """切换交互模式"""
           from qfluentwidgets.components.vispy.drawing import InteractionMode
           
           # 获取当前模式
           current_mode = self.drawing_view.drawingWidget.getInteractionMode()
           
           # 切换到下一个模式
           modes = [
               InteractionMode.DEFAULT,
               InteractionMode.MOVE,
               InteractionMode.DRAW_LINE,
               InteractionMode.DRAW_RECTANGLE,
               InteractionMode.DRAW_CIRCLE
           ]
           
           try:
               current_index = modes.index(current_mode)
               next_index = (current_index + 1) % len(modes)
               next_mode = modes[next_index]
           except ValueError:
               next_mode = InteractionMode.DEFAULT
           
           # 设置新模式
           self.drawing_view.drawingWidget.setInteractionMode(next_mode)
           
           mode_name = next_mode.name if hasattr(next_mode, 'name') else str(next_mode)
           self.status_label.setText(f"状态: 已切换到 {mode_name} 模式")
       
       def show_info(self):
           """显示视图信息"""
           # 获取当前模式
           mode = self.drawing_view.drawingWidget.getInteractionMode()
           mode_name = mode.name if hasattr(mode, 'name') else str(mode)
           
           # 获取当前样式
           style = self.drawing_view.drawingWidget.getDefaultStyle()
           
           # 获取图元数量
           all_primitives = self.drawing_view.drawingWidget.getAllPrimitives()
           
           info_lines = [
               f"当前模式: {mode_name}",
               f"线宽: {style.lineWidth:.1f}",
               f"线宽颜色: {style.lineColor}",
               f"填充颜色: {style.fillColor}",
               f"图元数量: {len(all_primitives)}"
           ]
           
           self.status_label.setText("\n".join(info_lines))
       
       def on_primitive_added(self, primitive_id):
           """图元添加处理"""
           print(f"图元已添加: {primitive_id}")
       
       def on_mode_changed(self, mode):
           """模式变化处理"""
           mode_name = mode.name if hasattr(mode, 'name') else str(mode)
           self.status_label.setText(f"状态: 模式已切换到 {mode_name}")
       
       def on_style_changed(self, style):
           """样式变化处理"""
           print(f"样式已变化: 线宽={style.lineWidth:.1f}")
           self.status_label.setText(f"状态: 样式已更新，线宽={style.lineWidth:.1f}")

自定义绘图视图
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import DrawingView, ConfigPanel
   from qfluentwidgets.components.vispy.drawing import StyleData
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   
   class CustomDrawingViewWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_drawing_view()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("自定义绘图视图")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.custom_btn = PushButton("自定义样式")
           self.reset_btn = PushButton("重置样式")
           self.preset_btn = PushButton("预设样式")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.custom_btn)
           header_layout.addWidget(self.reset_btn)
           header_layout.addWidget(self.preset_btn)
           
           # 创建绘图视图
           self.drawing_view = DrawingView(parent=self)
           self.drawing_view.setFixedSize(800, 600)
           
           # 显示当前状态
           self.status_label = Label("状态: 自定义绘图视图已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.drawing_view)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_drawing_view(self):
           """设置自定义绘图视图"""
           # 连接信号
           self.drawing_view.drawingWidget.primitiveAdded.connect(self.on_primitive_added)
           self.drawing_view.configPanel.styleChanged.connect(self.on_style_changed)
           
           # 创建预设样式
           self.create_preset_styles()
           
           self.status_label.setText("状态: 自定义绘图视图已设置")
       
       def create_preset_styles(self):
           """创建预设样式"""
           self.preset_styles = {
               'default': StyleData(
                   lineWidth=2.0,
                   lineColor=(0.0, 0.0, 0.0, 1.0),
                   filled=True,
                   fillColor=(0.5, 0.5, 0.5, 0.5)
               ),
               'red': StyleData(
                   lineWidth=3.0,
                   lineColor=(1.0, 0.0, 0.0, 1.0),
                   filled=True,
                   fillColor=(1.0, 0.5, 0.5, 0.5)
               ),
               'blue': StyleData(
                   lineWidth=2.5,
                   lineColor=(0.0, 0.0, 1.0, 1.0),
                   filled=True,
                   fillColor=(0.5, 0.5, 1.0, 0.5)
               ),
               'green': StyleData(
                   lineWidth=1.5,
                   lineColor=(0.0, 1.0, 0.0, 1.0),
                   filled=True,
                   fillColor=(0.5, 1.0, 0.5, 0.5)
               )
           }
           self.current_preset = 0
           self.preset_names = list(self.preset_styles.keys())
       
       def setup_connections(self):
           """设置连接"""
           self.custom_btn.clicked.connect(self.apply_custom_style)
           self.reset_btn.clicked.connect(self.reset_style)
           self.preset_btn.clicked.connect(self.cycle_preset)
       
       def apply_custom_style(self):
           """应用自定义样式"""
           import random
           
           # 创建自定义随机样式
           custom_style = StyleData(
               lineWidth=random.uniform(0.5, 5.0),
               lineColor=(random.random(), random.random(), random.random(), 1.0),
               filled=random.choice([True, False]),
               fillColor=(random.random(), random.random(), random.random(), 0.7) if random.random() > 0.3 else (0, 0, 0, 0),
               borderColor=(random.random(), random.random(), random.random(), 1.0),
               borderWidth=random.uniform(0.5, 3.0),
               pointSize=random.uniform(3.0, 10.0)
           )
           
           # 应用样式
           self.drawing_view.configPanel.setStyleData(custom_style)
           self.drawing_view.drawingWidget.setDefaultStyle(custom_style)
           
           self.status_label.setText("状态: 已应用自定义随机样式")
       
       def reset_style(self):
           """重置为默认样式"""
           default_style = self.preset_styles['default']
           
           # 应用默认样式
           self.drawing_view.configPanel.setStyleData(default_style)
           self.drawing_view.drawingWidget.setDefaultStyle(default_style)
           
           self.status_label.setText("状态: 已重置为默认样式")
       
       def cycle_preset(self):
           """循环切换预设样式"""
           self.current_preset = (self.current_preset + 1) % len(self.preset_names)
           preset_name = self.preset_names[self.current_preset]
           preset_style = self.preset_styles[preset_name]
           
           # 应用预设样式
           self.drawing_view.configPanel.setStyleData(preset_style)
           self.drawing_view.drawingWidget.setDefaultStyle(preset_style)
           
           self.status_label.setText(f"状态: 已应用预设样式 '{preset_name}'")
       
       def on_primitive_added(self, primitive_id):
           """图元添加处理"""
           print(f"图元已添加: {primitive_id}")
       
       def on_style_changed(self, style):
           """样式变化处理"""
           print(f"样式已变化: 线宽={style.lineWidth:.1f}")

最佳实践
--------

1. **界面布局** - 合理安排工具面板、配置面板和绘图区域
2. **样式管理** - 使用统一的样式管理机制
3. **信号连接** - 正确连接和处理各种信号
4. **工具切换** - 提供流畅的工具切换体验
5. **键盘处理** - 支持常用的键盘快捷键

注意事项
--------

- 绘图视图需要有效的vispy环境
- 工具面板支持子工具的展开和收起
- 配置面板会根据当前工具自动切换
- ESC键可以取消当前操作并切换到默认模式
- 样式变化会实时应用到新创建的图元
- 大量图元可能影响性能

相关模块
--------

- :doc:`components.vispy.drawing.drawing_widget` - 绘图控件
- :doc:`components.vispy.drawing.interaction_manager` - 交互管理
- :doc:`components.vispy.drawing.data_models` - 数据模型
- :doc:`components.widgets.tool_panel` - 工具面板
- :doc:`components.widgets.color_dialog` - 颜色对话框
