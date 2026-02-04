# Tests 目录文件说明

本文档描述了 `tests/` 目录下各个测试文件的简单说明和作用。

## 📁 目录结构

### 🔧 调试和工具类

#### `check_path.py`
- **作用**: 简单的路径检查工具
- **说明**: 打印 qfluentwidgets 模块文件路径和当前工作目录，用于调试导入问题

#### `debug_crash.py`
- **作用**: QtWebEngine 组件导入调试
- **说明**: 逐步测试 QtWebEngineWidgets 的导入和创建过程，用于诊断崩溃问题

#### `debug_resources_2.py`
- **作用**: 资源文件调试工具
- **说明**: 用于调试资源文件加载问题

---

### 🎨 Vispy 组件测试

#### `test_vispy_widget.py`
- **作用**: Vispy 2D/3D 图形组件综合测试
- **说明**: 
  - 包含 2D 和 3D 场景的完整测试界面
  - 支持云母特效（Mica Effect）和最大化窗口
  - 提供可见性控制组，动态控制图形元素显示/隐藏
  - 2D 场景支持自由旋转、翻转等操作
  - 3D 场景支持多种视角切换和图形绘制

#### `debug_camera_test.py`
- **作用**: 相机和坐标系统调试
- **说明**: 专门用于调试 Vispy 相机控制和坐标转换的详细测试

#### `debug_coordinate_test.py`
- **作用**: 坐标转换调试
- **说明**: 测试和调试坐标系统转换功能

#### `debug_mouse_events.py`
- **作用**: 鼠标事件详细调试
- **说明**: 全面测试鼠标事件获取和处理机制

#### `drawing_app.py`
- **作用**: 交互式绘图应用程序
- **说明**: 
  - 完整的绘图应用，支持多种绘图工具
  - 包含颜色选择器、画笔设置等功能
  - 集成工具面板和绘图区域

#### `test_drawing_view.py`
- **作用**: 绘图视图基础测试
- **说明**: 简单的绘图视图功能测试

---

### 📊 表格和数据展示

#### `table_view.py`
- **作用**: 表格组件实现和测试
- **说明**: 包含表格视图的完整实现，支持自定义委托、样式和交互

#### `test_sortable_table.py`
- **作用**: 可排序表格功能测试
- **说明**: 
  - 测试三态排序循环（降序→升序→无排序）
  - 验证表头图标显示和智能文件排序
  - 测试高性能排序算法

---

### 🧭 导航和窗口管理

#### `test_navigation.py`
- **作用**: 基础导航窗口测试
- **说明**: 测试 FluentWindow 导航功能，支持云母特效

#### `test_navigation_acrylic.py`
- **作用**: 亚克力特效导航测试
- **说明**: 专门测试亚克力（Acrylic）窗口特效

#### `test_navigation_layout_fix.py`
- **作用**: 导航布局修复测试
- **说明**: 测试导航布局相关的修复方案

#### `test_navigation_opengl.py`
- **作用**: OpenGL 导航测试
- **说明**: 测试集成 OpenGL 的导航窗口

#### `test_navigation_titlebar_fix.py`
- **作用**: 标题栏修复测试
- **说明**: 测试标题栏相关的修复功能

#### `test_top_navigation.py`
- **作用**: 顶部导航测试
- **说明**: 测试顶部导航栏的实现和功能

#### `test_top_navigation_simple.py`
- **作用**: 简化版顶部导航测试
- **说明**: 轻量级的顶部导航功能测试

#### `test_top_navigation_window.py`
- **作用**: 顶部导航窗口测试
- **说明**: 完整的顶部导航窗口实现测试

---

### 🎯 界面组件测试

#### `test_color_pickers.py`
- **作用**: 颜色选择器组件测试
- **说明**: 
  - 测试各种颜色选择器组件
  - 包括 ColorDialog、DropDownColorPalette、CircleColorPicker 等

#### `test_command_bar_advanced.py`
- **作用**: 高级命令栏功能测试
- **说明**: 
  - 全面测试所有 CommandBar 变体和功能
  - 包括方向、响应式和可移动命令栏

#### `test_command_bar_orientation.py`
- **作用**: 命令栏方向测试
- **说明**: 测试不同方向的命令栏布局

#### `test_command_bar_views.py`
- **作用**: 命令栏视图测试
- **说明**: 测试命令栏的视图功能

#### `test_tool_panel.py`
- **作用**: 工具面板组件测试
- **说明**: 
  - 测试 Photoshop 风格的工具箱
  - 包括垂直工具面板和布局

#### `test_tool_panel_views.py`
- **作用**: 工具面板视图测试
- **说明**: 测试工具面板的不同视图模式

#### `test_tool_panel_with_text.py`
- **作用**: 带文本的工具面板测试
- **说明**: 测试包含文本标签的工具面板

#### `test_menu_bar.py`
- **作用**: 菜单栏组件测试
- **说明**: 
  - 测试独立的 MenuBar 组件
  - 包括基础菜单、可勾选菜单等功能

#### `test_splitter.py`
- **作用**: 分割器组件测试
- **说明**: 测试窗口分割器的功能

---

### 🎭 主题和特效测试

#### `test_detailed_mica.py`
- **作用**: 详细云母特效测试
- **说明**: 深入测试云母特效的各种细节和配置

#### `test_maximize_fix.py`
- **作用**: 最大化修复测试
- **说明**: 测试窗口最大化相关的修复方案

#### `test_maximize_mica_effect.py`
- **作用**: 最大化云母特效测试
- **说明**: 测试最大化状态下的云母特效保持

#### `test_simple_maximize.py`
- **作用**: 简单最大化测试
- **说明**: 基础的窗口最大化功能测试

#### `test_pywinstyles.py`
- **作用**: Windows 样式测试
- **说明**: 测试 Windows 特定的窗口样式功能

---

### 🛠️ 其他功能测试

#### `echarts_test.py`
- **作用**: ECharts 图表组件测试
- **说明**: 
  - 测试动态图表功能
  - 包括时间序列数据的实时更新

#### `test_auto_resize_demo.py`
- **作用**: 自动调整大小演示
- **说明**: 测试组件的自动调整大小功能

#### `test_fix_verification.py`
- **作用**: 修复验证测试
- **说明**: 验证各种修复方案的有效性

#### `test_new_interaction.py`
- **作用**: 新交互方式测试
- **说明**: 测试新的用户交互模式和功能

#### `test_tooltip_follow.py`
- **作用**: 工具提示跟随测试
- **说明**: 测试工具提示的跟随行为

#### `test_tooltip_slider.py`
- **作用**: 滑块工具提示测试
- **说明**: 测试滑块组件的工具提示功能

#### `label_line_edit_test.py`
- **作用**: 标签和行编辑测试
- **说明**: 测试标签和输入框组件的组合使用

#### `draw_icon_example.py`
- **作用**: 图标绘制示例
- **说明**: 演示如何绘制自定义图标

---

## 📝 使用说明

### 运行测试
大多数测试文件可以直接运行：
```bash
python test_vispy_widget.py
python test_navigation.py
python test_color_pickers.py
```

### 依赖要求
- Python 3.8+
- PySide6
- vispy（用于 3D 图形测试）
- 其他可选依赖根据具体测试文件而定

### 注意事项
1. 部分测试需要特定的系统环境（如 Windows 11 用于云母特效）
2. Vispy 相关测试需要安装 vispy 库
3. 某些功能测试可能需要额外的系统权限或配置

---

## 🔄 更新日志

本文档随测试文件的添加和修改而更新，确保与实际测试内容保持同步。
