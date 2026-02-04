基础控件 (Widgets)
==================

本节介绍 PySide6-Fluent-Widgets 中的基础控件。

按钮 (Buttons)
-------------

PushButton
~~~~~~~~~~~

基础按钮组件，支持多种样式和状态。

.. code-block:: python

   from qfluentwidgets import PushButton

   # 创建基本按钮
   button = PushButton('点击我')

   # 设置图标
   button.setIcon(FluentIcon.ROBOT)

   # 连接信号
   button.clicked.connect(lambda: print('按钮被点击'))

PrimaryPushButton
~~~~~~~~~~~~~~~~~

主要按钮，用于强调主要操作。

.. code-block:: python

   from qfluentwidgets import PrimaryPushButton

   primary_btn = PrimaryPushButton('保存')
   primary_btn.clicked.connect(save_data)

DropDownButton
~~~~~~~~~~~~~~

下拉按钮，点击后显示菜单。

.. code-block:: python

   from qfluentwidgets import DropDownButton, Action, FluentIcon

   dropdown_btn = DropDownButton('更多选项')
   
   # 添加菜单项
   dropdown_btn.addAction(Action(FluentIcon.COPY, '复制'))
   dropdown_btn.addAction(Action(FluentIcon.PASTE, '粘贴'))

HyperlinkButton
~~~~~~~~~~~~~~~

超链接按钮，用于导航。

.. code-block:: python

   from qfluentwidgets import HyperlinkButton

   link_btn = HyperlinkButton('https://example.com', '访问网站')

输入控件 (Input Controls)
-------------------------

LineEdit
~~~~~~~~

单行文本输入框。

.. code-block:: python

   from qfluentwidgets import LineEdit

   # 基本输入框
   line_edit = LineEdit()
   line_edit.setPlaceholderText('请输入文本...')

   # 密码输入框
   password_edit = LineEdit()
   password_edit.setEchoMode(LineEdit.Password)

   # 只读输入框
   readonly_edit = LineEdit()
   readonly_edit.setReadOnly(True)

TextEdit
~~~~~~~~

多行文本编辑器。

.. code-block:: python

   from qfluentwidgets import TextEdit

   text_edit = TextEdit()
   text_edit.setPlaceholderText('请输入多行文本...')
   text_edit.setPlainText('默认文本')

SpinBox
~~~~~~~

数值输入框。

.. code-block:: python

   from qfluentwidgets import SpinBox, DoubleSpinBox

   # 整数输入框
   spin_box = SpinBox()
   spin_box.setRange(0, 100)
   spin_box.setValue(50)

   # 浮点数输入框
   double_spin = DoubleSpinBox()
   double_spin.setRange(0.0, 1.0)
   double_spin.setValue(0.5)
   double_spin.setDecimals(2)

ComboBox
~~~~~~~~

下拉选择框。

.. code-block:: python

   from qfluentwidgets import ComboBox

   combo_box = ComboBox()
   combo_box.addItems(['选项1', '选项2', '选项3'])
   combo_box.setCurrentText('选项1')

选择控件 (Selection Controls)
----------------------------

RadioButton
~~~~~~~~~~~

单选按钮。

.. code-block:: python

   from qfluentwidgets import RadioButton

   radio1 = RadioButton('选项1')
   radio2 = RadioButton('选项2')
   radio3 = RadioButton('选项3')

   # 设置按钮组
   from PySide6.QtWidgets import QButtonGroup
   button_group = QButtonGroup()
   button_group.addButton(radio1)
   button_group.addButton(radio2)
   button_group.addButton(radio3)

CheckBox
~~~~~~~~

复选框。

.. code-block:: python

   from qfluentwidgets import CheckBox

   checkbox = CheckBox('启用此功能')
   checkbox.setChecked(True)

   # 连接信号
   checkbox.stateChanged.connect(lambda state: print(f'状态: {state}'))

Switch
~~~~~~

开关控件。

.. code-block:: python

   from qfluentwidgets import Switch

   switch = Switch()
   switch.setText('通知')
   switch.setChecked(True)

进度控件 (Progress Controls)
--------------------------

ProgressBar
~~~~~~~~~~~

水平进度条。

.. code-block:: python

   from qfluentwidgets import ProgressBar

   progress_bar = ProgressBar()
   progress_bar.setValue(30)
   progress_bar.setRange(0, 100)

ProgressRing
~~~~~~~~~~~~

环形进度条。

.. code-block:: python

   from qfluentwidgets import ProgressRing

   progress_ring = ProgressRing()
   progress_ring.setValue(60)

Slider
~~~~~~

滑块控件。

.. code-block:: python

   from qfluentwidgets import Slider

   slider = Slider()
   slider.setRange(0, 100)
   slider.setValue(50)

   # 连接信号
   slider.valueChanged.connect(lambda value: print(f'值: {value}'))

显示控件 (Display Controls)
--------------------------

Label
~~~~~

文本标签。

.. code-block:: python

   from qfluentwidgets import Label, SubtitleLabel, CaptionLabel

   # 基本标签
   label = Label('普通文本')

   # 副标题标签
   subtitle = SubtitleLabel('副标题')

   # 说明标签
   caption = CaptionLabel('说明文字')

Icon Widget
~~~~~~~~~~~

图标控件。

.. code-block:: python

   from qfluentwidgets import IconWidget

   icon_widget = IconWidget(FluentIcon.SETTING)
   icon_widget.setFixedSize(32, 32)

信息提示 (Information Display)
------------------------------

InfoBar
~~~~~~~

信息提示栏。

.. code-block:: python

   from qfluentwidgets import InfoBar, InfoBarPosition

   # 成功提示
   InfoBar.success(
       title='成功',
       content='操作完成',
       orient=Qt.Horizontal,
       isClosable=True,
       position=InfoBarPosition.TOP,
       duration=3000,
       parent=self
   )

   # 错误提示
   InfoBar.error(
       title='错误',
       content='操作失败',
       orient=Qt.Horizontal,
       isClosable=True,
       position=InfoBarPosition.TOP,
       duration=3000,
       parent=self
   )

ToolTip
~~~~~~~

工具提示。

.. code-block:: python

   from qfluentwidgets import ToolTip

   button = PushButton('帮助')
   button.setToolTip('这是一个帮助按钮')

   # 自定义工具提示
   tooltip = ToolTip('详细说明')
   button.setToolTip(tooltip)

最佳实践
--------

1. **合理使用按钮类型**: 主要操作使用 PrimaryPushButton，次要操作使用 PushButton
2. **设置合适的占位符**: 为输入框设置清晰的占位符文本
3. **验证输入**: 在用户输入完成后进行验证
4. **提供反馈**: 使用 InfoBar 为用户提供操作反馈
5. **保持一致性**: 在整个应用中保持控件样式的一致性

样式自定义
--------

可以通过 QSS 自定义控件样式：

.. code-block:: python

   # 自定义按钮样式
   button.setStyleSheet("""
       PushButton {
           background-color: #0078d4;
           color: white;
           border: none;
           border-radius: 4px;
           padding: 8px 16px;
       }
       PushButton:hover {
           background-color: #106ebe;
       }
       PushButton:pressed {
           background-color: #005a9e;
       }
   """)
