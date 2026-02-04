基础控件 (Widgets)
==================

本节介绍 PySide6-Fluent-Widgets 中的基础控件，包含所有可用的UI组件。

按钮组件 (Buttons)
-----------------

PushButton
~~~~~~~~~~
基础按钮组件。

.. code-block:: python

   button = PushButton('点击我')
   button.clicked.connect(lambda: print('按钮被点击'))

PrimaryPushButton
~~~~~~~~~~~~~~~~~
主要按钮，用于强调重要操作。

.. code-block:: python

   primary_btn = PrimaryPushButton('保存')
   primary_btn.clicked.connect(save_data)

DropDownPushButton
~~~~~~~~~~~~~~~~~~
下拉按钮。

.. code-block:: python

   dropdown_btn = DropDownPushButton('更多选项')
   dropdown_btn.addAction(Action(FluentIcon.COPY, '复制'))
   dropdown_btn.addAction(Action(FluentIcon.PASTE, '粘贴'))

ToggleButton
~~~~~~~~~~~~
切换按钮。

.. code-block:: python

   toggle_btn = ToggleButton('开关')
   toggle_btn.setChecked(True)

HyperlinkButton
~~~~~~~~~~~~~~
超链接按钮。

.. code-block:: python

   link_btn = HyperlinkButton('https://example.com', '访问网站')

PillPushButton
~~~~~~~~~~~~~~
胶囊形按钮。

.. code-block:: python

   pill_btn = PillPushButton('胶囊按钮')

卡片组件 (Cards)
---------------

CardWidget
~~~~~~~~~~
基础卡片组件。

.. code-block:: python

   card = CardWidget()
   layout = QVBoxLayout(card)
   layout.addWidget(QLabel('卡片内容'))

ElevatedCardWidget
~~~~~~~~~~~~~~~~~~
带阴影的卡片。

.. code-block:: python

   elevated_card = ElevatedCardWidget()
   elevated_card.setShadowElevation(5)

SimpleCardWidget
~~~~~~~~~~~~~~~~
简单卡片。

.. code-block:: python

   simple_card = SimpleCardWidget()
   simple_card.setBorderRadius(8)

HeaderCardWidget
~~~~~~~~~~~~~~~~
带头部的卡片。

.. code-block:: python

   header_card = HeaderCardWidget()
   header_card.setTitle('卡片标题')
   header_card.setContent('卡片内容')

输入组件 (Input Components)
----------------------------

LineEdit
~~~~~~~~
单行文本输入框。

.. code-block:: python

   line_edit = LineEdit()
   line_edit.setPlaceholderText('请输入文本...')
   line_edit.setClearButtonEnabled(True)

SearchLineEdit
~~~~~~~~~~~~~~
搜索输入框。

.. code-block:: python

   search_edit = SearchLineEdit()
   search_edit.setPlaceholderText('搜索...')

PasswordLineEdit
~~~~~~~~~~~~~~~~
密码输入框。

.. code-block:: python

   password_edit = PasswordLineEdit()
   password_edit.setEchoMode(LineEdit.Password)

TextEdit
~~~~~~~~
多行文本编辑器。

.. code-block:: python

   text_edit = TextEdit()
   text_edit.setPlaceholderText('请输入多行文本...')

ComboBox
~~~~~~~~
下拉选择框。

.. code-block:: python

   combo_box = ComboBox()
   combo_box.addItems(['选项1', '选项2', '选项3'])

EditableComboBox
~~~~~~~~~~~~~~~~
可编辑的下拉框。

.. code-block:: python

   editable_combo = EditableComboBox()
   editable_combo.addItems(['选项1', '选项2'])

SpinBox
~~~~~~~
数值输入框。

.. code-block:: python

   spin_box = SpinBox()
   spin_box.setRange(0, 100)
   spin_box.setValue(50)

DoubleSpinBox
~~~~~~~~~~~~
浮点数输入框。

.. code-block:: python

   double_spin = DoubleSpinBox()
   double_spin.setRange(0.0, 1.0)
   double_spin.setDecimals(2)

选择组件 (Selection Components)
------------------------------

CheckBox
~~~~~~~~
复选框。

.. code-block:: python

   checkbox = CheckBox('记住密码')
   checkbox.setChecked(True)

RadioButton
~~~~~~~~~~
单选按钮。

.. code-block:: python

   radio = RadioButton('选项A')
   radio.setChecked(True)

SwitchButton
~~~~~~~~~~~~
开关按钮。

.. code-block:: python

   switch = SwitchButton()
   switch.setChecked(True)

进度组件 (Progress Components)
------------------------------

ProgressBar
~~~~~~~~~~
进度条。

.. code-block:: python

   progress_bar = ProgressBar()
   progress_bar.setRange(0, 100)
   progress_bar.setValue(65)

IndeterminateProgressBar
~~~~~~~~~~~~~~~~~~~~~~~
不确定进度条。

.. code-block:: python

   indeterminate_progress = IndeterminateProgressBar()
   indeterminate_progress.start()

ProgressRing
~~~~~~~~~~~~
环形进度条。

.. code-block:: python

   progress_ring = ProgressRing()
   progress_ring.setValue(75)

IndeterminateProgressRing
~~~~~~~~~~~~~~~~~~~~~~~~
不确定环形进度条。

.. code-block:: python

   indeterminate_ring = IndeterminateProgressRing()
   indeterminate_ring.start()

滑块组件 (Slider Components)
----------------------------

Slider
~~~~~~
滑块。

.. code-block:: python

   slider = Slider()
   slider.setRange(0, 100)
   slider.setValue(30)

ClickableSlider
~~~~~~~~~~~~~~~
可点击滑块。

.. code-block:: python

   clickable_slider = ClickableSlider()
   clickable_slider.setRange(0, 100)

ToolTipSlider
~~~~~~~~~~~~
带工具提示的滑块。

.. code-block:: python

   tooltip_slider = ToolTipSlider()
   tooltip_slider.setRange(0, 100)

列表组件 (List Components)
--------------------------

ListWidget
~~~~~~~~~~
列表控件。

.. code-block:: python

   list_widget = ListWidget()
   list_widget.addItems(['项目1', '项目2', '项目3'])

ListView
~~~~~~~~
列表视图。

.. code-block:: python

   list_view = ListView()
   model = QStandardItemModel()
   list_view.setModel(model)

CycleListWidget
~~~~~~~~~~~~~~
循环列表控件。

.. code-block:: python

   cycle_list = CycleListWidget()
   cycle_list.addItems(['项目1', '项目2', '项目3'])

表格组件 (Table Components)
--------------------------

TableWidget
~~~~~~~~~~
表格控件。

.. code-block:: python

   table = TableWidget()
   table.setColumnCount(3)
   table.setRowCount(5)
   table.setHorizontalHeaderLabels(['列1', '列2', '列3'])

SortableTableWidget
~~~~~~~~~~~~~~~~~~
可排序表格控件。

.. code-block:: python

   sortable_table = SortableTableWidget()
   sortable_table.setColumnCount(3)
   sortable_table.setRowCount(5)

TableView
~~~~~~~~~
表格视图。

.. code-block:: python

   table_view = TableView()
   model = QStandardItemModel()
   table_view.setModel(model)

SortableTableView
~~~~~~~~~~~~~~~~~
可排序表格视图。

.. code-block:: python

   sortable_view = SortableTableView()
   model = QStandardItemModel()
   sortable_view.setModel(model)

树形组件 (Tree Components)
--------------------------

TreeWidget
~~~~~~~~~~
树形控件。

.. code-block:: python

   tree_widget = TreeWidget()
   item1 = QTreeWidgetItem(['根节点1'])
   item1.addChild(QTreeWidgetItem(['子节点1']))
   tree_widget.addTopLevelItem(item1)

TreeView
~~~~~~~~
树形视图。

.. code-block:: python

   tree_view = TreeView()
   model = QStandardItemModel()
   tree_view.setModel(model)

标签组件 (Label Components)
--------------------------

Label
~~~~~
基础标签。

.. code-block:: python

   label = Label('文本标签')

CaptionLabel
~~~~~~~~~~~~
说明标签。

.. code-block:: python

   caption = CaptionLabel('说明文字')

BodyLabel
~~~~~~~~
正文标签。

.. code-block:: python

   body = BodyLabel('正文内容')

SubtitleLabel
~~~~~~~~~~~~
副标题标签。

.. code-block:: python

   subtitle = SubtitleLabel('副标题')

TitleLabel
~~~~~~~~~~
标题标签。

.. code-block:: python

   title = TitleLabel('标题')

LargeTitleLabel
~~~~~~~~~~~~~~
大标题标签。

.. code-block:: python

   large_title = LargeTitleLabel('大标题')

DisplayLabel
~~~~~~~~~~~~
显示标签。

.. code-block:: python

   display = DisplayLabel('显示文本')

ImageLabel
~~~~~~~~~~
图片标签。

.. code-block:: python

   image_label = ImageLabel()
   image_label.setImage('path/to/image.png')

AvatarWidget
~~~~~~~~~~~~
头像组件。

.. code-block:: python

   avatar = AvatarWidget()
   avatar.setAvatar('path/to/avatar.png')

HyperlinkLabel
~~~~~~~~~~~~~~
超链接标签。

.. code-block:: python

   link_label = HyperlinkLabel('https://example.com', '链接文本')

信息组件 (Info Components)
--------------------------

InfoBar
~~~~~~~
信息提示栏。

.. code-block:: python

   InfoBar.success(
       title='成功',
       content='操作完成',
       position=InfoBarPosition.TOP,
       duration=3000,
       parent=self
   )

InfoBadge
~~~~~~~~~
信息徽章。

.. code-block:: python

   badge = InfoBadge.success()
   badge.setText('新')

StateToolTip
~~~~~~~~~~~~
状态工具提示。

.. code-block:: python

   tooltip = StateToolTip('状态', '这是状态信息', parent=self)
   tooltip.show()

TeachingTip
~~~~~~~~~~~
教学提示。

.. code-block:: python

   tip = TeachingTip.create(
       target=button,
       title='提示',
       content='这是一个教学提示',
       isClosable=True,
       tailPosition=TeachingTipTailPosition.BOTTOM
   )

菜单组件 (Menu Components)
--------------------------

RoundMenu
~~~~~~~~~
圆形菜单。

.. code-block:: python

   menu = RoundMenu(parent=self)
   menu.addAction('菜单项1')
   menu.addAction('菜单项2')

DWMMenu
~~~~~~~
DWM风格菜单。

.. code-block:: python

   dwm_menu = DWMMenu(parent=self)
   dwm_menu.addAction('DWM菜单项')

CheckableMenu
~~~~~~~~~~~~
可勾选菜单。

.. code-block:: python

   checkable_menu = CheckableMenu(parent=self)
   checkable_menu.addAction('可勾选项')

SystemTrayMenu
~~~~~~~~~~~~~~
系统托盘菜单。

.. code-block:: python

   tray_menu = SystemTrayMenu()
   tray_menu.addAction('托盘菜单项')

MenuBar
~~~~~~
菜单栏。

.. code-block:: python

   menu_bar = MenuBar()
   file_menu = menu_bar.addMenu('文件')
   file_menu.addAction('新建')

标签页组件 (Tab Components)
----------------------------

TabBar
~~~~~~
标签栏。

.. code-block:: python

   tab_bar = TabBar()
   tab_bar.addTab('标签1')
   tab_bar.addTab('标签2')

TabWidget
~~~~~~~~~
标签页控件。

.. code-block:: python

   tab_widget = TabWidget()
   tab1 = QWidget()
   tab2 = QWidget()
   tab_widget.addTab(tab1, '标签1')
   tab_widget.addTab(tab2, '标签2')

分页组件 (Pagination Components)
------------------------------

PipsPager
~~~~~~~~~
分页器。

.. code-block:: python

   pips_pager = PipsPager()
   pips_pager.setPageCount(10)
   pips_pager.setCurrentPage(1)

滚动组件 (Scroll Components)
----------------------------

ScrollArea
~~~~~~~~~~
滚动区域。

.. code-block:: python

   scroll_area = ScrollArea()
   scroll_area.setWidget(content_widget)

SmoothScrollArea
~~~~~~~~~~~~~~~~
平滑滚动区域。

.. code-block:: python

   smooth_scroll = SmoothScrollArea()
   smooth_scroll.setWidget(content_widget)

ScrollBar
~~~~~~~~~
滚动条。

.. code-block:: python

   scroll_bar = ScrollBar()
   scroll_bar.setRange(0, 100)
   scroll_bar.setValue(50)

SmoothScrollBar
~~~~~~~~~~~~~~
平滑滚动条。

.. code-block:: python

   smooth_scroll_bar = SmoothScrollBar()
   smooth_scroll_bar.setRange(0, 100)

分隔符组件 (Separator Components)
----------------------------------

HorizontalSeparator
~~~~~~~~~~~~~~~~~~
水平分隔符。

.. code-block:: python

   h_separator = HorizontalSeparator()
   h_separator.setFixedHeight(2)

VerticalSeparator
~~~~~~~~~~~~~~~~
垂直分隔符。

.. code-block:: python

   v_separator = VerticalSeparator()
   v_separator.setFixedWidth(2)

弹出组件 (Popup Components)
---------------------------

Flyout
~~~~~~
弹出框。

.. code-block:: python

   flyout = Flyout.create(
       target=button,
       title='弹出框',
       content='这是弹出内容',
       isClosable=True
   )

FlipView
~~~~~~~~
翻转视图。

.. code-block:: python

   flip_view = FlipView()
   flip_view.addWidget(widget1)
   flip_view.addWidget(widget2)

命令栏组件 (Command Bar Components)
----------------------------------

CommandBar
~~~~~~~~~~
命令栏。

.. code-block:: python

   command_bar = CommandBar()
   command_bar.addAction('命令1')
   command_bar.addAction('命令2')

VerticalCommandBar
~~~~~~~~~~~~~~~~~~~
垂直命令栏。

.. code-block:: python

   v_command_bar = VerticalCommandBar()
   v_command_bar.addAction('垂直命令')

ResponsiveCommandBar
~~~~~~~~~~~~~~~~~~~~
响应式命令栏。

.. code-block:: python

   responsive_bar = ResponsiveCommandBar()
   responsive_bar.addAction('响应式命令')

工具面板组件 (Tool Panel Components)
------------------------------------

ToolPanel
~~~~~~~~~
工具面板。

.. code-block:: python

   tool_panel = ToolPanel()
   tool_panel.addWidget(QPushButton('工具1'))

VerticalToolPanel
~~~~~~~~~~~~~~~~~
垂直工具面板。

.. code-block:: python

   v_tool_panel = VerticalToolPanel()
   v_tool_panel.addWidget(QPushButton('垂直工具'))

堆叠组件 (Stacked Components)
------------------------------

PopUpAniStackedWidget
~~~~~~~~~~~~~~~~~~~~~~
弹出动画堆叠控件。

.. code-block:: python

   stacked = PopUpAniStackedWidget()
   stacked.addWidget(widget1)
   stacked.addWidget(widget2)

OpacityAniStackedWidget
~~~~~~~~~~~~~~~~~~~~~~
透明度动画堆叠控件。

.. code-block:: python

   opacity_stacked = OpacityAniStackedWidget()
   opacity_stacked.addWidget(widget1)
   opacity_stacked.addWidget(widget2)

TransitionStackedWidget
~~~~~~~~~~~~~~~~~~~~~~
过渡动画堆叠控件。

.. code-block:: python

   transition_stacked = TransitionStackedWidget()
   transition_stacked.addWidget(widget1)
   transition_stacked.addWidget(widget2)

图标组件 (Icon Components)
--------------------------

IconWidget
~~~~~~~~~~
图标控件。

.. code-block:: python

   icon_widget = IconWidget(FluentIcon.HOME)
   icon_widget.setFixedSize(32, 32)

工具提示组件 (Tooltip Components)
---------------------------------

ToolTip
~~~~~~~
工具提示。

.. code-block:: python

   tooltip = ToolTip('这是工具提示')
   button.setToolTip(tooltip)

完整示例
--------

下面是一个完整的基础控件使用示例：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QGroupBox
   from PySide6.QtCore import Qt
   from qfluentwidgets import *

   class WidgetsDemoWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           
           self.setWindowTitle('基础控件示例')
           self.resize(1000, 800)
           
           self.setup_ui()

       def setup_ui(self):
           """设置界面"""
           central_widget = QWidget()
           self.setCentralWidget(central_widget)
           
           layout = QVBoxLayout(central_widget)
           layout.setSpacing(20)
           layout.setContentsMargins(20, 20, 20, 20)
           
           # 添加各种控件组
           self.add_button_group(layout)
           self.add_input_group(layout)
           self.add_progress_group(layout)
           self.add_info_group(layout)

       def add_button_group(self, layout):
           """添加按钮组"""
           group = QGroupBox('按钮组件')
           group_layout = QVBoxLayout(group)
           
           # 按钮行
           button_row1 = QHBoxLayout()
           button_row1.addWidget(PrimaryPushButton('主要按钮'))
           button_row1.addWidget(PushButton('普通按钮'))
           button_row1.addWidget(PushButton('危险按钮'))
           group_layout.addLayout(button_row1)
           
           # 特殊按钮行
           button_row2 = QHBoxLayout()
           button_row2.addWidget(ToggleButton('切换按钮'))
           button_row2.addWidget(PillPushButton('胶囊按钮'))
           button_row2.addWidget(HyperlinkButton('https://example.com', '链接'))
           group_layout.addLayout(button_row2)
           
           layout.addWidget(group)

       def add_input_group(self, layout):
           """添加输入组件组"""
           group = QGroupBox('输入组件')
           group_layout = QVBoxLayout(group)
           
           # 输入框行
           input_row1 = QHBoxLayout()
           input_row1.addWidget(QLabel('文本框:'))
           input_row1.addWidget(LineEdit())
           input_row1.addWidget(QLabel('搜索框:'))
           input_row1.addWidget(SearchLineEdit())
           group_layout.addLayout(input_row1)
           
           # 选择组件行
           input_row2 = QHBoxLayout()
           input_row2.addWidget(QLabel('下拉框:'))
           input_row2.addWidget(ComboBox())
           input_row2.addWidget(QLabel('数值框:'))
           input_row2.addWidget(SpinBox())
           group_layout.addLayout(input_row2)
           
           # 复选框行
           input_row3 = QHBoxLayout()
           input_row3.addWidget(CheckBox('复选框'))
           input_row3.addWidget(RadioButton('单选框'))
           input_row3.addWidget(SwitchButton())
           group_layout.addLayout(input_row3)
           
           layout.addWidget(group)

       def add_progress_group(self, layout):
           """添加进度组件组"""
           group = QGroupBox('进度组件')
           group_layout = QVBoxLayout(group)
           
           # 进度条行
           progress_row1 = QHBoxLayout()
           progress_row1.addWidget(QLabel('进度条:'))
           progress_row1.addWidget(ProgressBar())
           progress_row1.addWidget(QLabel('环形进度:'))
           progress_row1.addWidget(ProgressRing())
           group_layout.addLayout(progress_row1)
           
           # 滑块行
           slider_row = QHBoxLayout()
           slider_row.addWidget(QLabel('滑块:'))
           slider_row.addWidget(Slider())
           group_layout.addLayout(slider_row)
           
           layout.addWidget(group)

       def add_info_group(self, layout):
           """添加信息组件组"""
           group = QGroupBox('信息组件')
           group_layout = QVBoxLayout(group)
           
           # 信息徽章行
           info_row1 = QHBoxLayout()
           info_row1.addWidget(QLabel('徽章:'))
           info_row1.addWidget(InfoBadge.success())
           info_row1.addWidget(InfoBadge.info())
           info_row1.addWidget(InfoBadge.warning())
           group_layout.addLayout(info_row1)
           
           # 标签行
           label_row = QHBoxLayout()
           label_row.addWidget(CaptionLabel('说明标签'))
           label_row.addWidget(BodyLabel('正文标签'))
           label_row.addWidget(SubtitleLabel('副标题'))
           group_layout.addLayout(label_row)
           
           layout.addWidget(group)

   if __name__ == '__main__':
       app = QApplication(sys.argv)
       window = WidgetsDemoWindow()
       window.show()
       sys.exit(app.exec())

最佳实践
--------

1. **控件选择**: 根据功能需求选择合适的控件
2. **布局管理**: 使用Qt布局管理器组织控件
3. **信号连接**: 合理使用信号槽机制处理交互
4. **样式统一**: 保持控件样式的一致性
5. **响应式设计**: 确保界面在不同尺寸下正常显示

样式自定义
--------

可以通过QSS自定义控件样式：

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
