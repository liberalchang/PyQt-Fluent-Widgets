# ToolPanel 设计文档

## 产品概述

ToolPanel 是一个类似 Adobe Photoshop 工具栏的工具面板组件，提供灵活的工具选择和管理功能。该组件专为图形设计、图像编辑等需要大量工具切换的应用场景设计。

### 设计目标

- 提供直观的工具选择界面
- 支持灵活的布局和显示模式
- 实现响应式布局，适应不同屏幕尺寸
- 支持工具的二级选项扩展
- 遵循 Fluent2 设计规范，提供现代化的视觉体验

## 核心功能

### 1. 布局方向
- **水平布局**: 工具从左到右排列，适合顶部工具栏
- **垂直布局**: 工具从上到下排列，适合侧边工具栏
- **动态切换**: 支持运行时动态切换布局方向

### 2. 显示模式
- **仅图标**: 节省空间，适合图标语义明确的工具
- **图标+文本(旁边)**: 文本在图标右侧，适合水平布局
- **图标+文本(下方)**: 文本在图标下方，适合垂直布局

### 3. 工具按钮
- **可选中状态**: 工具支持选中/未选中两种状态
- **互斥选择**: 同一面板内只能选中一个工具
- **选中视觉反馈**: 选中工具显示主题色背景
- **悬停效果**: 鼠标悬停时显示半透明背景

### 4. 二级选项
- **触发方式**: 右键点击或长按（1秒）工具按钮
- **菜单展示**: 使用 CheckableMenu 显示子选项
- **子选项互斥**: 同一工具的子选项间互斥选择
- **视觉指示**: 有子选项的工具显示右下角小三角形标记

### 5. 响应式布局
- **自动隐藏**: 空间不足时自动隐藏超出的工具
- **更多按钮**: 隐藏的工具通过"更多"菜单访问
- **动态调整**: 容器尺寸变化时自动重新布局
- **智能计算**: 根据按钮尺寸和容器大小计算可见数量

### 6. 数据模型驱动
- **字典格式**: 使用简单的字典结构定义工具
- **批量创建**: 支持通过数据列表批量添加工具
- **状态导出**: 支持导出所有工具的当前状态
- **灵活扩展**: 支持自定义数据字段（userData）

### 7. 工具提示
- **集成 ToolTipFilter**: 使用项目统一的工具提示系统
- **显示快捷键**: 自动在工具提示中显示快捷键
- **延迟显示**: 300ms 延迟，避免频繁触发
- **位置控制**: 工具提示显示在工具按钮上方

### 8. 快捷键支持
- **全局配置**: 通过 qconfig 管理快捷键配置
- **显示提示**: 在工具提示中显示快捷键
- **预留接口**: 为未来的快捷键响应功能预留接口

### 9. 主题适配
- **双主题**: 完整支持浅色和深色主题
- **Fluent2 设计**: 遵循 Fluent2 设计规范
- **样式系统**: 使用 QSS 文件 + FluentStyleSheet 枚举
- **动态切换**: 支持运行时切换主题

## 技术架构

### 类层次结构

```
QFrame
  └─ ToolPanel                    # 工具面板容器
       ├─ VerticalToolPanel       # 垂直工具面板便捷类

TransparentToggleToolButton
  └─ ToolPanelButton              # 工具按钮
       └─ MoreToolsButton         # "更多工具"按钮

QWidget
  └─ ToolPanelSeparator           # 工具分隔符
```

### 核心组件

#### 1. ToolPanel (工具面板容器)

**职责**:
- 管理所有工具按钮和分隔符
- 实现响应式布局逻辑
- 处理工具的互斥选择
- 提供工具添加/删除接口
- 触发布局更新

**关键属性**:
```python
self._orientation: Qt.Orientation      # 布局方向
self._buttonGroup: QButtonGroup        # 按钮组（互斥控制）
self._widgets: List[QWidget]           # 所有子组件列表
self._hiddenWidgets: List[QWidget]     # 隐藏的组件列表
self.moreButton: MoreToolsButton       # "更多"按钮
self._spacing: int                     # 组件间距
self._buttonSize: QSize                # 按钮尺寸
```

**关键方法**:
```python
addTool()           # 添加单个工具
addTools()          # 批量添加工具
addSeparator()      # 添加分隔符
currentTool()       # 获取当前选中工具
getToolsData()      # 导出工具数据
setOrientation()    # 设置布局方向
updateGeometry()    # 更新布局
_visibleWidgets()   # 计算可见组件
_showMoreToolsMenu() # 显示更多菜单
```

**信号**:
```python
toolClicked(button: ToolPanelButton)    # 工具被点击
toolChanged(button: ToolPanelButton)    # 选中工具改变
```

#### 2. ToolPanelButton (工具按钮)

**职责**:
- 显示工具图标和文本
- 处理工具选中状态
- 管理二级选项数据
- 显示二级选项菜单
- 处理长按事件

**关键属性**:
```python
self._text: str                        # 按钮文本
self._toolData: Dict                   # 工具数据
self._subOptions: List[Dict]           # 二级选项列表
self._currentSubIndex: int             # 当前选中的二级选项索引
self._longPressTimer: QTimer           # 长按定时器
self._longPressThreshold: int          # 长按触发时间阈值
self._isLongPressing: bool            # 是否正在长按
```

**关键方法**:
```python
setSubOptions()         # 设置二级选项
currentSubOption()      # 获取当前二级选项
setCurrentSubOption()   # 设置当前二级选项
toolData()              # 获取工具数据
setToolData()           # 设置工具数据
_showSubOptionsMenu()   # 显示二级选项菜单
_onLongPress()          # 长按触发处理
mousePressEvent()       # 鼠标按下事件
mouseReleaseEvent()     # 鼠标释放事件
```

**信号**:
```python
subOptionChanged(index: int, option: Dict)  # 二级选项改变
```

#### 3. ToolPanelSeparator (分隔符)

**职责**:
- 在工具之间提供视觉分隔
- 支持水平和垂直两种方向
- 适应不同主题的颜色

**关键属性**:
```python
self._orientation: Qt.Orientation      # 分隔符方向
```

**关键方法**:
```python
setOrientation()    # 设置方向
paintEvent()        # 绘制分隔线
```

#### 4. MoreToolsButton ("更多工具"按钮)

**职责**:
- 显示"更多"图标
- 提供访问隐藏工具的入口

继承自 ToolPanelButton，但不可选中，不支持二级选项。

### 数据流

```
用户操作
  ├─ 点击工具按钮
  │    ├─ 左键: 选中工具
  │    │    ├─ 更新按钮选中状态
  │    │    ├─ 取消其他按钮选中状态（互斥）
  │    │    └─ 发出 toolClicked/toolChanged 信号
  │    └─ 右键: 显示二级选项菜单（如有）
  │         ├─ 创建 CheckableMenu
  │         ├─ 添加子选项动作
  │         └─ 显示菜单
  │
  ├─ 长按工具按钮（1秒）
  │    └─ 显示二级选项菜单（如有）
  │
  ├─ 点击"更多"按钮
  │    ├─ 创建 RoundMenu
  │    ├─ 添加隐藏工具动作
  │    └─ 显示菜单
  │
  ├─ 选择二级选项
  │    ├─ 更新按钮图标和文本
  │    ├─ 更新子选项选中状态
  │    └─ 发出 subOptionChanged 信号
  │
  └─ 调整容器尺寸
       ├─ 触发 resizeEvent
       ├─ 调用 updateGeometry
       ├─ 计算可见组件
       ├─ 更新组件位置
       └─ 显示/隐藏"更多"按钮
```

## 布局算法

### 水平布局

```python
def updateGeometry(self):
    # 1. 计算可见组件
    visible_widgets = self._visibleWidgets()
    
    # 2. 计算起始位置
    x = self._spacing
    y = (self.height() - self._buttonSize.height()) // 2
    
    # 3. 依次排列组件
    for widget in visible_widgets:
        widget.move(x, y)
        widget.show()
        
        if isinstance(widget, ToolPanelSeparator):
            x += 10 + self._spacing
        else:
            x += self._buttonSize.width() + self._spacing
    
    # 4. 显示/隐藏"更多"按钮
    if self._hiddenWidgets:
        self.moreButton.move(x, y)
        self.moreButton.show()
    else:
        self.moreButton.hide()
```

### 垂直布局

```python
def updateGeometry(self):
    # 1. 计算可见组件
    visible_widgets = self._visibleWidgets()
    
    # 2. 计算起始位置
    x = (self.width() - self._buttonSize.width()) // 2
    y = self._spacing
    
    # 3. 依次排列组件
    for widget in visible_widgets:
        widget.move(x, y)
        widget.show()
        
        if isinstance(widget, ToolPanelSeparator):
            y += 10 + self._spacing
        else:
            y += self._buttonSize.height() + self._spacing
    
    # 4. 显示/隐藏"更多"按钮
    if self._hiddenWidgets:
        self.moreButton.move(x, y)
        self.moreButton.show()
    else:
        self.moreButton.hide()
```

### 可见组件计算

```python
def _visibleWidgets(self) -> List[QWidget]:
    """计算可见组件列表"""
    # 1. 获取可用空间
    if self._orientation == Qt.Horizontal:
        available_space = self.width() - 2 * self._spacing
    else:
        available_space = self.height() - 2 * self._spacing
    
    # 2. 预留"更多"按钮空间
    more_button_space = self._buttonSize.width() + self._spacing
    available_space -= more_button_space
    
    # 3. 计算可以显示多少个组件
    visible = []
    hidden = []
    used_space = 0
    
    for widget in self._widgets:
        if isinstance(widget, ToolPanelSeparator):
            widget_space = 10 + self._spacing
        else:
            widget_space = self._buttonSize.width() + self._spacing
        
        if used_space + widget_space <= available_space:
            visible.append(widget)
            used_space += widget_space
        else:
            hidden.append(widget)
    
    # 4. 更新隐藏列表
    self._hiddenWidgets = hidden
    
    return visible
```

## 样式设计

### Fluent2 设计原则

1. **圆角**: 8px 圆角，柔和现代
2. **间距**: 8px 标准间距，12px/16px 内边距
3. **颜色**: 微妙的背景色，避免过于鲜艳
4. **动画**: 平滑的过渡效果（hover/pressed）
5. **对比度**: 确保在深色和浅色主题下都清晰可见

### 按钮状态样式

#### 正常状态
```css
ToolPanelButton {
    background-color: transparent;
    border: none;
    border-radius: 8px;
    padding: 8px;
}
```

#### 悬停状态
```css
ToolPanelButton:hover {
    background-color: rgba(0, 0, 0, 0.06);  /* 浅色主题 */
    background-color: rgba(255, 255, 255, 0.08);  /* 深色主题 */
}
```

#### 按下状态
```css
ToolPanelButton:pressed {
    background-color: rgba(0, 0, 0, 0.09);  /* 浅色主题 */
    background-color: rgba(255, 255, 255, 0.12);  /* 深色主题 */
}
```

#### 选中状态
```css
ToolPanelButton:checked {
    background-color: rgba(--ThemeColorPrimary, 0.1);  /* 使用主题色 */
    border: 1px solid --ThemeColorPrimary;
}
```

#### 禁用状态
```css
ToolPanelButton:disabled {
    opacity: 0.5;
}
```

### 分隔符样式

```css
ToolPanelSeparator[horizontal] {
    height: 1px;
    background-color: rgba(0, 0, 0, 0.08);  /* 浅色主题 */
    background-color: rgba(255, 255, 255, 0.08);  /* 深色主题 */
}

ToolPanelSeparator[vertical] {
    width: 1px;
    background-color: rgba(0, 0, 0, 0.08);  /* 浅色主题 */
    background-color: rgba(255, 255, 255, 0.08);  /* 深色主题 */
}
```

### 小三角形指示器

有二级选项的工具按钮右下角显示小三角形：

```python
def paintEvent(self, event):
    super().paintEvent(event)
    
    # 如果有子选项，绘制小三角形
    if self._subOptions:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # 三角形位置（右下角）
        x = self.width() - 12
        y = self.height() - 12
        
        # 绘制三角形
        triangle = QPolygon([
            QPoint(x, y + 6),
            QPoint(x + 6, y + 6),
            QPoint(x + 6, y)
        ])
        
        painter.setBrush(QColor(255, 255, 255, 180))
        painter.setPen(Qt.NoPen)
        painter.drawPolygon(triangle)
```

## 性能优化

### 1. 布局计算缓存

```python
def updateGeometry(self):
    # 缓存按钮尺寸，避免重复计算
    if not hasattr(self, '_cachedButtonSize'):
        self._cachedButtonSize = self._calculateButtonSize()
```

### 2. 增量更新

```python
def addTool(self, ...):
    # 添加工具后只更新必要的部分
    button = ToolPanelButton(...)
    self._widgets.append(button)
    
    # 只在必要时触发完整布局
    if self.isVisible():
        self.updateGeometry()
```

### 3. 事件节流

```python
def resizeEvent(self, event):
    # 使用定时器延迟布局更新，避免频繁计算
    if not hasattr(self, '_resizeTimer'):
        self._resizeTimer = QTimer(self)
        self._resizeTimer.setSingleShot(True)
        self._resizeTimer.timeout.connect(self.updateGeometry)
    
    self._resizeTimer.start(100)  # 100ms 延迟
```

### 4. 虚拟化（未来优化）

对于工具数量非常多的情况，可以实现虚拟化：
- 只创建可见范围内的按钮实例
- 滚动时动态创建/销毁按钮
- 使用对象池复用按钮实例

## 扩展性设计

### 1. 自定义按钮类

```python
class CustomToolButton(ToolPanelButton):
    """自定义工具按钮"""
    def __init__(self, icon=None, parent=None):
        super().__init__(icon, parent)
        # 自定义初始化
    
    def paintEvent(self, event):
        # 自定义绘制
        super().paintEvent(event)

# 使用自定义按钮
panel = ToolPanel()
panel._buttonFactory = CustomToolButton  # 设置按钮工厂
```

### 2. 自定义菜单

```python
def _showSubOptionsMenu(self):
    """重写菜单显示方法"""
    menu = CustomMenu(parent=self)
    # 自定义菜单逻辑
    menu.exec(...)
```

### 3. 插件钩子

预留钩子方法供子类扩展：

```python
def _beforeAddTool(self, tool_data: Dict) -> Dict:
    """添加工具前的钩子"""
    return tool_data

def _afterAddTool(self, button: ToolPanelButton):
    """添加工具后的钩子"""
    pass

def _beforeLayout(self):
    """布局前的钩子"""
    pass

def _afterLayout(self):
    """布局后的钩子"""
    pass
```

## 测试策略

### 1. 单元测试

```python
def test_add_tool():
    """测试添加工具"""
    panel = ToolPanel()
    button = panel.addTool(FluentIcon.BRUSH, 'Brush')
    assert button in panel._widgets
    assert button.text() == 'Brush'

def test_exclusive_selection():
    """测试互斥选择"""
    panel = ToolPanel()
    btn1 = panel.addTool(FluentIcon.BRUSH, 'Brush', checked=True)
    btn2 = panel.addTool(FluentIcon.EDIT, 'Eraser')
    
    btn2.click()
    assert btn2.isChecked()
    assert not btn1.isChecked()

def test_sub_options():
    """测试二级选项"""
    panel = ToolPanel()
    btn = panel.addTool(
        FluentIcon.BRUSH, 'Brush',
        subOptions=[
            {'icon': FluentIcon.BRUSH, 'name': 'Brush', 'checked': True},
            {'icon': FluentIcon.PENCIL_INK, 'name': 'Pencil', 'checked': False}
        ]
    )
    
    assert btn.currentSubOption()['name'] == 'Brush'
    btn.setCurrentSubOption(1)
    assert btn.currentSubOption()['name'] == 'Pencil'
```

### 2. 集成测试

```python
def test_responsive_layout():
    """测试响应式布局"""
    panel = ToolPanel()
    panel.resize(200, 50)
    
    # 添加多个工具
    for i in range(10):
        panel.addTool(FluentIcon.BRUSH, f'Tool {i}')
    
    # 检查是否有工具被隐藏
    panel.updateGeometry()
    assert len(panel._hiddenWidgets) > 0
    assert panel.moreButton.isVisible()
```

### 3. UI 测试

使用 pytest-qt 进行 UI 测试：

```python
def test_tool_click(qtbot):
    """测试工具点击"""
    panel = ToolPanel()
    btn = panel.addTool(FluentIcon.BRUSH, 'Brush')
    
    with qtbot.waitSignal(panel.toolClicked):
        qtbot.mouseClick(btn, Qt.LeftButton)
    
    assert btn.isChecked()

def test_right_click_menu(qtbot):
    """测试右键菜单"""
    panel = ToolPanel()
    btn = panel.addTool(
        FluentIcon.BRUSH, 'Brush',
        subOptions=[{'icon': FluentIcon.BRUSH, 'name': 'Sub1'}]
    )
    
    qtbot.mouseClick(btn, Qt.RightButton)
    # 验证菜单是否显示
    # ...
```

## 文档结构

```
docs/
├── TOOLPANEL_USAGE.md          # 使用文档
│   ├── 快速开始
│   ├── API 参考
│   ├── 示例代码
│   └── 常见问题
│
├── TOOLPANEL_DESIGN.md         # 设计文档（本文档）
│   ├── 架构设计
│   ├── 技术细节
│   ├── 性能优化
│   └── 扩展指南
│
└── examples/
    └── tool_panel_demo.py      # 完整示例
```

## 未来改进

### 短期 (1-2个月)

1. **拖放支持**: 支持拖放重新排序工具
2. **工具分组**: 支持工具分组折叠/展开
3. **自定义图标**: 支持自定义 SVG 图标
4. **动画效果**: 添加工具切换的动画效果

### 中期 (3-6个月)

1. **快捷键响应**: 实现全局快捷键响应功能
2. **工具预设**: 支持保存和加载工具预设配置
3. **上下文菜单**: 右键面板空白区域显示上下文菜单
4. **工具搜索**: 添加工具搜索功能

### 长期 (6个月+)

1. **虚拟化**: 实现大量工具的虚拟化渲染
2. **插件系统**: 提供完整的插件扩展系统
3. **工具统计**: 记录工具使用频率，智能排序
4. **多语言**: 支持国际化

## 总结

ToolPanel 是一个功能完整、设计精良的工具面板组件，具有以下特点：

✅ **易用性**: 简单的 API，数据驱动，快速上手  
✅ **灵活性**: 支持多种布局和显示模式，高度可定制  
✅ **响应式**: 自适应容器尺寸，智能隐藏溢出工具  
✅ **可扩展**: 预留钩子方法，支持自定义扩展  
✅ **高性能**: 优化的布局算法，流畅的交互体验  
✅ **现代化**: 遵循 Fluent2 设计规范，美观大方  

该组件适用于各种需要工具选择的应用场景，特别是图形设计、图像编辑、CAD 等专业软件。
