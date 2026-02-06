Button 按钮模块
================

Button 模块提供各种样式的按钮控件，包括普通按钮、主要按钮、透明按钮、切换按钮、超链接按钮、单选按钮、工具按钮、下拉按钮、分割按钮和药丸按钮等。该模块实现了Fluent Design的按钮样式，提供丰富的交互效果。

主要功能
--------

- **多种按钮样式** - 支持普通、主要、透明、切换等多种样式
- **图标支持** - 支持图标和文本的组合显示
- **下拉菜单** - 提供下拉按钮和分割按钮
- **超链接功能** - 支持超链接按钮自动打开URL
- **单选功能** - 提供单选按钮控件
- **工具按钮** - 适用于工具栏的工具按钮
- **药丸样式** - 提供圆角的药丸按钮样式

核心组件
--------

PushButton
~~~~~~~~~~

基础按钮控件，提供标准的按钮功能。

.. code-block:: python

   from qfluentwidgets.components.widgets.button import PushButton
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建基础按钮
   button = PushButton("点击我", parent=parent)
   
   # 创建带图标的按钮
   button_with_icon = PushButton(FIF.DOWNLOAD, "下载", parent=parent)
   
   # 连接信号
   button.clicked.connect(self.on_button_clicked)

**构造函数：**
- ``PushButton(parent: QWidget = None)``
- ``PushButton(text: str, parent: QWidget = None, icon: QIcon | str | FluentIconBase = None)``
- ``PushButton(icon: QIcon | FluentIcon, text: str, parent: QWidget = None)``

**主要方法：**
- ``setIcon()`` - 设置图标
- ``icon()`` - 获取图标

PrimaryPushButton
~~~~~~~~~~~~~~~~

主要按钮控件，使用主题色作为背景色。

.. code-block:: python

   from qfluentwidgets.components.widgets.button import PrimaryPushButton
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建主要按钮
   primary_button = PrimaryPushButton("保存", parent=parent)
   
   # 创建带图标的主要按钮
   primary_button_with_icon = PrimaryPushButton(FIF.SAVE, "保存", parent=parent)
   
   # 连接信号
   primary_button.clicked.connect(self.on_save_clicked)

**特点：**
- 使用主题色作为背景
- 图标颜色会根据主题自动反转
- 适用于主要操作按钮

TransparentPushButton
~~~~~~~~~~~~~~~~~~~~

透明按钮控件，背景透明。

.. code-block:: python

   from qfluentwidgets.components.widgets.button import TransparentPushButton
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建透明按钮
   transparent_button = TransparentPushButton("取消", parent=parent)
   
   # 创建带图标的透明按钮
   transparent_button_with_icon = TransparentPushButton(FIF.CANCEL, "取消", parent=parent)

**特点：**
- 背景透明
- 适用于次要操作按钮

ToggleButton
~~~~~~~~~~~~

切换按钮控件，支持选中/未选中状态。

.. code-block:: python

   from qfluentwidgets.components.widgets.button import ToggleButton
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建切换按钮
   toggle_button = ToggleButton("开关", parent=parent)
   
   # 设置初始状态
   toggle_button.setChecked(True)
   
   # 连接信号
   toggle_button.toggled.connect(self.on_toggle_changed)

**特点：**
- 支持选中/未选中状态
- 选中时使用主要按钮样式
- 提供``toggled``信号

TransparentTogglePushButton
~~~~~~~~~~~~~~~~~~~~~~~~~~~

透明切换按钮控件，背景透明的切换按钮。

.. code-block:: python

   from qfluentwidgets.components.widgets.button import TransparentTogglePushButton
   
   # 创建透明切换按钮
   transparent_toggle = TransparentTogglePushButton("静音", parent=parent)
   
   # 连接信号
   transparent_toggle.toggled.connect(self.on_mute_changed)

HyperlinkButton
~~~~~~~~~~~~~~

超链接按钮控件，点击时自动打开URL。

.. code-block:: python

   from qfluentwidgets.components.widgets.button import HyperlinkButton
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建超链接按钮
   link_button = HyperlinkButton("https://example.com", "访问网站", parent=parent)
   
   # 创建带图标的超链接按钮
   link_button_with_icon = HyperlinkButton(FIF.LINK, "https://example.com", "访问网站", parent=parent)
   
   # 设置URL
   link_button.setUrl("https://newsite.com")
   
   # 获取URL
   url = link_button.getUrl()

**特点：**
- 点击时自动打开URL
- 支持图标显示
- 鼠标悬停时显示手型光标

RadioButton
~~~~~~~~~~~

单选按钮控件，用于单选操作。

.. code-block:: python

   from qfluentwidgets.components.widgets.button import RadioButton
   
   # 创建单选按钮
   radio1 = RadioButton("选项1", parent=parent)
   radio2 = RadioButton("选项2", parent=parent)
   radio3 = RadioButton("选项3", parent=parent)
   
   # 设置默认选中
   radio1.setChecked(True)
   
   # 连接信号
   radio1.toggled.connect(self.on_radio_changed)

**特点：**
- 支持单选功能
- 自定义绘制样式
- 支持图标显示

ToolButton
~~~~~~~~~~

工具按钮控件，适用于工具栏。

.. code-block:: python

   from qfluentwidgets.components.widgets.button import ToolButton
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建工具按钮
   tool_button = ToolButton(FIF.SETTING, parent=parent)
   
   # 创建带文本的工具按钮
   tool_button_with_text = ToolButton(FIF.HELP, "帮助", parent=parent)
   
   # 连接信号
   tool_button.clicked.connect(self.on_tool_clicked)

**特点：**
- 适用于工具栏
- 支持图标和文本
- 紧凑的样式设计

下拉按钮系列
~~~~~~~~~~~~

DropDownButtonBase
^^^^^^^^^^^^^^^^^^

下拉按钮基类。

.. code-block:: python

   from qfluentwidgets.components.widgets.button import DropDownButtonBase
   from qfluentwidgets import RoundMenu, Action
   
   class CustomDropDownButton(DropDownButtonBase):
       def __init__(self, text, parent=None):
           super().__init__(text, parent)
           
           # 设置下拉菜单
           menu = RoundMenu(parent=self)
           menu.addAction(Action(FIF.COPY, "复制"))
           menu.addAction(Action(FIF.PASTE, "粘贴"))
           menu.addAction(Action(FIF.CUT, "剪切"))
           
           self.setFlyout(menu)

DropDownPushButton
^^^^^^^^^^^^^^^^^^

下拉按钮控件。

.. code-block:: python

   from qfluentwidgets.components.widgets.button import DropDownPushButton
   from qfluentwidgets import RoundMenu, Action, FluentIcon as FIF
   
   # 创建下拉按钮
   dropdown_button = DropDownPushButton("文件", parent=parent)
   
   # 设置下拉菜单
   menu = RoundMenu(parent=dropdown_button)
   menu.addAction(Action(FIF.NEW, "新建"))
   menu.addAction(Action(FIF.OPEN, "打开"))
   menu.addAction(Action(FIF.SAVE, "保存"))
   
   dropdown_button.setFlyout(menu)

TransparentDropDownPushButton
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

透明下拉按钮控件。

.. code-block:: python

   from qfluentwidgets.components.widgets.button import TransparentDropDownPushButton
   
   # 创建透明下拉按钮
   transparent_dropdown = TransparentDropDownPushButton("编辑", parent=parent)
   
   # 设置下拉菜单
   menu = RoundMenu(parent=transparent_dropdown)
   menu.addAction(Action(FIF.UNDO, "撤销"))
   menu.addAction(Action(FIF.REDO, "重做"))
   
   transparent_dropdown.setFlyout(menu)

DropDownToolButton
^^^^^^^^^^^^^^^^^^

下拉工具按钮控件。

.. code-block:: python

   from qfluentwidgets.components.widgets.button import DropDownToolButton
   from qfluentwidgets import RoundMenu, Action, FluentIcon as FIF
   
   # 创建下拉工具按钮
   dropdown_tool = DropDownToolButton(FIF.MORE, parent=parent)
   
   # 设置下拉菜单
   menu = RoundMenu(parent=dropdown_tool)
   menu.addAction(Action(FIF.REFRESH, "刷新"))
   menu.addAction(Action(FIF.DOWNLOAD, "下载"))
   
   dropdown_tool.setFlyout(menu)

PrimaryDropDownButton
^^^^^^^^^^^^^^^^^^^^

主要下拉按钮控件。

.. code-block:: python

   from qfluentwidgets.components.widgets.button import PrimaryDropDownButton
   from qfluentwidgets import RoundMenu, Action, FluentIcon as FIF
   
   # 创建主要下拉按钮
   primary_dropdown = PrimaryDropDownButton("操作", parent=parent)
   
   # 设置下拉菜单
   menu = RoundMenu(parent=primary_dropdown)
   menu.addAction(Action(FIF.ADD, "添加"))
   menu.addAction(Action(FIF.DELETE, "删除"))
   
   primary_dropdown.setFlyout(menu)

分割按钮系列
~~~~~~~~~~~~

SplitWidgetBase
^^^^^^^^^^^^^^^

分割按钮基类。

.. code-block:: python

   from qfluentwidgets.components.widgets.button import SplitWidgetBase
   
   class CustomSplitButton(SplitWidgetBase):
       def __init__(self, text, parent=None):
           super().__init__(text, parent)
           # 自定义实现

SplitPushButton
^^^^^^^^^^^^^^^

分割按钮控件。

.. code-block:: python

   from qfluentwidgets.components.widgets.button import SplitPushButton
   from qfluentwidgets import RoundMenu, Action, FluentIcon as FIF
   
   # 创建分割按钮
   split_button = SplitPushButton("保存", parent=parent)
   
   # 设置下拉菜单
   menu = RoundMenu(parent=split_button)
   menu.addAction(Action(FIF.SAVE, "保存"))
   menu.addAction(Action(FIF.SAVE_AS, "另存为"))
   
   split_button.setFlyout(menu)
   
   # 连接主按钮点击信号
   split_button.clicked.connect(self.on_save_clicked)

PrimarySplitPushButton
^^^^^^^^^^^^^^^^^^^^^

主要分割按钮控件。

.. code-block:: python

   from qfluentwidgets.components.widgets.button import PrimarySplitPushButton
   from qfluentwidgets import RoundMenu, Action, FluentIcon as FIF
   
   # 创建主要分割按钮
   primary_split = PrimarySplitPushButton("导出", parent=parent)
   
   # 设置下拉菜单
   menu = RoundMenu(parent=primary_split)
   menu.addAction(Action(FIF.EXPORT, "导出PDF"))
   menu.addAction(Action(FIF.EXPORT, "导出Excel"))
   
   primary_split.setFlyout(menu)

SplitToolButton
^^^^^^^^^^^^^^^

分割工具按钮控件。

.. code-block:: python

   from qfluentwidgets.components.widgets.button import SplitToolButton
   from qfluentwidgets import RoundMenu, Action, FluentIcon as FIF
   
   # 创建分割工具按钮
   split_tool = SplitToolButton(FIF.SHARE, parent=parent)
   
   # 设置下拉菜单
   menu = RoundMenu(parent=split_tool)
   menu.addAction(Action(FIF.EMAIL, "邮件分享"))
   menu.addAction(Action(FIF.LINK, "复制链接"))
   
   split_tool.setFlyout(menu)

PrimarySplitToolButton
^^^^^^^^^^^^^^^^^^^^^^

主要分割工具按钮控件。

.. code-block:: python

   from qfluentwidgets.components.widgets.button import PrimarySplitToolButton
   
   # 创建主要分割工具按钮
   primary_split_tool = PrimarySplitToolButton(FIF.SYNC, parent=parent)
   
   # 设置下拉菜单
   menu = RoundMenu(parent=primary_split_tool)
   menu.addAction(Action(FIF.SYNC, "立即同步"))
   menu.addAction(Action(FIF.SETTING, "同步设置"))
   
   primary_split_tool.setFlyout(menu)

药丸按钮系列
~~~~~~~~~~~~

PillButtonBase
^^^^^^^^^^^^^^

药丸按钮基类。

.. code-block:: python

   from qfluentwidgets.components.widgets.button import PillButtonBase
   
   class CustomPillButton(PillButtonBase):
       def __init__(self, text, parent=None):
           super().__init__(text, parent)
           # 自定义实现

PillPushButton
^^^^^^^^^^^^^^

药丸按钮控件。

.. code-block:: python

   from qfluentwidgets.components.widgets.button import PillPushButton
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建药丸按钮
   pill_button = PillPushButton("选项1", parent=parent)
   
   # 创建带图标的药丸按钮
   pill_button_with_icon = PillPushButton(FIF.HEART, "收藏", parent=parent)
   
   # 连接信号
   pill_button.toggled.connect(self.on_pill_toggled)

**特点：**
- 圆角矩形样式
- 支持切换状态
- 适用于选项卡或模式切换

PillToolButton
^^^^^^^^^^^^^^

药丸工具按钮控件。

.. code-block:: python

   from qfluentwidgets.components.widgets.button import PillToolButton
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建药丸工具按钮
   pill_tool = PillToolButton(FIF.VIEW, parent=parent)
   
   # 连接信号
   pill_tool.toggled.connect(self.on_view_mode_changed)

实际应用
--------

基本按钮应用
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.widgets.button import (
       PushButton, PrimaryPushButton, TransparentPushButton
   )
   from qfluentwidgets import CardWidget, Label, QVBoxLayout
   from PySide6.QtCore import Qt
   
   class BasicButtonWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_buttons()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("基本按钮应用")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建各种按钮
           self.normal_button = PushButton("普通按钮", parent=self)
           self.primary_button = PrimaryPushButton("主要按钮", parent=self)
           self.transparent_button = TransparentPushButton("透明按钮", parent=self)
           
           # 设置按钮样式
           self.normal_button.setFixedSize(120, 32)
           self.primary_button.setFixedSize(120, 32)
           self.transparent_button.setFixedSize(120, 32)
           
           # 显示当前状态
           self.status_label = Label("状态: 按钮已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.normal_button)
           layout.addWidget(self.primary_button)
           layout.addWidget(self.transparent_button)
           layout.addWidget(self.status_label)
           layout.addStretch()
           
           self.setLayout(layout)
       
       def setup_buttons(self):
           """设置按钮连接"""
           self.normal_button.clicked.connect(self.on_normal_clicked)
           self.primary_button.clicked.connect(self.on_primary_clicked)
           self.transparent_button.clicked.connect(self.on_transparent_clicked)
           
           self.status_label.setText("状态: 按钮连接已设置")
       
       def on_normal_clicked(self):
           """普通按钮点击处理"""
           self.status_label.setText("状态: 普通按钮被点击")
       
       def on_primary_clicked(self):
           """主要按钮点击处理"""
           self.status_label.setText("状态: 主要按钮被点击")
       
       def on_transparent_clicked(self):
           """透明按钮点击处理"""
           self.status_label.setText("状态: 透明按钮被点击")

切换按钮应用
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.widgets.button import (
       ToggleButton, TransparentTogglePushButton, PillPushButton
   )
   from qfluentwidgets import CardWidget, Label, QVBoxLayout
   from PySide6.QtCore import Qt
   
   class ToggleButtonWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_toggles()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("切换按钮应用")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建各种切换按钮
           self.toggle_button = ToggleButton("切换按钮", parent=self)
           self.transparent_toggle = TransparentTogglePushButton("透明切换", parent=self)
           self.pill_toggle = PillPushButton("药丸切换", parent=self)
           
           # 设置按钮样式
           self.toggle_button.setFixedSize(120, 32)
           self.transparent_toggle.setFixedSize(120, 32)
           self.pill_toggle.setFixedSize(120, 32)
           
           # 显示当前状态
           self.status_label = Label("状态: 切换按钮已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.toggle_button)
           layout.addWidget(self.transparent_toggle)
           layout.addWidget(self.pill_toggle)
           layout.addWidget(self.status_label)
           layout.addStretch()
           
           self.setLayout(layout)
       
       def setup_toggles(self):
           """设置切换按钮连接"""
           self.toggle_button.toggled.connect(self.on_toggle_changed)
           self.transparent_toggle.toggled.connect(self.on_transparent_changed)
           self.pill_toggle.toggled.connect(self.on_pill_changed)
           
           self.status_label.setText("状态: 切换按钮连接已设置")
       
       def on_toggle_changed(self, checked):
           """切换按钮状态改变处理"""
           state = "开启" if checked else "关闭"
           self.status_label.setText(f"状态: 切换按钮已{state}")
       
       def on_transparent_changed(self, checked):
           """透明切换按钮状态改变处理"""
           state = "开启" if checked else "关闭"
           self.status_label.setText(f"状态: 透明切换已{state}")
       
       def on_pill_changed(self, checked):
           """药丸切换按钮状态改变处理"""
           state = "选中" if checked else "未选中"
           self.status_label.setText(f"状态: 药丸切换已{state}")

下拉按钮应用
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.widgets.button import (
       DropDownPushButton, PrimaryDropDownButton, SplitPushButton
   )
   from qfluentwidgets import RoundMenu, Action, CardWidget, Label, QVBoxLayout
   from qfluentwidgets import FluentIcon as FIF
   from PySide6.QtCore import Qt
   
   class DropdownButtonWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_dropdowns()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("下拉按钮应用")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 创建下拉按钮
           self.dropdown_button = DropDownPushButton("文件操作", parent=self)
           self.primary_dropdown = PrimaryDropDownButton("主要操作", parent=self)
           self.split_button = SplitPushButton("分割操作", parent=self)
           
           # 设置按钮样式
           self.dropdown_button.setFixedSize(150, 32)
           self.primary_dropdown.setFixedSize(150, 32)
           self.split_button.setFixedSize(150, 32)
           
           # 显示当前状态
           self.status_label = Label("状态: 下拉按钮已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.dropdown_button)
           layout.addWidget(self.primary_dropdown)
           layout.addWidget(self.split_button)
           layout.addWidget(self.status_label)
           layout.addStretch()
           
           self.setLayout(layout)
       
       def setup_dropdowns(self):
           """设置下拉按钮菜单"""
           # 文件操作菜单
           file_menu = RoundMenu(parent=self.dropdown_button)
           file_menu.addAction(Action(FIF.NEW, "新建文件"))
           file_menu.addAction(Action(FIF.OPEN, "打开文件"))
           file_menu.addAction(Action(FIF.SAVE, "保存文件"))
           file_menu.addSeparator()
           file_menu.addAction(Action(FIF.EXIT, "退出"))
           self.dropdown_button.setFlyout(file_menu)
           
           # 主要操作菜单
           main_menu = RoundMenu(parent=self.primary_dropdown)
           main_menu.addAction(Action(FIF.ADD, "添加项目"))
           main_menu.addAction(Action(FIF.DELETE, "删除项目"))
           main_menu.addAction(Action(FIF.EDIT, "编辑项目"))
           self.primary_dropdown.setFlyout(main_menu)
           
           # 分割操作菜单
           split_menu = RoundMenu(parent=self.split_button)
           split_menu.addAction(Action(FIF.COPY, "复制"))
           split_menu.addAction(Action(FIF.PASTE, "粘贴"))
           split_menu.addAction(Action(FIF.CUT, "剪切"))
           self.split_button.setFlyout(split_menu)
           
           # 连接信号
           self.split_button.clicked.connect(self.on_split_clicked)
           
           self.status_label.setText("状态: 下拉按钮菜单已设置")
       
       def on_split_clicked(self):
           """分割按钮主按钮点击处理"""
           self.status_label.setText("状态: 分割按钮主按钮被点击")

高级按钮应用
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.widgets.button import (
       HyperlinkButton, RadioButton, ToolButton
   )
   from qfluentwidgets import CardWidget, Label, QVBoxLayout, QHBoxLayout
   from qfluentwidgets import FluentIcon as FIF
   from PySide6.QtCore import Qt
   from PySide6.QtWidgets import QButtonGroup
   
   class AdvancedButtonWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_advanced_buttons()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("高级按钮应用")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 超链接按钮
           self.link_button = HyperlinkButton(
               "https://github.com", "访问GitHub", FIF.GITHUB, parent=self
           )
           
           # 单选按钮组
           radio_layout = QHBoxLayout()
           self.radio_group = QButtonGroup(self)
           
           self.radio1 = RadioButton("选项A", parent=self)
           self.radio2 = RadioButton("选项B", parent=self)
           self.radio3 = RadioButton("选项C", parent=self)
           
           self.radio_group.addButton(self.radio1, 0)
           self.radio_group.addButton(self.radio2, 1)
           self.radio_group.addButton(self.radio3, 2)
           
           radio_layout.addWidget(self.radio1)
           radio_layout.addWidget(self.radio2)
           radio_layout.addWidget(self.radio3)
           radio_layout.addStretch()
           
           # 工具按钮组
           tool_layout = QHBoxLayout()
           
           self.tool_button1 = ToolButton(FIF.UNDO, parent=self)
           self.tool_button2 = ToolButton(FIF.REDO, parent=self)
           self.tool_button3 = ToolButton(FIF.REFRESH, parent=self)
           self.tool_button4 = ToolButton(FIF.SETTING, parent=self)
           
           tool_layout.addWidget(self.tool_button1)
           tool_layout.addWidget(self.tool_button2)
           tool_layout.addWidget(self.tool_button3)
           tool_layout.addWidget(self.tool_button4)
           tool_layout.addStretch()
           
           # 显示当前状态
           self.status_label = Label("状态: 高级按钮已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.link_button)
           layout.addLayout(radio_layout)
           layout.addLayout(tool_layout)
           layout.addWidget(self.status_label)
           layout.addStretch()
           
           self.setLayout(layout)
       
       def setup_advanced_buttons(self):
           """设置高级按钮连接"""
           # 连接单选按钮
           self.radio1.toggled.connect(self.on_radio_changed)
           self.radio2.toggled.connect(self.on_radio_changed)
           self.radio3.toggled.connect(self.on_radio_changed)
           
           # 连接工具按钮
           self.tool_button1.clicked.connect(self.on_undo)
           self.tool_button2.clicked.connect(self.on_redo)
           self.tool_button3.clicked.connect(self.on_refresh)
           self.tool_button4.clicked.connect(self.on_setting)
           
           # 设置默认选中
           self.radio1.setChecked(True)
           
           self.status_label.setText("状态: 高级按钮连接已设置")
       
       def on_radio_changed(self):
           """单选按钮状态改变处理"""
           selected_id = self.radio_group.checkedId()
           options = ["选项A", "选项B", "选项C"]
           selected_option = options[selected_id]
           self.status_label.setText(f"状态: 已选择{selected_option}")
       
       def on_undo(self):
           """撤销操作"""
           self.status_label.setText("状态: 执行撤销操作")
       
       def on_redo(self):
           """重做操作"""
           self.status_label.setText("状态: 执行重做操作")
       
       def on_refresh(self):
           """刷新操作"""
           self.status_label.setText("状态: 执行刷新操作")
       
       def on_setting(self):
           """设置操作"""
           self.status_label.setText("状态: 打开设置")

最佳实践
--------

1. **按钮选择** - 根据操作重要性选择合适的按钮样式
2. **图标使用** - 为按钮添加合适的图标增强识别度
3. **状态管理** - 正确处理切换按钮的状态变化
4. **菜单设计** - 合理设计下拉菜单的结构和分组
5. **响应式布局** - 确保按钮在不同尺寸下正常显示

注意事项
--------

- 主要按钮用于最重要的操作
- 透明按钮用于次要操作
- 切换按钮需要明确的状态指示
- 下拉按钮菜单要有合理的层次结构
- 单选按钮需要使用QButtonGroup管理
- 工具按钮适用于紧凑的工具栏
- 药丸按钮适用于模式切换场景

相关模块
--------

- :doc:`components.widgets.menu` - 菜单控件
- :doc:`common.icon` - 图标资源
- :doc:`common.style_sheet` - 样式表
- :doc:`common.font` - 字体管理
- :doc:`common.color` - 颜色管理
