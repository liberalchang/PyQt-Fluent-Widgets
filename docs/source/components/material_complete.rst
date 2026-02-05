材质设计组件 (Material)
=======================

本节介绍 PySide6-Fluent-Widgets 中的材质设计相关组件。

AcrylicMenu
-----------

亚克力菜单，带毛玻璃效果的菜单。

.. code-block:: python

   from qfluentwidgets import AcrylicMenu

   # 创建亚克力菜单
   menu = AcrylicMenu()
   menu.addAction('菜单项1')
   menu.addAction('菜单项2')
   menu.addSeparator()
   menu.addAction('退出')
   
   # 创建按钮显示菜单
   button = QPushButton('菜单')
   button.setMenu(menu)

AcrylicLineEditMenu
-------------------

亚克力行编辑菜单。

.. code-block:: python

   from qfluentwidgets import AcrylicLineEditMenu

   # 创建亚克力行编辑菜单
   menu = AcrylicLineEditMenu()
   menu.addAction('剪切')
   menu.addAction('复制')
   menu.addAction('粘贴')

AcrylicCheckableMenu
--------------------

可勾选的亚克力菜单。

.. code-block:: python

   from qfluentwidgets import AcrylicCheckableMenu

   # 创建可勾选亚克力菜单
   menu = AcrylicCheckableMenu()
   menu.addAction('选项1').setCheckable(True)
   menu.addAction('选项2').setCheckable(True)

AcrylicCheckableSystemTrayMenu
------------------------------

可勾选的亚克力系统托盘菜单。

.. code-block:: python

   from qfluentwidgets import AcrylicCheckableSystemTrayMenu

   # 创建可勾选亚克力系统托盘菜单
   menu = AcrylicCheckableSystemTrayMenu()
   menu.addAction('显示').setCheckable(True)
   menu.addAction('静音').setCheckable(True)

AcrylicSystemTrayMenu
----------------------

亚克力系统托盘菜单。

.. code-block:: python

   from qfluentwidgets import AcrylicSystemTrayMenu

   # 创建亚克力系统托盘菜单
   menu = AcrylicSystemTrayMenu()
   menu.addAction('打开')
   menu.addAction('退出')

AcrylicLineEditBase
-------------------

亚克力行编辑基础类。

.. code-block:: python

   from qfluentwidgets import AcrylicLineEditBase

   # 创建自定义亚克力行编辑
   class CustomAcrylicLineEdit(AcrylicLineEditBase):
       def __init__(self, parent=None):
           super().__init__(parent)
           # 自定义实现

AcrylicLineEdit
--------------

亚克力行编辑框。

.. code-block:: python

   from qfluentwidgets import AcrylicLineEdit

   # 创建亚克力行编辑框
   line_edit = AcrylicLineEdit()
   line_edit.setPlaceholderText('请输入文本...')
   line_edit.setFixedHeight(40)

AcrylicSearchLineEdit
---------------------

亚克力搜索行编辑框。

.. code-block:: python

   from qfluentwidgets import AcrylicSearchLineEdit

   # 创建亚克力搜索框
   search_edit = AcrylicSearchLineEdit()
   search_edit.setPlaceholderText('搜索...')
   search_edit.setFixedHeight(40)

AcrylicComboBox
---------------

亚克力下拉框。

.. code-block:: python

   from qfluentwidgets import AcrylicComboBox

   # 创建亚克力下拉框
   combo = AcrylicComboBox()
   combo.addItems(['选项1', '选项2', '选项3'])
   combo.setFixedHeight(40)

AcrylicComboBoxSettingCard
--------------------------

亚克力下拉框设置卡片。

.. code-block:: python

   from qfluentwidgets import AcrylicComboBoxSettingCard

   # 创建亚克力下拉框设置卡片
   card = AcrylicComboBoxSettingCard(
       icon=FluentIcon.LANGUAGE,
       title='语言设置',
       content='选择界面语言'
   )
   card.addItems(['中文', 'English', '日本語'])

AcrylicEditableComboBox
-----------------------

可编辑的亚克力下拉框。

.. code-block:: python

   from qfluentwidgets import AcrylicEditableComboBox

   # 创建可编辑亚克力下拉框
   combo = AcrylicEditableComboBox()
   combo.addItems(['选项1', '选项2', '选项3'])
   combo.setFixedHeight(40)

AcrylicWidget
-------------

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

AcrylicBrush
------------

亚克力画刷。

.. code-block:: python

   from qfluentwidgets import AcrylicBrush

   # 创建亚克力画刷
   brush = AcrylicBrush()
   brush.setColor('#0078d4')
   brush.setOpacity(0.8)

AcrylicFlyoutView
----------------

亚克力弹出视图。

.. code-block:: python

   from qfluentwidgets import AcrylicFlyoutView

   # 创建亚克力弹出视图
   flyout = AcrylicFlyoutView()
   flyout.setFixedSize(300, 200)

AcrylicFlyoutViewBase
--------------------

亚克力弹出视图基础类。

.. code-block:: python

   from qfluentwidgets import AcrylicFlyoutViewBase

   # 创建自定义亚克力弹出视图
   class CustomAcrylicFlyout(AcrylicFlyoutViewBase):
       def __init__(self, parent=None):
           super().__init__(parent)
           # 自定义实现

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

AcrylicToolTipFilter
--------------------

亚克力工具提示过滤器。

.. code-block:: python

   from qfluentwidgets import AcrylicToolTipFilter

   # 创建亚克力工具提示过滤器
   filter = AcrylicToolTipFilter()
   # 应用到控件

完整示例
--------

下面是一个完整的材质设计组件使用示例：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                                QWidget, QLabel, QPushButton, QScrollArea)
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
           scroll_area = QScrollArea()
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
           self.add_acrylic_menus(container_layout)
           self.add_acrylic_flyouts(container_layout)
           
           # 添加弹性空间
           container_layout.addStretch()
           
           scroll_area.setWidget(container)
           self.setCentralWidget(scroll_area)

       def add_acrylic_widgets(self, layout):
           """添加亚克力组件"""
           group = QGroupBox('亚克力组件')
           group_layout = QVBoxLayout(group)
           
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
           
           # 亚克力搜索框
           search_edit = AcrylicSearchLineEdit()
           search_edit.setPlaceholderText('搜索...')
           search_edit.setFixedHeight(40)
           group_layout.addWidget(search_edit)
           
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
           widget_layout.addWidget(QushButton('内部按钮'))
           group_layout.addWidget(acrylic_widget)
           
           layout.addWidget(group)

       def add_acrylic_menus(self, layout):
           """添加亚克力菜单示例"""
           group = QGroupBox('亚克力菜单')
           group_layout = QVBoxLayout(group)
           
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
           
           # 创建可勾选菜单
           checkable_menu = AcrylicCheckableMenu()
           checkable_menu.addAction('显示工具栏').setCheckable(True)
           checkable_menu.addAction('显示状态栏').setCheckable(True)
           
           checkable_button = QPushButton('可勾选菜单')
           checkable_button.setMenu(checkable_menu)
           checkable_button.setFixedHeight(40)
           group_layout.addWidget(checkable_button)
           
           layout.addWidget(group)

       def add_acrylic_flyouts(self, layout):
           """添加亚克力弹出框示例"""
           group = QGroupBox('亚克力弹出框')
           group_layout = QVBoxLayout(group)
           
           label = QLabel('亚克力弹出框示例:')
           label.setStyleSheet('color: white; font-size: 14px;')
           group_layout.addWidget(label)
           
           # 创建弹出框按钮
           flyout_button = QPushButton('显示弹出框')
           flyout_button.setFixedHeight(40)
           flyout_button.clicked.connect(self.show_flyout)
           group_layout.addWidget(flyout_button)
           
           # 亚克力工具提示
           tooltip_button = QPushButton('工具提示')
           tooltip_button.setFixedHeight(40)
           
           tooltip = AcrylicToolTip('这是一个亚克力工具提示')
           tooltip_button.setToolTip(tooltip)
           group_layout.addWidget(tooltip_button)
           
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

组件对比
--------

| 组件 | 用途 | 特点 |
|------|------|------|
| AcrylicWidget | 亚克力容器 | 基础亚克力效果容器 |
| AcrylicLineEdit | 亚克力输入框 | 毛玻璃效果的输入框 |
| AcrylicComboBox | 亚克力下拉框 | 毛玻璃效果的下拉框 |
| AcrylicMenu | 亚克力菜单 | 毛玻璃效果的菜单 |
| AcrylicFlyout | 亚克力弹出框 | 毛玻璃效果的弹出框 |

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
