Setting Card 设置卡片模块
=============================

Setting Card 模块提供基础设置卡片功能，支持多种设置控件类型。
该模块提供现代化的设置界面组件，包括开关、滑块、按钮、颜色选择等。

主要功能
--------

- **基础卡片** - 提供统一的设置卡片布局
- **开关设置** - 支持布尔值开关控制
- **范围设置** - 支持数值范围滑块控制
- **按钮设置** - 支持点击操作按钮
- **颜色设置** - 支持颜色选择器
- **下拉框** - 支持选项下拉选择
- **超链接** - 支持外部链接跳转

核心组件
--------

SettingCard
~~~~~~~~~~

基础设置卡片，提供统一的设置卡片布局。

.. code-block:: python

   from qfluentwidgets.components.settings import SettingCard
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建基础设置卡片
   setting_card = SettingCard(
       icon=FIF.SETTING,
       title="设置标题",
       content="设置说明"
   )

SwitchSettingCard
~~~~~~~~~~~~~~~~

开关设置卡片，提供布尔值开关功能。

.. code-block:: python

   from qfluentwidgets.components.settings import SwitchSettingCard
   from qfluentwidgets.common.config import ConfigItem
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建配置项
   switch_config = ConfigItem("App", "EnableNotification", True)
   
   # 创建开关设置卡片
   switch_card = SwitchSettingCard(
       icon=FIF.BELL,
       title="通知设置",
       content="启用系统通知",
       configItem=switch_config
   )
   
   # 连接开关变化信号
   switch_card.checkedChanged.connect(self.on_switch_changed)

RangeSettingCard
~~~~~~~~~~~~~~~~

范围设置卡片，提供数值范围滑块功能。

.. code-block:: python

   from qfluentwidgets.components.settings import RangeSettingCard
   from qfluentwidgets.common.config import RangeConfigItem
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建范围配置项
   range_config = RangeConfigItem("App", "Volume", 50, 0, 100)
   
   # 创建范围设置卡片
   range_card = RangeSettingCard(
       icon=FIF.VOLUME,
       title="音量设置",
       content="调整系统音量",
       configItem=range_config
   )
   
   # 连接数值变化信号
   range_card.valueChanged.connect(self.on_value_changed)

PushSettingCard
~~~~~~~~~~~~~~~~

按钮设置卡片，提供点击操作功能。

.. code-block:: python

   from qfluentwidgets.components.settings import PushSettingCard
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建按钮设置卡片
   push_card = PushSettingCard(
       icon=FIF.DOWNLOAD,
       title="下载更新",
       content="检查并下载最新版本"
   )
   
   # 连接点击信号
   push_card.clicked.connect(self.on_button_clicked)

ColorSettingCard
~~~~~~~~~~~~~~~~

颜色设置卡片，提供颜色选择功能。

.. code-block:: python

   from qfluentwidgets.components.settings import ColorSettingCard
   from qfluentwidgets.common.config import ColorConfigItem
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建颜色配置项
   color_config = ColorConfigItem("App", "ThemeColor", "#0078d4")
   
   # 创建颜色设置卡片
   color_card = ColorSettingCard(
       icon=FIF.PALETTE,
       title="主题颜色",
       content="选择应用程序主题颜色",
       configItem=color_config
   )
   
   # 连接颜色变化信号
   color_card.colorChanged.connect(self.on_color_changed)

实际应用
--------

综合设置界面
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.settings import (
       SettingCard, SwitchSettingCard, RangeSettingCard,
       PushSettingCard, ColorSettingCard, ComboBoxSettingCard
   )
   from qfluentwidgets.common.config import ConfigItem, RangeConfigItem, ColorConfigItem
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout, QScrollArea
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class ComprehensiveSettingsWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("综合设置界面")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建滚动区域
           scroll_area = QScrollArea()
           scroll_widget = QWidget()
           scroll_layout = QVBoxLayout(scroll_widget)
           
           # 创建配置项
           self.create_configs()
           
           # 创建设置卡片
           self.create_setting_cards(scroll_layout)
           
           # 显示当前状态
           self.status_label = Label("状态: 就绪")
           self.status_label.setStyleSheet("padding: 10px;")
           
           scroll_area.setWidget(scroll_widget)
           scroll_area.setWidgetResizable(True)
           scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
           
           layout.addWidget(title_label)
           layout.addWidget(scroll_area)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def create_configs(self):
           """创建配置项"""
           # 通知配置
           self.notification_config = ConfigItem("App", "EnableNotification", True)
           
           # 音量配置
           self.volume_config = RangeConfigItem("App", "Volume", 50, 0, 100)
           
           # 主题颜色配置
           self.theme_color_config = ColorConfigItem("App", "ThemeColor", "#0078d4")
       
       def create_setting_cards(self, layout):
           """创建设置卡片"""
           # 通知设置
           notification_card = SwitchSettingCard(
               FIF.BELL, "通知设置", "启用系统通知", self.notification_config
           )
           
           # 音量设置
           volume_card = RangeSettingCard(
               FIF.VOLUME, "音量设置", "调整系统音量", self.volume_config
           )
           
           # 主题颜色设置
           color_card = ColorSettingCard(
               FIF.PALETTE, "主题颜色", "选择应用程序主题颜色", self.theme_color_config
           )
           
           # 操作按钮
           action_card = PushSettingCard(
               FIF.SAVE, "保存设置", "保存所有配置更改"
           )
           
           layout.addWidget(notification_card)
           layout.addWidget(volume_card)
           layout.addWidget(color_card)
           layout.addWidget(action_card)
           
           # 添加弹性空间
           layout.addStretch()
       
       def setup_connections(self):
           """设置连接"""
           # 这里可以连接各种信号
           pass

高级设置界面
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.settings import (
       SettingCard, SwitchSettingCard, RangeSettingCard,
       PrimaryPushSettingCard, HyperlinkCard, ComboBoxSettingCard
   )
   from qfluentwidgets.common.config import ConfigItem, RangeConfigItem, OptionsConfigItem
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QScrollArea
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class AdvancedSettingsWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("高级设置界面")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.reset_btn = PushButton("重置设置")
           self.export_btn = PushButton("导出配置")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.reset_btn)
           header_layout.addWidget(self.export_btn)
           
           # 创建滚动区域
           scroll_area = QScrollArea()
           scroll_widget = QWidget()
           scroll_layout = QVBoxLayout(scroll_widget)
           
           # 创建配置项
           self.create_advanced_configs()
           
           # 创建设置卡片
           self.create_advanced_cards(scroll_layout)
           
           # 显示当前状态
           self.status_label = Label("状态: 就绪")
           self.status_label.setStyleSheet("padding: 10px;")
           
           scroll_area.setWidget(scroll_widget)
           scroll_area.setWidgetResizable(True)
           scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
           
           layout.addLayout(header_layout)
           layout.addWidget(scroll_area)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def create_advanced_configs(self):
           """创建高级配置项"""
           # 性能配置
           self.performance_config = ConfigItem("App", "HighPerformance", False)
           
           # 质量配置
           self.quality_config = RangeConfigItem("App", "Quality", 2, 0, 4)  # Low=0, Medium=1, High=2, Ultra=3
           
           # 语言配置
           self.language_config = OptionsConfigItem(
               "App", "Language", "中文", ["中文", "English", "日本語"]
           )
           
           # 自动更新配置
           self.auto_update_config = ConfigItem("App", "AutoUpdate", True)
       
       def create_advanced_cards(self, layout):
           """创建高级设置卡片"""
           # 性能设置
           performance_card = SwitchSettingCard(
               FIF.SPEED, "性能模式", "启用高性能模式", self.performance_config
           )
           
           # 质量设置
           quality_card = RangeSettingCard(
               FIF.HD, "质量设置", "选择输出质量", self.quality_config
           )
           
           # 语言设置
           language_card = ComboBoxSettingCard(
               FIF.LANGUAGE, "语言设置", "选择界面语言", self.language_config
           )
           
           # 自动更新设置
           update_card = SwitchSettingCard(
               FIF.SYNC, "自动更新", "自动检查并安装更新", self.auto_update_config
           )
           
           # 主要操作按钮
           primary_card = PrimaryPushSettingCard(
               FIF.SAVE, "保存所有设置", "保存所有配置更改"
           )
           
           # 帮助链接
           help_card = HyperlinkCard(
               "https://example.com/help", "获取帮助", "访问在线帮助文档", FIF.HELP
           )
           
           layout.addWidget(performance_card)
           layout.addWidget(quality_card)
           layout.addWidget(language_card)
           layout.addWidget(update_card)
           layout.addWidget(primary_card)
           layout.addWidget(help_card)
           
           # 添加弹性空间
           layout.addStretch()
       
       def setup_connections(self):
           """设置连接"""
           self.reset_btn.clicked.connect(self.reset_settings)
           self.export_btn.clicked.connect(self.export_settings)
       
       def reset_settings(self):
           """重置设置"""
           self.performance_config.value = False
           self.quality_config.value = 2  # High
           self.language_config.value = "中文"
           self.auto_update_config.value = True
           
           self.status_label.setText("所有设置已重置为默认值")
       
       def export_settings(self):
           """导出设置"""
           settings = {
               "performance": self.performance_config.value,
               "quality": self.quality_config.value,
               "language": self.language_config.value,
               "auto_update": self.auto_update_config.value
           }
           
           # 这里可以实现导出到文件的逻辑
           self.status_label.setText(f"设置已导出: {len(settings)} 项配置")

最佳实践
--------

1. **配置管理** - 正确使用各种ConfigItem进行配置管理
2. **布局优化** - 合理组织设置卡片的布局和间距
3. **状态同步** - 确保UI状态与配置同步
4. **用户体验** - 提供清晰的操作反馈和状态显示
5. **响应式设计** - 考虑不同屏幕尺寸下的显示效果

注意事项
--------

- 设置卡片会自动处理主题适配
- 配置项需要正确初始化并连接信号
- 不同类型的设置卡片适用于不同的配置项类型
- 滚动区域适合大量设置项的展示
- 按钮设置卡片适合触发操作
- 颜色设置卡片支持透明度选项

相关模块
--------

- :doc:`components.settings.expand_setting_card` - 展开设置卡片
- :doc:`components.settings.custom_color_setting_card` - 自定义颜色设置卡片
- :doc:`components.widgets.button` - 按钮组件
- :doc:`components.widgets.slider` - 滑块组件
- :doc:`common.config` - 配置管理
