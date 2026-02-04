架构概览
========

PySide6-Fluent-Widgets 采用模块化设计，将不同功能的组件分别组织在不同的模块中。
这种设计使得代码结构清晰，便于维护和扩展。

整体架构
--------

.. code-block:: text

   qfluentwidgets/
   ├── __init__.py              # 主入口文件
   ├── common/                  # 通用工具和基础类
   │   ├── animation.py         # 动画相关
   │   ├── color.py            # 颜色管理
   │   ├── config.py           # 配置管理
   │   ├── icon.py             # 图标管理
   │   ├── style_sheet.py      # 样式表
   │   └── ...
   ├── components/             # UI 组件
   │   ├── widgets/            # 基础控件
   │   ├── navigation/         # 导航组件
   │   ├── dialog_box/         # 对话框
   │   ├── settings/           # 设置组件
   │   ├── material/           # 材质设计组件
   │   ├── charts/             # 图表组件
   │   ├── date_time/          # 日期时间组件
   │   ├── layout/             # 布局组件
   │   └── vispy/              # 2D/3D 可视化组件
   ├── window/                 # 窗口相关
   │   ├── fluent_window.py    # Fluent 风格窗口
   │   ├── drawer_window.py    # 抽屉窗口
   │   └── ...
   ├── multimedia/             # 多媒体组件
   └── _rc/                    # 资源文件

模块说明
--------

common 模块
-----------

通用模块提供了整个组件库的基础功能，包括：

* **animation.py**: 动画引擎和过渡效果
* **color.py**: 颜色管理和主题色彩系统
* **config.py**: 配置文件管理和设置
* **icon.py**: 图标加载和管理
* **style_sheet.py**: QSS 样式表管理
* **font.py**: 字体管理
* **theme_listener.py**: 主题变化监听

components 模块
---------------

这是核心的 UI 组件模块，按功能分类：

widgets 子模块
~~~~~~~~~~~~~~

基础控件，包括：

* **PushButton**: 按钮组件
* **PrimaryPushButton**: 主要按钮
* **DropDownButton**: 下拉按钮
* **HyperlinkButton**: 超链接按钮
* **RadioButton**: 单选按钮
* **CheckBox**: 复选框
* **Switch**: 开关
* **Slider**: 滑块
* **ProgressBar**: 进度条
* **ProgressRing**: 环形进度条
* **LineEdit**: 输入框
* **TextEdit**: 文本编辑器
* **SpinBox**: 数值输入框
* **ComboBox**: 下拉框
* **ListView**: 列表视图
* **TableView**: 表格视图

navigation 子模块
~~~~~~~~~~~~~~~~~

导航相关组件：

* **Pivot**: 透视导航
* **Segmented**: 分段控件
* **Breadcrumb**: 面包屑导航
* **TabBar**: 标签栏
* **NavigationInterface**: 导航界面

dialog_box 子模块
~~~~~~~~~~~~~~~~~

对话框组件：

* **MessageBox**: 消息框
* **FileDialog**: 文件对话框
* **ColorDialog**: 颜色选择对话框
* **FolderListDialog**: 文件夹列表对话框

settings 子模块
~~~~~~~~~~~~~~~~

设置相关组件：

* **SettingCard**: 设置卡片
* **SwitchSettingCard**: 开关设置卡片
* **RangeSettingCard**: 范围设置卡片
* **ComboBoxSettingCard**: 下拉设置卡片
* **GroupSettingCard**: 分组设置卡片

material 子模块
~~~~~~~~~~~~~~~~

材质设计组件：

* **AcrylicLabel**: 亚克力标签
* **AcrylicBrush**: 亚克力画笔
* **ElevationEffect**: 高度效果

charts 子模块
~~~~~~~~~~~~~~

图表组件：

* **ChartView**: 图表视图
* **LineChart**: 折线图
* **BarChart**: 柱状图
* **PieChart**: 饼图

date_time 子模块
~~~~~~~~~~~~~~~~~

日期时间组件：

* **Calendar**: 日历
* **DatePicker**: 日期选择器
* **TimePicker**: 时间选择器

layout 子模块
~~~~~~~~~~~~~~

布局组件：

* **FlowLayout**: 流式布局
* **VBoxLayout**: 垂直布局
* **HBoxLayout**: 水平布局

vispy 子模块
~~~~~~~~~~~~

2D/3D 可视化组件：

* **VispyWidget2D**: 2D 可视化组件
* **VispyWidget3D**: 3D 可视化组件
* **PointCloudViewer**: 点云查看器

window 模块
-----------

窗口相关组件：

* **FluentWindow**: Fluent 风格主窗口
* **DrawerWindow**: 带抽屉的窗口
* **SplashScreen**: 启动画面
* **StackedWidget**: 堆叠窗口组件

multimedia 模块
---------------

多媒体相关组件：

* **MediaPlayer**: 媒体播放器
* **MediaPlayBar**: 媒体播放控制栏

设计原则
--------

1. **模块化**: 按功能划分模块，降低耦合度
2. **一致性**: 统一的 API 设计和命名规范
3. **可扩展**: 支持自定义样式和行为
4. **性能**: 优化渲染性能，减少资源占用
5. **可访问性**: 支持键盘导航和屏幕阅读器

主题系统
--------

PySide6-Fluent-Widgets 采用基于 QSS 的主题系统：

* **亮色主题**: 适合白天使用
* **暗色主题**: 适合夜间使用  
* **自动主题**: 跟随系统主题设置
* **自定义主题**: 支持用户自定义颜色方案

主题配置通过 `common/config.py` 中的 `qconfig` 类管理：

.. code-block:: python

   from qfluentwidgets import qconfig, Theme, setTheme

   # 获取当前主题
   current_theme = qconfig.theme

   # 设置主题
   setTheme(Theme.DARK)

   # 设置主题色
   qconfig.set('theme_color', '#0078d4')

国际化支持
----------

组件库支持多语言，通过 `common/translator.py` 实现：

.. code-block:: python

   from qfluentwidgets import FluentIcon, setTheme, isDarkTheme

   # 图标会根据主题自动切换
   icon = FluentIcon.SETTING

扩展开发
--------

如何添加新组件：

1. 在对应的模块目录下创建新的组件文件
2. 继承适当的基础类
3. 实现必要的虚函数
4. 添加中文文档字符串
5. 在 `__init__.py` 中导出新组件

示例：

.. code-block:: python

   from PySide6.QtWidgets import QWidget
   from qfluentwidgets.common.style_sheet import FluentStyleSheet

   class CustomWidget(QWidget):
       """自定义组件"""
       
       def __init__(self, parent=None):
           super().__init__(parent)
           # 初始化代码
           FluentStyleSheet.CUSTOM_WIDGET.apply(self)

性能优化
--------

* **延迟加载**: 组件按需创建
* **缓存机制**: 图标和样式缓存
* **批量更新**: 减少重绘次数
* **内存管理**: 及时释放不需要的资源

测试策略
--------

* **单元测试**: 每个组件的基本功能测试
* **集成测试**: 组件间交互测试
* **UI 测试**: 界面渲染和交互测试
* **性能测试**: 渲染性能和内存使用测试
