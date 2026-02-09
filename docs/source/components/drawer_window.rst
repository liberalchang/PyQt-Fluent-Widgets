DrawerWindow 抽屉窗口模块
==========================

DrawerWindow 模块提供抽屉窗口控件，用于侧边栏和抽屉式界面。支持多种抽屉方向和动画效果。

主要功能
--------

- **抽屉显示** - 提供侧边栏抽屉功能
- **多种方向** - 支持左右上下四个方向
- **动画效果** - 提供流畅的抽屉动画
- **内容管理** - 支持抽屉内容的动态管理
- **交互控制** - 提供完整的交互控制

核心组件
--------

Drawer
~~~~~~~

抽屉控件，提供基础的抽屉功能。

DrawerWindow
~~~~~~~~~~~~~

抽屉窗口控件，提供窗口级别的抽屉功能。

使用示例
--------

基础抽屉窗口使用：

.. code-block:: python

   from qfluentwidgets.window.drawer_window import DrawerWindow
   
   # 创建抽屉窗口
   drawer = DrawerWindow()
   
   # 添加内容
   content = QWidget()
   drawer.addWidget(content)
   
   # 显示抽屉
   drawer.show()

注意事项
--------

1. **方向选择** - 根据界面布局选择合适的抽屉方向
2. **内容管理** - 合理组织抽屉内容
3. **动画设置** - 选择合适的抽屉动画效果

相关组件
--------

- :doc:`fluent_window` - Fluent窗口控件
- :doc:`button` - 按钮控件
