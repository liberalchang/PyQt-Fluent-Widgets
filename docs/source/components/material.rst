材质设计组件 (Material)
=======================

本节介绍 PySide6-Fluent-Widgets 中的材质设计相关组件。

AcrylicWidget
------------

亚克力效果的基础组件，提供毛玻璃背景效果。

.. code-block:: python

   from qfluentwidgets import AcrylicWidget
   from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton

   # 创建亚克力组件
   acrylic = AcrylicWidget()
   acrylic.setFixedHeight(200)
   
   # 添加内容
   layout = QVBoxLayout(acrylic)
   layout.addWidget(QLabel('亚克力效果'))
   layout.addWidget(QPushButton('按钮'))

AcrylicLabel
------------

带亚克力效果的标签组件。

.. code-block:: python

   from qfluentwidgets import AcrylicLabel

   # 创建亚克力标签
   label = AcrylicLabel('亚克力标签')
   label.setFixedHeight(50)
   label.setStyleSheet('color: white; font-size: 16px;')

AcrylicLineEdit
--------------

带亚克力效果的输入框。

.. code-block:: python

   from qfluentwidgets import AcrylicLineEdit

   # 创建亚克力输入框
   line_edit = AcrylicLineEdit()
   line_edit.setPlaceholderText('请输入文本...')
   line_edit.setFixedHeight(40)

AcrylicComboBox
---------------

带亚克力效果的下拉框。

.. code-block:: python

   from qfluentwidgets import AcrylicComboBox

   # 创建亚克力下拉框
   combo = AcrylicComboBox()
   combo.addItems(['选项1', '选项2', '选项3'])
   combo.setFixedHeight(40)

AcrylicMenu
-----------

带亚克力效果的菜单。

.. code-block:: python

   from qfluentwidgets import AcrylicMenu
   from PySide6.QtWidgets import QPushButton, QApplication

   # 创建亚克力菜单
   menu = AcrylicMenu()
   menu.addAction('菜单项1')
   menu.addAction('菜单项2')
   menu.addSeparator()
   menu.addAction('退出')
   
   # 创建按钮显示菜单
   button = QPushButton('菜单')
   button.setMenu(menu)

AcrylicFlyout
-------------

亚克力弹出框组件。

.. code-block:: python

   from qfluentwidgets import AcrylicFlyout
   from PySide6.QtWidgets import QLabel, QVBoxLayout, QPushButton

   # 创建亚克力弹出框
   flyout = AcrylicFlyout()
   
   # 添加内容
   content = QWidget()
   layout = QVBoxLayout(content)
   layout.addWidget(QLabel('弹出框内容'))
   layout.addWidget(QPushButton('确定'))
   
   flyout.setWidget(content)
   
   # 显示弹出框
   flyout.show(button)

AcrylicToolTip
--------------

带亚克力效果的工具提示。

.. code-block:: python

   from qfluentwidgets import AcrylicToolTip

   # 创建亚克力工具提示
   tooltip = AcrylicToolTip('这是一个亚克力工具提示')
   
   # 设置到控件
   button = QPushButton('按钮')
   button.setToolTip(tooltip)

完整示例
--------

下面是一个完整的材质设计组件使用示例：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                                QWidget, QLabel, QPushButton, ScrollArea)
   from PySide6.QtCore import Qt
   from qfluentwidgets import *

   class MaterialDemoWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           
           self.setWindowTitle('材质设计组件示例')
           self.resize(800, 600)
           
           # 设置背景图片（亚克力效果需要背景）
           self.setStyleSheet("""
               QMainWindow {
                   background-image: url('background.jpg');
                   background-position: center;
                   background-repeat: no-repeat;
               }
           """)
           
           # 创建界面
           self.setup_ui()

       def setup_ui(self):
           """设置界面"""
           # 创建滚动区域
           scroll_area = ScrollArea()
           scroll_area.setWidgetResizable(True)
           scroll_area.setFrameShape(ScrollArea.NoFrame)
           
           # 创建主容器
           container = QWidget()
           container_layout = QVBoxLayout(container)
           container_layout.setSpacing(20)
           container_layout.setContentsMargins(20, 20, 20, 20)
           
           # 添加标题
           title = AcrylicLabel('材质设计组件')
           title.setAlignment(Qt.AlignCenter)
           title.setStyleSheet('color: white; font-size: 24px; font-weight: bold;')
           title.setFixedHeight(60)
           container_layout.addWidget(title)
           
           # 添加各种亚克力组件
           self.add_acrylic_widgets(container_layout)
           
           # 添加亚克力菜单示例
           self.add_menu_example(container_layout)
           
           # 添加亚克力弹出框示例
           self.add_flyout_example(container_layout)
           
           # 添加弹性空间
           container_layout.addStretch()
           
           scroll_area.setWidget(container)
           self.setCentralWidget(scroll_area)

       def add_acrylic_widgets(self, layout):
           """添加亚克力组件"""
           group = QWidget()
           group_layout = QVBoxLayout(group)
           group_layout.setSpacing(10)
           
           # 亚克力标签
           label = AcrylicLabel('亚克力标签组件')
           label.setStyleSheet('color: white; font-size: 16px; padding: 10px;')
           label.setFixedHeight(50)
           group_layout.addWidget(label)
           
           # 亚克力输入框
           line_edit = AcrylicLineEdit()
           line_edit.setPlaceholderText('请输入文本...')
           line_edit.setFixedHeight(40)
           group_layout.addWidget(line_edit)
           
           # 亚克力下拉框
           combo = AcrylicComboBox()
           combo.addItems(['选项1', '选项2', '选项3'])
           combo.setFixedHeight(40)
           group_layout.addWidget(combo)
           
           # 亚克力容器
           acrylic_widget = AcrylicWidget()
           acrylic_widget.setFixedHeight(100)
           widget_layout = QVBoxLayout(acrylic_widget)
           widget_layout.addWidget(QLabel('亚克力容器'))
           widget_layout.addWidget(QPushButton('内部按钮'))
           group_layout.addWidget(acrylic_widget)
           
           layout.addWidget(group)

       def add_menu_example(self, layout):
           """添加菜单示例"""
           group = QWidget()
           group_layout = QVBoxLayout(group)
           group_layout.setSpacing(10)
           
           label = QLabel('亚克力菜单示例:')
           label.setStyleSheet('color: white; font-size: 14px;')
           group_layout.addWidget(label)
           
           # 创建亚克力菜单
           menu = AcrylicMenu()
           menu.addAction('新建文件')
           menu.addAction('打开文件')
           menu.addAction('保存文件')
           menu.addSeparator()
           menu.addAction('退出')
           
           # 创建按钮显示菜单
           menu_button = QPushButton('显示菜单')
           menu_button.setMenu(menu)
           menu_button.setFixedHeight(40)
           group_layout.addWidget(menu_button)
           
           layout.addWidget(group)

       def add_flyout_example(self, layout):
           """添加弹出框示例"""
           group = QWidget()
           group_layout = QVBoxLayout(group)
           group_layout.setSpacing(10)
           
           label = QLabel('亚克力弹出框示例:')
           label.setStyleSheet('color: white; font-size: 14px;')
           group_layout.addWidget(label)
           
           # 创建弹出框按钮
           flyout_button = QPushButton('显示弹出框')
           flyout_button.setFixedHeight(40)
           flyout_button.clicked.connect(self.show_flyout)
           group_layout.addWidget(flyout_button)
           
           layout.addWidget(group)

       def show_flyout(self):
           """显示弹出框"""
           # 创建亚克力弹出框
           flyout = AcrylicFlyout()
           
           # 添加内容
           content = QWidget()
           content.setFixedSize(300, 200)
           content_layout = QVBoxLayout(content)
           
           title = QLabel('弹出框标题')
           title.setStyleSheet('color: white; font-size: 16px; font-weight: bold;')
           content_layout.addWidget(title)
           
           message = QLabel('这是一个亚克力弹出框示例')
           message.setStyleSheet('color: white; font-size: 14px;')
           message.setWordWrap(True)
           content_layout.addWidget(message)
           
           button_layout = QHBoxLayout()
           ok_button = QPushButton('确定')
           cancel_button = QPushButton('取消')
           
           button_layout.addWidget(ok_button)
           button_layout.addWidget(cancel_button)
           content_layout.addLayout(button_layout)
           
           flyout.setWidget(content)
           
           # 显示弹出框
           flyout.show(self.sender())

   if __name__ == '__main__':
       app = QApplication(sys.argv)
       window = MaterialDemoWindow()
       window.show()
       sys.exit(app.exec())

最佳实践
--------

1. **背景设置**: 
   - 亚克力效果需要适当的背景图片或颜色
   - 使用高对比度的背景以获得最佳效果

2. **性能考虑**: 
   - 亚克力效果会增加渲染开销
   - 在大量使用时注意性能影响

3. **主题适配**: 
   - 亚克力组件会自动适配主题
   - 在暗色主题下效果更佳

4. **使用场景**: 
   - 适用于现代化界面设计
   - 常用于侧边栏、工具栏、弹出框等

样式自定义
--------

可以通过 QSS 自定义亚克力组件样式：

.. code-block:: python

   # 自定义亚克力样式
   acrylic_widget.setStyleSheet("""
       AcrylicWidget {
           background-color: rgba(255, 255, 255, 0.1);
           border: 1px solid rgba(255, 255, 255, 0.2);
           border-radius: 8px;
           backdrop-filter: blur(10px);
       }
       
       AcrylicLabel {
           background-color: rgba(255, 255, 255, 0.1);
           color: white;
           padding: 8px 16px;
           border-radius: 4px;
       }
       
       AcrylicLineEdit {
           background-color: rgba(255, 255, 255, 0.1);
           color: white;
           border: 1px solid rgba(255, 255, 255, 0.3);
           border-radius: 4px;
           padding: 8px;
       }
       
       AcrylicLineEdit::placeholder {
           color: rgba(255, 255, 255, 0.7);
       }
   """)
