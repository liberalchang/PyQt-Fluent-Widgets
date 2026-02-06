Custom Color Setting Card 自定义颜色设置卡片模块
===================================================

Custom Color Setting Card 模块提供自定义颜色设置卡片功能，支持默认颜色和自定义颜色选择。
该模块提供现代化的颜色设置界面，支持颜色对话框和配置管理。

主要功能
--------

- **颜色选择** - 提供默认颜色和自定义颜色选择
- **配置集成** - 支持配置项的自动保存和加载
- **颜色对话框** - 集成颜色选择对话框
- **单选切换** - 支持默认颜色和自定义颜色的切换
- **透明度支持** - 可选的透明度通道支持

核心组件
--------

CustomColorSettingCard
~~~~~~~~~~~~~~~~~~~~

自定义颜色设置卡片，提供完整的颜色设置功能。

.. code-block:: python

   from qfluentwidgets.components.settings import CustomColorSettingCard
   from qfluentwidgets.common.config import ColorConfigItem
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建颜色配置项
   color_config = ColorConfigItem("App", "ThemeColor", "#0078d4")
   
   # 创建自定义颜色设置卡片
   color_card = CustomColorSettingCard(
       configItem=color_config,
       icon=FIF.PALETTE,
       title="主题颜色",
       content="选择应用程序主题颜色",
       enableAlpha=False
   )
   
   # 连接颜色变化信号
   color_card.colorChanged.connect(self.on_color_changed)

**主要信号：**
- ``colorChanged`` - 颜色变化信号

**主要方法：**
- ``setValue()`` - 设置颜色值
- ``value()`` - 获取当前颜色值

实际应用
--------

基本自定义颜色设置
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.settings import CustomColorSettingCard
   from qfluentwidgets.common.config import ColorConfigItem
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from PySide6.QtGui import QColor
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class BasicCustomColorWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("自定义颜色设置示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建颜色配置项
           self.theme_color_config = ColorConfigItem("App", "ThemeColor", "#0078d4")
           self.accent_color_config = ColorConfigItem("App", "AccentColor", "#ff6b6b")
           
           # 创建自定义颜色设置卡片
           self.theme_color_card = CustomColorSettingCard(
               configItem=self.theme_color_config,
               icon=FIF.PALETTE,
               title="主题颜色",
               content="选择应用程序主题颜色"
           )
           
           self.accent_color_card = CustomColorSettingCard(
               configItem=self.accent_color_config,
               icon=FIF.BRUSH,
               title="强调色",
               content="选择应用程序强调色"
           )
           
           # 显示当前选择
           self.current_label = Label("当前主题颜色: #0078d4")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.theme_color_card)
           layout.addWidget(self.accent_color_card)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.theme_color_card.colorChanged.connect(self.on_theme_color_changed)
           self.accent_color_card.colorChanged.connect(self.on_accent_color_changed)
       
       def on_theme_color_changed(self, color):
           """主题颜色变化处理"""
           self.current_label.setText(f"当前主题颜色: {color.name()}")
       
       def on_accent_color_changed(self, color):
           """强调色变化处理"""
           self.current_label.setText(f"当前强调色: {color.name()}")

高级自定义颜色设置
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.settings import CustomColorSettingCard
   from qfluentwidgets.common.config import ColorConfigItem
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   from PySide6.QtGui import QColor
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class AdvancedCustomColorWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("高级自定义颜色设置")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.reset_btn = PushButton("重置颜色")
           self.preview_btn = PushButton("预览效果")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.reset_btn)
           header_layout.addWidget(self.preview_btn)
           
           # 创建颜色配置项
           self.create_color_configs()
           
           # 创建自定义颜色设置卡片
           self.create_color_cards()
           
           # 显示当前选择
           self.current_label = Label("当前颜色配置: 默认")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.primary_color_card)
           layout.addWidget(self.secondary_color_card)
           layout.addWidget(self.background_color_card)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def create_color_configs(self):
           """创建颜色配置项"""
           self.primary_color_config = ColorConfigItem("App", "PrimaryColor", "#0078d4")
           self.secondary_color_config = ColorConfigItem("App", "SecondaryColor", "#6c757d")
           self.background_color_config = ColorConfigItem("App", "BackgroundColor", "#ffffff")
       
       def create_color_cards(self):
           """创建颜色卡片"""
           self.primary_color_card = CustomColorSettingCard(
               configItem=self.primary_color_config,
               icon=FIF.PALETTE,
               title="主要颜色",
               content="应用程序的主要颜色"
           )
           
           self.secondary_color_card = CustomColorSettingCard(
               configItem=self.secondary_color_config,
               icon=FIF.BRUSH,
               title="次要颜色",
               content="应用程序的次要颜色"
           )
           
           self.background_color_card = CustomColorSettingCard(
               configItem=self.background_color_config,
               icon=FIF.BACKGROUND,
               title="背景颜色",
               content="应用程序的背景颜色"
           )
       
       def setup_connections(self):
           """设置连接"""
           self.reset_btn.clicked.connect(self.reset_colors)
           self.preview_btn.clicked.connect(self.preview_colors)
           
           self.primary_color_card.colorChanged.connect(self.on_color_changed)
           self.secondary_color_card.colorChanged.connect(self.on_color_changed)
           self.background_color_card.colorChanged.connect(self.on_color_changed)
       
       def reset_colors(self):
           """重置颜色"""
           self.primary_color_config.value = "#0078d4"
           self.secondary_color_config.value = "#6c757d"
           self.background_color_config.value = "#ffffff"
           
           self.current_label.setText("颜色配置已重置为默认值")
       
       def preview_colors(self):
           """预览颜色效果"""
           primary_color = self.primary_color_config.value
           secondary_color = self.secondary_color_config.value
           background_color = self.background_color_config.value
           
           self.current_label.setText(
               f"预览 - 主要: {primary_color.name()}, "
               f"次要: {secondary_color.name()}, "
               f"背景: {background_color.name()}"
           )
       
       def on_color_changed(self, color):
           """颜色变化处理"""
           self.current_label.setText(f"颜色已更新: {color.name()}")

透明度支持的自定义颜色
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.settings import CustomColorSettingCard
   from qfluentwidgets.common.config import ColorConfigItem
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from PySide6.QtGui import QColor
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class AlphaCustomColorWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("透明度支持的自定义颜色")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建颜色配置项
           self.overlay_color_config = ColorConfigItem("App", "OverlayColor", "#00000080")
           
           # 创建支持透明度的自定义颜色设置卡片
           self.overlay_color_card = CustomColorSettingCard(
               configItem=self.overlay_color_config,
               icon=FIF.TRANSPARENCY,
               title="覆盖层颜色",
               content="选择覆盖层颜色（支持透明度）",
               enableAlpha=True
           )
           
           # 显示当前选择
           self.current_label = Label("当前覆盖层颜色: #00000080")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.overlay_color_card)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.overlay_color_card.colorChanged.connect(self.on_overlay_color_changed)
       
       def on_overlay_color_changed(self, color):
           """覆盖层颜色变化处理"""
           alpha = color.alpha()
           rgba = f"rgba({color.red()}, {color.green()}, {color.blue()}, {alpha/255:.2f})"
           self.current_label.setText(f"当前覆盖层颜色: {rgba}")

最佳实践
--------

1. **配置管理** - 正确使用ColorConfigItem进行配置管理
2. **默认颜色** - 为颜色设置合理的默认值
3. **透明度处理** - 根据需要启用透明度支持
4. **颜色验证** - 验证颜色值的有效性
5. **用户体验** - 提供颜色预览和重置功能

注意事项
--------

- 自定义颜色设置卡片会自动处理配置的保存和加载
- 颜色对话框支持多种颜色格式
- 透明度支持需要显式启用
- 默认颜色和自定义颜色通过单选按钮切换
- 颜色变化会自动触发配置更新
- 需要正确初始化ColorConfigItem

相关模块
--------

- :doc:`components.settings.setting_card` - 设置卡片
- :doc:`components.settings.expand_setting_card` - 展开设置卡片
- :doc:`components.dialog_box.color_dialog` - 颜色对话框
- :doc:`common.config` - 配置管理
