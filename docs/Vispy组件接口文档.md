# Vispy 组件接口文档

## 📋 目录

- [核心接口](#核心接口)
- [2D 组件接口](#2d-组件接口)
- [3D 组件接口](#3d-组件接口)
- [Canvas 接口](#canvas-接口)
- [Visual 接口](#visual-接口)
- [工具函数](#工具函数)

## 🎯 核心接口

### VispyWidget2D

2D 可视化组件的主要接口。

#### 构造函数

```python
VispyWidget2D(parent: QWidget = None)
```

**参数:**
- `parent`: 父组件，默认为 None

#### 数据添加方法

##### add_point()

添加点云数据。

```python
add_point(pos: np.ndarray, 
          color: Union[str, np.ndarray] = 'blue', 
          size: Union[float, np.ndarray] = 5.0,
          alpha: float = 1.0,
          edge_color: Union[str, np.ndarray] = None,
          edge_width: float = 1.0,
          symbol: str = 'disc',
          name: str = None) -> MarkersEntry
```

**参数:**
- `pos`: 点位置数组，形状为 (N, 2)
- `color`: 颜色，可以是颜色字符串或 RGB 数组
- `size`: 点大小，可以是标量或数组
- `alpha`: 透明度 (0-1)
- `edge_color`: 边框颜色
- `edge_width`: 边框宽度
- `symbol`: 符号类型 ('disc', 'square', 'triangle', 'cross', etc.)
- `name`: 元素名称

**返回:** `MarkersEntry` 对象

**示例:**
```python
# 基本点云
points = np.random.rand(100, 2)
vispy_widget.add_point(points, color='red', size=5)

# 多色点云
colors = np.random.rand(100, 3)
sizes = np.random.rand(100) * 10
vispy_widget.add_point(points, color=colors, size=sizes)
```

##### add_line()

添加线条数据。

```python
add_line(pos: Union[np.ndarray, List[np.ndarray]], 
         color: Union[str, np.ndarray, List[str]] = 'blue',
         width: Union[float, np.ndarray] = 1.0,
         style: str = 'solid',
         alpha: float = 1.0,
         connect: str = 'strip',
         name: str = None) -> LineEntry
```

**参数:**
- `pos`: 线条位置，可以是单个数组或数组列表
- `color`: 线条颜色
- `width`: 线条宽度
- `style`: 线条样式 ('solid', 'dashed', 'dotted')
- `alpha`: 透明度
- `connect`: 连接方式 ('strip', 'segments')
- `name`: 元素名称

**返回:** `LineEntry` 对象

**示例:**
```python
# 单条线
line = np.array([[0, 0], [1, 1], [2, 0]])
vispy_widget.add_line(line, color='green', width=2)

# 多条线
lines = [np.array([[0, 0], [1, 1]]), np.array([[0, 1], [1, 0]])]
vispy_widget.add_line(lines, color=['red', 'blue'])
```

##### add_image()

添加图像数据。

```python
add_image(data: np.ndarray,
          pos: tuple = (0, 0),
          scale: tuple = (1, 1),
          origin: str = 'lower-left',
          interpolation: str = 'bilinear',
          name: str = None) -> ImageEntry
```

**参数:**
- `data`: 图像数据数组
- `pos`: 图像位置 (x, y)
- `scale`: 缩放比例 (sx, sy)
- `origin`: 原点位置 ('lower-left', 'upper-left')
- `interpolation`: 插值方式
- `name`: 元素名称

**返回:** `ImageEntry` 对象

**示例:**
```python
# 显示图像
image = np.random.rand(256, 256, 3)
vispy_widget.add_image(image, pos=(5, 5), scale=(2, 2))
```

##### add_text()

添加文本标注。

```python
add_text(text: Union[str, List[str]],
         pos: Union[tuple, List[tuple]],
         color: str = 'white',
         size: float = 12.0,
         anchor: str = 'center',
         name: str = None) -> TextEntry
```

**参数:**
- `text`: 文本内容，可以是字符串或字符串列表
- `pos`: 文本位置，可以是坐标或坐标列表
- `color`: 文本颜色
- `size`: 字体大小
- `anchor`: 锚点位置 ('center', 'top-left', etc.)
- `name`: 元素名称

**返回:** `TextEntry` 对象

**示例:**
```python
# 单个文本
vispy_widget.add_text('Hello', pos=(5, 5), color='red')

# 多个文本
texts = ['A', 'B', 'C']
positions = [(1, 1), (2, 2), (3, 3)]
vispy_widget.add_text(texts, pos=positions, color='blue')
```

#### 视图控制方法

##### auto_range()

自动调整视图以显示所有数据。

```python
auto_range(padding: float = 0.1, aspect: float = None)
```

**参数:**
- `padding`: 边距比例
- `aspect`: 宽高比，None 表示自动

##### reset_view()

重置视图到初始状态。

```python
reset_view()
```

##### set_xlim()

设置 X 轴范围。

```python
set_xlim(xmin: float, xmax: float)
```

##### set_ylim()

设置 Y 轴范围。

```python
set_ylim(ymin: float, ymax: float)
```

##### get_xlim()

获取当前 X 轴范围。

```python
get_xlim() -> tuple[float, float]
```

##### get_ylim()

获取当前 Y 轴范围。

```python
get_ylim() -> tuple[float, float]
```

#### 显示控制方法

##### show_grid()

显示/隐藏网格。

```python
show_grid(show: bool = True, 
         color: str = 'gray', 
         alpha: float = 0.5,
         spacing: float = 1.0)
```

##### show_axes()

显示/隐藏坐标轴。

```python
show_axes(show: bool = True,
         color: str = 'black',
         width: float = 1.0)
```

##### set_theme()

设置显示主题。

```python
set_theme(theme: str)
```

**参数:**
- `theme`: 主题名称 ('light', 'dark')

##### set_background_color()

设置背景颜色。

```python
set_background_color(color: str)
```

#### 数据管理方法

##### clear()

清空所有数据。

```python
clear()
```

##### remove_visual()

移除指定的视觉元素。

```python
remove_visual(visual: VisualEntry)
```

##### get_visual()

获取指定的视觉元素。

```python
get_visual(name: str) -> VisualEntry
```

##### list_visuals()

列出所有视觉元素。

```python
list_visuals() -> List[VisualEntry]
```

### VispyWidget3D

3D 可视化组件的主要接口。

#### 构造函数

```python
VispyWidget3D(parent: QWidget = None)
```

#### 数据添加方法

##### add_points()

添加 3D 点云。

```python
add_points(pos: np.ndarray,
           color: Union[str, np.ndarray] = 'blue',
           size: Union[float, np.ndarray] = 5.0,
           alpha: float = 1.0,
           edge_color: Union[str, np.ndarray] = None,
           edge_width: float = 1.0,
           face_color: Union[str, np.ndarray] = None,
           shading: str = 'smooth',
           name: str = None) -> MarkersEntry
```

**参数:**
- `pos`: 点位置数组，形状为 (N, 3)
- `color`: 颜色
- `size`: 点大小
- `alpha`: 透明度
- `edge_color`: 边框颜色
- `edge_width`: 边框宽度
- `face_color`: 面颜色
- `shading`: 着色方式 ('flat', 'smooth')
- `name`: 元素名称

##### add_mesh()

添加 3D 网格。

```python
add_mesh(vertices: np.ndarray,
         faces: np.ndarray,
         color: Union[str, np.ndarray] = 'lightblue',
         vertex_colors: np.ndarray = None,
         face_colors: np.ndarray = None,
         texture: np.ndarray = None,
         shading: str = 'smooth',
         backface_culling: bool = True,
         name: str = None) -> MeshEntry
```

**参数:**
- `vertices`: 顶点数组，形状为 (N, 3)
- `faces`: 面片数组，形状为 (M, 3)
- `color`: 默认颜色
- `vertex_colors`: 顶点颜色
- `face_colors`: 面片颜色
- `texture`: 纹理图像
- `shading`: 着色方式
- `backface_culling`: 是否启用背面剔除
- `name`: 元素名称

##### add_surface()

添加 3D 曲面。

```python
add_surface(z: np.ndarray,
           x: np.ndarray = None,
           y: np.ndarray = None,
           color: Union[str, np.ndarray] = 'viridis',
           face_color: np.ndarray = None,
           colormap: str = 'viridis',
           shading: str = 'smooth',
           name: str = None) -> SurfacePlotEntry
```

**参数:**
- `z`: Z 值数组
- `x`: X 坐标数组
- `y`: Y 坐标数组
- `color`: 颜色或颜色映射
- `face_color`: 面颜色
- `colormap`: 颜色映射名称
- `shading`: 着色方式
- `name`: 元素名称

##### add_volume()

添加 3D 体数据。

```python
add_volume(data: np.ndarray,
           threshold: float = 0.5,
           cmap: str = 'grays',
           interpolation: str = 'linear',
           relative_step_size: float = 1.0,
           name: str = None) -> VolumeEntry
```

**参数:**
- `data`: 3D 体数据数组
- `threshold`: 显示阈值
- `cmap`: 颜色映射
- `interpolation`: 插值方式
- `relative_step_size`: 相对步长
- `name`: 元素名称

#### 相机控制方法

##### set_camera_position()

设置相机位置。

```python
set_camera_position(eye: tuple, center: tuple = (0, 0, 0), up: tuple = (0, 0, 1))
```

**参数:**
- `eye`: 相机位置 (x, y, z)
- `center`: 观察目标位置
- `up`: 上方向向量

##### reset_camera()

重置相机到默认位置。

```python
reset_camera()
```

##### set_camera_fov()

设置相机视角。

```python
set_camera_fov(fov: float)
```

**参数:**
- `fov`: 视角角度（度）

##### get_camera_position()

获取当前相机位置。

```python
get_camera_position() -> dict
```

**返回:** 包含 'eye', 'center', 'up' 的字典

#### 光照控制方法

##### set_ambient_light()

设置环境光。

```python
set_ambient_light(intensity: float)
```

##### set_directional_light()

设置方向光。

```python
set_directional_light(direction: tuple, intensity: float = 1.0, color: str = 'white')
```

##### set_point_light()

设置点光源。

```python
set_point_light(position: tuple, intensity: float = 1.0, color: str = 'white')
```

## 🎨 Canvas 接口

### VispyCanvas2D

2D 渲染画布的接口。

#### 构造函数

```python
VispyCanvas2D(keys: str = 'interactive', show: bool = False)
```

#### 主题设置

##### set_theme()

设置画布主题。

```python
set_theme(is_dark: bool)
```

##### update_theme()

更新主题。

```python
update_theme()
```

#### 网格管理

##### create_grid()

创建网格。

```python
create_grid(spacing: float = 1.0, color: str = 'gray', alpha: float = 0.5)
```

##### remove_grid()

移除网格。

```python
remove_grid()
```

##### update_grid()

更新网格。

```python
update_grid()
```

### VispyCanvas3D

3D 渲染画布的接口。

#### 坐标轴管理

##### create_axes()

创建坐标轴。

```python
create_axes(size: float = 1.0, color: str = 'black')
```

##### remove_axes()

移除坐标轴。

```python
remove_axes()
```

##### update_axes()

更新坐标轴。

```python
update_axes()
```

## 🎭 Visual 接口

### VisualEntry (基类)

所有视觉元素的基类。

#### 属性

- `visual`: Vispy Visual 对象
- `parent_view`: 父视图
- `scene`: 场景对象
- `visible`: 可见性
- `name`: 元素名称
- `visual_id`: 唯一标识符

#### 方法

##### set_data()

设置数据。

```python
set_data(**kwargs)
```

##### set_visible()

设置可见性。

```python
set_visible(visible: bool)
```

##### get_visible()

获取可见性。

```python
get_visible() -> bool
```

##### set_color()

设置颜色。

```python
set_color(color: Union[str, np.ndarray])
```

##### set_alpha()

设置透明度。

```python
set_alpha(alpha: float)
```

##### update()

更新显示。

```python
update()
```

##### remove()

移除元素。

```python
remove()
```

##### get_bounds()

获取边界框。

```python
get_bounds() -> np.ndarray
```

**返回:** 形状为 (2, 3) 的数组，表示最小和最大坐标

### MarkersEntry

点云元素的接口。

#### 特有方法

##### set_size()

设置点大小。

```python
set_size(size: Union[float, np.ndarray])
```

##### set_symbol()

设置符号类型。

```python
set_symbol(symbol: str)
```

##### set_edge_color()

设置边框颜色。

```python
set_edge_color(color: Union[str, np.ndarray])
```

##### set_edge_width()

设置边框宽度。

```python
set_edge_width(width: float)
```

### LineEntry

线条元素的接口。

#### 特有方法

##### set_width()

设置线条宽度。

```python
set_width(width: Union[float, np.ndarray])
```

##### set_style()

设置线条样式。

```python
set_style(style: str)
```

##### set_connect()

设置连接方式。

```python
set_connect(connect: str)
```

### MeshEntry

网格元素的接口。

#### 特有方法

##### set_vertex_colors()

设置顶点颜色。

```python
set_vertex_colors(colors: np.ndarray)
```

##### set_face_colors()

设置面片颜色。

```python
set_face_colors(colors: np.ndarray)
```

##### set_texture()

设置纹理。

```python
set_texture(texture: np.ndarray)
```

##### set_shading()

设置着色方式。

```python
set_shading(shading: str)
```

##### set_backface_culling()

设置背面剔除。

```python
set_backface_culling(enabled: bool)
```

### ImageEntry

图像元素的接口。

#### 特有方法

##### set_pos()

设置位置。

```python
set_pos(pos: tuple)
```

##### set_scale()

设置缩放。

```python
set_scale(scale: tuple)
```

##### set_interpolation()

设置插值方式。

```python
set_interpolation(interpolation: str)
```

### TextEntry

文本元素的接口。

#### 特有方法

##### set_text()

设置文本内容。

```python
set_text(text: Union[str, List[str]])
```

##### set_size()

设置字体大小。

```python
set_size(size: float)
```

##### set_anchor()

设置锚点。

```python
set_anchor(anchor: str)
```

## 🛠️ 工具函数

### 全局函数

#### initialize_vispy()

初始化 Vispy 后端。

```python
initialize_vispy()
```

#### VISPY_AVAILABLE

检查 Vispy 是否可用。

```python
VISPY_AVAILABLE -> bool
```

### 颜色工具

#### color_to_array()

将颜色字符串转换为 RGB 数组。

```python
color_to_array(color: str) -> np.ndarray
```

#### hex_to_rgb()

将十六进制颜色转换为 RGB。

```python
hex_to_rgb(hex_color: str) -> tuple[int, int, int]
```

#### rgb_to_hex()

将 RGB 转换为十六进制颜色。

```python
rgb_to_hex(r: int, g: int, b: int) -> str
```

### 数据工具

#### normalize_data()

标准化数据。

```python
normalize_data(data: np.ndarray) -> np.ndarray
```

#### rescale_data()

重新缩放数据。

```python
rescale_data(data: np.ndarray, target_range: tuple) -> np.ndarray
```

#### compute_bounds()

计算数据边界。

```python
compute_bounds(data: np.ndarray) -> tuple[tuple, tuple]
```

## 📊 事件接口

### 鼠标事件

#### mousePressEvent

鼠标按下事件。

```python
mousePressEvent(event: QMouseEvent)
```

#### mouseMoveEvent

鼠标移动事件。

```python
mouseMoveEvent(event: QMouseEvent)
```

#### mouseReleaseEvent

鼠标释放事件。

```python
mouseReleaseEvent(event: QMouseEvent)
```

#### wheelEvent

滚轮事件。

```python
wheelEvent(event: QWheelEvent)
```

### 键盘事件

#### keyPressEvent

键盘按下事件。

```python
keyPressEvent(event: QKeyEvent)
```

#### keyReleaseEvent

键盘释放事件。

```python
keyReleaseEvent(event: QKeyEvent)
```

### 自定义事件

#### data_updated_event

数据更新事件。

```python
data_updated_event(visual: VisualEntry)
```

#### theme_changed_event

主题变更事件。

```python
theme_changed_event(is_dark: bool)
```

## 🔧 配置接口

### 全局配置

#### set_default_theme()

设置默认主题。

```python
set_default_theme(theme: str)
```

#### get_default_theme()

获取默认主题。

```python
get_default_theme() -> str
```

#### set_performance_mode()

设置性能模式。

```python
set_performance_mode(mode: str)  # 'quality', 'performance', 'balanced'
```

### 渲染配置

#### set_fps_limit()

设置帧率限制。

```python
set_fps_limit(fps: int)
```

#### enable_vsync()

启用垂直同步。

```python
enable_vsync(enabled: bool)
```

#### set_antialiasing()

设置抗锯齿。

```python
set_antialiasing(enabled: bool, samples: int = 4)
```

## 🎯 总结

Vispy 组件提供了完整的 2D/3D 可视化接口：

- **统一的 API**: 2D 和 3D 组件使用相似的接口设计
- **丰富的功能**: 支持点、线、面、体等各种可视化元素
- **灵活的配置**: 提供详细的显示和行为配置选项
- **事件驱动**: 支持丰富的交互事件处理
- **性能优化**: 提供多层次的性能控制选项

通过这些接口，开发者可以轻松构建各种复杂的数据可视化应用。
