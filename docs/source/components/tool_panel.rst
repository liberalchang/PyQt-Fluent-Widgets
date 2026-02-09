ToolPanel 工具面板模块
======================

ToolPanel 模块提供工具面板控件，用于组织和管理工具按钮。支持多种布局模式。

主要功能
--------

- **工具组织** - 组织和管理工具按钮
- **多种布局** - 支持水平和垂直布局
- **滚动支持** - 支持滚动显示更多工具
- **响应式** - 支持响应式布局调整
- **样式定制** - 提供Fluent Design样式

核心组件
--------

ToolPanel
~~~~~~~~~~

工具面板控件，提供基础的工具管理功能。

**主要子类：**
- ``VerticalToolPanel`` - 垂直工具面板

ToolPanelButton
~~~~~~~~~~~~~~~~

工具面板按钮控件，用于工具面板中的按钮。

使用示例
--------

基础工具面板使用：

.. code-block:: python

   from qfluentwidgets.components.widgets.tool_panel import ToolPanel
   
   # 创建工具面板
   panel = ToolPanel()
   
   # 添加工具按钮
   panel.addTool("工具1")
   panel.addTool("工具2")

注意事项
--------

1. **工具组织** - 合理组织工具按钮
2. **布局选择** - 根据界面选择合适的布局
3. **响应式设计** - 考虑不同屏幕尺寸的适配

相关组件
--------

- :doc:`button` - 按钮控件
- :doc:`menu` - 菜单控件
