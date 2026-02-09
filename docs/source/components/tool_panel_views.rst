ToolPanelViews 工具面板视图模块
==============================

ToolPanelViews 模块提供工具面板视图控件，用于不同布局的工具面板显示。支持响应式和滚动模式。

主要功能
--------

- **多种视图** - 支持多种工具面板视图模式
- **响应式布局** - 自动适应不同屏幕尺寸
- **滚动支持** - 支持滚动显示更多工具
- **布局管理** - 智能的工具布局管理
- **样式统一** - 提供统一的Fluent Design样式

核心组件
--------

VerticalToolPanelView
~~~~~~~~~~~~~~~~~~~~

垂直工具面板视图，提供垂直布局的工具面板。

HorizontalToolPanelView
~~~~~~~~~~~~~~~~~~~~~~

水平工具面板视图，提供水平布局的工具面板。

ScrollableToolPanelView
~~~~~~~~~~~~~~~~~~~~~~~

可滚动工具面板视图，支持滚动显示更多工具。

ResponsiveToolPanelView
~~~~~~~~~~~~~~~~~~~~~~~

响应式工具面板视图，自动适应布局变化。

使用示例
--------

基础工具面板视图使用：

.. code-block:: python

   from qfluentwidgets.components.widgets.tool_panel_views import VerticalToolPanelView
   
   # 创建垂直工具面板视图
   panel_view = VerticalToolPanelView()
   
   # 添加工具
   panel_view.addTool("工具1")
   panel_view.addTool("工具2")

注意事项
--------

1. **视图选择** - 根据需求选择合适的视图类型
2. **响应式设计** - 考虑不同屏幕尺寸的适配
3. **性能优化** - 大量工具时注意性能优化

相关组件
--------

- :doc:`tool_panel` - 工具面板控件
- :doc:`button` - 按钮控件
