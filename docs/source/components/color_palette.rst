Color Palette 颜色调色板模块
===============================

Color Palette 模块提供完整的颜色调色板功能，支持屏幕取色、主题颜色和自定义颜色管理。
该模块提供专业的颜色选择界面，包含多种颜色选择方式和颜色管理功能。

主要功能
--------

- **屏幕取色** - 支持从屏幕任意位置取色
- **主题颜色** - 提供系统主题相关的颜色选择
- **自定义颜色** - 支持用户自定义颜色管理
- **下拉调色板** - 提供下拉式的颜色选择界面
- **颜色预览** - 提供实时的颜色预览功能

核心组件
--------

ColorPalette
~~~~~~~~~~~~

颜色调色板控件，提供完整的颜色选择功能。

.. code-block:: python

   from qfluentwidgets.components.dialog_box.color_palette import ColorPalette
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QColor
   
   # 创建颜色调色板
   color_palette = ColorPalette()
   
   # 设置自定义颜色
   custom_colors = [
       QColor("#FF6B6B"),
       QColor("#4ECDC4"),
       QColor("#45B7D1"),
   ]
   color_palette.setCustomColors(custom_colors)
   
   # 连接信号
   color_palette.colorSelected.connect(on_color_selected)

**主要信号：**
- ``colorSelected`` - 颜色选择信号
- ``customColorsChanged`` - 自定义颜色变化信号

**主要方法：**
- ``setCustomColors()`` - 设置自定义颜色
- ``setAutoColor()`` - 设置自动颜色
- ``addCustomColor()`` - 添加自定义颜色

DropDownColorPalette
~~~~~~~~~~~~~~~~~~~

下拉式颜色调色板，提供紧凑的颜色选择界面。

.. code-block:: python

   from qfluentwidgets.components.dialog_box.color_palette import DropDownColorPalette
   from qfluentwidgets import CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QColor
   
   # 创建下拉颜色调色板
   dropdown_palette = DropDownColorPalette()
   
   # 连接信号
   dropdown_palette.colorSelected.connect(on_color_selected)

ColorSwatch
~~~~~~~~~~~

颜色样本控件，单个颜色的显示组件。

.. code-block:: python

   from qfluentwidgets.components.dialog_box.color_palette import ColorSwatch
   from PySide6.QtGui import QColor
   
   # 创建颜色样本
   color_swatch = ColorSwatch(QColor("#FF6B6B"))
   
   # 连接信号
   color_swatch.colorChanged.connect(on_color_changed)

实际应用
--------

基本颜色调色板
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.color_palette import ColorPalette
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtGui import QColor
   
   class BasicColorPaletteWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("颜色调色板")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 创建颜色调色板
           self.color_palette = ColorPalette()
           
           # 设置自定义颜色
           custom_colors = [
               QColor("#FF6B6B"),  # 红色
               QColor("#4ECDC4"),  # 青色
               QColor("#45B7D1"),  # 蓝色
               QColor("#96CEB4"),  # 绿色
               QColor("#FFEAA7"),  # 黄色
               QColor("#DDA0DD"),  # 紫色
           ]
           self.color_palette.setCustomColors(custom_colors)
           
           # 显示选中的颜色
           self.selected_color_label = Label("未选择颜色")
           self.selected_color_label.setAlignment(Qt.AlignCenter)
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           add_color_btn = PushButton("添加颜色")
           clear_btn = PushButton("清空")
           
           add_color_btn.clicked.connect(self.add_random_color)
           clear_btn.clicked.connect(self.clear_colors)
           
           button_layout.addWidget(add_color_btn)
           button_layout.addWidget(clear_btn)
           
           layout.addWidget(title_label)
           layout.addWidget(self.color_palette)
           layout.addWidget(self.selected_color_label)
           layout.addLayout(button_layout)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.color_palette.colorSelected.connect(self.on_color_selected)
           self.color_palette.customColorsChanged.connect(self.on_custom_colors_changed)
       
       def on_color_selected(self, color):
           """颜色选择处理"""
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
       
       def on_custom_colors_changed(self, colors):
           """自定义颜色变化处理"""
           print(f"自定义颜色数量: {len(colors)}")
       
       def add_random_color(self):
           """添加随机颜色"""
           import random
           r = random.randint(0, 255)
           g = random.randint(0, 255)
           b = random.randint(0, 255)
           random_color = QColor(r, g, b)
           self.color_palette.addCustomColor(random_color)
       
       def clear_colors(self):
           """清空自定义颜色"""
           self.color_palette.setCustomColors([])

下拉式颜色选择器
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.color_palette import DropDownColorPalette
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QColor
   
   class DropDownColorPaletteWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("下拉式颜色选择器")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 创建下拉颜色调色板
           self.dropdown_palette = DropDownColorPalette()
           
           # 显示选中的颜色
           self.selected_color_label = Label("未选择颜色")
           self.selected_color_label.setAlignment(Qt.AlignCenter)
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           show_palette_btn = PushButton("显示调色板")
           reset_btn = PushButton("重置")
           
           show_palette_btn.clicked.connect(self.show_palette)
           reset_btn.clicked.connect(self.reset_color)
           
           button_layout.addWidget(show_palette_btn)
           button_layout.addWidget(reset_btn)
           
           layout.addWidget(title_label)
           layout.addWidget(self.dropdown_palette)
           layout.addWidget(self.selected_color_label)
           layout.addLayout(button_layout)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.dropdown_palette.colorSelected.connect(self.on_color_selected)
       
       def on_color_selected(self, color):
           """颜色选择处理"""
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
       
       def show_palette(self):
           """显示调色板"""
           # 点击下拉按钮会自动显示调色板
           self.dropdown_palette.click()
       
       def reset_color(self):
           """重置颜色"""
           default_color = QColor("#FF6B6B")
           # 这里需要设置下拉调色板的颜色
           # 具体实现取决于DropDownColorPalette的API

高级用法
--------

自定义颜色调色板
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.color_palette import ColorPalette, ColorSwatch
   from qfluentwidgets import CardWidget, Label, LineEdit
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout
   from PySide6.QtGui import QColor
   
   class CustomColorPaletteWidget(CardWidget):
       """自定义颜色调色板"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
           self.setup_color_swatchs()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("自定义颜色调色板")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 颜色输入区域
           input_layout = QHBoxLayout()
           
           color_input_label = Label("颜色值:")
           self.color_input = LineEdit()
           self.color_input.setPlaceholderText("#FF0000")
           
           add_btn = PushButton("添加")
           add_btn.clicked.connect(self.add_color_from_input)
           
           input_layout.addWidget(color_input_label)
           input_layout.addWidget(self.color_input)
           input_layout.addWidget(add_btn)
           
           # 颜色样本网格
           self.swatch_layout = QGridLayout()
           
           # 创建颜色调色板
           self.color_palette = ColorPalette()
           
           # 显示当前颜色
           self.current_color_label = Label("当前颜色: 无")
           self.current_color_label.setAlignment(Qt.AlignCenter)
           
           layout.addWidget(title_label)
           layout.addLayout(input_layout)
           layout.addLayout(self.swatch_layout)
           layout.addWidget(self.color_palette)
           layout.addWidget(self.current_color_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.color_palette.colorSelected.connect(self.on_color_selected)
       
       def setup_color_swatchs(self):
           """设置颜色样本"""
           # 创建预设颜色样本
           preset_colors = [
               "#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4",
               "#FFEAA7", "#DDA0DD", "#FF8E53", "#C44569",
               "#F8B500", "#FF6348", "#00D2D3", "#3498DB"
           ]
           
           row, col = 0, 0
           for color_hex in preset_colors:
               color = QColor(color_hex)
               swatch = ColorSwatch(color)
               swatch.colorChanged.connect(self.on_swatch_color_changed)
               
               self.swatch_layout.addWidget(swatch, row, col)
               
               col += 1
               if col >= 6:
                   col = 0
                   row += 1
       
       def on_color_selected(self, color):
           """颜色选择处理"""
           if color.isValid():
               color_name = color.name().upper()
               self.current_color_label.setText(f"当前颜色: {color_name}")
               self.current_color_label.setStyleSheet(
                   f"background-color: {color_name}; color: white; "
                   f"padding: 5px; border-radius: 3px;"
               )
       
       def on_swatch_color_changed(self, color):
           """颜色样本变化处理"""
           self.on_color_selected(color)
           self.color_palette.addCustomColor(color)
       
       def add_color_from_input(self):
           """从输入框添加颜色"""
           color_text = self.color_input.text().strip()
           if color_text:
               try:
                   color = QColor(color_text)
                   if color.isValid():
                       self.color_palette.addCustomColor(color)
                       self.color_input.clear()
                       self.on_color_selected(color)
                   else:
                       self.color_input.setStyleSheet("border: 1px solid red;")
               except:
                   self.color_input.setStyleSheet("border: 1px solid red;")

颜色主题管理器
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.color_palette import ColorPalette
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
               "彩色主题",
               "商务主题"
           ])
           
           theme_layout.addWidget(theme_label)
           theme_layout.addWidget(self.theme_combo)
           
           # 创建颜色调色板
           self.color_palette = ColorPalette()
           
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
           layout.addWidget(self.color_palette)
           layout.addLayout(button_layout)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.theme_combo.currentTextChanged.connect(self.on_theme_changed)
           self.color_palette.colorSelected.connect(self.on_color_selected)
       
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
       
       def on_color_selected(self, color):
           """颜色选择处理"""
           print(f"选择了主题颜色: {color.name().upper()}")
       
       def apply_theme(self):
           """应用主题"""
           theme_name = self.theme_combo.currentText()
           colors = self.themes.get(theme_name, [])
           self.color_palette.setCustomColors(colors)
       
       def save_theme(self):
           """保存当前主题"""
           current_colors = self.color_palette.customColors
           theme_name = self.theme_combo.currentText()
           
           # 更新主题
           self.themes[theme_name] = current_colors
           print(f"已保存主题: {theme_name}")

最佳实践
--------

1. **颜色管理** - 合理管理自定义颜色列表
2. **用户体验** - 提供直观的颜色选择界面
3. **主题一致性** - 保持与应用整体主题的一致性
4. **性能优化** - 避免过多的颜色项影响性能
5. **可访问性** - 确保颜色选择的可访问性

注意事项
--------

- 屏幕取色功能需要正确的权限支持
- 自定义颜色列表需要合理管理，避免重复
- 下拉调色板需要正确处理弹出位置
- 大量颜色可能影响界面布局和性能
- 颜色选择事件可能频繁触发，需要防抖处理

相关模块
--------

- :doc:`components.dialog_box.color_dialog` - 颜色对话框
- :doc:`components.dialog_box.circle_color_picker` - 圆形颜色选择器
- :doc:`components.dialog_box.screen_color_picker` - 屏幕取色器
- :doc:`common.color` - 颜色管理
