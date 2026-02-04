项目介绍
========

PySide6-Fluent-Widgets 是一个基于 PySide6 的 Fluent Design 风格组件库。
它提供了丰富的现代化 UI 组件，帮助开发者快速构建美观的应用程序。

什么是 Fluent Design？
--------------------

Fluent Design 是 Microsoft 推出的现代化设计语言，具有以下特点：

* **光照**: 使用光影效果创造深度和层次感
* **材质**: 采用真实的材质纹理
* **深度**: 通过空间和层次创造立体感
* **动画**: 流畅的过渡动画提升用户体验
* **缩放**: 适应不同屏幕尺寸的响应式设计

为什么选择 PySide6-Fluent-Widgets？
----------------------------------

* **现代化外观**: 符合当前设计趋势的 UI 组件
* **完整组件库**: 涵盖常用 UI 组件，无需额外开发
* **主题支持**: 内置亮色/暗色主题，支持系统主题自动切换
* **易于集成**: 简单的 API 设计，快速上手
* **跨平台**: 支持 Windows、Linux、macOS
* **开源免费**: LGPLv3 协议，商业友好

安装方法
--------

使用 pip 安装：

.. code-block:: bash

   pip install PySide6-Fluent-Widgets

或者从源码安装：

.. code-block:: bash

   git clone https://github.com/zhiyiYo/PyQt-Fluent-Widgets.git
   cd PyQt-Fluent-Widgets
   pip install -r requirements.txt
   python setup.py install

系统要求
--------

* Python 3.8+
* PySide6 6.4.2+
* 支持 Windows、Linux、macOS

快速开始
--------

基本用法示例：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
   from qfluentwidgets import *

   class MainWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           
           # 创建中央窗口
           self.central_widget = QWidget()
           self.setCentralWidget(self.central_widget)
           
           # 创建布局
           layout = QVBoxLayout(self.central_widget)
           
           # 添加组件
           button = PushButton('点击我')
           line_edit = LineEdit()
           progress_bar = ProgressBar()
           
           layout.addWidget(button)
           layout.addWidget(line_edit)
           layout.addWidget(progress_bar)
           
           # 连接信号
           button.clicked.connect(self.on_button_clicked)
           
           self.setWindowTitle('PySide6-Fluent-Widgets 示例')
           self.resize(400, 300)

       def on_button_clicked(self):
           InfoBar.info(
               title='提示',
               content='按钮被点击了！',
               orient=Qt.Horizontal,
               isClosable=True,
               position=InfoBarPosition.TOP,
               duration=3000,
               parent=self
           )

   if __name__ == '__main__':
       app = QApplication(sys.argv)
       window = MainWindow()
       window.show()
       sys.exit(app.exec())

主题设置
--------

PySide6-Fluent-Widgets 支持多种主题模式：

.. code-block:: python

   from qfluentwidgets import setTheme, Theme, isDarkTheme

   # 设置亮色主题
   setTheme(Theme.LIGHT)
   
   # 设置暗色主题
   setTheme(Theme.DARK)
   
   # 跟随系统主题
   setTheme(Theme.AUTO)
   
   # 检查当前是否为暗色主题
   if isDarkTheme():
       print("当前为暗色主题")

常见问题
--------

**Q: 如何自定义组件颜色？**

A: 可以使用 QSS 样式表或者主题配置：

.. code-block:: python

   # 使用 QSS
   button.setStyleSheet("PushButton { background-color: #0078d4; }")
   
   # 使用主题配置
   from qfluentwidgets import setThemeColor
   setThemeColor('#0078d4')

**Q: 如何支持中文？**

A: 确保应用程序设置了正确的编码和字体：

.. code-block:: python

   import sys
   from PySide6.QtCore import QLocale
   
   # 设置中文本地化
   QLocale.setDefault(QLocale.Chinese)

**Q: 如何在现有项目中集成？**

A: 只需要导入需要的组件即可：

.. code-block:: python

   from qfluentwidgets import PushButton, LineEdit, ComboBox
   # 然后像普通 PySide6 组件一样使用

下一步
------

* 阅读 :doc:`architecture` 了解项目架构
* 查看 :doc:`components/index` 学习各组件的使用方法
* 参考 :doc:`examples/index` 中的示例代码
* 浏览 :doc:`api/index` 查看完整的 API 文档
