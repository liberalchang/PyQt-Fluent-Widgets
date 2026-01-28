# Vispy 组件使用指南

## 📋 目录

- [快速开始](#快速开始)
- [2D 可视化](#2d-可视化)
- [3D 可视化](#3d-可视化)
- [高级用法](#高级用法)
- [最佳实践](#最佳实践)
- [常见问题](#常见问题)

## 🚀 快速开始

### 安装依赖

```bash
pip install vispy
```

### 基本导入

```python
from qfluentwidgets import VispyWidget2D, VispyWidget3D
import numpy as np
```

### 最简单的示例

```python
from PySide6.QtWidgets import QApplication, QMainWindow
from qfluentwidgets import VispyWidget2D
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 创建 2D 可视化组件
        self.vispy_widget = VispyWidget2D(self)
        self.setCentralWidget(self.vispy_widget)
        
        # 添加一些随机点
        points = np.random.rand(100, 2) * 10
        self.vispy_widget.add_point(points, color='red', size=5)
        
        # 自动调整视图
        self.vispy_widget.auto_range()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
```

## 📊 2D 可视化

### 基本图形元素

#### 1. 点云 (Point Cloud)

```python
# 基本点云
points = np.random.rand(1000, 2) * 10
vispy_widget.add_point(points, color='blue', size=3)

# 多色点云
points = np.random.rand(1000, 2) * 10
colors = np.random.rand(1000, 3)  # RGB 颜色
sizes = np.random.rand(1000) * 10  # 不同大小
vispy_widget.add_point(points, color=colors, size=sizes)
```

#### 2. 线条 (Lines)

```python
# 单条线
line_points = np.array([[0, 0], [1, 1], [2, 0], [3, 1]])
vispy_widget.add_line(line_points, color='green', width=2)

# 多条线
lines = [
    np.array([[0, 0], [1, 1]]),
    np.array([[0, 1], [1, 0]]),
    np.array([[0.5, 0], [0.5, 1]])
]
vispy_widget.add_line(lines, color=['red', 'green', 'blue'], width=2)
```

#### 3. 图像 (Images)

```python
# 显示图像
from PIL import Image
import numpy as np

# 加载图像
image = Image.open('path/to/image.png')
image_array = np.array(image)

# 显示
vispy_widget.add_image(image_array, origin='lower-left')

# 调整图像位置和大小
vispy_widget.add_image(image_array, 
                      pos=[5, 5], 
                      scale=[2, 2],
                      origin='lower-left')
```

#### 4. 文本 (Text)

```python
# 添加文本
vispy_widget.add_text('Hello World', pos=[5, 5], color='white', size=12)

# 多个文本
texts = ['Point A', 'Point B', 'Point C']
positions = [[1, 1], [2, 2], [3, 3]]
vispy_widget.add_text(texts, pos=positions, color='red', size=10)
```

### 高级 2D 功能

#### 1. 网格显示

```python
# 显示网格
vispy_widget.show_grid(True)

# 自定义网格
vispy_widget.show_grid(True, color='gray', alpha=0.5, spacing=1.0)
```

#### 2. 坐标轴

```python
# 显示坐标轴
vispy_widget.show_axes(True)

# 自定义坐标轴
vispy_widget.show_axes(True, color='black', width=2)
```

#### 3. 主题设置

```python
# 设置主题
vispy_widget.set_theme('dark')    # 暗色主题
vispy_widget.set_theme('light')   # 亮色主题

# 自定义背景色
vispy_widget.set_background_color('#1E1E1E')
```

## 🎮 3D 可视化

### 基本图形元素

#### 1. 3D 点云

```python
# 3D 点云
points = np.random.rand(1000, 3) * 10
vispy_widget.add_points(points, color='red', size=5)

# 带法向量的点云
points = np.random.rand(1000, 3) * 10
normals = np.random.rand(1000, 3) - 0.5  # 归一化法向量
vispy_widget.add_points(points, color='blue', size=3, face_color=normals)
```

#### 2. 网格 (Mesh)

```python
# 创建网格数据
vertices = np.array([
    [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],  # 底面
    [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]   # 顶面
])

faces = np.array([
    [0, 1, 2], [0, 2, 3],  # 底面
    [4, 5, 6], [4, 6, 7],  # 顶面
    [0, 1, 5], [0, 5, 4],  # 前面
    [2, 3, 7], [2, 7, 6],  # 后面
    [0, 3, 7], [0, 7, 4],  # 左面
    [1, 2, 6], [1, 6, 5]   # 右面
])

# 添加网格
vispy_widget.add_mesh(vertices, faces, color='lightblue', shading='smooth')

# 带纹理的网格
texture = np.random.rand(256, 256, 3)  # 随机纹理
vispy_widget.add_mesh(vertices, faces, texture=texture, shading='smooth')
```

#### 3. 曲面 (Surface)

```python
# 创建曲面数据
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# 添加曲面
vispy_widget.add_surface(Z, x=x, y=y, color='viridis')

# 带着色的曲面
colors = np.cos(np.sqrt(X**2 + Y**2))
vispy_widget.add_surface(Z, x=x, y=y, face_color=colors, colormap='plasma')
```

#### 4. 体数据 (Volume)

```python
# 创建 3D 体数据
volume = np.random.rand(64, 64, 64)

# 添加体数据
vispy_widget.add_volume(volume, threshold=0.5, cmap='grays')

# 带颜色的体数据
rgb_volume = np.random.rand(64, 64, 64, 3)
vispy_widget.add_volume(rgb_volume, threshold=0.3, interpolation='linear')
```

### 高级 3D 功能

#### 1. 光照设置

```python
# 设置环境光
vispy_widget.set_ambient_light(0.3)

# 设置方向光
vispy_widget.set_directional_light(direction=[1, 1, 1], intensity=0.7)

# 设置点光源
vispy_widget.set_point_light(position=[5, 5, 5], intensity=0.8, color='white')
```

#### 2. 坐标轴

```python
# 显示 3D 坐标轴
vispy_widget.show_axes(True)

# 自定义坐标轴
vispy_widget.show_axes(True, 
                      x_color='red', 
                      y_color='green', 
                      z_color='blue',
                      length=2.0)
```

#### 3. 相机控制

```python
# 设置相机位置
vispy_widget.set_camera_position(eye=[5, 5, 5], center=[0, 0, 0], up=[0, 0, 1])

# 重置相机
vispy_widget.reset_camera()

# 设置视角
vispy_widget.set_camera_fov(45)  # 45度视角
```

## 🔧 高级用法

### 1. 动画更新

```python
import time
from PySide6 QtCore import QTimer

class AnimatedVisualization(QMainWindow):
    def __init__(self):
        super().__init__()
        self.vispy_widget = VispyWidget2D(self)
        self.setCentralWidget(self.vispy_widget)
        
        # 初始化数据
        self.points = np.random.rand(100, 2)
        self.point_visual = self.vispy_widget.add_point(self.points, color='red')
        
        # 设置动画定时器
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(50)  # 20 FPS
    
    def update_animation(self):
        # 更新点位置
        self.points += np.random.randn(100, 2) * 0.01
        self.point_visual.set_data(self.points)
        self.vispy_widget.update()
```

### 2. 交互事件

```python
class InteractiveVisualization(QMainWindow):
    def __init__(self):
        super().__init__()
        self.vispy_widget = VispyWidget2D(self)
        self.setCentralWidget(self.vispy_widget)
        
        # 连接鼠标事件
        self.vispy_widget.mousePressEvent.connect(self.on_mouse_press)
        self.vispy_widget.mouseMoveEvent.connect(self.on_mouse_move)
        self.vispy_widget.mouseReleaseEvent.connect(self.on_mouse_release)
    
    def on_mouse_press(self, event):
        # 获取鼠标位置的数据坐标
        data_pos = self.vispy_widget.canvas.scene.node_transform(
            self.vispy_widget.canvas.scene, event.pos)
        print(f"Mouse pressed at: {data_pos}")
    
    def on_mouse_move(self, event):
        if event.buttons():
            # 鼠标拖拽时的处理
            pass
    
    def on_mouse_release(self, event):
        # 鼠标释放时的处理
        pass
```

### 3. 多图层管理

```python
# 创建多个图层
layer1 = vispy_widget.add_point(points1, color='red', name='layer1')
layer2 = vispy_widget.add_line(lines2, color='blue', name='layer2')
layer3 = vispy_widget.add_image(image3, name='layer3')

# 控制图层可见性
vispy_widget.set_layer_visible('layer1', False)  # 隐藏 layer1
vispy_widget.set_layer_visible('layer2', True)   # 显示 layer2

# 获取图层
layer = vispy_widget.get_layer('layer1')
if layer:
    layer.set_color('green')  # 修改颜色

# 删除图层
vispy_widget.remove_layer('layer3')
```

### 4. 自定义着色器

```python
# 创建自定义着色器的点云
vertex_shader = """
attribute vec3 a_position;
attribute vec3 a_color;
varying vec3 v_color;

void main() {
    gl_Position = vec4(a_position, 1.0);
    gl_PointSize = 10.0;
    v_color = a_color;
}
"""

fragment_shader = """
varying vec3 v_color;

void main() {
    gl_FragColor = vec4(v_color, 1.0);
}
"""

# 使用自定义着色器
vispy_widget.add_point(points, 
                      color=colors,
                      vertex_shader=vertex_shader,
                      fragment_shader=fragment_shader)
```

## 💡 最佳实践

### 1. 性能优化

```python
# 批量添加数据而不是逐个添加
points = np.random.rand(10000, 2)
vispy_widget.add_point(points)  # ✅ 好的做法

# 避免
# for point in points:
#     vispy_widget.add_point(point)  # ❌ 差的做法

# 使用适当的数据类型
points = np.random.rand(10000, 2).astype(np.float32)  # ✅ 使用 float32
```

### 2. 内存管理

```python
# 及时清理不需要的数据
old_visual = vispy_widget.add_point(old_data)
# ... 使用 old_visual
vispy_widget.remove_visual(old_visual)  # 及时清理

# 使用 clear() 清空所有数据
vispy_widget.clear()
```

### 3. 错误处理

```python
try:
    vispy_widget = VispyWidget2D()
    points = np.random.rand(1000, 2)
    vispy_widget.add_point(points)
except Exception as e:
    print(f"Vispy 初始化失败: {e}")
    # 降级到普通 QWidget
    from PySide6.QtWidgets import QLabel
    vispy_widget = QLabel("Vispy 不可用")
```

### 4. 主题适配

```python
from qfluentwidgets import isDarkTheme

class ThemedVisualization(QMainWindow):
    def __init__(self):
        super().__init__()
        self.vispy_widget = VispyWidget2D(self)
        self.setCentralWidget(self.vispy_widget)
        
        # 根据当前主题设置可视化主题
        self.update_theme()
    
    def update_theme(self):
        if isDarkTheme():
            self.vispy_widget.set_theme('dark')
        else:
            self.vispy_widget.set_theme('light')
```

## ❓ 常见问题

### Q1: Vispy 组件不显示任何内容？

**A**: 检查以下几点：
```python
# 1. 确保 Vispy 已安装
import vispy
print(f"Vispy version: {vispy.__version__}")

# 2. 检查数据范围
points = np.random.rand(100, 2)
print(f"Points range: [{points.min()}, {points.max()}]")

# 3. 调用 auto_range()
vispy_widget.auto_range()

# 4. 手动更新
vispy_widget.update()
```

### Q2: 性能很差，渲染很慢？

**A**: 尝试以下优化：
```python
# 1. 减少数据点数量
points = points[::10]  # 每10个点取1个

# 2. 使用更简单的着色器
vispy_widget.add_point(points, shading='flat')

# 3. 关闭不必要的功能
vispy_widget.show_grid(False)
vispy_widget.show_axes(False)
```

### Q3: 如何保存渲染结果？

**A**: 使用截图功能：
```python
# 保存为图片
vispy_widget.save_screenshot('output.png')

# 获取图像数据
image_data = vispy_widget.get_screenshot()
```

### Q4: 如何在 FluentWindow 中使用？

**A**: 集成到 FluentWindow：
```python
from qfluentwidgets import FluentWindow, NavigationItemPosition, FluentIcon as FIF

class VispyWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        
        # 创建可视化界面
        self.vispy_interface = VispyInterface(self)
        self.addSubInterface(
            self.vispy_interface, 
            FIF.CHART, 
            'Visualization'
        )

class VispyInterface(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        
        self.vispy_widget = VispyWidget2D(self)
        layout.addWidget(self.vispy_widget)
        
        # 添加数据
        points = np.random.rand(1000, 2)
        self.vispy_widget.add_point(points)
        self.vispy_widget.auto_range()
```

### Q5: 如何处理大数据集？

**A**: 使用数据分块和 LOD：
```python
# 分块处理
def add_large_dataset(large_points, chunk_size=10000):
    for i in range(0, len(large_points), chunk_size):
        chunk = large_points[i:i+chunk_size]
        vispy_widget.add_point(chunk, alpha=0.5)

# 使用细节层次 (LOD)
def add_with_lod(points, distances):
    # 根据距离使用不同的点大小和密度
    far_points = points[distances > 10][::5]  # 远距离，低密度
    near_points = points[distances <= 10]     # 近距离，高密度
    
    vispy_widget.add_point(far_points, size=2, alpha=0.3)
    vispy_widget.add_point(near_points, size=5, alpha=0.8)
```

## 🎯 总结

Vispy 组件提供了强大而易用的 2D/3D 可视化功能：

- **简单易用**: Qt 风格的 API，学习成本低
- **功能丰富**: 支持点、线、面、体等各种可视化元素
- **性能优秀**: 基于 OpenGL 的高性能渲染
- **扩展性强**: 易于添加自定义功能
- **集成良好**: 与 FluentWidgets 完美集成

通过本指南，你应该能够快速上手使用 Vispy 组件进行各种数据可视化任务。
