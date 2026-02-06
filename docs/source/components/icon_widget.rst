IconWidget 图标控件模块
========================

IconWidget 模块提供图标显示控件，支持多种图标格式和自定义样式。该模块实现了现代化的图标显示功能，提供灵活的图标管理。

主要功能
--------

- **多格式支持** - 支持QIcon、FluentIconBase、字符串路径等多种格式
- **自定义绘制** - 提供高质量的图标绘制
- **属性支持** - 支持Qt属性系统
- **主题适配** - 自动适应深色/浅色主题

核心组件
--------

IconWidget
~~~~~~~~~~

图标控件，用于显示各种类型的图标。

.. code-block:: python

   from qfluentwidgets.components.widgets.icon_widget import IconWidget
   from qfluentwidgets import FluentIcon as FIF
   
   # 创建图标控件
   icon_widget = IconWidget(FIF.SETTING, parent=parent)
   icon_widget.setFixedSize(32, 32)
   
   # 或者创建空图标控件后设置
   icon_widget = IconWidget(parent=parent)
   icon_widget.setIcon(FIF.DOWNLOAD)

**构造函数：**
- ``IconWidget(parent: QWidget = None)``
- ``IconWidget(icon: QIcon | str | FluentIconBase, parent: QWidget = None)``

**主要方法：**
- ``setIcon(icon: QIcon | str | FluentIconBase)`` - 设置图标
- ``icon()`` - 获取图标

**特点：**
- 支持多种图标格式
- 自动尺寸适配
- 高质量绘制
- 主题颜色适配

使用示例
--------

基础图标显示示例：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel
   from qfluentwidgets.components.widgets.icon_widget import IconWidget
   from qfluentwidgets import FluentIcon as FIF
   
   class IconDemo(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()
           
       def initUI(self):
           layout = QHBoxLayout(self)
           
           # 创建不同类型的图标
           icons = [
               (FIF.SETTING, "设置"),
               (FIF.DOWNLOAD, "下载"),
               (FIF.UPLOAD, "上传"),
               (FIF.DELETE, "删除"),
               (FIF.EDIT, "编辑"),
               (FIF.SEARCH, "搜索")
           ]
           
           for icon, text in icons:
               icon_widget = IconWidget(icon, self)
               icon_widget.setFixedSize(24, 24)
               
               label = QLabel(text)
               
               layout.addWidget(icon_widget)
               layout.addWidget(label)
               
           layout.addStretch()
   
   if __name__ == "__main__":
       app = QApplication(sys.argv)
       demo = IconDemo()
       demo.show()
       sys.exit(app.exec())

注意事项
--------

1. **图标格式** - 支持QIcon、FluentIconBase和字符串路径
2. **尺寸设置** - 建议使用setFixedSize()设置合适的尺寸
3. **主题适配** - 图标会自动适应系统主题颜色

相关组件
--------

- :doc:`icon` - 图标管理模块
- :doc:`button` - 按钮控件，常配合图标使用
