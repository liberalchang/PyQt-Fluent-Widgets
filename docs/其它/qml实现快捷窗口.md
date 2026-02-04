# FluentWindow 混合架构设计文档（QML 标题栏+侧边栏 + Widget 功能窗）
## 一、设计目标
1. 基于现有 `PySide6-Fluent-Widgets` 项目扩展，不取代原有 `FluentWindow` 实现；
2. 采用「QML 负责交互层 + Widget 负责功能层」混合架构：
   - QML 实现标题栏（窗口控制、主题切换、动画）和侧边栏（导航、菜单、动态交互）；
   - 保留 Widget 承载核心业务功能窗口，复用项目现有 Widget 组件生态；
3. 优化交互动画流畅性，贴合 Fluent Design 动效规范，确保 QML 动画与 Widget 功能无冲突。

## 二、整体架构
### 1. 架构分层（从上到下）
| 层级         | 技术栈       | 核心职责                                                                 | 依赖组件（项目现有）               |
|--------------|--------------|--------------------------------------------------------------------------|----------------------------------|
| 交互层       | QML + Qt Quick | 标题栏（窗口拖动、最小化/关闭、主题切换）、侧边栏（导航菜单、滑入滑出动画）、全局动效管理 | `Theme` 单例、`FluentIcon`、QSS 主题资源 |
| 适配层       | PySide6（Python） | QML 与 Widget 通信、窗口尺寸同步、主题状态同步、动画时序控制                 | `QQuickWidget`、`QStackedWidget`、信号槽 |
| 功能层       | Widget       | 核心业务窗口承载、现有 Widget 组件复用（如 `SettingCard`、`DataTable` 等） | 项目所有 Widget 组件、布局管理器 |
| 基础层       | PySide6 核心 | 窗口容器、全局配置、主题管理、资源加载                                   | `FluentWindowBase`、`qconfig`、`StyleSheetBase` |

### 2. 核心组件关系
```
FluentHybridWindow（主窗口）
├─ QQuickWidget（QML 容器）
│  ├─ TitleBar.qml（QML 标题栏）
│  └─ SideNavigation.qml（QML 侧边栏）
├─ QStackedWidget（Widget 功能窗容器）
│  └─ 现有 Widget 功能窗口（如 SettingInterface、DataInterface 等）
├─ 适配层模块
│  ├─ CommunicationBridge（信号槽通信）
│  ├─ ThemeSyncManager（主题同步）
│  └─ AnimationCoordinator（动画时序协调）
└─ 依赖现有核心模块
   ├─ Theme 单例（主题状态）
   ├─ qconfig（全局配置）
   └─ StyleSheetBase（样式管理）
```

## 三、核心模块设计
### 1. 主窗口容器：FluentHybridWindow
- 继承自 `FluentWindowBase`（保留项目原有窗口基础能力），无标题栏（`setWindowFlags(Qt.FramelessWindowHint)`）；
- 核心布局：
  - 顶部：嵌入 `QQuickWidget`（加载 QML 标题栏，高度固定 48px）；
  - 主体：左侧 `QQuickWidget`（加载 QML 侧边栏，宽度自适应）+ 右侧 `QStackedWidget`（承载 Widget 功能窗）；
- 关键能力：
  - 传递窗口句柄给 QML，支持 QML 控制窗口拖动、resize；
  - 暴露 `QStackedWidget` 接口给适配层，支持 QML 触发功能窗切换。

### 2. QML 交互层设计
#### （1）TitleBar.qml（标题栏）
- 功能：窗口拖动、最小化/最大化/关闭按钮、主题切换按钮、窗口标题显示；
- 动画：
  - 按钮 hover 渐变（`PropertyAnimation` 控制 `opacity` 和 `backgroundColor`）；
  - 主题切换圆形过渡（复用项目 `CircularReveal` 逻辑，QML 实现 `RadialGradient` 过渡）；
  - 窗口 resize 时标题栏平滑缩放（`Behavior on width` 绑定动画）；
- 通信：通过 `signal` 发送窗口控制信号（如 `requestMinimize`）、主题切换信号（`themeChanged`）。

#### （2）SideNavigation.qml（侧边栏）
- 功能：导航菜单（支持多级菜单）、选中高亮、折叠/展开切换、菜单点击触发功能窗切换；
- 动画：
  - 滑入滑出：`Translate` + `PropertyAnimation`（从左向右滑入，时长 300ms，缓动曲线 `InOutCubic`）；
  - 选中高亮：`ColorAnimation` 控制选中项背景渐变；
  - 折叠动画：`ScaleAnimation` 配合 `OpacityAnimation` 实现菜单文本显隐；
- 数据绑定：通过 `QQmlContext` 接收 Widget 侧传递的导航菜单数据（如菜单名称、图标、路由键）。

### 3. 适配层设计（核心桥梁）
#### （1）CommunicationBridge（通信桥梁）
- 核心职责：解决 QML 与 Widget 跨技术栈通信；
- 实现方式：
  - QML → Widget：QML 信号通过 `QQuickWidget.rootObject()` 连接到 Widget 槽函数（如侧边栏菜单点击 → 切换 `QStackedWidget` 页面）；
  - Widget → QML：通过 `QQmlContext` 暴露 `QObject` 实例给 QML，Widget 状态变化（如功能窗标题更新）通过属性通知 QML；
- 关键信号：
  - QML → Widget：`menuClicked(routeKey)`、`windowMinimize()`、`themeToggle()`；
  - Widget → QML：`functionWindowChanged(title)`、`sidebarExpandChanged(isExpand)`。

#### （2）ThemeSyncManager（主题同步）
- 核心职责：确保 QML 与 Widget 主题一致性，复用项目 `Theme` 单例；
- 实现逻辑：
  - 监听 `qconfig.themeChanged` 信号，同步主题模式（Light/Dark/Auto）到 QML 上下文；
  - QML 主题资源（颜色、图标）绑定项目现有 QSS 变量（如 `Theme.res.textFillColorPrimary`）；
  - 主题切换时，先触发 QML 过渡动画，再同步更新 Widget 样式表（`StyleSheet.apply()`）。

#### （3）AnimationCoordinator（动画时序协调）
- 核心职责：避免 QML 动画与 Widget 操作冲突，确保时序对齐；
- 关键逻辑：
  - 侧边栏滑入/滑出时，禁止 Widget 功能窗交互（通过 `setEnabled(False)`），动画结束后恢复；
  - Widget 功能窗切换时，同步触发 QML 侧边栏选中项高亮动画；
  - 主题切换时，先执行 QML 圆形过渡动画，再更新 Widget 主题样式。

### 4. 功能层适配
- 复用项目现有 `QStackedWidget` 管理功能窗口，每个功能窗继承自项目 `QWidget` 或现有界面类（如 `SettingInterface`）；
- 功能窗尺寸通过适配层同步 QML 侧边栏展开/折叠状态：侧边栏折叠时，功能窗宽度自动拉伸，反之收缩；
- 现有 Widget 组件（如 `ProgressBar`、`InfoBadge`）的主题样式，通过 `Theme` 单例与 QML 保持一致。

## 四、关键功能实现
### 1. 窗口控制（QML 标题栏 → Widget 主窗口）
- QML 标题栏通过 `MouseArea` 实现窗口拖动：
  ```qml
  MouseArea {
      anchors.fill: parent
      drag.target: parent
      drag.minimumX: 0
      drag.minimumY: 0
      onReleased: {
          // 传递窗口位置给 Widget 主窗口
          windowController.syncWindowPos(mouseX, mouseY)
      }
  }
  ```
- 窗口控制按钮（最小化/关闭）通过信号触发 Widget 接口：
  ```python
  # 适配层代码
  class WindowController(QObject):
      requestMinimize = Signal()
      requestClose = Signal()

      def syncWindowPos(self, x, y):
          self.parent().move(x, y)  # parent 为 FluentHybridWindow
  ```

### 2. 侧边栏导航（QML → Widget 功能窗切换）
- QML 侧边栏菜单数据绑定项目导航配置：
  ```python
  # 导航数据初始化（复用项目 NavigationItem 逻辑）
  nav_items = [
      {"routeKey": "home", "text": "首页", "icon": "FIF.HOME"},
      {"routeKey": "setting", "text": "设置", "icon": "FIF.SETTING"}
  ]
  # 暴露给 QML
  self.qml_context.setContextProperty("navItems", nav_items)
  ```
- 菜单点击触发功能窗切换：
  ```qml
  ListView {
      model: navItems
      delegate: MenuItem {
          onClicked: {
              communicationBridge.menuClicked(model.routeKey)
          }
      }
  }
  ```
- Widget 侧响应：
  ```python
  # 适配层响应 QML 信号
  self.communication_bridge.menuClicked.connect(lambda k: self.stacked_widget.setCurrentWidget(self.get_widget_by_route_key(k)))
  ```

### 3. 主题切换动画（复用项目 CircularReveal 逻辑）
- QML 实现圆形过渡动画（替代 C++ 实现，更轻量）：
  ```qml
  Rectangle {
      id: revealOverlay
      anchors.fill: parent
      color: Theme.dark ? "#1e1e1e" : "#ffffff"
      opacity: 0
      clip: true

      RadialGradient {
          id: revealGradient
          center: themeToggleButton.position
          radius: revealRadius
          gradient: Gradient {
              GradientStop { position: 0; color: "transparent" }
              GradientStop { position: 1; color: revealOverlay.color }
          }
      }

      PropertyAnimation {
          id: revealAnim
          target: revealOverlay
          property: "opacity"
          duration: 358
          easing.type: Easing.InOutCubic
      }
  }
  ```
- 与 Widget 主题同步：
  ```python
  # 主题切换信号联动
  self.communication_bridge.themeToggle.connect(lambda: self.sync_theme_and_anim())
  def sync_theme_and_anim(self):
      # 1. 启动 QML 动画
      self.qml_root_object.startRevealAnim()
      # 2. 切换 Theme 单例状态
      toggleTheme()
      # 3. 同步 Widget 样式
      StyleSheet.apply(self.stacked_widget.currentWidget())
  ```

## 五、复用项目现有资源
### 1. 组件复用
| 资源类型       | 复用内容                                                                 | 使用方式                                  |
|----------------|--------------------------------------------------------------------------|-------------------------------------------|
| Widget 组件    | 所有业务组件（`SettingCard`、`ProgressRing`）、布局（`FlowLayout`）、功能界面（`SettingInterface`） | 直接嵌入 `QStackedWidget`                  |
| 主题资源       | `Theme` 单例、`qconfig` 配置、Light/Dark 模式 QSS、`FluentIcon`             | QML 绑定 `Theme` 属性，Widget 复用原有 QSS |
| 工具类         | `StyleSheetBase`（样式管理）、`SignalBus`（信号总线）、`Screen`（屏幕适配）   | 适配层直接调用，同步 QML 与 Widget 状态    |

### 2. 配置复用
- 全局配置：复用 `qconfig` 管理窗口尺寸、主题模式、侧边栏展开状态等，确保重启后恢复；
- 样式管理：QML 样式通过 `Theme.res` 绑定项目现有 QSS 变量，避免重复定义；
- 资源加载：复用项目 `resource.qrc` 资源文件，QML 直接引用现有图标、图片资源（如 `:/gallery/images/logo.png`）。

## 六、动画优化策略
1. QML 渲染优化：标题栏和侧边栏启用 `layer.enabled: true` 硬件加速，复杂动画使用 `Behavior` 简化状态过渡；
2. 减少跨层通信开销：UI 交互信号（如菜单点击）直接触发功能窗切换，核心数据通过 `QQmlProperty` 批量传递；
3. 时序对齐：侧边栏动画与 Widget 功能窗显示动画同步触发（QML 动画启动时发送信号，Widget 侧通过 `QPropertyAnimation` 同步淡入）；
4. 高 DPI 适配：QML 中通过 `Screen.devicePixelRatio` 同步 Widget 侧 DPI 缩放比例，确保尺寸一致性。

## 七、兼容性与风险控制
### 1. 兼容性保障
- 项目版本兼容：基于 `PySide6>=6.4.2`（项目最低依赖），不引入额外第三方依赖；
- 原有功能兼容：新架构 `FluentHybridWindow` 与原有 `FluentWindow` 并行存在，用户可按需选择；
- 系统兼容：支持 Win32/Linux/macOS（与项目现有平台一致），QML 动效通过 Qt Quick 跨平台渲染适配。

### 2. 风险与解决方案
| 风险点                     | 解决方案                                                               |
|----------------------------|------------------------------------------------------------------------|
| QML 与 Widget 尺寸冲突     | 适配层监听 QML 侧边栏尺寸变化，实时更新 `QStackedWidget` 几何布局       |
| 动画卡顿                   | 禁用 QML 过度绘制，Widget 功能窗避免重绘频繁的操作（如实时刷新表格）     |
| 主题同步延迟               | 采用「先动画后同步」时序，通过信号槽确保 QML 动画结束后再更新 Widget 样式 |
| 窗口拖动冲突               | QML 标题栏 `MouseArea` 仅响应顶部区域，避免与 Widget 交互区域重叠         |

## 八、部署与使用
### 1. 项目目录扩展（不修改原有结构）
```
zhiyiyo-pyqt-fluent-widgets/
├─ qfluentwidgets/
│  └─ hybrid/（新增混合架构模块）
│     ├─ __init__.py
│     ├─ fluent_hybrid_window.py（FluentHybridWindow 主类）
│     ├─ communication_bridge.py（适配层通信）
│     └─ qml/（QML 交互层）
│        ├─ TitleBar.qml
│        ├─ SideNavigation.qml
│        └─ qml.qrc（QML 资源文件）
└─ examples/
   └─ hybrid_window_demo/（新增示例）
      └─ demo.py（使用示例）
```

### 2. 快速使用示例
```python
from qfluentwidgets import FluentHybridWindow, SettingInterface, HomeInterface
from qfluentwidgets.hybrid import FluentHybridWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 1. 创建混合架构主窗口
    window = FluentHybridWindow()
    # 2. 添加 Widget 功能窗
    window.add_function_widget("home", HomeInterface())
    window.add_function_widget("setting", SettingInterface())
    # 3. 配置 QML 侧边栏导航
    window.set_side_nav_items([
        {"routeKey": "home", "text": "首页", "icon": "FIF.HOME"},
        {"routeKey": "setting", "text": "设置", "icon": "FIF.SETTING"}
    ])
    window.show()
    app.exec()
```

## 九、扩展方向
1. 支持 QML 侧边栏自定义皮肤，复用项目 `Acrylic` 材质效果；
2. 增加 QML 动画模板库（如淡入淡出、缩放、滑动），支持业务定制；
3. 适配项目 `NavigationInterface` 原有导航逻辑，实现 QML 侧边栏与原有导航无缝切换。

---

需要我帮你生成 **核心模块的代码实现（如 `FluentHybridWindow` 主类、QML 标题栏/侧边栏代码）**，直接基于项目现有依赖可运行？

当前文件内容过长，豆包只阅读了前 25%。