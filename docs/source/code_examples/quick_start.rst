快速开始示例
=============

这是一个完整的 PySide6-Fluent-Widgets 快速开始示例，展示了如何创建一个现代化的应用程序界面。

.. code-block:: python

   import sys
   from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QLabel
   from PySide6.QtCore import Qt
   from qfluentwidgets import *

   class MainWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           
           # 设置窗口属性
           self.setWindowTitle('PySide6-Fluent-Widgets 示例')
           self.resize(900, 700)
           
           # 设置主题
           setTheme(Theme.AUTO)
           
           # 创建主界面
           self.setup_ui()

       def setup_ui(self):
           """设置主界面"""
           central_widget = QWidget()
           self.setCentralWidget(central_widget)
           
           layout = QVBoxLayout(central_widget)
           layout.setSpacing(20)
           layout.setContentsMargins(30, 30, 30, 30)
           
           # 添加标题
           title = SubtitleLabel('PySide6-Fluent-Widgets 示例应用')
           title.setAlignment(Qt.AlignCenter)
           layout.addWidget(title)
           
           # 添加分隔线
           layout.addWidget(Separator())
           
           # 添加各种组件示例
           self.add_button_examples(layout)
           self.add_input_examples(layout)
           self.add_progress_examples(layout)
           self.add_info_bar_example(layout)

       def add_button_examples(self, layout):
           """添加按钮示例"""
           group = QGroupBox('按钮组件')
           group_layout = QVBoxLayout(group)
           
           # 按钮行
           button_row1 = QHBoxLayout()
           
           primary_btn = PrimaryPushButton('主要按钮')
           primary_btn.clicked.connect(lambda: self.show_info('主要按钮被点击'))
           
           secondary_btn = PushButton('次要按钮')
           secondary_btn.clicked.connect(lambda: self.show_info('次要按钮被点击'))
           
           danger_btn = PushButton('危险按钮')
           danger_btn.clicked.connect(lambda: self.show_warning('危险按钮被点击'))
           
           button_row1.addWidget(primary_btn)
           button_row1.addWidget(secondary_btn)
           button_row1.addWidget(danger_btn)
           
           # 第二行按钮
           button_row2 = QHBoxLayout()
           
           dropdown_btn = DropDownButton('下拉菜单')
           dropdown_btn.addAction(Action(FluentIcon.COPY, '复制'))
           dropdown_btn.addAction(Action(FluentIcon.PASTE, '粘贴'))
           dropdown_btn.addAction(Action(FluentIcon.CUT, '剪切'))
           
           hyperlink_btn = HyperlinkButton('https://github.com', '访问 GitHub')
           
           button_row2.addWidget(dropdown_btn)
           button_row2.addWidget(hyperlink_btn)
           button_row2.addStretch()
           
           group_layout.addLayout(button_row1)
           group_layout.addLayout(button_row2)
           
           layout.addWidget(group)

       def add_input_examples(self, layout):
           """添加输入组件示例"""
           group = QGroupBox('输入组件')
           group_layout = QVBoxLayout(group)
           
           # 输入框行
           input_row1 = QHBoxLayout()
           
           line_edit = LineEdit()
           line_edit.setPlaceholderText('请输入文本...')
           line_edit.setFixedWidth(200)
           
           search_edit = LineEdit()
           search_edit.setPlaceholderText('搜索...')
           search_edit.setFixedWidth(200)
           
           input_row1.addWidget(QLabel('文本输入:'))
           input_row1.addWidget(line_edit)
           input_row1.addWidget(QLabel('搜索框:'))
           input_row1.addWidget(search_edit)
           input_row1.addStretch()
           
           # 选择组件行
           input_row2 = QHBoxLayout()
           
           combo_box = ComboBox()
           combo_box.addItems(['选项1', '选项2', '选项3'])
           combo_box.setFixedWidth(150)
           
           spin_box = SpinBox()
           spin_box.setRange(0, 100)
           spin_box.setValue(50)
           spin_box.setFixedWidth(100)
           
           input_row2.addWidget(QLabel('下拉框:'))
           input_row2.addWidget(combo_box)
           input_row2.addWidget(QLabel('数字输入:'))
           input_row2.addWidget(spin_box)
           input_row2.addStretch()
           
           # 开关和复选框行
           input_row3 = QHBoxLayout()
           
           switch = Switch()
           switch.setText('启用通知')
           switch.setChecked(True)
           
           checkbox = CheckBox('记住密码')
           checkbox.setChecked(False)
           
           radio1 = RadioButton('选项A')
           radio2 = RadioButton('选项B')
           
           input_row3.addWidget(switch)
           input_row3.addWidget(checkbox)
           input_row3.addWidget(radio1)
           input_row3.addWidget(radio2)
           input_row3.addStretch()
           
           group_layout.addLayout(input_row1)
           group_layout.addLayout(input_row2)
           group_layout.addLayout(input_row3)
           
           layout.addWidget(group)

       def add_progress_examples(self, layout):
           """添加进度组件示例"""
           group = QGroupBox('进度组件')
           group_layout = QVBoxLayout(group)
           
           # 进度条行
           progress_row1 = QHBoxLayout()
           
           progress_bar = ProgressBar()
           progress_bar.setRange(0, 100)
           progress_bar.setValue(65)
           
           progress_ring = ProgressRing()
           progress_ring.setFixedSize(50, 50)
           progress_ring.setValue(75)
           
           progress_row1.addWidget(QLabel('进度条:'))
           progress_row1.addWidget(progress_bar)
           progress_row1.addWidget(QLabel('环形进度:'))
           progress_row1.addWidget(progress_ring)
           progress_row1.addStretch()
           
           # 滑块行
           slider_row = QHBoxLayout()
           
           slider = Slider()
           slider.setRange(0, 100)
           slider.setValue(30)
           slider.setFixedWidth(200)
           
           self.slider_value_label = QLabel('30')
           
           slider.valueChanged.connect(lambda v: self.slider_value_label.setText(str(v)))
           
           slider_row.addWidget(QLabel('滑块:'))
           slider_row.addWidget(slider)
           slider_row.addWidget(self.slider_value_label)
           slider_row.addStretch()
           
           group_layout.addLayout(progress_row1)
           group_layout.addLayout(slider_row)
           
           layout.addWidget(group)

       def add_info_bar_example(self, layout):
           """添加信息栏示例"""
           group = QGroupBox('信息提示')
           group_layout = QVBoxLayout(group)
           
           # 信息提示按钮行
           info_row = QHBoxLayout()
           
           success_btn = PushButton('成功提示')
           success_btn.clicked.connect(lambda: self.show_success('操作成功完成'))
           
           info_btn = PushButton('信息提示')
           info_btn.clicked.connect(lambda: self.show_info('这是一条信息'))
           
           warning_btn = PushButton('警告提示')
           warning_btn.clicked.connect(lambda: self.show_warning('请注意潜在风险'))
           
           error_btn = PushButton('错误提示')
           error_btn.clicked.connect(lambda: self.show_error('发生了错误'))
           
           info_row.addWidget(success_btn)
           info_row.addWidget(info_btn)
           info_row.addWidget(warning_btn)
           info_row.addWidget(error_btn)
           
           group_layout.addLayout(info_row)
           
           layout.addWidget(group)

       def show_success(self, message):
           """显示成功信息"""
           InfoBar.success(
               title='成功',
               content=message,
               orient=Qt.Horizontal,
               isClosable=True,
               position=InfoBarPosition.TOP,
               duration=3000,
               parent=self
           )

       def show_info(self, message):
           """显示信息"""
           InfoBar.info(
               title='提示',
               content=message,
               orient=Qt.Horizontal,
               isClosable=True,
               position=InfoBarPosition.TOP,
               duration=3000,
               parent=self
           )

       def show_warning(self, message):
           """显示警告信息"""
           InfoBar.warning(
               title='警告',
               content=message,
               orient=Qt.Horizontal,
               isClosable=True,
               position=InfoBarPosition.TOP,
               duration=3000,
               parent=self
           )

       def show_error(self, message):
           """显示错误信息"""
           InfoBar.error(
               title='错误',
               content=message,
               orient=Qt.Horizontal,
               isClosable=True,
               position=InfoBarPosition.TOP,
               duration=3000,
               parent=self
           )

   if __name__ == '__main__':
       app = QApplication(sys.argv)
       
       # 设置应用程序属性
       app.setApplicationName('PySide6-Fluent-Widgets 示例')
       app.setOrganizationName('示例公司')
       
       # 创建并显示主窗口
       window = MainWindow()
       window.show()
       
       # 运行应用程序
       sys.exit(app.exec())

运行方法
--------

1. 确保已安装 PySide6-Fluent-Widgets：

.. code-block:: bash

   pip install PySide6-Fluent-Widgets

2. 将上述代码保存为 `example.py`

3. 运行程序：

.. code-block:: bash

   python example.py

功能特点
--------

这个示例展示了以下功能：

- **主题支持**: 自动适配系统主题
- **现代化按钮**: 主要按钮、次要按钮、下拉按钮等
- **输入组件**: 文本框、搜索框、下拉框、数字输入等
- **选择组件**: 开关、复选框、单选按钮等
- **进度组件**: 进度条、环形进度、滑块等
- **信息提示**: 成功、信息、警告、错误提示
- **响应式布局**: 使用 Qt 布局管理器
- **中文支持**: 完整的中文界面

扩展建议
--------

基于这个示例，您可以：

1. 添加更多组件示例（表格、图表、对话框等）
2. 实现数据持久化
3. 添加主题切换功能
4. 集成网络功能
5. 添加多语言支持
6. 实现插件系统
