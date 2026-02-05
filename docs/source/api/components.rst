Components 模块 API
===================

Components 模块是 PySide6-Fluent-Widgets 的核心，包含所有的 UI 组件。
这些组件按照功能进行了分类，包括基础控件、导航组件、对话框、设置组件等。

主要特点：
- 基于 Fluent Design 设计语言
- 支持亮色/暗色主题自动切换
- 完整的中文本地化支持
- 丰富的自定义选项和信号槽机制

使用方法：
.. code-block:: python

   from qfluentwidgets import PushButton, ComboBox, InfoBar
   
   # 创建基础组件
   button = PushButton('点击我')
   combo = ComboBox()
   
   # 连接信号
   button.clicked.connect(lambda: InfoBar.success(title='成功', content='按钮被点击'))

.. automodule:: qfluentwidgets.components
   :members:
   :undoc-members:
   :show-inheritance:

Widgets
-------

基础控件模块，包含最常用的 UI 组件。

包含38个组件文件，提供：
- 按钮组件族（23种变体）
- 输入组件族（输入框、下拉框、数值框等）
- 显示组件族（标签、卡片、图标等）
- 进度组件族（进度条、环形进度等）
- 列表和表格组件
- 菜单和工具提示组件

这些组件是构建应用界面的基础，支持完整的主题系统和交互功能。

.. automodule:: qfluentwidgets.components.widgets
   :members:
   :undoc-members:
   :show-inheritance:

Navigation
----------

导航组件模块，提供应用导航和布局相关的功能。

包含11个组件，提供：
- NavigationInterface：完整的导航界面框架
- Pivot：透视导航，类似标签页
- Breadcrumb：面包屑导航
- SegmentedWidget：分段控件
- NavigationPanel：可折叠的导航面板

适用于构建具有复杂导航结构的应用程序。

.. automodule:: qfluentwidgets.components.navigation
   :members:
   :undoc-members:
   :show-inheritance:

Dialog Box
----------

对话框组件模块，提供各种对话框和选择器。

包含11个组件，提供：
- ColorDialog：颜色选择对话框
- MessageBox：消息框
- FolderListDialog：文件夹列表对话框
- ColorPalette：颜色面板
- ScreenColorPicker：屏幕颜色选择器

支持模态和非模态对话框，提供丰富的自定义选项。

.. automodule:: qfluentwidgets.components.dialog_box
   :members:
   :undoc-members:
   :show-inheritance:

Settings
--------

设置相关组件模块，用于构建设置界面。

包含8个组件，提供：
- SettingCard：设置卡片基类
- SwitchSettingCard：开关设置卡片
- RangeSettingCard：范围设置卡片
- ComboBoxSettingCard：下拉设置卡片
- OptionsSettingCard：选项设置卡片

专门用于构建应用的设置界面，支持分组和展开功能。

.. automodule:: qfluentwidgets.components.settings
   :members:
   :undoc-members:
   :show-inheritance:

Material
--------

材质设计组件模块，实现 Fluent Design 的材质效果。

包含6个组件，提供：
- AcrylicWidget：亚克力效果组件
- AcrylicMenu：亚克力菜单
- AcrylicLineEdit：亚克力输入框
- AcrylicComboBox：亚克力下拉框
- AcrylicToolTip：亚克力工具提示

实现毛玻璃效果和材质设计语言，提供现代化的视觉体验。

.. automodule:: qfluentwidgets.components.material
   :members:
   :undoc-members:
   :show-inheritance:

Charts
------

图表组件模块，提供数据可视化功能。

包含2个组件，提供：
- EChartsWidget：基于 ECharts 的图表组件
- ChartBridge：图表桥接器

支持多种图表类型：折线图、柱状图、饼图、散点图等。
集成了 Apache ECharts，提供丰富的交互和动画效果。

.. automodule:: qfluentwidgets.components.charts
   :members:
   :undoc-members:
   :show-inheritance:

Date Time
---------

日期时间组件模块，提供日期和时间选择功能。

包含6个组件，提供：
- CalendarPicker：日历选择器
- DatePicker：日期选择器
- TimePicker：时间选择器
- FastCalendarView：快速日历视图

支持多种日期格式和本地化设置，提供友好的用户界面。

.. automodule:: qfluentwidgets.components.date_time
   :members:
   :undoc-members:
   :show-inheritance:

Layout
------

布局组件模块，提供自定义布局管理器。

包含5个组件，提供：
- FlowLayout：流式布局
- ExpandLayout：可展开布局
- VBoxLayout：垂直盒子布局
- FluentSplitter：分割器

这些布局管理器补充了 Qt 内置的布局，提供更灵活的界面布局选项。

.. automodule:: qfluentwidgets.components.layout
   :members:
   :undoc-members:
   :show-inheritance:

Vispy
-----

2D/3D 可视化组件模块，基于 Vispy 库实现。

包含14个组件，提供：
- VispyWidget2D：2D 可视化组件
- VispyWidget3D：3D 可视化组件
- PointCloudViewer：点云查看器
- 交互式绘图工具

适用于科学计算、数据可视化和 3D 图形应用开发。

.. automodule:: qfluentwidgets.components.vispy
   :members:
   :undoc-members:
   :show-inheritance:
