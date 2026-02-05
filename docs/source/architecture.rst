架构概览
========

PySide6-Fluent-Widgets 是一个基于 PySide6 的现代化 UI 组件库，采用模块化设计架构。
本文档详细介绍项目的整体架构、模块组织和设计原则。

整体架构
--------

.. code-block:: text

   qfluentwidgets/
   ├── __init__.py                 # 主入口文件，导出所有公共API
   ├── common/                     # 通用工具和基础类
   │   ├── animation.py            # 动画引擎和过渡效果
   │   ├── auto_wrap.py           # 自动文本换行
   │   ├── chart_resource.py      # 图表资源管理
   │   ├── color.py               # 颜色管理和主题色彩系统
   │   ├── config.py              # 配置文件管理和设置
   │   ├── exception_handler.py   # 异常处理机制
   │   ├── font.py                # 字体管理和加载
   │   ├── icon.py                # 图标加载和管理系统
   │   ├── image_utils.py         # 图像处理工具
   │   ├── overload.py            # 函数重载装饰器
   │   ├── router.py              # 路由管理
   │   ├── screen.py              # 屏幕信息获取
   │   ├── smooth_scroll.py        # 平滑滚动实现
   │   ├── style_sheet.py         # QSS 样式表管理
   │   ├── theme_listener.py       # 主题变化监听
   │   └── translator.py          # 国际化翻译支持
   ├── components/                 # 核心 UI 组件模块
   │   ├── widgets/               # 基础控件 (38个文件)
   │   ├── navigation/            # 导航组件 (11个文件)
   │   ├── dialog_box/            # 对话框组件 (11个文件)
   │   ├── settings/              # 设置组件 (8个文件)
   │   ├── material/              # 材质设计组件 (6个文件)
   │   ├── charts/                # 图表组件 (2个文件)
   │   ├── date_time/             # 日期时间组件 (6个文件)
   │   ├── layout/                # 布局组件 (5个文件)
   │   └── vispy/                 # 2D/3D 可视化组件 (14个文件)
   ├── window/                     # 窗口相关组件 (5个文件)
   ├── multimedia/                 # 多媒体组件 (4个文件)
   ├── hybrid/                     # 混合开发支持 (6个文件)
   └── _rc/                        # 资源文件 (2个文件)

模块详细说明
------------

common 模块 - 基础设施
~~~~~~~~~~~~~~~~~~~~~~~

通用模块提供了整个组件库的基础设施和工具：

**核心功能模块**:

* **animation.py**: 动画引擎，提供平滑的过渡效果和动画
  - `AnimationBase`: 动画基类
  - `FluentAnimation`: Fluent 风格动画
  - 支持平移、缩放、透明度、旋转等动画效果

* **color.py**: 颜色管理和主题色彩系统
  - `ThemeColor`: 主题颜色管理
  - 支持亮色/暗色主题自动切换
  - 提供标准 Fluent Design 色彩

* **config.py**: 配置管理系统
  - `qconfig`: 全局配置对象
  - 支持主题、颜色、字体等配置
  - 配置持久化和自动加载

* **icon.py**: 图标管理系统
  - `FluentIcon`: 内置图标集合
  - 支持多尺寸和主题适配
  - 图标缓存和按需加载

* **style_sheet.py**: QSS 样式表管理
  - `FluentStyleSheet`: 样式表管理器
  - 支持动态样式切换
  - 主题样式自动应用

* **font.py**: 字体管理
  - 系统字体检测和加载
  - 支持自定义字体配置
  - 字体回退机制

**工具模块**:

* **smooth_scroll.py**: 平滑滚动实现
  - `SmoothScroll`: 平滑滚动引擎
  - 支持自适应和固定步长模式
  - 优化的滚动性能

* **theme_listener.py**: 主题变化监听
  - 实时主题变化检测
  - 自动样式更新机制
  - 支持自定义主题监听器

components 模块 - UI 组件核心
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

这是项目的核心模块，包含所有 UI 组件，按功能域组织：

**widgets 子模块 - 基础控件** (38个文件)

包含最常用的基础 UI 控件：

* **按钮组件族**: 
  - `PushButton`: 基础按钮
  - `PrimaryPushButton`: 主要按钮
  - `DropDownPushButton`: 下拉按钮
  - `ToggleButton`: 切换按钮
  - `HyperlinkButton`: 超链接按钮
  - `PillPushButton`: 胶囊按钮
  - 等 23 种按钮变体

* **输入组件族**:
  - `LineEdit`: 单行输入框
  - `LabelLineEdit`: 带标签输入框
  - `SearchLineEdit`: 搜索输入框
  - `PasswordLineEdit`: 密码输入框
  - `TextEdit`: 多行文本编辑器
  - `ComboBox`: 下拉框
  - `SpinBox`: 数值输入框

* **显示组件族**:
  - `Label`: 标签组件族 (11种变体)
  - `CardWidget`: 卡片组件族 (6种变体)
  - `IconWidget`: 图标组件

* **进度组件族**:
  - `ProgressBar`: 进度条
  - `ProgressRing`: 环形进度条
  - `IndeterminateProgressBar`: 不确定进度条
  - `IndeterminateProgressRing`: 不确定环形进度

* **列表和表格**:
  - `ListView`: 列表视图
  - `TableView`: 表格视图
  - `SortableTableView`: 可排序表格
  - `TreeView`: 树形视图

**navigation 子模块 - 导航组件** (11个文件)

提供应用导航和布局相关的组件：

* **NavigationInterface**: 完整的导航界面框架
* **Pivot**: 透视导航，类似标签页
* **Breadcrumb**: 面包屑导航
* **SegmentedWidget**: 分段控件
* **NavigationPanel**: 可折叠的导航面板

**dialog_box 子模块 - 对话框组件** (11个文件)

提供各种对话框和选择器：

* **ColorDialog**: 颜色选择对话框
* **MessageBox**: 消息框
* **FolderListDialog`: 文件夹列表对话框
* **ColorPalette`: 颜色面板
* **ScreenColorPicker`: 屏幕颜色选择器

**其他专业模块**:

* **settings**: 设置相关组件 (8个文件)
* **material**: 材质设计组件 (6个文件)  
* **charts**: 图表组件 (2个文件)
* **date_time**: 日期时间组件 (6个文件)
* **layout**: 布局组件 (5个文件)
* **vispy**: 2D/3D 可视化组件 (14个文件)

window 模块 - 窗口框架
~~~~~~~~~~~~~~~~~~~~~~~

提供应用窗口和框架组件：

* **FluentWindow**: Fluent 风格主窗口
  - 集成标题栏、菜单栏、工具栏
  - 支持窗口状态管理
  - 自适应主题变化

* **DrawerWindow**: 带侧边抽屉的窗口
* **SplashScreen**: 应用启动画面
* **StackedWidget`: 窗口堆叠管理

multimedia 模块 - 多媒体支持
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

提供媒体播放和处理功能：

* **MediaPlayer**: 媒体播放器核心
* **MediaPlayBar`: 播放控制栏
* **VideoWidget`: 视频显示组件

hybrid 模块 - 混合开发
~~~~~~~~~~~~~~~~~~~~~~

支持 PySide6 与 QML 混合开发：

* **FluentHybridWindow`: 混合开发窗口
* **CommunicationBridge`: PySide6-QML 通信桥
* **QMLManager`: QML 资源管理器

设计原则和架构特点
------------------

**1. 模块化设计**
* 按功能域清晰划分模块
* 低耦合，高内聚
* 支持按需导入和加载

**2. 分层架构**
```
应用层 (用户代码)
    ↓
组件层 (components/)
    ↓  
基础层 (common/)
    ↓
系统层 (PySide6/Qt)
```

**3. 统一的 API 设计**
* 一致的命名规范
* 统一的参数接口
* 标准的信号槽机制

**4. 主题系统集成**
* 自动主题检测
* 动态样式切换
* 组件级主题适配

**5. 国际化支持**
* 内置中文本地化
* 可扩展的语言系统
* 自动文本方向适配

性能优化策略
------------

**1. 渲染优化**
* 使用硬件加速
* 批量样式更新
* 智能重绘机制

**2. 内存管理**
* 延迟加载组件
* 图标和资源缓存
* 自动垃圾回收

**3. 事件处理**
* 事件队列优化
* 防抖和节流
* 异步事件处理

扩展和自定义
------------

**添加新组件的标准流程**:

1. **选择合适的模块**: 根据组件功能选择对应目录
2. **继承基类**: 选择合适的基础类继承
3. **实现接口**: 实现必要的方法和信号
4. **添加样式**: 在 FluentStyleSheet 中添加样式定义
5. **导出组件**: 在模块的 `__init__.py` 中导出
6. **编写文档**: 添加 docstring 和使用示例

**自定义样式示例**:

.. code-block:: python

   from qfluentwidgets import PushButton, FluentStyleSheet
   
   # 创建自定义按钮
   custom_button = PushButton('自定义按钮')
   
   # 应用自定义样式
   custom_button.setStyleSheet("""
       PushButton {
           background-color: #0078d4;
           color: white;
           border: none;
           border-radius: 6px;
           padding:8px 16px;
           font-weight: 500;
       }
       
       PushButton:hover {
           background-color: #106ebe;
           transform: translateY(-1px);
       }
       
       PushButton:pressed {
           background-color: #005a9e;
           transform: translateY(0px);
       }
   """)

测试和质量保证
------------

**测试架构**:
* 单元测试：每个组件的基本功能
* 集成测试：组件间交互
* UI 测试：界面渲染和用户交互
* 性能测试：内存使用和渲染性能

**代码质量**:
* 类型注解覆盖
* 文档字符串规范
* 代码风格统一
* 静态分析检查

版本兼容性
------------

* **PySide6**: 主要支持平台
* **Python 3.8+**: 最低版本要求
* **跨平台**: Windows, macOS, Linux
* **向后兼容**: API 稳定性保证

总结
----

PySide6-Fluent-Widgets 采用现代软件架构设计原则，提供了：

* **105个组件文件** 的完整 UI 组件库
* **模块化架构** 便于维护和扩展
* **统一的设计语言** 确保视觉一致性
* **完善的主题系统** 支持个性化定制
* **丰富的文档** 降低学习成本

这种架构设计使得组件库既保持了高性能，又提供了良好的开发体验，是构建现代化桌面应用的理想选择。
