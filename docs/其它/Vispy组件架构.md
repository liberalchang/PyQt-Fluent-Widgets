# Vispy 组件架构文档

## 📋 目录

- [架构概览](#架构概览)
- [组件层次结构](#组件层次结构)
- [核心模块](#核心模块)
- [数据流](#数据流)
- [设计模式](#设计模式)
- [扩展性](#扩展性)

## 🏗️ 架构概览

Vispy 组件采用分层架构设计，将复杂的 3D 可视化功能封装为易用的 Qt 组件。

```
┌─────────────────────────────────────────────────────────┐
│                    应用层 (Application)                    │
├─────────────────────────────────────────────────────────┤
│                  VispyWidget (UI层)                      │
│  ┌─────────────────┐    ┌─────────────────┐              │
│  │  VispyWidget2D  │    │  VispyWidget3D  │              │
│  └─────────────────┘    └─────────────────┘              │
├─────────────────────────────────────────────────────────┤
│                 VispyCanvas (渲染层)                      │
│  ┌─────────────────┐    ┌─────────────────┐              │
│  │  VispyCanvas2D  │    │  VispyCanvas3D  │              │
│  └─────────────────┘    └─────────────────┘              │
├─────────────────────────────────────────────────────────┤
│                VispyVisuals (数据层)                      │
│  ┌─────────────────┐    ┌─────────────────┐              │
│  │  VisualEntry    │    │  具体Visual类   │              │
│  └─────────────────┘    └─────────────────┘              │
├─────────────────────────────────────────────────────────┤
│                   Vispy (引擎层)                         │
│              SceneCanvas + Scene + Visuals                │
└─────────────────────────────────────────────────────────┘
```

## 🔧 组件层次结构

### 1. Widget 层 (UI 接口层)

**职责**: 提供 Qt 风格的 API 接口，处理用户交互

#### VispyWidget2D
```python
class VispyWidget2D(QWidget):
    """2D 可视化组件"""
    
    # 核心功能
    - add_point()      # 添加点云
    - add_line()       # 添加线条
    - add_image()      # 添加图像
    - add_text()       # 添加文本
    - auto_range()     # 自动调整视图
    - clear()          # 清空场景
```

#### VispyWidget3D
```python
class VispyWidget3D(QWidget):
    """3D 可视化组件"""
    
    # 核心功能
    - add_points()     # 添加点云
    - add_mesh()       # 添加网格
    - add_surface()    # 添加曲面
    - add_volume()     # 添加体数据
    - auto_range()     # 自动调整视图
    - clear()          # 清空场景
```

### 2. Canvas 层 (渲染控制层)

**职责**: 管理 Vispy 场景、相机、渲染循环

#### VispyCanvasBase
```python
class VispyCanvasBase:
    """Canvas 基类"""
    
    # 核心属性
    - canvas: SceneCanvas        # Vispy 画布
    - view: ViewBox              # 视图容器
    - camera: Camera             # 相机对象
    - entries: Dict[str, VisualEntry]  # 视觉元素管理
```

#### VispyCanvas2D
```python
class VispyCanvas2D(VispyCanvasBase):
    """2D Canvas 实现"""
    
    # 特殊功能
    - PanZoomCamera: 支持 2D 平移和缩放
    - 网格显示: 坐标网格辅助
    - 主题适配: 明暗主题切换
```

#### VispyCanvas3D
```python
class VispyCanvas3D(VispyCanvasBase):
    """3D Canvas 实现"""
    
    # 特殊功能
    - TurntableCamera: 支持 3D 旋转
    - 坐标轴: XYZ 轴显示
    - 光照管理: 3D 光照效果
```

### 3. Visuals 层 (数据抽象层)

**职责**: 封装 Vispy Visual 对象，提供统一的数据接口

#### VisualEntry (基类)
```python
class VisualEntry:
    """视觉元素基类"""
    
    # 核心属性
    - visual: Visual              # Vispy Visual 对象
    - parent_view: ViewBox        # 父视图
    - scene: Scene                # 场景引用
    - visible: bool              # 可见性
    - name: str                  # 元素名称
    
    # 核心方法
    - set_data()                 # 设置数据
    - set_visible()              # 设置可见性
    - update()                   # 更新显示
    - remove()                   # 移除元素
```

#### 具体实现类
```python
# 2D 视觉元素
- PointVisualEntry      # 点云
- LineVisualEntry       # 线条
- ImageVisualEntry      # 图像
- TextVisualEntry       # 文本

# 3D 视觉元素  
- MeshVisualEntry       # 网格
- SurfaceVisualEntry    # 曲面
- VolumeVisualEntry     # 体数据
- AxesVisualEntry       # 坐标轴
```

## 🌊 数据流

### 数据添加流程
```
用户调用 API
    ↓
VispyWidget.xxx_add()
    ↓
VispyCanvas.add_visual()
    ↓
VisualEntry.set_data()
    ↓
Vispy Visual 更新
    ↓
SceneCanvas 渲染
```

### 渲染更新流程
```
Vispy 渲染循环
    ↓
SceneCanvas.update()
    ↓
所有 Visual.update()
    ↓
GPU 渲染
    ↓
显示输出
```

## 🎨 设计模式

### 1. 适配器模式 (Adapter Pattern)
- **目的**: 将 Vispy 的复杂 API 适配为简单的 Qt 风格接口
- **实现**: VispyWidget 作为适配器，简化 Vispy 的使用

### 2. 工厂模式 (Factory Pattern)
- **目的**: 统一创建不同类型的 VisualEntry
- **实现**: Canvas 中的 `add_xxx()` 方法

### 3. 观察者模式 (Observer Pattern)
- **目的**: 数据变化时自动更新显示
- **实现**: VisualEntry 的 `set_data()` 触发重绘

### 4. 策略模式 (Strategy Pattern)
- **目的**: 2D/3D 使用不同的相机和渲染策略
- **实现**: VispyCanvas2D/3D 的差异化实现

## 🔧 扩展性设计

### 1. 添加新的 Visual 类型

```python
# 1. 创建新的 VisualEntry 子类
class CustomVisualEntry(VisualEntry):
    def __init__(self, parent_view, scene, **kwargs):
        super().__init__(parent_view, scene)
        self.visual = CustomVisual(**kwargs)
    
    def set_data(self, data):
        self.visual.set_data(data)

# 2. 在 Canvas 中添加创建方法
class VispyCanvas2D:
    def add_custom(self, data, **kwargs):
        entry = CustomVisualEntry(self.view, self.canvas.scene, **kwargs)
        entry.set_data(data)
        return self._add_visual_entry(entry)
```

### 2. 自定义 Widget

```python
class CustomVispyWidget(VispyWidget2D):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 添加自定义功能
        self.setup_custom_features()
    
    def setup_custom_features(self):
        # 自定义初始化
        pass
```

### 3. 主题扩展

```python
class CustomTheme:
    @staticmethod
    def get_colors(is_dark):
        # 返回自定义颜色方案
        return {
            'background': '#1E1E1E' if is_dark else '#FFFFFF',
            'grid': '#333333' if is_dark else '#CCCCCC',
            'text': '#FFFFFF' if is_dark else '#000000'
        }
```

## 📊 性能优化

### 1. 数据管理
- **延迟渲染**: 批量数据更新时延迟渲染
- **LOD 系统**: 大数据集使用细节层次
- **视锥剔除**: 只渲染可见区域

### 2. 内存管理
- **对象池**: 重用 Visual 对象
- **数据缓存**: 缓存计算结果
- **垃圾回收**: 及时清理不用的对象

### 3. GPU 优化
- **批量渲染**: 合并相似对象的渲染
- **着色器优化**: 使用高效的 GLSL 着色器
- **纹理压缩**: 压缩大型纹理数据

## 🔄 事件处理

### 1. 鼠标事件
```python
# 2D: 平移和缩放
- 左键拖拽: 平移视图
- 滚轮: 缩放视图
- 右键: 重置视图

# 3D: 旋转和缩放  
- 左键拖拽: 旋转视图
- 滚轮: 缩放视图
- 右键: 平移视图
```

### 2. 键盘事件
```python
- R: 重置视图
- G: 切换网格显示
- F: 全屏显示
- ESC: 退出全屏
```

### 3. 自定义事件
```python
# 用户可以扩展事件处理
class CustomVispyWidget(VispyWidget2D):
    def mousePressEvent(self, event):
        # 自定义鼠标事件处理
        super().mousePressEvent(event)
```

## 🎯 总结

Vispy 组件架构的核心优势：

1. **分层清晰**: UI、渲染、数据三层分离
2. **接口统一**: 2D/3D 使用相似的 API
3. **扩展性强**: 易于添加新的 Visual 类型
4. **性能优化**: 多层次的性能优化策略
5. **Qt 集成**: 完美融入 Qt 生态系统

这种架构设计使得复杂的 3D 可视化变得简单易用，同时保持了高度的灵活性和扩展性。
