Vispy Visuals Vispy可视化元素模块
=========================================

Vispy Visuals 模块提供统一的 Visual 元素接口，封装 Vispy 的各种可视化对象。
该模块支持2D和3D图形元素，提供统一的可见性、数据更新和销毁操作。

主要功能
--------

- **统一接口** - 提供所有Visual元素的抽象基类
- **2D图形** - 支持线条、标记点、矩形、椭圆等2D元素
- **3D图形** - 支持网格模型、曲面图、体数据、坐标轴等3D元素
- **边界计算** - 提供统一的边界框计算方法
- **动态更新** - 支持实时更新元素属性
- **OpenGL优化** - 针对大量数据的性能优化

核心组件
--------

VisualEntry
~~~~~~~~~~~

Visual元素基类，所有场景图形元素的基础接口。

.. code-block:: python

   from qfluentwidgets.components.vispy.vispy_visuals import VisualEntry
   
   # 创建自定义Visual元素
   class CustomVisual(VisualEntry):
       def __init__(self, parent_view, visual_id):
           super().__init__(parent_view, visual_id)
           # 初始化具体实现
       
       def set_visible(self, visible: bool) -> None:
           self.visible = visible
           # 实现可见性设置
       
       def update_data(self, **kwargs) -> None:
           # 实现数据更新
           pass
       
       def destroy(self) -> None:
           # 实现销毁逻辑
           pass
       
       @property
       def bounds(self) -> np.ndarray:
           # 返回边界框 [[min_x, min_y, min_z], [max_x, max_y, max_z]]
           return np.array([[0, 0, 0], [1, 1, 1]])

**抽象方法：**
- ``set_visible()`` - 设置可见性
- ``update_data()`` - 更新数据
- ``destroy()`` - 销毁Visual对象
- ``bounds`` - 返回边界框

2D Visual元素
~~~~~~~~~~~~

LineEntry
~~~~~~~~~~

2D/3D线条元素。

.. code-block:: python

   from qfluentwidgets.components.vispy.vispy_visuals import LineEntry
   import numpy as np
   
   # 创建线条元素
   line = LineEntry(
       parent_view=view,
       visual_id="line_001",
       pos=np.array([[0, 0, 0], [10, 10, 0]],  # 3D点坐标
       color='red',
       width=2.0
   )
   
   # 更新线条
   line.update_data(pos=np.array([[0, 0, 0], [20, 20, 0]]))
   
   # 设置可见性
   line.set_visible(True)
   
   # 获取边界
   bounds = line.bounds

MarkersEntry
~~~~~~~~~~~~

2D/3D标记点元素。

.. code-block:: python

   from qfluentwidgets.components.vispy.vispy_visuals import MarkersEntry
   import numpy as np
   
   # 创建标记点元素
   markers = MarkersEntry(
       parent_view=view,
       visual_id="markers_001",
       pos=np.array([[0, 0, 0], [5, 5, 0], [10, 0, 0]]),
       colors=['red', 'green', 'blue'],
       sizes=[5.0, 8.0, 6.0],
       symbol='o'
   )
   
   # 更新标记点
   markers.update_data(
       pos=np.array([[0, 0, 0], [7, 7, 0], [14, 0, 0]]),
       colors=['yellow', 'cyan', 'magenta']
   )
   
   # 设置边缘样式
   markers.update_data(edge_color='black', edge_width=1.0)

RectangleEntry
~~~~~~~~~~~~

2D矩形元素。

.. code-block:: python

   from qfluentwidgets.components.vispy.vispy_visuals import RectangleEntry
   
   # 创建矩形元素
   rect = RectangleEntry(
       parent_view=view,
       visual_id="rect_001",
       pos=(0, 0),  # 左上角坐标
       size=(10, 5),  # 宽度和高度
       color='blue',
       border_color='white'
   )
   
   # 更新矩形
   rect.update_data(pos=(5, 5), size=(20, 10))
   
   # 获取边界
   bounds = rect.bounds  # [[0, 0, 0], [25, 15, 0]]

EllipseEntry
~~~~~~~~~~~~

2D椭圆/圆形元素。

.. code-block:: python

   from qfluentwidgets.components.vispy.vispy_visuals import EllipseEntry
   
   # 创建圆形元素
   circle = EllipseEntry(
       parent_view=view,
       visual_id="circle_001",
       center=(10, 10),  # 中心坐标
       radius=5.0,  # 半径
       color='green'
   )
   
   # 创建椭圆元素
   ellipse = EllipseEntry(
       parent_view=view,
       visual_id="ellipse_001",
       center=(10, 10),
       radius=(8.0, 5.0),  # x半径, y半径
       color='purple'
   )
   
   # 更新椭圆
   ellipse.update_data(center=(15, 15), radius=(10.0, 6.0))

3D Visual元素
~~~~~~~~~~~~

MeshEntry
~~~~~~~~~~

3D网格模型元素。

.. code-block:: python

   from qfluentwidgets.components.vispy.vispy_visuals import MeshEntry
   import numpy as np
   
   # 创建立方体网格
   vertices = np.array([
       [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],  # 底面
       [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]   # 顶面
   ], dtype=np.float32)
   
   faces = np.array([
       [0, 1, 2], [3, 4, 5],  # 底面和顶面
       [0, 1, 5], [0, 2, 3],  # 侧面
       [1, 2, 6], [2, 3, 7],  # 另一个侧面
   [0, 3, 7], [0, 5, 4],  # 第三个侧面
       [1, 5, 6], [3, 2, 7],  # 第四个侧面
   ], dtype=np.uint32)
   
   # 创建网格元素
   mesh = MeshEntry(
       parent_view=view,
       visual_id="mesh_001",
       vertices=vertices,
       faces=faces,
       color='cyan',
       shading='smooth'
   )
   
   # 更新网格
   mesh.update_data(color='magenta', shading='flat')

SurfacePlotEntry
~~~~~~~~~~~~~~~~

3D曲面图元素。

.. code-block:: python

   from qfluentwidgets.components.vispy.vispy_visuals import SurfacePlotEntry
   import numpy as np
   
   # 创建曲面数据
   x = np.linspace(-5, 5, 20)
   y = np.linspace(-5, 5, 20)
   X, Y = np.meshgrid(x, y)
   Z = np.sin(np.sqrt(X**2 + Y**2))
   
   # 创建曲面图元素
   surface = SurfacePlotEntry(
       parent_view=view,
       visual_id="surface_001",
       x=X,
       y=Y,
       z=Z,
       color='yellow',
       shading='smooth'
   )
   
   # 更新曲面
   surface.update_data(z=np.cos(np.sqrt(X**2 + Y**2)))

VolumeEntry
~~~~~~~~~~~~

3D体数据元素。

.. code-block:: python

   from qfluentwidgets.components.vispy.vispy_visuals import VolumeEntry
   import numpy as np
   
   # 创建3D体数据（3D MRI 数据示例）
   data = np.random.rand(50, 50, 50)  # 50x50x50 体数据
   
   # 创建体元素
   volume = VolumeEntry(
       parent_view=view,
       visual_id="volume_001",
       data=data,
       method='mip',  # 最大强度投影
       threshold=0.5
   )
   
   # 更新体数据
   volume.update_data(method='iso', threshold=0.7)

AxesEntry
~~~~~~~~~~~~

3D坐标轴元素。

.. code-block:: python

   from qfluentwidgets.components.vispy.vispy_visuals import AxesEntry
   
   # 创建坐标轴元素
   axes = AxesEntry(
       parent_view=view,
       visual_id="axes_001",
       size=10.0
   )
   
   # 更新坐标轴大小
   axes.update_data(size=15.0)

GridLinesEntry
~~~~~~~~~~~~

3D网格线元素。

.. code-block:: python

   from qfluentwidgets.components.vispy.vispy_visuals import GridLinesEntry
   
   # 创建网格线元素
   grid = GridLinesEntry(
       parent_view=view,
       visual_id="grid_001",
       scale=(1.0, 1.0, 1.0),  # 网格间距
       color=(0.5, 0.5, 0.5, 0.3)  # 半透明灰色
   )
   
   # 更新网格
   grid.update_data(scale=(2.0, 2.0, 2.0))

实际应用
--------

基本2D图形应用
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.vispy_visuals import (
       LineEntry, MarkersEntry, RectangleEntry, EllipseEntry
   )
   from qfluentwidgets.components.vispy.vispy_canvas import VispyCanvas2D
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   import numpy as np
   
   class Basic2DVisualsWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_canvas()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("基本2D图形应用")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.line_btn = PushButton("添加线条")
           self.markers_btn = PushButton("添加标记")
           self.rect_btn = PushButton("添加矩形")
           self.ellipse_btn = PushButton("添加椭圆")
           self.clear_btn = PushButton("清空画布")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.line_btn)
           header_layout.addWidget(self.markers_btn)
           header_layout.addWidget(self.rect_btn)
           header_layout.addWidget(self.ellipse_btn)
           header_layout.addWidget(self.clear_btn)
           
           # 创建2D画布
           self.canvas = VispyCanvas2D()
           
           # 显示当前状态
           self.status_label = Label("状态: 2D画布已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.canvas.native_widget)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_canvas(self):
           """设置画布和视觉元素"""
           self.visual_elements = []
           self.status_label.setText("状态: 2D画布已设置")
       
       def setup_connections(self):
           """设置连接"""
           self.line_btn.clicked.connect(self.add_line)
           self.markers_btn.clicked.connect(self.add_markers)
           self.rect_btn.clicked.connect(self.add_rectangle)
           self.ellipse_btn.clicked.connect(self.add_ellipse)
           self.clear_btn.clicked.connect(self.clear_canvas)
       
       def add_line(self):
           """添加线条元素"""
           import random
           
           # 随机生成线条点
           points = np.array([
               [random.uniform(-10, 10), random.uniform(-10, 10), 0],
               [random.uniform(-10, 10), random.uniform(-10, 10), 0]
           ], dtype=np.float32)
           
           # 随机颜色
           colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']
           color = random.choice(colors)
           
           # 创建线条元素
           line = LineEntry(
               parent_view=self.canvas.view,
               visual_id=f"line_{len(self.visual_elements)}",
               pos=points,
               color=color,
               width=random.uniform(1, 3)
           )
           
           self.visual_elements.append(line)
           self.status_label.setText(f"状态: 已添加线条，颜色: {color}")
       
       def add_markers(self):
           """添加标记点元素"""
           import random
           
           # 随机生成标记点
           num_points = random.randint(3, 8)
           positions = np.random.uniform(-10, 10, (num_points, 3))
           
           # 随机颜色和大小
           colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']
           colors_array = np.random.choice(colors, num_points)
           sizes = np.random.uniform(3, 8, num_points)
           
           # 创建标记点元素
           markers = MarkersEntry(
               parent_view=self.canvas.view,
               visual_id=f"markers_{len(self.visual_elements)}",
               pos=positions,
               colors=colors_array,
               sizes=sizes,
               symbol=random.choice(['o', 's', '^', 'd'])
           )
           
           self.visual_elements.append(markers)
           self.status_label.setText(f"状态: 已添加 {num_points} 个标记点")
       
       def add_rectangle(self):
           """添加矩形元素"""
           import random
           
           # 随机生成矩形参数
           pos = (random.uniform(-10, 5), random.uniform(-10, 5))
           size = (random.uniform(5, 15), random.uniform(5, 10))
           
           # 随机颜色
           colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']
           color = random.choice(colors)
           
           # 创建矩形元素
           rect = RectangleEntry(
               parent_view=self.canvas.view,
               visual_id=f"rect_{len(self.visual_elements)}",
               pos=pos,
               size=size,
               color=color,
               border_color='white'
           )
           
           self.visual_elements.append(rect)
           self.status_label.setText(f"状态: 已添加矩形，位置: {pos}")
       
       def add_ellipse(self):
           """添加椭圆元素"""
           import random
           
           # 随机生成椭圆参数
           center = (random.uniform(-5, 5), random.uniform(-5, 5))
           radius = (random.uniform(3, 8), random.uniform(2, 6))
           
           # 随机颜色
           colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']
           color = random.choice(colors)
           
           # 创建椭圆元素
           ellipse = EllipseEntry(
               parent_view=self.canvas.view,
               visual_id=f"ellipse_{len(self.visual_elements)}",
               center=center,
               radius=radius,
               color=color
           )
           
           self.visual_elements.append(ellipse)
           self.status_label.setText(f"状态: 已添加椭圆，中心: {center}")
       
       def clear_canvas(self):
           """清空画布"""
           for element in self.visual_elements:
               element.destroy()
           self.visual_elements.clear()
           self.status_label.setText("状态: 画布已清空")

高级3D图形应用
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.vispy_visuals import (
       MeshEntry, SurfacePlotEntry, VolumeEntry, AxesEntry, GridLinesEntry
   )
   from qfluentwidgets.components.vispy.vispy_canvas import VispyCanvas3D
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   import numpy as np
   
   class Advanced3DVisualsWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_canvas()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("高级3D图形应用")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.mesh_btn = PushButton("添加网格")
           self.surface_btn = PushButton("添加曲面")
           self.volume_btn = PushButton("添加体数据")
           self.axes_btn = PushButton("添加坐标轴")
           self.grid_btn = PushButton("添加网格线")
           self.clear_btn = PushButton("清空画布")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.mesh_btn)
           header_layout.addWidget(self.surface_btn)
           header_layout.addWidget(self.volume_btn)
           header_layout.addWidget(self.axes_btn)
           header_layout.addWidget(self.grid_btn)
           header_layout.addWidget(self.clear_btn)
           
           # 创建3D画布
           self.canvas = VispyCanvas3D()
           
           # 显示当前状态
           self.status_label = Label("状态: 3D画布已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.canvas.native_widget)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_canvas(self):
           """设置画布和3D视觉元素"""
           self.visual_elements = []
           self.status_label.setText("状态: 3D画布已设置")
       
       def setup_connections(self):
           """设置连接"""
           self.mesh_btn.clicked.connect(self.add_mesh)
           self.surface_btn.clicked.connect(self.add_surface)
           self.volume_btn.clicked.connect(self.add_volume)
           self.axes_btn.clicked.connect(self.add_axes)
           self.grid_btn.clicked.connect(self.add_grid)
           self.clear_btn.clicked.connect(self.clear_canvas)
       
       def add_mesh(self):
           """添加网格模型"""
           # 创建立方体网格
           vertices = np.array([
               [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],  # 底面
               [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]   # 顶面
           ], dtype=np.float32)
           
           faces = np.array([
               [0, 1, 2], [3, 4, 5],  # 底面和顶面
               [0, 1, 5], [0, 2, 3],  # 侧面
               [1, 2, 6], [2, 3, 7],  # 另一个侧面
               [0, 3, 7], [0, 5, 4],  # 第三个侧面
               [1, 5, 6], [3, 2, 7],  # 第四个侧面
           ], dtype=np.uint32)
           
           # 创建网格元素
           mesh = MeshEntry(
               parent_view=self.canvas.view,
               visual_id=f"mesh_{len(self.visual_elements)}",
               vertices=vertices,
               faces=faces,
               color='cyan',
               shading='smooth'
           )
           
           self.visual_elements.append(mesh)
           self.status_label.setText("状态: 已添加立方体网格")
       
       def add_surface(self):
           """添加曲面图"""
           # 创建参数化曲面
           x = np.linspace(-5, 5, 20)
           y = np.linspace(-5, 5, 20)
           X, Y = np.meshgrid(x, y)
           Z = np.sin(np.sqrt(X**2 + Y**2)) * np.cos(np.sqrt(X**2 + Y**2))
           
           # 创建曲面图元素
           surface = SurfacePlotEntry(
               parent_view=self.canvas.view,
               visual_id=f"surface_{len(self.visual_elements)}",
               x=X,
               y=Y,
               z=Z,
               color='yellow',
               shading='smooth'
           )
           
           self.visual_elements.append(surface)
           self.status_label.setText("状态: 已添加参数化曲面")
       
       def add_volume(self):
           """添加体数据"""
           # 创建3D体数据
           data = np.random.rand(30, 30, 30)
           
           # 创建体元素
           volume = VolumeEntry(
               parent_view=self.canvas.view,
               visual_id=f"volume_{len(self.visual_elements)}",
               data=data,
               method='mip',
               threshold=0.5
           )
           
           self.visual_elements.append(volume)
           self.status_label.setText("状态: 已添加3D体数据")
       
       def add_axes(self):
           """添加坐标轴"""
           # 创建坐标轴元素
           axes = AxesEntry(
               parent_view=self.canvas.view,
               visual_id=f"axes_{len(self.visual_elements)}",
               size=10.0
           )
           
           self.visual_elements.append(axes)
           self.status_label.setText("状态: 已添加3D坐标轴")
       
       def add_grid(self):
           """添加网格线"""
           # 创建网格线元素
           grid = GridLinesEntry(
               parent_view=self.canvas.view,
               visual_id=f"grid_{len(self.visual_elements)}",
               scale=(1.0, 1.0, 1.0),
               color=(0.5, 0.5, 0.5, 0.3)
           )
           
           self.visual_elements.append(grid)
           self.status_label.setText("状态: 已添加3D网格线")
       
       def clear_canvas(self):
           """清空画布"""
           for element in self.visual_elements:
               element.destroy()
           self.visual_elements.clear()
           self.status_label.setText("状态: 3D画布已清空")

最佳实践
--------

1. **元素管理** - 合理管理Visual元素的生命周期
2. **性能优化** - 使用批量更新和OpenGL优化
3. **边界计算** - 利用统一的边界框计算方法
4. **内存管理** - 及时销毁不需要的Visual元素
5. **错误处理** - 妥善处理VISPY不可用的情况

注意事项
--------

- 需要安装vispy库才能正常工作
- 3D元素需要正确的顶点和面数据格式
- 大量元素可能影响渲染性能
- 边界框计算基于元素的几何属性
- 动态更新会触发重新渲染
- OpenGL状态优化适用于大量数据

相关模块
--------

- :doc:`components.vispy.vispy_canvas` - Vispy画布
- :doc:`components.vispy.vispy_widget` - Vispy控件
- :doc:`components.vispy.drawing` - 交互式绘图
- :doc:`common.geometry` - 几何计算
- :doc:`common.color` - 颜色管理
