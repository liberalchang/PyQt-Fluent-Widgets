Screen Color Picker 屏幕取色器模块
=====================================

Screen Color Picker 模块提供屏幕取色功能，支持实时预览和放大镜效果。
该模块允许用户从屏幕任意位置选取颜色，提供专业的取色界面和颜色预览功能。

主要功能
--------

- **屏幕取色** - 支持从屏幕任意位置取色
- **实时预览** - 提供实时的颜色预览和放大镜效果
- **放大镜效果** - 支持鼠标滚轮调节放大倍数
- **颜色显示** - 显示选中颜色的HEX值
- **颜色编辑** - 支持手动输入颜色值

核心组件
--------

ScreenColorPicker
~~~~~~~~~~~~~~~~~

屏幕取色器控件，提供完整的屏幕取色功能。

.. code-block:: python

   from qfluentwidgets.components.dialog_box.screen_color_picker import ScreenColorPicker
   from qfluentwidgets import CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QColor
   
   # 创建屏幕取色器
   color_picker = ScreenColorPicker(QColor("#FF6B6B"))
   
   # 连接信号
   color_picker.colorChanged.connect(on_color_changed)
   
   # 开始取色
   color_picker.startPicking()

**主要信号：**
- ``colorChanged`` - 颜色变化信号

**主要方法：**
- ``startPicking()`` - 开始取色
- ``setColor()`` - 设置颜色

ScreenColorPickerOverlay
~~~~~~~~~~~~~~~~~~~~~~~~

屏幕取色覆盖层，提供全屏取色界面。

.. code-block:: python

   from qfluentwidgets.components.dialog_box.screen_color_picker import ScreenColorPickerOverlay
   from PySide6.QtGui import QColor
   
   # 创建取色覆盖层
   overlay = ScreenColorPickerOverlay()
   
   # 连接信号
   overlay.colorSelected.connect(on_color_selected)
   
   # 显示覆盖层
   overlay.show()

ColorPreview
~~~~~~~~~~~~

颜色预览标签，显示当前选中的颜色。

.. code-block:: python

   from qfluentwidgets.components.dialog_box.screen_color_picker import ColorPreview
   from PySide6.QtGui import QColor
   
   # 创建颜色预览
   preview = ColorPreview(QColor("#FF6B6B"))
   
   # 设置颜色
   preview.setColor(QColor("#4ECDC4"))

实际应用
--------

基本屏幕取色器
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.screen_color_picker import ScreenColorPicker
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QColor
   
   class BasicScreenColorPickerWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("屏幕取色器")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 创建屏幕取色器
           self.color_picker = ScreenColorPicker(QColor("#FF6B6B"))
           
           # 显示选中的颜色
           self.selected_color_label = Label("当前颜色: #FF6B6B")
           self.selected_color_label.setAlignment(Qt.AlignCenter)
           
           # 控制按钮
           self.pick_color_btn = PushButton("开始取色")
           
           layout.addWidget(title_label)
           layout.addWidget(self.color_picker)
           layout.addWidget(self.selected_color_label)
           layout.addWidget(self.pick_color_btn)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.pick_color_btn.clicked.connect(self.start_picking)
           self.color_picker.colorChanged.connect(self.on_color_changed)
       
       def start_picking(self):
           """开始取色"""
           self.color_picker.startPicking()
       
       def on_color_changed(self, color):
           """颜色变化处理"""
           if color.isValid():
               color_name = color.name().upper()
               self.selected_color_label.setText(f"当前颜色: {color_name}")
               self.selected_color_label.setStyleSheet(
                   f"background-color: {color_name}; color: white; "
                   f"padding: 5px; border-radius: 3px;"
               )

颜色采集器
~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.screen_color_picker import ScreenColorPicker
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtGui import QColor
   
   class ColorCollectorWidget(CardWidget):
       """颜色采集器"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
           self.collected_colors = []
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("颜色采集器")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 创建屏幕取色器
           self.color_picker = ScreenColorPicker(QColor("#FF6B6B"))
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           self.pick_btn = PushButton("取色")
           self.save_btn = PushButton("保存颜色")
           self.clear_btn = PushButton("清空")
           
           button_layout.addWidget(self.pick_btn)
           button_layout.addWidget(self.save_btn)
           button_layout.addWidget(self.clear_btn)
           
           # 显示采集的颜色
           self.colors_label = Label("未采集颜色")
           self.colors_label.setAlignment(Qt.AlignCenter)
           
           layout.addWidget(title_label)
           layout.addWidget(self.color_picker)
           layout.addLayout(button_layout)
           layout.addWidget(self.colors_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.pick_btn.clicked.connect(self.start_picking)
           self.save_btn.clicked.connect(self.save_color)
           self.clear_btn.clicked.connect(self.clear_colors)
           self.color_picker.colorChanged.connect(self.on_color_changed)
       
       def start_picking(self):
           """开始取色"""
           self.color_picker.startPicking()
       
       def on_color_changed(self, color):
           """颜色变化处理"""
           if color.isValid():
               self.current_color = color
               color_name = color.name().upper()
               self.colors_label.setText(f"当前颜色: {color_name}")
               self.colors_label.setStyleSheet(
                   f"background-color: {color_name}; color: white; "
                   f"padding: 5px; border-radius: 3px;"
               )
       
       def save_color(self):
           """保存颜色"""
           if hasattr(self, 'current_color') and self.current_color.isValid():
               color_name = self.current_color.name().upper()
               if color_name not in self.collected_colors:
                   self.collected_colors.append(color_name)
                   self.update_colors_display()
       
       def clear_colors(self):
           """清空颜色"""
           self.collected_colors = []
           self.update_colors_display()
       
       def update_colors_display(self):
           """更新颜色显示"""
           if self.collected_colors:
               colors_text = "已采集颜色:\n" + "\n".join(self.collected_colors)
               self.colors_label.setText(colors_text)
               self.colors_label.setStyleSheet("padding: 5px; border-radius: 3px;")
           else:
               self.colors_label.setText("未采集颜色")
               self.colors_label.setStyleSheet("")

高级用法
--------

自定义取色器
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.screen_color_picker import ScreenColorPickerOverlay, ColorPreview
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtGui import QColor
   
   class CustomScreenColorPickerWidget(CardWidget):
       """自定义屏幕取色器"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("自定义屏幕取色器")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 颜色预览区域
           preview_layout = QHBoxLayout()
           
           self.preview_label = ColorPreview(QColor("#FF6B6B"))
           self.color_info_label = Label("#FF6B6B")
           
           preview_layout.addWidget(self.preview_label)
           preview_layout.addWidget(self.color_info_label)
           preview_layout.addStretch()
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           self.pick_btn = PushButton("开始取色")
           self.advanced_btn = PushButton("高级取色")
           
           button_layout.addWidget(self.pick_btn)
           button_layout.addWidget(self.advanced_btn)
           
           # 显示详细信息
           self.detail_label = Label("RGB: 255, 107, 107")
           self.detail_label.setAlignment(Qt.AlignCenter)
           
           layout.addWidget(title_label)
           layout.addLayout(preview_layout)
           layout.addLayout(button_layout)
           layout.addWidget(self.detail_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.pick_btn.clicked.connect(self.start_basic_picking)
           self.advanced_btn.clicked.connect(self.start_advanced_picking)
       
       def start_basic_picking(self):
           """开始基本取色"""
           from qfluentwidgets.components.dialog_box.screen_color_picker import ScreenColorPicker
           color_picker = ScreenColorPicker()
           color_picker.colorChanged.connect(self.on_color_changed)
           color_picker.startPicking()
       
       def start_advanced_picking(self):
           """开始高级取色"""
           overlay = ScreenColorPickerOverlay()
           overlay.colorSelected.connect(self.on_color_selected)
           overlay.show()
       
       def on_color_changed(self, color):
           """颜色变化处理"""
           self.update_color_display(color)
       
       def on_color_selected(self, color):
           """颜色选择处理"""
           self.update_color_display(color)
       
       def update_color_display(self, color):
           """更新颜色显示"""
           if color.isValid():
               color_name = color.name().upper()
               rgb = f"RGB({color.red()}, {color.green()}, {color.blue()})"
               hsv = f"HSV({color.hue()}, {color.saturation()}, {color.value()})"
               
               self.preview_label.setColor(color)
               self.color_info_label.setText(color_name)
               self.detail_label.setText(f"{rgb}\n{hsv}")

颜色历史记录器
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.screen_color_picker import ScreenColorPicker
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem
   from PySide6.QtGui import QColor, QPixmap
   from PySide6.QtCore import Qt
   
   class ColorHistoryWidget(CardWidget):
       """颜色历史记录器"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
           self.color_history = []
           self.max_history = 20
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("颜色历史记录器")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 屏幕取色器
           self.color_picker = ScreenColorPicker(QColor("#FF6B6B"))
           
           # 历史记录列表
           self.history_list = QListWidget()
           self.history_list.setMaximumHeight(200)
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           self.pick_btn = PushButton("取色")
           self.clear_btn = PushButton("清空历史")
           
           button_layout.addWidget(self.pick_btn)
           button_layout.addWidget(self.clear_btn)
           
           layout.addWidget(title_label)
           layout.addWidget(self.color_picker)
           layout.addWidget(self.history_list)
           layout.addLayout(button_layout)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.pick_btn.clicked.connect(self.start_picking)
           self.clear_btn.clicked.connect(self.clear_history)
           self.color_picker.colorChanged.connect(self.on_color_changed)
           self.history_list.itemClicked.connect(self.on_history_item_clicked)
       
       def start_picking(self):
           """开始取色"""
           self.color_picker.startPicking()
       
       def on_color_changed(self, color):
           """颜色变化处理"""
           if color.isValid():
               self.add_to_history(color)
       
       def add_to_history(self, color):
           """添加到历史记录"""
           color_name = color.name().upper()
           
           # 检查是否已存在
           for i in range(self.history_list.count()):
               item = self.history_list.item(i)
               if item.data(Qt.UserRole) == color_name:
                   return
           
           # 创建列表项
           item = QListWidgetItem()
           item.setData(Qt.UserRole, color_name)
           
           # 创建颜色图标
           pixmap = QPixmap(16, 16)
               pixmap.fill(color)
               item.setIcon(pixmap)
               
               # 设置文本
               item.setText(color_name)
               
               # 添加到列表
               self.history_list.insertItem(0, item)
               
               # 限制历史记录数量
               if self.history_list.count() > self.max_history:
                   self.history_list.takeItem(self.max_history)
       
       def on_history_item_clicked(self, item):
           """历史项点击处理"""
           color_name = item.data(Qt.UserRole)
           color = QColor(color_name)
           if color.isValid():
               self.color_picker.setColor(color)
       
       def clear_history(self):
           """清空历史记录"""
           self.history_list.clear()

最佳实践
--------

1. **权限检查** - 确保应用有屏幕访问权限
2. **用户体验** - 提供清晰的取色引导和反馈
3. **颜色格式** - 支持多种颜色格式的显示和输入
4. **历史记录** - 保存用户的取色历史
5. **快捷操作** - 提供键盘快捷键支持

注意事项
--------

- 屏幕取色需要正确的系统权限
- 取色覆盖层会覆盖整个屏幕
- 鼠标滚轮可以调节放大倍数
- ESC键可以取消取色操作
- 颜色值支持HEX格式输入

相关模块
--------

- :doc:`components.dialog_box.color_dialog` - 颜色对话框
- :doc:`components.dialog_box.color_palette` - 颜色调色板
- :doc:`common.color` - 颜色管理
