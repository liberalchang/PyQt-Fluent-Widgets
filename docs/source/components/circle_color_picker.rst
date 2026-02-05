Circle Color Picker 圆形颜色选择器模块
=========================================

Circle Color Picker 模块提供圆形颜色选择功能，支持颜色列表管理和动态添加删除。
该模块提供直观的圆形颜色选择界面，支持颜色的选择、添加、删除等操作。

主要功能
--------

- **圆形显示** - 以圆形形式显示颜色选项
- **颜色管理** - 支持颜色列表的动态管理
- **交互操作** - 支持点击选择和右键删除
- **信号通知** - 提供丰富的颜色变化信号
- **主题适配** - 完美适配Fluent Design主题

核心组件
--------

CircleColorPicker
~~~~~~~~~~~~~~~~~

圆形颜色选择器，提供颜色选择和管理功能。

.. code-block:: python

   from qfluentwidgets.components.dialog_box.circle_color_picker import CircleColorPicker
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QColor
   
   # 创建圆形颜色选择器
   color_picker = CircleColorPicker()
   
   # 设置颜色列表
   colors = [
       QColor("#FF0000"),  # 红色
       QColor("#00FF00"),  # 绿色
       QColor("#0000FF"),  # 蓝色
   ]
   color_picker.setColors(colors)
   
   # 连接信号
   color_picker.colorChanged.connect(on_color_changed)
   color_picker.addColorClicked.connect(on_add_color)
   color_picker.colorRemoved.connect(on_color_removed)

**主要信号：**
- ``colorChanged`` - 颜色变化信号
- ``addColorClicked`` - 添加颜色点击信号
- ``colorRemoved`` - 颜色删除信号
- ``colorAdded`` - 颜色添加信号
- ``colorsChanged`` - 颜色列表变化信号

**主要方法：**
- ``setColors()`` - 设置颜色列表
- ``setColor()`` - 设置当前颜色
- ``color()`` - 获取当前颜色
- ``addColor()`` - 添加颜色
- ``removeColor()`` - 删除颜色

CircleColorItem
~~~~~~~~~~~~~~~

圆形颜色项，单个颜色的显示组件。

.. code-block:: python

   from qfluentwidgets.components.dialog_box.circle_color_picker import CircleColorItem
   from PySide6.QtGui import QColor
   from PySide6.QtWidgets import QVBoxLayout
   
   # 创建圆形颜色项
   color_item = CircleColorItem(QColor("#FF6B6B"))
   
   # 连接删除信号
   color_item.removeRequested.connect(on_remove_requested)

实际应用
--------

基本颜色选择器
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.circle_color_picker import CircleColorPicker
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtGui import QColor
   
   class BasicColorPickerWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("选择颜色")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 创建圆形颜色选择器
           self.color_picker = CircleColorPicker()
           
           # 设置默认颜色
           default_colors = [
               QColor("#FF6B6B"),  # 红色
               QColor("#4ECDC4"),  # 青色
               QColor("#45B7D1"),  # 蓝色
               QColor("#96CEB4"),  # 绿色
               QColor("#FFEAA7"),  # 黄色
               QColor("#DDA0DD"),  # 紫色
           ]
           self.color_picker.setColors(default_colors)
           
           # 显示选中的颜色
           self.selected_color_label = Label("未选择颜色")
           self.selected_color_label.setAlignment(Qt.AlignCenter)
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           add_custom_btn = PushButton("添加自定义颜色")
           reset_btn = PushButton("重置")
           
           add_custom_btn.clicked.connect(self.add_custom_color)
           reset_btn.clicked.connect(self.reset_colors)
           
           button_layout.addWidget(add_custom_btn)
           button_layout.addWidget(reset_btn)
           
           layout.addWidget(title_label)
           layout.addWidget(self.color_picker)
           layout.addWidget(self.selected_color_label)
           layout.addLayout(button_layout)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.color_picker.colorChanged.connect(self.on_color_changed)
           self.color_picker.addColorClicked.connect(self.on_add_color)
           self.color_picker.colorRemoved.connect(self.on_color_removed)
       
       def on_color_changed(self, color):
           """颜色变化处理"""
           if color.isValid():
               color_name = color.name().upper()
               self.selected_color_label.setText(f"已选择: {color_name}")
               self.selected_color_label.setStyleSheet(
                   f"background-color: {color_name}; color: white; padding: 5px; border-radius: 3px;"
               )
           else:
               self.selected_color_label.setText("未选择颜色")
               self.selected_color_label.setStyleSheet("")
       
       def on_add_color(self):
           """添加颜色点击处理"""
           # 这里可以打开颜色选择对话框
           from qfluentwidgets.components.dialog_box.color_dialog import ColorDialog
           
           color_dialog = ColorDialog(self)
           if color_dialog.exec():
               new_color = color_dialog.color
               self.color_picker.addColor(new_color)
       
       def on_color_removed(self, color):
           """颜色删除处理"""
           print(f"删除了颜色: {color.name()}")
       
       def add_custom_color(self):
           """添加自定义颜色"""
           # 添加一些预设颜色
           custom_colors = [
               QColor("#FF1744"),  # 亮红色
               QColor("#D500F9"),  # 亮紫色
               QColor("#00E676"),  # 亮绿色
           ]
           
           for color in custom_colors:
               self.color_picker.addColor(color)
       
       def reset_colors(self):
           """重置颜色"""
           default_colors = [
               QColor("#FF6B6B"),
               QColor("#4ECDC4"),
               QColor("#45B7D1"),
           ]
           self.color_picker.setColors(default_colors)

动态颜色管理
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.circle_color_picker import CircleColorPicker
   from qfluentwidgets import CardWidget, Label, PushButton, LineEdit
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtGui import QColor
   
   class DynamicColorPickerWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("动态颜色管理")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 创建圆形颜色选择器
           self.color_picker = CircleColorPicker()
           
           # 颜色输入
           input_layout = QHBoxLayout()
           
           color_input_label = Label("颜色值:")
           self.color_input = LineEdit()
           self.color_input.setPlaceholderText("#FF0000")
           
           add_btn = PushButton("添加")
           add_btn.clicked.connect(self.add_color_from_input)
           
           input_layout.addWidget(color_input_label)
           input_layout.addWidget(self.color_input)
           input_layout.addWidget(add_btn)
           
           # 预设颜色按钮
           preset_layout = QHBoxLayout()
           
           red_btn = PushButton("红色系")
           blue_btn = PushButton("蓝色系")
           green_btn = PushButton("绿色系")
           clear_btn = PushButton("清空")
           
           red_btn.clicked.connect(lambda: self.add_preset_colors("red"))
           blue_btn.clicked.connect(lambda: self.add_preset_colors("blue"))
           green_btn.clicked.connect(lambda: self.add_preset_colors("green"))
           clear_btn.clicked.connect(self.clear_all_colors)
           
           preset_layout.addWidget(red_btn)
           preset_layout.addWidget(blue_btn)
           preset_layout.addWidget(green_btn)
           preset_layout.addWidget(clear_btn)
           
           # 显示颜色数量
           self.count_label = Label("颜色数量: 0")
           
           layout.addWidget(title_label)
           layout.addWidget(self.color_picker)
           layout.addLayout(input_layout)
           layout.addLayout(preset_layout)
           layout.addWidget(self.count_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.color_picker.colorChanged.connect(self.on_color_changed)
           self.color_picker.colorsChanged.connect(self.on_colors_changed)
       
       def on_color_changed(self, color):
           """颜色变化处理"""
           if color.isValid():
               print(f"选择了颜色: {color.name()}")
       
       def on_colors_changed(self, colors):
           """颜色列表变化处理"""
           self.count_label.setText(f"颜色数量: {len(colors)}")
       
       def add_color_from_input(self):
           """从输入框添加颜色"""
           color_text = self.color_input.text().strip()
           if color_text:
               try:
                   color = QColor(color_text)
                   if color.isValid():
                       self.color_picker.addColor(color)
                       self.color_input.clear()
                   else:
                       self.color_input.setStyleSheet("border: 1px solid red;")
               except:
                   self.color_input.setStyleSheet("border: 1px solid red;")
       
       def add_preset_colors(self, color_type):
           """添加预设颜色"""
           preset_colors = {
               "red": [
                   QColor("#FF6B6B"), QColor("#FF8E53"), QColor("#FF6B9D"),
                   QColor("#C44569"), QColor("#F8B500"), QColor("#FF6348")
               ],
               "blue": [
                   QColor("#4ECDC4"), QColor("#45B7D1"), QColor("#5F27CD"),
                   QColor("#00D2D3"), QColor("#3498DB"), QColor("#2980B9")
               ],
               "green": [
                   QColor("#96CEB4"), QColor("#88D8B0"), QColor("#6AB04C"),
                   QColor("#44BD32"), QColor("#4CD137"), QColor("#00D2D3")
               ]
           }
           
           colors = preset_colors.get(color_type, [])
           for color in colors:
               self.color_picker.addColor(color)
       
       def clear_all_colors(self):
           """清空所有颜色"""
           self.color_picker.setColors([])

高级用法
--------

自定义圆形颜色项
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.circle_color_picker import CircleColorItem
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QColor, QPainter, QPen
   from PySide6.QtCore import Qt
   
   class CustomCircleColorItem(CircleColorItem):
       """自定义圆形颜色项"""
       
       def __init__(self, color: QColor, parent=None):
           super().__init__(color, parent)
           self.show_border = True
           self.border_width = 2
       
       def paintEvent(self, e):
           """重写绘制事件"""
           painter = QPainter(self)
           painter.setRenderHints(QPainter.Antialiasing)
           
           # 中心点和半径
           cx, cy = self.width() / 2, self.height() / 2
           
           if self.isChecked():
               # 选中状态：外圈+内圈
               radius_outer = 13
               radius_inner = 9
               
               # 绘制外圈
               pen = QPen(self.color, self.border_width)
               painter.setPen(pen)
               painter.setBrush(Qt.NoBrush)
               painter.drawEllipse(QRectF(cx - radius_outer, cy - radius_outer, 
                                        radius_outer * 2, radius_outer * 2))
               
               # 绘制内圈
               painter.setPen(Qt.NoPen)
               painter.setBrush(self.color)
               painter.drawEllipse(QRectF(cx - radius_inner, cy - radius_inner, 
                                        radius_inner * 2, radius_inner * 2))
           else:
               # 普通状态：实心圆
               radius = 11
               
               painter.setPen(Qt.NoPen)
               painter.setBrush(self.color)
               painter.drawEllipse(QRectF(cx - radius, cy - radius, 
                                        radius * 2, radius * 2))
               
               # 悬停效果
               if self.isDown():
                   painter.setBrush(QColor(0, 0, 0, 20))
                   painter.drawEllipse(QRectF(cx - radius, cy - radius, 
                                            radius * 2, radius * 2))
           
           # 自定义边框
           if self.show_border and not self.isChecked():
               painter.setPen(QPen(Qt.gray, 1))
               painter.setBrush(Qt.NoBrush)
               painter.drawEllipse(QRectF(cx - radius, cy - radius, 
                                        radius * 2, radius * 2))
   
   class CustomColorPickerWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("自定义颜色选择器")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 显示自定义颜色项
           custom_item = CustomCircleColorItem(QColor("#FF6B6B"))
           
           layout.addWidget(title_label)
           layout.addWidget(custom_item)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           pass

颜色主题管理
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.circle_color_picker import CircleColorPicker
   from qfluentwidgets import CardWidget, Label, ComboBox, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtGui import QColor
   
   class ThemeColorPickerWidget(CardWidget):
       """主题颜色选择器"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
           self.setup_themes()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("主题颜色选择器")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 主题选择
           theme_layout = QHBoxLayout()
           
           theme_label = Label("主题:")
           self.theme_combo = ComboBox()
           self.theme_combo.addItems([
               "默认主题",
               "暗色主题",
               "亮色主题",
               "彩色主题",
               "商务主题"
           ])
           
           theme_layout.addWidget(theme_label)
           theme_layout.addWidget(self.theme_combo)
           
           # 创建圆形颜色选择器
           self.color_picker = CircleColorPicker()
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           apply_theme_btn = PushButton("应用主题")
           save_theme_btn = PushButton("保存主题")
           
           apply_theme_btn.clicked.connect(self.apply_theme)
           save_theme_btn.clicked.connect(self.save_theme)
           
           button_layout.addWidget(apply_theme_btn)
           button_layout.addWidget(save_theme_btn)
           
           layout.addWidget(title_label)
           layout.addLayout(theme_layout)
           layout.addWidget(self.color_picker)
           layout.addLayout(button_layout)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.theme_combo.currentTextChanged.connect(self.on_theme_changed)
           self.color_picker.colorChanged.connect(self.on_color_changed)
       
       def setup_themes(self):
           """设置主题"""
           self.themes = {
               "默认主题": [
                   QColor("#FF6B6B"), QColor("#4ECDC4"), QColor("#45B7D1"),
                   QColor("#96CEB4"), QColor("#FFEAA7"), QColor("#DDA0DD")
               ],
               "暗色主题": [
                   QColor("#2C3E50"), QColor("#34495E"), QColor("#7F8C8D"),
                   QColor("#95A5A6"), QColor("#BDC3C7"), QColor("#ECF0F1")
               ],
               "亮色主题": [
                   QColor("#FFFFFF"), QColor("#F8F9FA"), QColor("#E9ECEF"),
                   QColor("#DEE2E6"), QColor("#CED4DA"), QColor("#ADB5BD")
               ],
               "彩色主题": [
                   QColor("#FF6B6B"), QColor("#4ECDC4"), QColor("#45B7D1"),
                   QColor("#96CEB4"), QColor("#FFEAA7"), QColor("#FD79A8")
               ],
               "商务主题": [
                   QColor("#2C3E50"), QColor("#3498DB"), QColor("#E74C3C"),
                   QColor("#F39C12"), QColor("#27AE60"), QColor("#8E44AD")
               ]
           }
           
           # 应用默认主题
           self.apply_theme()
       
       def on_theme_changed(self, theme_name):
           """主题变化处理"""
           self.apply_theme()
       
       def on_color_changed(self, color):
           """颜色变化处理"""
           print(f"选择了主题颜色: {color.name()}")
       
       def apply_theme(self):
           """应用主题"""
           theme_name = self.theme_combo.currentText()
           colors = self.themes.get(theme_name, [])
           self.color_picker.setColors(colors)
       
       def save_theme(self):
           """保存当前主题"""
           current_colors = self.color_picker.colors
           theme_name = self.theme_combo.currentText()
           
           # 更新主题
           self.themes[theme_name] = current_colors
           print(f"已保存主题: {theme_name}")

最佳实践
--------

1. **颜色管理** - 合理管理颜色列表，避免重复
2. **用户体验** - 提供直观的颜色选择和添加方式
3. **主题一致性** - 保持与应用整体主题的一致性
4. **性能优化** - 避免过多的颜色项影响性能
5. **可访问性** - 确保颜色选择的可访问性

注意事项
--------

- 颜色值需要使用QColor或有效的颜色字符串
- 右键菜单需要正确处理删除操作
- 颜色项的选中状态需要正确管理
- 大量颜色可能影响界面布局
- 自定义绘制需要正确处理主题适配

相关模块
--------

- :doc:`components.dialog_box.color_dialog` - 颜色对话框
- :doc:`components.dialog_box.color_palette` - 颜色调色板
- :doc:`common.color` - 颜色管理
