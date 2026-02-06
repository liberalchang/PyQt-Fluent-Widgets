Options Setting Card 选项设置卡片模块
=======================================

Options Setting Card 模块提供选项设置卡片功能，支持单选按钮组和配置管理。
该模块提供现代化的选项设置界面，支持多个选项的选择和配置保存。

主要功能
--------

- **选项组** - 提供单选按钮组的功能
- **配置集成** - 支持OptionsConfigItem的自动保存和加载
- **展开卡片** - 继承展开卡片的功能
- **动态选项** - 支持动态添加和配置选项
- **状态同步** - 自动同步选项状态和配置

核心组件
--------

OptionsSettingCard
~~~~~~~~~~~~~~~~~

选项设置卡片，提供完整的选项设置功能。

.. code-block:: python

   from qfluentwidgets.components.settings import OptionsSettingCard
   from qfluentwidgets.common.config import OptionsConfigItem
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建选项配置项
   options_config = OptionsConfigItem(
       "App", "Language", "中文", ["中文", "English", "日本語"]
   )
   
   # 创建选项设置卡片
   options_card = OptionsSettingCard(
       configItem=options_config,
       icon=FIF.LANGUAGE,
       title="语言设置",
       content="选择界面语言",
       texts=["中文", "English", "日本語"]
   )
   
   # 连接选项变化信号
   options_card.optionChanged.connect(self.on_option_changed)

**主要信号：**
- ``optionChanged`` - 选项变化信号

**主要方法：**
- ``setValue()`` - 设置选项值
- ``value()`` - 获取当前选项值

实际应用
--------

基本选项设置卡片
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.settings import OptionsSettingCard
   from qfluentwidgets.common.config import OptionsConfigItem
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class BasicOptionsWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("选项设置卡片示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建选项配置项
           self.language_config = OptionsConfigItem(
               "App", "Language", "中文", ["中文", "English", "日本語"]
           )
           
           # 创建选项设置卡片
           self.language_card = OptionsSettingCard(
               configItem=self.language_config,
               icon=FIF.LANGUAGE,
               title="语言设置",
               content="选择界面语言",
               texts=["中文", "English", "日本語"]
           )
           
           # 显示当前选择
           self.current_label = Label("当前语言: 中文")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.language_card)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.language_card.optionChanged.connect(self.on_language_changed)
       
       def on_language_changed(self, config_item):
           """语言变化处理"""
           current_language = config_item.value
           self.current_label.setText(f"当前语言: {current_language}")

高级选项设置卡片
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.settings import OptionsSettingCard
   from qfluentwidgets.common.config import OptionsConfigItem
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class AdvancedOptionsWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("高级选项设置卡片")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.reset_btn = PushButton("重置选项")
           self.random_btn = PushButton("随机选择")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.reset_btn)
           header_layout.addWidget(self.random_btn)
           
           # 创建多个选项配置
           self.create_option_configs()
           
           # 创建选项设置卡片
           self.create_option_cards()
           
           # 显示当前状态
           self.status_label = Label("状态: 就绪")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.theme_card)
           layout.addWidget(self.quality_card)
           layout.addWidget(self.format_card)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def create_option_configs(self):
           """创建选项配置项"""
           self.theme_config = OptionsConfigItem(
               "App", "Theme", "Light", ["Light", "Dark", "Auto"]
           )
           
           self.quality_config = OptionsConfigItem(
               "App", "Quality", "High", ["Low", "Medium", "High", "Ultra"]
           )
           
           self.format_config = OptionsConfigItem(
               "App", "Format", "PDF", ["PDF", "DOCX", "TXT", "HTML"]
           )
       
       def create_option_cards(self):
           """创建选项卡片"""
           self.theme_card = OptionsSettingCard(
               configItem=self.theme_config,
               icon=FIF.BRUSH,
               title="主题设置",
               content="选择应用程序主题",
               texts=["Light", "Dark", "Auto"]
           )
           
           self.quality_card = OptionsSettingCard(
               configItem=self.quality_config,
               icon=FIF.HD,
               title="质量设置",
               content="选择输出质量",
               texts=["Low", "Medium", "High", "Ultra"]
           )
           
           self.format_card = OptionsSettingCard(
               configItem=self.format_config,
               icon=FIF.DOCUMENT,
               title="格式设置",
               content="选择文件格式",
               texts=["PDF", "DOCX", "TXT", "HTML"]
           )
       
       def setup_connections(self):
           """设置连接"""
           self.reset_btn.clicked.connect(self.reset_options)
           self.random_btn.clicked.connect(self.random_select)
           
           self.theme_card.optionChanged.connect(self.on_theme_changed)
           self.quality_card.optionChanged.connect(self.on_quality_changed)
           self.format_card.optionChanged.connect(self.on_format_changed)
       
       def reset_options(self):
           """重置选项"""
           self.theme_config.value = "Light"
           self.quality_config.value = "High"
           self.format_config.value = "PDF"
           self.status_label.setText("所有选项已重置为默认值")
       
       def random_select(self):
           """随机选择"""
           import random
           
           themes = ["Light", "Dark", "Auto"]
           qualities = ["Low", "Medium", "High", "Ultra"]
           formats = ["PDF", "DOCX", "TXT", "HTML"]
           
           self.theme_config.value = random.choice(themes)
           self.quality_config.value = random.choice(qualities)
           self.format_config.value = random.choice(formats)
           
           self.status_label.setText("已随机选择所有选项")
       
       def on_theme_changed(self, config_item):
           """主题变化处理"""
           self.status_label.setText(f"主题已更新: {config_item.value}")
       
       def on_quality_changed(self, config_item):
           """质量变化处理"""
           self.status_label.setText(f"质量已更新: {config_item.value}")
       
       def on_format_changed(self, config_item):
           """格式变化处理"""
           self.status_label.setText(f"格式已更新: {config_item.value}")

动态选项管理
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.settings import OptionsSettingCard
   from qfluentwidgets.common.config import OptionsConfigItem
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   from qfluentwidgets.common.icon import FluentIcon as FIF
   
   class DynamicOptionsWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("动态选项管理")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.add_option_btn = PushButton("添加选项")
           self.remove_option_btn = PushButton("移除选项")
           self.clear_all_btn = PushButton("清空选项")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.add_option_btn)
           header_layout.addWidget(self.remove_option_btn)
           header_layout.addWidget(self.clear_all_btn)
           
           # 创建动态选项配置
           self.create_dynamic_config()
           
           # 创建选项设置卡片
           self.dynamic_card = OptionsSettingCard(
               configItem=self.dynamic_config,
               icon=FIF.SETTING,
               title="动态选项",
               content="管理动态选项列表",
               texts=self.dynamic_config.options
           )
           
           # 显示当前状态
           self.status_label = Label("状态: 就绪")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.dynamic_card)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def create_dynamic_config(self):
           """创建动态配置项"""
           initial_options = ["选项1", "选项2", "选项3"]
           self.dynamic_config = OptionsConfigItem(
               "App", "DynamicOptions", "选项1", initial_options
           )
       
       def setup_connections(self):
           """设置连接"""
           self.add_option_btn.clicked.connect(self.add_option)
           self.remove_option_btn.clicked.connect(self.remove_option)
           self.clear_all_btn.clicked.connect(self.clear_all_options)
           
           self.dynamic_card.optionChanged.connect(self.on_dynamic_changed)
       
       def add_option(self):
           """添加选项"""
           import random
           
           new_options = [
               "新选项A", "新选项B", "新选项C", "新选项D", "新选项E"
           ]
           
           current_options = self.dynamic_config.options.copy()
           new_option = random.choice(new_options)
           
           if new_option not in current_options:
               current_options.append(new_option)
               self.dynamic_config.options = current_options
               
               # 重新创建选项卡片
               self.recreate_dynamic_card()
               
               self.status_label.setText(f"已添加选项: {new_option}")
           else:
               self.status_label.setText(f"选项已存在: {new_option}")
       
       def remove_option(self):
           """移除选项"""
           current_options = self.dynamic_config.options.copy()
           
           if len(current_options) > 1:
               removed_option = current_options.pop()
               self.dynamic_config.options = current_options
               
               # 重新创建选项卡片
               self.recreate_dynamic_card()
               
               self.status_label.setText(f"已移除选项: {removed_option}")
           else:
               self.status_label.setText("至少需要保留一个选项")
       
       def clear_all_options(self):
           """清空所有选项"""
           self.dynamic_config.options = ["默认选项"]
           
           # 重新创建选项卡片
           self.recreate_dynamic_card()
           
           self.status_label.setText("已清空所有选项，保留默认选项")
       
       def recreate_dynamic_card(self):
           """重新创建动态选项卡片"""
           # 这里需要重新创建选项卡片以更新选项列表
           # 由于OptionsSettingCard在初始化时创建按钮，这里只是示例
           # 实际使用中可能需要重新设计以支持动态更新
           pass
       
       def on_dynamic_changed(self, config_item):
           """动态选项变化处理"""
           self.status_label.setText(f"动态选项已更新: {config_item.value}")

最佳实践
--------

1. **配置管理** - 正确使用OptionsConfigItem进行配置管理
2. **默认选项** - 为选项设置合理的默认值
3. **选项验证** - 验证选项值的有效性
4. **状态同步** - 确保UI状态与配置同步
5. **用户体验** - 提供清晰的选项描述和反馈

注意事项
--------

- 选项设置卡片会自动处理配置的保存和加载
- 选项列表需要在初始化时提供
- 单选按钮组会自动处理互斥选择
- 配置项需要正确初始化为OptionsConfigItem类型
- 选项变化会自动触发配置更新
- 展开卡片会根据内容自动调整高度

相关模块
--------

- :doc:`components.settings.setting_card` - 设置卡片
- :doc:`components.settings.expand_setting_card` - 展开设置卡片
- :doc:`components.widgets.button` - 按钮组件
- :doc:`common.config` - 配置管理
