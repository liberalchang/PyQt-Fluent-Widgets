Acrylic Combo Box 亚克力组合框模块
=====================================

Acrylic Combo Box 模块提供亚克力风格的组合框组件，支持透明效果和现代化设计。
该模块结合了亚克力视觉效果和组合框功能，提供美观的选项选择界面。

主要功能
--------

- **亚克力效果** - 提供现代化的亚克力视觉效果
- **组合框功能** - 支持下拉选项选择
- **可编辑支持** - 提供可编辑的组合框变体
- **设置卡片** - 集成设置卡片的组合框组件
- **动画效果** - 支持平滑的下拉动画

核心组件
--------

AcrylicComboBox
~~~~~~~~~~~~~~~

亚克力组合框，提供标准的下拉选择功能。

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_combo_box import AcrylicComboBox
   from qfluentwidgets import CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   
   # 创建亚克力组合框
   combo_box = AcrylicComboBox()
   
   # 添加选项
   combo_box.addItems(["选项1", "选项2", "选项3"])
   
   # 连接信号
   combo_box.currentIndexChanged.connect(on_selection_changed)

**主要信号：**
- ``currentIndexChanged`` - 当前索引变化信号

AcrylicEditableComboBox
~~~~~~~~~~~~~~~~~~~~~~~

可编辑的亚克力组合框，支持用户输入。

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_combo_box import AcrylicEditableComboBox
   from qfluentwidgets import CardWidget
   from PySide6.QtWidgets import QVBoxLayout
   
   # 创建可编辑亚克力组合框
   editable_combo = AcrylicEditableComboBox()
   
   # 添加选项
   editable_combo.addItems(["项目1", "项目2", "项目3"])
   
   # 连接信号
   editable_combo.currentTextChanged.connect(on_text_changed)

AcrylicComboBoxSettingCard
~~~~~~~~~~~~~~~~~~~~~~~~~~

带组合框的设置卡片，用于配置界面。

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_combo_box import AcrylicComboBoxSettingCard
   from qfluentwidgets.common.config import OptionsConfigItem, qconfig
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建配置项
   config_item = OptionsConfigItem("theme", "Light", options=["Light", "Dark", "Auto"])
   
   # 创建设置卡片
   setting_card = AcrylicComboBoxSettingCard(
       configItem=config_item,
       icon=FIF.PALETTE,
       title="主题选择",
       content="选择应用的主题模式",
       texts=["浅色", "深色", "自动"],
       parent=parent
   )

实际应用
--------

基本亚克力组合框
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_combo_box import AcrylicComboBox
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   
   class BasicAcrylicComboBoxWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("亚克力组合框示例")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建亚克力组合框
           self.combo_box = AcrylicComboBox()
           
           # 添加选项
           languages = ["Python", "JavaScript", "TypeScript", "C++", "Java", "Go"]
           self.combo_box.addItems(languages)
           
           # 显示选择结果
           self.result_label = Label("未选择语言")
           self.result_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.combo_box)
           layout.addWidget(self.result_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.combo_box.currentIndexChanged.connect(self.on_selection_changed)
       
       def on_selection_changed(self, index):
           """选择变化处理"""
           if index >= 0:
               selected_text = self.combo_box.currentText()
               self.result_label.setText(f"已选择: {selected_text}")
           else:
               self.result_label.setText("未选择语言")

可编辑亚克力组合框
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_combo_box import AcrylicEditableComboBox
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout
   
   class EditableAcrylicComboBoxWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("可编辑亚克力组合框")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建可编辑亚克力组合框
           self.editable_combo = AcrylicEditableComboBox()
           
           # 添加预设选项
           frameworks = ["React", "Vue.js", "Angular", "Svelte", "Next.js"]
           self.editable_combo.addItems(frameworks)
           self.editable_combo.setPlaceholderText("输入或选择框架...")
           
           # 控制按钮
           self.add_current_btn = PushButton("添加当前文本")
           self.clear_btn = PushButton("清空选项")
           
           # 显示当前选项
           self.current_label = Label("当前文本: 无")
           self.current_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.editable_combo)
           layout.addWidget(self.add_current_btn)
           layout.addWidget(self.clear_btn)
           layout.addWidget(self.current_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.editable_combo.currentTextChanged.connect(self.on_text_changed)
           self.add_current_btn.clicked.connect(self.add_current_text)
           self.clear_btn.clicked.connect(self.clear_options)
       
       def on_text_changed(self, text):
           """文本变化处理"""
           self.current_label.setText(f"当前文本: {text if text else '无'}")
       
       def add_current_text(self):
           """添加当前文本到选项"""
           current_text = self.editable_combo.currentText()
           if current_text and current_text not in [self.editable_combo.itemText(i) for i in range(self.editable_combo.count())]:
               self.editable_combo.addItem(current_text)
               self.editable_combo.setCurrentText(current_text)
       
       def clear_options(self):
           """清空所有选项"""
           self.editable_combo.clear()

高级用法
--------

设置卡片组合框
~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_combo_box import AcrylicComboBoxSettingCard
   from qfluentwidgets.common.config import OptionsConfigItem, qconfig, ConfigItem
   from qfluentwidgets import CardWidget, Label, PushButton
   from qfluentwidgets.common.icon import FluentIcon as FIF
   from PySide6.QtWidgets import QVBoxLayout
   
   class SettingCardComboBoxWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
           self.setup_config()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("设置卡片组合框")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建语言设置卡片
           self.language_card = AcrylicComboBoxSettingCard(
               configItem=self.language_config,
               icon=FIF.LANGUAGE,
               title="界面语言",
               content="选择应用程序的界面语言",
               texts=["简体中文", "English", "日本語", "한국어"],
               parent=self
           )
           
           # 创建主题设置卡片
           self.theme_card = AcrylicComboBoxSettingCard(
               configItem=self.theme_config,
               icon=FIF.PALETTE,
               title="主题模式",
               content="选择应用程序的主题模式",
               texts=["浅色", "深色", "跟随系统"],
               parent=self
           )
           
           # 创建字体大小设置卡片
           self.font_size_card = AcrylicComboBoxSettingCard(
               configItem=self.font_size_config,
               icon=FIF.FONT,
               title="字体大小",
               content="调整界面字体大小",
               texts=["小", "中", "大", "特大"],
               parent=self
           )
           
           # 控制按钮
           self.show_config_btn = PushButton("显示当前配置")
           self.reset_btn = PushButton("重置为默认")
           
           # 显示配置信息
           self.config_label = Label("点击按钮查看配置")
           self.config_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.language_card)
           layout.addWidget(self.theme_card)
           layout.addWidget(self.font_size_card)
           layout.addWidget(self.show_config_btn)
           layout.addWidget(self.reset_btn)
           layout.addWidget(self.config_label)
           self.setLayout(layout)
       
       def setup_config(self):
           """设置配置项"""
           # 语言配置
           self.language_config = OptionsConfigItem(
               "language", "zh_CN", options=["zh_CN", "en_US", "ja_JP", "ko_KR"]
           )
           
           # 主题配置
           self.theme_config = OptionsConfigItem(
               "theme", "light", options=["light", "dark", "auto"]
           )
           
           # 字体大小配置
           self.font_size_config = OptionsConfigItem(
               "font_size", "medium", options=["small", "medium", "large", "xlarge"]
           )
           
           # 注册配置项
           qconfig.register(self.language_config)
           qconfig.register(self.theme_config)
           qconfig.register(self.font_size_config)
       
       def setup_connections(self):
           """设置连接"""
           self.show_config_btn.clicked.connect(self.show_config)
           self.reset_btn.clicked.connect(self.reset_config)
           
           # 监听配置变化
           self.language_config.valueChanged.connect(self.on_config_changed)
           self.theme_config.valueChanged.connect(self.on_config_changed)
           self.font_size_config.valueChanged.connect(self.on_config_changed)
       
       def on_config_changed(self):
           """配置变化处理"""
           self.update_config_display()
       
       def show_config(self):
           """显示当前配置"""
           language = qconfig.get(self.language_config)
           theme = qconfig.get(self.theme_config)
           font_size = qconfig.get(self.font_size_config)
           
           config_text = f"当前配置:\n语言: {language}\n主题: {theme}\n字体大小: {font_size}"
           self.config_label.setText(config_text)
       
       def reset_config(self):
           """重置为默认配置"""
           qconfig.set(self.language_config, "zh_CN")
           qconfig.set(self.theme_config, "light")
           qconfig.set(self.font_size_config, "medium")
           
           self.config_label.setText("配置已重置为默认值")
       
       def update_config_display(self):
           """更新配置显示"""
           if self.config_label.text() != "点击按钮查看配置":
               self.show_config()

动态选项管理
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.material.acrylic_combo_box import AcrylicComboBox, AcrylicEditableComboBox
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   
   class DynamicComboBoxWidget(CardWidget):
       """动态选项管理器"""
       
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_connections()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("动态选项管理")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 标准组合框
           standard_label = Label("标准组合框:")
           self.standard_combo = AcrylicComboBox()
           self.standard_combo.addItems(["选项1", "选项2", "选项3"])
           
           # 可编辑组合框
           editable_label = Label("可编辑组合框:")
           self.editable_combo = AcrylicEditableComboBox()
           self.editable_combo.addItems(["项目A", "项目B", "项目C"])
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           self.add_option_btn = PushButton("添加选项")
           self.remove_option_btn = PushButton("移除选项")
           self.clear_all_btn = PushButton("清空全部")
           
           button_layout.addWidget(self.add_option_btn)
           button_layout.addWidget(self.remove_option_btn)
           button_layout.addWidget(self.clear_all_btn)
           
           # 显示当前状态
           self.status_label = Label("就绪")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(standard_label)
           layout.addWidget(self.standard_combo)
           layout.addWidget(editable_label)
           layout.addWidget(self.editable_combo)
           layout.addLayout(button_layout)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_connections(self):
           """设置连接"""
           self.add_option_btn.clicked.connect(self.add_option)
           self.remove_option_btn.clicked.connect(self.remove_option)
           self.clear_all_btn.clicked.connect(self.clear_all)
           
           self.standard_combo.currentIndexChanged.connect(self.on_standard_changed)
           self.editable_combo.currentTextChanged.connect(self.on_editable_changed)
       
       def add_option(self):
           """添加新选项"""
           import random
           
           # 为标准组合框添加选项
           standard_options = ["新选项", "额外选项", "特殊选项"]
           standard_text = random.choice(standard_options) + str(random.randint(1, 99))
           self.standard_combo.addItem(standard_text)
           
           # 为可编辑组合框添加选项
           editable_options = ["新项目", "额外项目", "特殊项目"]
           editable_text = random.choice(editable_options) + str(random.randint(1, 99))
           self.editable_combo.addItem(editable_text)
           
           self.status_label.setText(f"已添加: {standard_text}, {editable_text}")
       
       def remove_option(self):
           """移除当前选项"""
           # 移除标准组合框的当前选项
           if self.standard_combo.currentIndex() >= 0:
               removed_text = self.standard_combo.currentText()
               self.standard_combo.removeItem(self.standard_combo.currentIndex())
               self.status_label.setText(f"已移除标准选项: {removed_text}")
           
           # 清空可编辑组合框的当前文本
           self.editable_combo.setCurrentText("")
       
       def clear_all(self):
           """清空所有选项"""
           self.standard_combo.clear()
           self.editable_combo.clear()
           self.status_label.setText("已清空所有选项")
       
       def on_standard_changed(self, index):
           """标准组合框变化处理"""
           if index >= 0:
               text = self.standard_combo.currentText()
               self.status_label.setText(f"标准选择: {text}")
       
       def on_editable_changed(self, text):
           """可编辑组合框变化处理"""
           if text:
               self.status_label.setText(f"可编辑输入: {text}")

最佳实践
--------

1. **配置管理** - 使用AcrylicComboBoxSettingCard进行配置管理
2. **选项组织** - 合理组织选项的顺序和分组
3. **用户体验** - 提供清晰的选项提示和反馈
4. **动态更新** - 支持运行时动态添加和移除选项
5. **样式一致** - 保持与应用整体风格的一致性

注意事项
--------

- 亚克力效果需要正确的背景支持
- 可编辑组合框需要处理用户输入验证
- 设置卡片需要正确配置ConfigItem
- 大量选项可能影响性能
- 选项文本长度需要考虑显示效果

相关模块
--------

- :doc:`components.material.acrylic_menu` - 亚克力菜单
- :doc:`components.material.acrylic_line_edit` - 亚克力输入框
- :doc:`components.widgets.combo_box` - 标准组合框
- :doc:`components.settings` - 设置组件
