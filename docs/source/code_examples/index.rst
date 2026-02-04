示例代码
=========

本节提供了丰富的示例代码，帮助您快速掌握 PySide6-Fluent-Widgets 的使用方法。

.. toctree::
   :maxdepth: 2
   :caption: 示例

   quick_start
   basic_components
   navigation_example
   dialog_example
   settings_example
   theme_example
   custom_component

快速开始示例
------------

下面是一个完整的快速开始示例：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
   from qfluentwidgets import *

   class MainWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           
           # 设置窗口属性
           self.setWindowTitle('PySide6-Fluent-Widgets 示例')
           self.resize(800, 600)
           
           # 创建中央窗口
           self.central_widget = QWidget()
           self.setCentralWidget(self.central_widget)
           
           # 创建布局
           layout = QVBoxLayout(self.central_widget)
           
           # 添加标题
           title = SubtitleLabel('PySide6-Fluent-Widgets 示例')
           layout.addWidget(title)
           
           # 创建按钮组
           button_layout = QHBoxLayout()
           
           primary_btn = PrimaryPushButton('主要按钮')
           secondary_btn = PushButton('次要按钮')
           danger_btn = PushButton('危险按钮')
           
           button_layout.addWidget(primary_btn)
           button_layout.addWidget(secondary_btn)
           button_layout.addWidget(danger_btn)
           
           layout.addLayout(button_layout)
           
           # 创建输入框
           line_edit = LineEdit()
           line_edit.setPlaceholderText('请输入文本...')
           layout.addWidget(line_edit)
           
           # 创建进度条
           progress_bar = ProgressBar()
           progress_bar.setValue(70)
           layout.addWidget(progress_bar)
           
           # 创建开关
           switch = Switch()
           switch.setText('启用通知')
           layout.addWidget(switch)
           
           # 连接信号
           primary_btn.clicked.connect(self.show_success_info)
           secondary_btn.clicked.connect(self.show_info)
           danger_btn.clicked.connect(self.show_warning)

       def show_success_info(self):
           InfoBar.success(
               title='成功',
               content='主要按钮被点击了！',
               orient=Qt.Horizontal,
               isClosable=True,
               position=InfoBarPosition.TOP,
               duration=3000,
               parent=self
           )

       def show_info(self):
           InfoBar.info(
               title='提示',
               content='次要按钮被点击了！',
               orient=Qt.Horizontal,
               isClosable=True,
               position=InfoBarPosition.TOP,
               duration=3000,
               parent=self
           )

       def show_warning(self):
           InfoBar.warning(
               title='警告',
               content='危险按钮被点击了！',
               orient=Qt.Horizontal,
               isClosable=True,
               position=InfoBarPosition.TOP,
               duration=3000,
               parent=self
           )

   if __name__ == '__main__':
       app = QApplication(sys.argv)
       
       # 设置主题
       setTheme(Theme.AUTO)
       
       window = MainWindow()
       window.show()
       sys.exit(app.exec())

运行示例
--------

要运行这些示例，请确保已安装 PySide6-Fluent-Widgets：

.. code-block:: bash

   pip install PySide6-Fluent-Widgets

然后将示例代码保存为 `.py` 文件并运行：

.. code-block:: bash

   python example.py

更多示例
--------

* **基础组件示例**: 展示各种基础控件的使用方法
* **导航示例**: 演示导航组件的使用
* **对话框示例**: 展示各种对话框的使用
* **设置示例**: 演示设置界面的构建
* **主题示例**: 展示主题切换和自定义
* **自定义组件示例**: 演示如何创建自定义组件

最佳实践
--------

1. **主题设置**: 在应用启动时设置主题
2. **布局管理**: 使用 Qt 布局管理器而不是固定位置
3. **信号连接**: 合理使用信号槽机制
4. **样式自定义**: 优先使用主题 API 而不是直接设置 QSS
5. **国际化**: 支持多语言文本

常见问题
--------

**Q: 如何让组件支持暗色主题？**

A: 组件会自动适配主题，只需要设置应用主题即可：

.. code-block:: python

   from qfluentwidgets import setTheme, Theme
   setTheme(Theme.DARK)

**Q: 如何自定义组件大小？**

A: 使用 `setFixedSize()` 或 `resize()` 方法：

.. code-block:: python

   button.setFixedSize(120, 32)
   button.resize(200, 50)

**Q: 如何禁用组件？**

A: 使用 `setEnabled(False)` 方法：

.. code-block:: python

   button.setEnabled(False)

**Q: 如何设置工具提示？**

A: 使用 `setToolTip()` 方法：

.. code-block:: python

   button.setToolTip('这是一个按钮')
