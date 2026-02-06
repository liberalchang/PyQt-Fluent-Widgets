FramelessWindow 无边框窗口模块
===============================

FramelessWindow 模块提供无边框窗口控件，支持Windows 11的Mica效果和现代化的窗口体验。该模块基于qframelesswindow库，提供了专门为Fluent Design优化的无边框窗口实现。

主要功能
--------

- **无边框设计** - 移除系统默认边框，提供自定义窗口外观
- **Mica效果** - 支持Windows 11的Mica背景效果
- **自定义标题栏** - 可自定义的标题栏和按钮
- **窗口拖拽** - 支持窗口拖拽和调整大小
- **平台适配** - 针对不同Windows版本的自适应

核心组件
--------

FramelessWindow
~~~~~~~~~~~~~~~

无边框窗口控件，提供现代化的窗口体验。

.. code-block:: python

   from qfluentwidgets.components.widgets.frameless_window import FramelessWindow
   from PySide6.QtWidgets import QVBoxLayout, QLabel
   
   # 创建无边框窗口
   window = FramelessWindow()
   
   # 添加内容
   layout = QVBoxLayout()
   layout.addWidget(QLabel("无边框窗口内容"))
   
   # 设置中心控件
   widget = QWidget()
   widget.setLayout(layout)
   window.setCentralWidget(widget)
   
   window.show()

**构造函数：**
- ``FramelessWindow(parent=None)``

**特点：**
- 自动应用Mica效果（Windows 11 22000+）
- 继承自qframelesswindow的AcrylicWindow
- 处理Windows消息以优化标题栏按钮交互
- 支持窗口拖拽和调整大小

**平台兼容性：**
- Windows 11 22000+：完整Mica效果支持
- 其他版本：基础无边框功能

使用示例
--------

基础无边框窗口示例：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
   from qfluentwidgets.components.widgets.frameless_window import FramelessWindow
   from qfluentwidgets.components.widgets.button import PrimaryPushButton
   
   class MainWindow(FramelessWindow):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           # 创建中心控件
           central_widget = QWidget()
           self.setCentralWidget(central_widget)
           
           # 设置布局
           layout = QVBoxLayout(central_widget)
           
           # 添加内容
           title = QLabel("Fluent Design 无边框窗口")
           title.setStyleSheet("font-size: 24px; font-weight: bold; margin: 20px;")
           
           content = QLabel("这是一个使用FramelessWindow创建的现代化无边框窗口")
           content.setStyleSheet("margin: 20px; color: #666666;")
           
           button = PrimaryPushButton("点击我", self)
           button.clicked.connect(self.on_button_clicked)
           
           layout.addWidget(title)
           layout.addWidget(content)
           layout.addWidget(button)
           layout.addStretch()
           
           # 设置窗口属性
           self.setWindowTitle("无边框窗口示例")
           self.resize(800, 600)
           
       def on_button_clicked(self):
           from qfluentwidgets.components.widgets.flyout import Flyout
           pos = self.mapToGlobal(self.rect().center())
           Flyout.show("按钮被点击了！", self, pos)
   
   if __name__ == "__main__":
       app = QApplication(sys.argv)
       window = MainWindow()
       window.show()
       sys.exit(app.exec())

注意事项
--------

1. **平台限制** - 仅支持Windows平台，其他平台会回退到基础功能
2. **Windows版本** - Mica效果需要Windows 11 22000或更高版本
3. **依赖库** - 需要安装qframelesswindow和pywin32库
4. **性能考虑** - Mica效果可能对性能有一定影响
5. **主题适配** - 窗口效果会自动适配系统主题

相关组件
--------

- :doc:`window` - 窗口控件
- :doc:`title_bar` - 标题栏控件
- :doc:`button` - 按钮控件
