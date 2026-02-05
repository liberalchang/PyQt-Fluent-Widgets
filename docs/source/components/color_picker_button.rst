Color Picker Button 颜色选择器按钮模块
=========================================

Color Picker Button 模块提供多种颜色选择器按钮，支持弹出式颜色选择界面。
该模块提供便捷的颜色选择按钮，包含标准颜色选择器、圆形颜色选择器和屏幕取色器等功能。

主要功能
--------

- **弹出式选择** - 提供弹出式的颜色选择界面
- **多种样式** - 支持标准、圆形、屏幕取色等多种样式
- **自定义颜色** - 支持用户自定义颜色管理
- **实时预览** - 提供实时的颜色预览功能
- **图标支持** - 支持自定义图标和文本显示

核心组件
--------

ColorButton
~~~~~~~~~~~

标准颜色选择器按钮，提供完整的颜色选择功能。

.. code-block:: python

   from qfluentwidgets.components.dialog_box.color_picker_button import ColorButton
   from qfluentwidgets import CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QColor
   
   # 创建颜色选择器按钮
   color_button = ColorButton(
       color=QColor("#FF6B6B"),
       title="选择颜色",
       showPreview=True
   )
   
   # 连接信号
   color_button.colorChanged.connect(on_color_changed)

**主要信号：**
- ``colorChanged`` - 颜色变化信号

**主要方法：**
- ``setColor()`` - 设置颜色
- ``color()`` - 获取颜色
- ``setIcon()`` - 设置图标

ColorDialogButton
~~~~~~~~~~~~~~~~

颜色对话框按钮，提供完整的颜色选择对话框界面。

.. code-block:: python

   from qfluentwidgets.components.dialog_box.color_picker_button import ColorDialogButton
   from qfluentwidgets import CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QColor
   
   # 创建颜色对话框按钮
   dialog_button = ColorDialogButton(
       color=QColor("#4ECDC4"),
       title="颜色对话框"
   )
   
   # 连接信号
   dialog_button.colorChanged.connect(on_color_changed)

CircleColorButton
~~~~~~~~~~~~~~~~

圆形颜色选择器按钮，提供圆形颜色选择界面。

.. code-block:: python

   from qfluentwidgets.components.dialog_box.color_picker_button import CircleColorButton
   from qfluentwidgets import CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QColor
   
   # 创建圆形颜色选择器按钮
   circle_button = CircleColorButton(
       color=QColor("#45B7D1"),
       title="圆形选择器"
   )
   
   # 连接信号
   circle_button.colorChanged.connect(on_color_changed)

ScreenColorButton
~~~~~~~~~~~~~~~~~

屏幕取色器按钮，提供屏幕取色功能。

.. code-block:: python

   from qfluentwidgets.components.dialog_box.color_picker_button import ScreenColorButton
   from qfluentwidgets import CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QColor
   
   # 创建屏幕取色器按钮
   screen_button = ScreenColorButton(
       color=QColor("#96CEB4"),
       title="屏幕取色"
   )
   
   # 连接信号
   screen_button.colorChanged.connect(on_color_changed)

实际应用
--------

基本颜色选择器按钮
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.color_picker_button import ColorButton
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QColor
   
   class BasicColorButtonWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("颜色选择器按钮")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 创建颜色选择器按钮
           self.color_button = ColorButton(
               color=QColor("#FF6B6B"),
               title="选择颜色",
               showPreview=True
           )
           
           # 显示选中的颜色
           self.selected_color_label = Label("未选择颜色")
           self.selected_color_label.setAlignment(Qt.AlignCenter)
           
           layout.addWidget(title_label)
           layout.addWidget(self.color_button)
           layout.addWidget(self.selected_color_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.color_button.colorChanged.connect(self.on_color_changed)
       
       def on_color_changed(self, color):
           """颜色变化处理"""
           if color.isValid():
               color_name = color.name().upper()
               self.selected_color_label.setText(f"已选择: {color_name}")
               self.selected_color_label.setStyleSheet(
                   f"background-color: {color_name}; color: white; "
                   f"padding: 5px; border-radius: 3px;"
               )
           else:
               self.selected_color_label.setText("未选择颜色")
               self.selected_color_label.setStyleSheet("")

多种颜色选择器
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.color_picker_button import (
       ColorButton, ColorDialogButton, CircleColorButton, ScreenColorButton
   )
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtGui import QColor
   
   class MultipleColorButtonWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("多种颜色选择器")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 标准颜色选择器按钮
           self.color_button = ColorButton(
               color=QColor("#FF6B6B"),
               title="标准选择器",
               showPreview=True
           )
           
           # 颜色对话框按钮
           self.dialog_button = ColorDialogButton(
               color=QColor("#4ECDC4"),
               title="对话框选择器"
           )
           
           # 圆形颜色选择器按钮
           self.circle_button = CircleColorButton(
               color=QColor("#45B7D1"),
               title="圆形选择器"
           )
           
           # 屏幕取色器按钮
           self.screen_button = ScreenColorButton(
               color=QColor("#96CEB4"),
               title="屏幕取色"
           )
           
           # 显示选中的颜色
           self.selected_color_label = Label("未选择颜色")
           self.selected_color_label.setAlignment(Qt.AlignCenter)
           
           # 布局
           button_layout1 = QHBoxLayout()
           button_layout1.addWidget(self.color_button)
           button_layout1.addWidget(self.dialog_button)
           
           button_layout2 = QHBoxLayout()
           button_layout2.addWidget(self.circle_button)
           button_layout2.addWidget(self.screen_button)
           
           layout.addWidget(title_label)
           layout.addLayout(button_layout1)
           layout.addLayout(button_layout2)
           layout.addWidget(self.selected_color_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.color_button.colorChanged.connect(self.on_color_changed)
           self.dialog_button.colorChanged.connect(self.on_color_changed)
           self.circle_button.colorChanged.connect(self.on_color_changed)
           self.screen_button.colorChanged.connect(self.on_color_changed)
       
       def on_color_changed(self, color):
           """颜色变化处理"""
           if color.isValid():
               color_name = color.name().upper()
               self.selected_color_label.setText(f"已选择: {color_name}")
               self.selected_color_label.setStyleSheet(
                   f"background-color: {color_name}; color: white; "
                   f"padding: 5px; border-radius: 3px;"
               )
           else:
               self.selected_color_label.setText("未选择颜色")
               self.selected_color_label.setStyleSheet("")

高级用法
--------

自定义颜色选择器按钮
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.color_picker_button import ColorButton
   from qfluentwidgets import CardWidget, Label
   from qfluentwidgets.common.icon import FluentIcon as FIF
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QColor
   
   class CustomColorButtonWidget(CardWidget):
       """自定义颜色选择器按钮"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("自定义颜色选择器按钮")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 带图标的颜色选择器按钮
           self.icon_color_button = ColorButton(
               color=QColor("#FF6B6B"),
               title="主题颜色",
               icon=FIF.PALETTE,
               showPreview=True
           )
           
           # 不显示预览的颜色选择器按钮
           self.no_preview_button = ColorButton(
               color=QColor("#4ECDC4"),
               title="无预览",
               showPreview=False
           )
           
           # 仅显示颜色预览的按钮
           self.preview_only_button = ColorButton(
               color=QColor("#45B7D1"),
               title="",
               showPreview=True
           )
           
           # 显示选中的颜色信息
           self.color_info_label = Label("未选择颜色")
           self.color_info_label.setAlignment(Qt.AlignCenter)
           
           layout.addWidget(title_label)
           layout.addWidget(self.icon_color_button)
           layout.addWidget(self.no_preview_button)
           layout.addWidget(self.preview_only_button)
           layout.addWidget(self.color_info_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.icon_color_button.colorChanged.connect(self.on_color_changed)
           self.no_preview_button.colorChanged.connect(self.on_color_changed)
           self.preview_only_button.colorChanged.connect(self.on_color_changed)
       
       def on_color_changed(self, color):
           """颜色变化处理"""
           if color.isValid():
               # 显示详细的颜色信息
               rgb = f"RGB({color.red()}, {color.green()}, {color.blue()})"
               hsv = f"HSV({color.hue()}, {color.saturation()}, {color.value()})"
               hex_color = color.name().upper()
               
               info_text = f"{hex_color}\n{rgb}\n{hsv}"
               self.color_info_label.setText(info_text)
               self.color_info_label.setStyleSheet(
                   f"background-color: {hex_color}; color: white; "
                   f"padding: 10px; border-radius: 4px;"
               )
           else:
               self.color_info_label.setText("未选择颜色")
               self.color_info_label.setStyleSheet("")

颜色主题管理器
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.color_picker_button import ColorButton
   from qfluentwidgets import CardWidget, Label, ComboBox, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtGui import QColor
   
   class ColorThemeManager(CardWidget):
       """颜色主题管理器"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
           self.setup_themes()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("颜色主题管理器")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 主题选择
           theme_layout = QHBoxLayout()
           
           theme_label = Label("主题:")
           self.theme_combo = ComboBox()
           self.theme_combo.addItems([
               "默认主题",
               "暗色主题",
               "亮色主题",
               "自定义主题"
           ])
           
           theme_layout.addWidget(theme_label)
           theme_layout.addWidget(self.theme_combo)
           
           # 主色调选择器
           self.primary_color_button = ColorButton(
               color=QColor("#FF6B6B"),
               title="主色调",
               showPreview=True
           )
           
           # 辅助色调选择器
           self.secondary_color_button = ColorButton(
               color=QColor("#4ECDC4"),
               title="辅助色调",
               showPreview=True
           )
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           apply_theme_btn = PushButton("应用主题")
           save_theme_btn = PushButton("保存主题")
           
           apply_theme_btn.clicked.connect(self.apply_theme)
           save_theme_btn.clicked.connect(self.save_theme)
           
           button_layout.addWidget(apply_theme_btn)
           button_layout.addWidget(save_theme_btn)
           
           # 显示主题信息
           self.theme_info_label = Label("选择主题颜色")
           self.theme_info_label.setAlignment(Qt.AlignCenter)
           
           layout.addWidget(title_label)
           layout.addLayout(theme_layout)
           layout.addWidget(self.primary_color_button)
           layout.addWidget(self.secondary_color_button)
           layout.addLayout(button_layout)
           layout.addWidget(self.theme_info_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.theme_combo.currentTextChanged.connect(self.on_theme_changed)
           self.primary_color_button.colorChanged.connect(self.on_color_changed)
           self.secondary_color_button.colorChanged.connect(self.on_color_changed)
       
       def setup_themes(self):
           """设置主题"""
           self.themes = {
               "默认主题": {
                   "primary": QColor("#FF6B6B"),
                   "secondary": QColor("#4ECDC4")
               },
               "暗色主题": {
                   "primary": QColor("#2C3E50"),
                   "secondary": QColor("#34495E")
               },
               "亮色主题": {
                   "primary": QColor("#ECF0F1"),
                   "secondary": QColor("#BDC3C7")
               },
               "自定义主题": {
                   "primary": QColor("#3498DB"),
                   "secondary": QColor("#E74C3C")
               }
           }
           
           # 应用默认主题
           self.apply_theme()
       
       def on_theme_changed(self, theme_name):
           """主题变化处理"""
           self.apply_theme()
       
       def on_color_changed(self, color):
           """颜色变化处理"""
           theme_name = self.theme_combo.currentText()
           if theme_name == "自定义主题":
               self.update_theme_info()
       
       def apply_theme(self):
           """应用主题"""
           theme_name = self.theme_combo.currentText()
           theme_colors = self.themes.get(theme_name, {})
           
           primary_color = theme_colors.get("primary", QColor("#FF6B6B"))
           secondary_color = theme_colors.get("secondary", QColor("#4ECDC4"))
           
           self.primary_color_button.setColor(primary_color)
           self.secondary_color_button.setColor(secondary_color)
           
           self.update_theme_info()
       
       def update_theme_info(self):
           """更新主题信息"""
           primary_color = self.primary_color_button.color()
           secondary_color = self.secondary_color_button.color()
           
           if primary_color.isValid() and secondary_color.isValid():
               theme_name = self.theme_combo.currentText()
               primary_hex = primary_color.name().upper()
               secondary_hex = secondary_color.name().upper()
               
               info_text = f"{theme_name}\n主色: {primary_hex}\n辅助色: {secondary_hex}"
               self.theme_info_label.setText(info_text)
               self.theme_info_label.setStyleSheet(
                   f"background: linear-gradient(45deg, {primary_hex} 50%, {secondary_hex} 50%); "
                   f"color: white; padding: 10px; border-radius: 4px;"
               )
       
       def save_theme(self):
           """保存当前主题"""
           theme_name = self.theme_combo.currentText()
           primary_color = self.primary_color_button.color()
           secondary_color = self.secondary_color_button.color()
           
           if theme_name == "自定义主题":
               self.themes[theme_name] = {
                   "primary": primary_color,
                   "secondary": secondary_color
               }
               print(f"已保存自定义主题")
           else:
               print(f"已更新主题: {theme_name}")

最佳实践
--------

1. **按钮样式** - 根据使用场景选择合适的按钮样式
2. **预览显示** - 合理使用颜色预览功能
3. **图标使用** - 使用合适的图标增强用户体验
4. **自定义颜色** - 提供自定义颜色的管理功能
5. **响应式设计** - 确保按钮在不同尺寸下的显示效果

注意事项
--------

- 弹出式界面需要正确处理父窗口关系
- 屏幕取色功能需要正确的权限支持
- 自定义颜色列表需要合理管理
- 大量的颜色变化事件可能影响性能
- 按钮的文本和图标需要合理布局

相关模块
--------

- :doc:`components.dialog_box.color_dialog` - 颜色对话框
- :doc:`components.dialog_box.color_palette` - 颜色调色板
- :doc:`components.dialog_box.circle_color_picker` - 圆形颜色选择器
- :doc:`components.dialog_box.screen_color_picker` - 屏幕取色器
