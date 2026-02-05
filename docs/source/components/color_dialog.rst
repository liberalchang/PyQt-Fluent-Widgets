Color Dialog 颜色对话框模块
===============================

Color Dialog 模块提供完整的颜色选择对话框功能，支持HSV颜色空间和透明度调整。
该模块提供专业的颜色选择界面，包含色相面板、亮度滑块、颜色卡片和数值输入等功能。

主要功能
--------

- **HSV颜色空间** - 支持色相、饱和度、亮度的调整
- **透明度支持** - 支持Alpha通道的调整
- **多种输入** - 支持HEX、RGB、HSL等多种颜色格式
- **实时预览** - 提供实时的颜色预览功能
- **专业界面** - 提供专业级的颜色选择界面

核心组件
--------

ColorDialog
~~~~~~~~~~~

颜色选择对话框，提供完整的颜色选择功能。

.. code-block:: python

   from qfluentwidgets.components.dialog_box.color_dialog import ColorDialog
   from PySide6.QtWidgets import QPushButton
   from PySide6.QtGui import QColor
   
   # 创建颜色选择对话框
   color_dialog = ColorDialog()
   
   # 设置初始颜色
   color_dialog.setColor(QColor("#FF6B6B"))
   
   # 连接信号
   color_dialog.colorChanged.connect(on_color_changed)
   
   # 显示对话框
   if color_dialog.exec():
       selected_color = color_dialog.color

**主要信号：**
- ``colorChanged`` - 颜色变化信号

**主要属性：**
- ``color`` - 当前选中的颜色

ColorPickerWidget
~~~~~~~~~~~~~~~~~

颜色选择器控件，提供颜色选择的核心功能。

.. code-block:: python

   from qfluentwidgets.components.dialog_box.color_dialog import ColorPickerWidget
   from qfluentwidgets import CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QColor
   
   # 创建颜色选择器
   color_picker = ColorPickerWidget()
   
   # 设置颜色
   color_picker.setColor(QColor("#4ECDC4"))
   
   # 连接信号
   color_picker.colorChanged.connect(on_color_changed)

HuePanel
~~~~~~~~~

色相面板，提供色相和饱和度的可视化选择。

.. code-block:: python

   from qfluentwidgets.components.dialog_box.color_dialog import HuePanel
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QColor
   
   # 创建色相面板
   hue_panel = HuePanel(QColor("#FF6B6B"))
   
   # 连接信号
   hue_panel.colorChanged.connect(on_hue_changed)

BrightnessSlider
~~~~~~~~~~~~~~~~

亮度滑块，用于调整颜色的亮度。

.. code-block:: python

   from qfluentwidgets.components.dialog_box.color_dialog import BrightnessSlider
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QColor
   
   # 创建亮度滑块
   brightness_slider = BrightnessSlider()
   
   # 设置颜色
   brightness_slider.setColor(QColor("#FF6B6B"))
   
   # 连接信号
   brightness_slider.colorChanged.connect(on_brightness_changed)

实际应用
--------

基本颜色选择对话框
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.color_dialog import ColorDialog
   from qfluentwidgets import PushButton, CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtGui import QColor
   
   class BasicColorDialogWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("颜色选择对话框")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 创建触发按钮
           self.open_dialog_btn = PushButton("选择颜色")
           
           # 显示选中的颜色
           self.color_display = Label("未选择颜色")
           self.color_display.setAlignment(Qt.AlignCenter)
           self.color_display.setFixedHeight(50)
           
           layout.addWidget(title_label)
           layout.addWidget(self.open_dialog_btn)
           layout.addWidget(self.color_display)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.open_dialog_btn.clicked.connect(self.open_color_dialog)
       
       def open_color_dialog(self):
           """打开颜色选择对话框"""
           color_dialog = ColorDialog(self)
           
           # 设置初始颜色
           initial_color = QColor("#FF6B6B")
           color_dialog.setColor(initial_color)
           
           # 连接信号
           color_dialog.colorChanged.connect(self.on_color_changed)
           
           # 显示对话框
           if color_dialog.exec():
               selected_color = color_dialog.color
               self.update_color_display(selected_color)
       
       def on_color_changed(self, color):
           """颜色变化处理"""
           if color.isValid():
               self.update_color_display(color)
       
       def update_color_display(self, color):
           """更新颜色显示"""
           if color.isValid():
               color_name = color.name().upper()
               self.color_display.setText(f"已选择: {color_name}")
               self.color_display.setStyleSheet(
                   f"background-color: {color_name}; color: white; "
                   f"border: 1px solid #ccc; border-radius: 4px;"
               )
           else:
               self.color_display.setText("未选择颜色")
               self.color_display.setStyleSheet("")

嵌入式颜色选择器
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.color_dialog import ColorPickerWidget
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtGui import QColor
   
   class EmbeddedColorPickerWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("嵌入式颜色选择器")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 创建颜色选择器
           self.color_picker = ColorPickerWidget()
           self.color_picker.setColor(QColor("#4ECDC4"))
           
           # 显示颜色信息
           self.color_info_label = Label("未选择颜色")
           self.color_info_label.setAlignment(Qt.AlignCenter)
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           reset_btn = PushButton("重置")
           random_btn = PushButton("随机颜色")
           
           reset_btn.clicked.connect(self.reset_color)
           random_btn.clicked.connect(self.random_color)
           
           button_layout.addWidget(reset_btn)
           button_layout.addWidget(random_btn)
           
           layout.addWidget(title_label)
           layout.addWidget(self.color_picker)
           layout.addWidget(self.color_info_label)
           layout.addLayout(button_layout)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.color_picker.colorChanged.connect(self.on_color_changed)
       
       def on_color_changed(self, color):
           """颜色变化处理"""
           if color.isValid():
               # 显示颜色信息
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
       
       def reset_color(self):
           """重置颜色"""
           default_color = QColor("#FF6B6B")
           self.color_picker.setColor(default_color)
       
       def random_color(self):
           """随机颜色"""
           import random
           r = random.randint(0, 255)
           g = random.randint(0, 255)
           b = random.randint(0, 255)
           random_color = QColor(r, g, b)
           self.color_picker.setColor(random_color)

高级用法
--------

自定义颜色选择器
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.color_dialog import ColorPickerWidget, HuePanel, BrightnessSlider
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtGui import QColor
   
   class CustomColorPickerWidget(CardWidget):
       """自定义颜色选择器"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("自定义颜色选择器")
           title_label.setAlignment(Qt.AlignCenter)
           
           # 色相面板和亮度滑块布局
           hsv_layout = QHBoxLayout()
           
           # 色相面板
           self.hue_panel = HuePanel(QColor("#FF6B6B"))
           
           # 亮度滑块
           self.brightness_slider = BrightnessSlider()
           self.brightness_slider.setFixedWidth(30)
           self.brightness_slider.setColor(QColor("#FF6B6B"))
           
           hsv_layout.addWidget(self.hue_panel)
           hsv_layout.addWidget(self.brightness_slider)
           
           # 显示颜色信息
           self.color_info_label = Label("未选择颜色")
           self.color_info_label.setAlignment(Qt.AlignCenter)
           
           layout.addWidget(title_label)
           layout.addLayout(hsv_layout)
           layout.addWidget(self.color_info_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.hue_panel.colorChanged.connect(self.on_hue_changed)
           self.brightness_slider.colorChanged.connect(self.on_brightness_changed)
       
       def on_hue_changed(self, color):
           """色相变化处理"""
           self.brightness_slider.setColor(color)
           self.update_color_info(color)
       
       def on_brightness_changed(self, color):
           """亮度变化处理"""
           self.hue_panel.setColor(color)
           self.update_color_info(color)
       
       def update_color_info(self, color):
           """更新颜色信息"""
           if color.isValid():
               hex_color = color.name().upper()
               hsv = f"HSV({color.hue()}, {color.saturation()}, {color.value()})"
               
               self.color_info_label.setText(f"{hex_color}\n{hsv}")
               self.color_info_label.setStyleSheet(
                   f"background-color: {hex_color}; color: white; "
                   f"padding: 10px; border-radius: 4px;"
               )

颜色主题管理器
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.dialog_box.color_dialog import ColorDialog
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
           
           # 颜色显示区域
           self.color_display = Label("选择主题颜色")
           self.color_display.setAlignment(Qt.AlignCenter)
           self.color_display.setFixedHeight(60)
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           select_color_btn = PushButton("选择颜色")
           apply_theme_btn = PushButton("应用主题")
           
           select_color_btn.clicked.connect(self.select_theme_color)
           apply_theme_btn.clicked.connect(self.apply_theme)
           
           button_layout.addWidget(select_color_btn)
           button_layout.addWidget(apply_theme_btn)
           
           layout.addWidget(title_label)
           layout.addLayout(theme_layout)
           layout.addWidget(self.color_display)
           layout.addLayout(button_layout)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.theme_combo.currentTextChanged.connect(self.on_theme_changed)
       
       def setup_themes(self):
           """设置主题"""
           self.themes = {
               "默认主题": QColor("#FF6B6B"),
               "暗色主题": QColor("#2C3E50"),
               "亮色主题": QColor("#ECF0F1"),
               "自定义主题": QColor("#3498DB")
           }
           
           self.current_theme_color = self.themes["默认主题"]
           self.update_color_display()
       
       def on_theme_changed(self, theme_name):
           """主题变化处理"""
           theme_color = self.themes.get(theme_name, QColor("#FF6B6B"))
           self.current_theme_color = theme_color
           self.update_color_display()
       
       def select_theme_color(self):
           """选择主题颜色"""
           color_dialog = ColorDialog(self)
           color_dialog.setColor(self.current_theme_color)
           
           if color_dialog.exec():
               new_color = color_dialog.color
               theme_name = self.theme_combo.currentText()
               
               if theme_name == "自定义主题":
                   self.themes[theme_name] = new_color
                   self.current_theme_color = new_color
                   self.update_color_display()
       
       def apply_theme(self):
           """应用主题"""
           theme_name = self.theme_combo.currentText()
           theme_color = self.current_theme_color
           
           print(f"应用主题: {theme_name}")
           print(f"主题颜色: {theme_color.name().upper()}")
           
           # 这里可以添加实际的主题应用逻辑
           # 例如：更新应用样式、设置全局颜色等
       
       def update_color_display(self):
           """更新颜色显示"""
           if self.current_theme_color.isValid():
               color_name = self.current_theme_color.name().upper()
               theme_name = self.theme_combo.currentText()
               
               self.color_display.setText(f"{theme_name}: {color_name}")
               self.color_display.setStyleSheet(
                   f"background-color: {color_name}; color: white; "
                   f"border: 1px solid #ccc; border-radius: 4px;"
               )

最佳实践
--------

1. **颜色空间** - 理解HSV颜色空间的工作原理
2. **用户体验** - 提供直观的颜色选择界面
3. **实时预览** - 提供实时的颜色预览功能
4. **格式支持** - 支持多种颜色格式的输入和显示
5. **性能优化** - 避免频繁的颜色更新操作

注意事项
--------

- HSV颜色空间与RGB颜色空间的转换需要正确处理
- 透明度支持需要在应用层面正确处理
- 颜色对话框的显示需要正确管理父窗口关系
- 大量的颜色变化事件可能影响性能
- 自定义颜色选择器需要正确处理组件间的交互

相关模块
--------

- :doc:`components.dialog_box.circle_color_picker` - 圆形颜色选择器
- :doc:`components.dialog_box.color_palette` - 颜色调色板
- :doc:`common.color` - 颜色管理
