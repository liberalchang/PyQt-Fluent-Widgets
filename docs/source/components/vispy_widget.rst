Vispy Widget Vispy控件模块
================================

Vispy Widget 模块提供 VispyWidget2D 和 VispyWidget3D 控件，集成主题管理和数据接口。
该模块提供高级的2D和3D图形控件，支持多种图形元素的绘制和管理。

主要功能
--------

- **2D图形** - 支持线条、标记点、矩形、椭圆、多边形、图像、文本等
- **3D图形** - 支持点云、网格、曲面、体数据、坐标轴、网格线等
- **主题管理** - 自动适配亮色/暗色主题
- **信号机制** - 提供图形元素添加/移除信号
- **降级处理** - Vispy不可用时提供友好提示
- **统一接口** - 提供一致的图形操作接口

核心组件
--------

VispyWidget2D
~~~~~~~~~~~~~~

2D Vispy图形控件，提供2D图形绘制功能。

.. code-block:: python

   from qfluentwidgets.components.vispy.vispy_widget import VispyWidget2D
   import numpy as np
   
   # 创建2D图形控件
   widget_2d = VispyWidget2D(parent=parent)
   
   # 添加线条
   line_id = widget_2d.add_line(
       pos=np.array([[0, 0], [10, 10]]),
       color='red',
       width=2.0
   )
   
   # 添加标记点
   markers_id = widget_2d.add_markers(
       pos=np.array([[5, 5], [8, 3], [2, 7]]),
       colors=['blue', 'green', 'yellow'],
       sizes=[5.0, 8.0, 6.0],
       symbol='o'
   )
   
   # 添加矩形
   rect_id = widget_2d.add_rectangle(
       pos=(1, 1),
       size=(8, 6),
       color='cyan',
       border_color='white'
   )
   
   # 连接信号
   widget_2d.visualAdded.connect(self.on_visual_added)
   widget_2d.visualRemoved.connect(self.on_visual_removed)

**主要信号：**
- ``visualAdded`` - 图形元素添加信号
- ``visualRemoved`` - 图形元素移除信号

**主要方法：**
- ``add_line()`` - 添加2D折线/曲线
- ``add_markers()`` - 添加2D散点标记
- ``add_rectangle()`` - 添加2D矩形
- ``add_ellipse()`` - 添加2D椭圆/圆形
- ``add_polygon()`` - 添加2D多边形
- ``add_image()`` - 添加2D图像
- ``add_text()`` - 添加2D文本标注
- ``remove_visual()`` - 移除指定Visual元素
- ``update_visual()`` - 更新Visual元素数据
- ``set_visible()`` - 设置Visual元素可见性
- ``clear_all()`` - 清空所有Visual元素
- ``auto_range()`` - 自动调整相机范围
- ``set_theme()`` - 设置主题

VispyWidget3D
~~~~~~~~~~~~~~

3D Vispy图形控件，提供3D图形绘制功能。

.. code-block:: python

   from qfluentwidgets.components.vispy.vispy_widget import VispyWidget3D
   import numpy as np
   
   # 创建3D图形控件
   widget_3d = VispyWidget3D(parent=parent, camera_mode='turntable')
   
   # 添加3D标记点
   points_id = widget_3d.add_markers(
       pos=np.array([[0, 0, 0], [5, 5, 5], [10, 0, 0]]),
       colors=['red', 'green', 'blue'],
       sizes=[10.0, 15.0, 12.0]
   )
   
   # 添加3D网格
   vertices = np.array([
       [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
       [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]
   ], dtype=np.float32)
   
   faces = np.array([
       [0, 1, 2], [3, 4, 5], [0, 1, 5], [0, 2, 3],
       [1, 2, 6], [2, 3, 7], [0, 3, 7], [0, 5, 4],
       [1, 5, 6], [3, 2, 7]
   ], dtype=np.uint32)
   
   mesh_id = widget_3d.add_mesh(
       vertices=vertices,
       faces=faces,
       color='cyan',
       shading='smooth'
   )
   
   # 添加坐标轴
   axes_id = widget_3d.add_axes(size=10.0)
   
   # 连接信号
   widget_3d.visualAdded.connect(self.on_visual_added)
   widget_3d.visualRemoved.connect(self.on_visual_removed)

**主要信号：**
- ``visualAdded`` - 图形元素添加信号
- ``visualRemoved`` - 图形元素移除信号

**主要方法：**
- ``add_markers()`` - 添加3D散点标记
- ``add_mesh()`` - 添加3D网格模型
- ``add_surface()`` - 添加3D曲面图
- ``add_volume()`` - 添加3D体数据
- ``add_axes()`` - 添加3D坐标轴
- ``add_gridlines()`` - 添加3D网格线
- ``add_text3d()`` - 添加3D文本标注
- ``remove_visual()`` - 移除指定Visual元素
- ``update_visual()`` - 更新Visual元素数据
- ``set_visible()`` - 设置Visual元素可见性
- ``clear_all()`` - 清空所有Visual元素
- ``auto_range()`` - 自动调整相机范围
- ``set_view()`` - 设置相机视角
- ``set_theme()`` - 设置主题

实际应用
--------

2D图形可视化应用
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.vispy_widget import VispyWidget2D
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   import numpy as np
   
   class Visualization2DWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_visualization()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("2D图形可视化应用")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.line_btn = PushButton("添加线条")
           self.scatter_btn = PushButton("添加散点")
           self.rect_btn = PushButton("添加矩形")
           self.circle_btn = PushButton("添加圆形")
           self.clear_btn = PushButton("清空画布")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.line_btn)
           header_layout.addWidget(self.scatter_btn)
           header_layout.addWidget(self.rect_btn)
           header_layout.addWidget(self.circle_btn)
           header_layout.addWidget(self.clear_btn)
           
           # 创建2D图形控件
           self.widget_2d = VispyWidget2D(parent=self)
           self.widget_2d.setFixedSize(800, 600)
           
           # 显示当前状态
           self.status_label = Label("状态: 2D图形控件已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.widget_2d)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_visualization(self):
           """设置可视化"""
           # 连接信号
           self.widget_2d.visualAdded.connect(self.on_visual_added)
           self.widget_2d.visualRemoved.connect(self.on_visual_removed)
           
           self.visual_count = 0
           self.status_label.setText("状态: 2D图形控件已设置")
       
       def setup_connections(self):
           """设置连接"""
           self.line_btn.clicked.connect(self.add_line)
           self.scatter_btn.clicked.connect(self.add_scatter)
           self.rect_btn.clicked.connect(self.add_rectangle)
           self.circle_btn.clicked.connect(self.add_circle)
           self.clear_btn.clicked.connect(self.clear_canvas)
       
       def add_line(self):
           """添加线条"""
           import random
           
           # 生成随机线条数据
           num_points = random.randint(5, 15)
           x = np.linspace(-10, 10, num_points)
           y = np.random.uniform(-8, 8, num_points)
           points = np.column_stack([x, y])
           
           # 随机颜色
           colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']
           color = random.choice(colors)
           
           # 添加线条
           line_id = self.widget_2d.add_line(
               pos=points,
               color=color,
               width=random.uniform(1, 3)
           )
           
           self.visual_count += 1
           self.status_label.setText(f"状态: 已添加线条 {self.visual_count}，颜色: {color}")
       
       def add_scatter(self):
           """添加散点"""
           import random
           
           # 生成随机散点数据
           num_points = random.randint(20, 100)
           positions = np.random.uniform(-10, 10, (num_points, 2))
           
           # 随机颜色和大小
           colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']
           colors_array = np.random.choice(colors, num_points)
           sizes = np.random.uniform(3, 10, num_points)
           
           # 添加散点
           scatter_id = self.widget_2d.add_markers(
               pos=positions,
               colors=colors_array,
               sizes=sizes,
               symbol=random.choice(['o', 's', '^', 'd'])
           )
           
           self.visual_count += 1
           self.status_label.setText(f"状态: 已添加散点 {self.visual_count}，{num_points} 个点")
       
       def add_rectangle(self):
           """添加矩形"""
           import random
           
           # 随机矩形参数
           pos = (random.uniform(-10, 5), random.uniform(-8, 4))
           size = (random.uniform(5, 15), random.uniform(3, 10))
           
           # 随机颜色
           colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']
           color = random.choice(colors)
           
           # 添加矩形
           rect_id = self.widget_2d.add_rectangle(
               pos=pos,
               size=size,
               color=color,
               border_color='white'
           )
           
           self.visual_count += 1
           self.status_label.setText(f"状态: 已添加矩形 {self.visual_count}，位置: {pos}")
       
       def add_circle(self):
           """添加圆形"""
           import random
           
           # 随机圆形参数
           center = (random.uniform(-5, 5), random.uniform(-5, 5))
           radius = random.uniform(2, 8)
           
           # 随机颜色
           colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']
           color = random.choice(colors)
           
           # 添加圆形
           circle_id = self.widget_2d.add_ellipse(
               center=center,
               radius=radius,
               color=color
           )
           
           self.visual_count += 1
           self.status_label.setText(f"状态: 已添加圆形 {self.visual_count}，中心: {center}")
       
       def clear_canvas(self):
           """清空画布"""
           self.widget_2d.clear_all()
           self.visual_count = 0
           self.status_label.setText("状态: 2D画布已清空")
       
       def on_visual_added(self, visual_id):
           """图形元素添加处理"""
           print(f"2D图形元素已添加: {visual_id}")
       
       def on_visual_removed(self, visual_id):
           """图形元素移除处理"""
           print(f"2D图形元素已移除: {visual_id}")

3D图形可视化应用
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.vispy_widget import VispyWidget3D
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   import numpy as np
   
   class Visualization3DWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_visualization()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("3D图形可视化应用")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.points_btn = PushButton("添加点云")
           self.mesh_btn = PushButton("添加网格")
           self.surface_btn = PushButton("添加曲面")
           self.axes_btn = PushButton("添加坐标轴")
           self.clear_btn = PushButton("清空画布")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.points_btn)
           header_layout.addWidget(self.mesh_btn)
           header_layout.addWidget(self.surface_btn)
           header_layout.addWidget(self.axes_btn)
           header_layout.addWidget(self.clear_btn)
           
           # 创建3D图形控件
           self.widget_3d = VispyWidget3D(parent=self, camera_mode='turntable')
           self.widget_3d.setFixedSize(800, 600)
           
           # 显示当前状态
           self.status_label = Label("状态: 3D图形控件已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.widget_3d)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_visualization(self):
           """设置可视化"""
           # 连接信号
           self.widget_3d.visualAdded.connect(self.on_visual_added)
           self.widget_3d.visualRemoved.connect(self.on_visual_removed)
           
           self.visual_count = 0
           self.status_label.setText("状态: 3D图形控件已设置")
       
       def setup_connections(self):
           """设置连接"""
           self.points_btn.clicked.connect(self.add_points)
           self.mesh_btn.clicked.connect(self.add_mesh)
           self.surface_btn.clicked.connect(self.add_surface)
           self.axes_btn.clicked.connect(self.add_axes)
           self.clear_btn.clicked.connect(self.clear_canvas)
       
       def add_points(self):
           """添加点云"""
           import random
           
           # 生成随机点云数据
           num_points = random.randint(100, 500)
           positions = np.random.uniform(-10, 10, (num_points, 3))
           
           # 随机颜色和大小
           colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']
           colors_array = np.random.choice(colors, num_points)
           sizes = np.random.uniform(2, 8, num_points)
           
           # 添加点云
           points_id = self.widget_3d.add_markers(
               pos=positions,
               colors=colors_array,
               sizes=sizes
           )
           
           self.visual_count += 1
           self.status_label.setText(f"状态: 已添加点云 {self.visual_count}，{num_points} 个点")
       
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
           
           # 随机颜色
           colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']
           color = random.choice(colors)
           
           # 添加网格
           mesh_id = self.widget_3d.add_mesh(
               vertices=vertices,
               faces=faces,
               color=color,
               shading='smooth'
           )
           
           self.visual_count += 1
           self.status_label.setText(f"状态: 已添加网格 {self.visual_count}，颜色: {color}")
       
       def add_surface(self):
           """添加曲面"""
           # 创建参数化曲面
           x = np.linspace(-5, 5, 30)
           y = np.linspace(-5, 5, 30)
           X, Y = np.meshgrid(x, y)
           Z = np.sin(np.sqrt(X**2 + Y**2)) * np.exp(-0.1 * (X**2 + Y**2))
           
           # 随机颜色
           colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']
           color = random.choice(colors)
           
           # 添加曲面
           surface_id = self.widget_3d.add_surface(
               x=X,
               y=Y,
               z=Z,
               color=color,
               shading='smooth'
           )
           
           self.visual_count += 1
           self.status_label.setText(f"状态: 已添加曲面 {self.visual_count}，颜色: {color}")
       
       def add_axes(self):
           """添加坐标轴"""
           # 随机大小
           size = random.uniform(5, 15)
           
           # 添加坐标轴
           axes_id = self.widget_3d.add_axes(size=size)
           
           self.visual_count += 1
           self.status_label.setText(f"状态: 已添加坐标轴 {self.visual_count}，大小: {size:.1f}")
       
       def clear_canvas(self):
           """清空画布"""
           self.widget_3d.clear_all()
           self.visual_count = 0
           self.status_label.setText("状态: 3D画布已清空")
       
       def on_visual_added(self, visual_id):
           """图形元素添加处理"""
           print(f"3D图形元素已添加: {visual_id}")
       
       def on_visual_removed(self, visual_id):
           """图形元素移除处理"""
           print(f"3D图形元素已移除: {visual_id}")

高级图形应用
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.vispy_widget import VispyWidget2D, VispyWidget3D
   from qfluentwidgets import CardWidget, Label, PushButton, TabWidget
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   import numpy as np
   
   class AdvancedVisualizationWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_visualization()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("高级图形可视化应用")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.theme_btn = PushButton("切换主题")
           self.auto_range_btn = PushButton("自动范围")
           self.export_btn = PushButton("导出数据")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.theme_btn)
           header_layout.addWidget(self.auto_range_btn)
           header_layout.addWidget(self.export_btn)
           
           # 创建选项卡控件
           self.tab_widget = TabWidget(parent=self)
           
           # 2D图形选项卡
           self.widget_2d = VispyWidget2D(parent=self)
           self.widget_2d.setFixedSize(800, 500)
           self.tab_widget.addTab(self.widget_2d, "2D图形")
           
           # 3D图形选项卡
           self.widget_3d = VispyWidget3D(parent=self, camera_mode='turntable')
           self.widget_3d.setFixedSize(800, 500)
           self.tab_widget.addTab(self.widget_3d, "3D图形")
           
           # 显示当前状态
           self.status_label = Label("状态: 高级图形控件已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.tab_widget)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_visualization(self):
           """设置可视化"""
           # 连接信号
           self.widget_2d.visualAdded.connect(self.on_2d_visual_added)
           self.widget_2d.visualRemoved.connect(self.on_2d_visual_removed)
           self.widget_3d.visualAdded.connect(self.on_3d_visual_added)
           self.widget_3d.visualRemoved.connect(self.on_3d_visual_removed)
           
           self.visual_count_2d = 0
           self.visual_count_3d = 0
           self.is_dark_theme = False
           
           # 添加示例数据
           self.add_sample_data()
           
           self.status_label.setText("状态: 高级图形控件已设置")
       
       def setup_connections(self):
           """设置连接"""
           self.theme_btn.clicked.connect(self.toggle_theme)
           self.auto_range_btn.clicked.connect(self.auto_range)
           self.export_btn.clicked.connect(self.export_data)
       
       def add_sample_data(self):
           """添加示例数据"""
           # 2D示例：正弦曲线
           x = np.linspace(-10, 10, 100)
           y = np.sin(x)
           points = np.column_stack([x, y])
           
           self.widget_2d.add_line(
               pos=points,
               color='blue',
               width=2.0
           )
           
           # 2D示例：散点
           scatter_points = np.random.normal(0, 2, (50, 2))
           self.widget_2d.add_markers(
               pos=scatter_points,
               colors='red',
               sizes=5.0
           )
           
           # 3D示例：螺旋线
           t = np.linspace(0, 4*np.pi, 200)
           x_spiral = t * np.cos(t)
           y_spiral = t * np.sin(t)
           z_spiral = t
           spiral_points = np.column_stack([x_spiral, y_spiral, z_spiral])
           
           self.widget_3d.add_markers(
               pos=spiral_points,
               colors='green',
               sizes=3.0
           )
           
           # 3D示例：球面
           u = np.linspace(0, 2 * np.pi, 30)
           v = np.linspace(0, np.pi, 20)
           x_sphere = 5 * np.outer(np.cos(u), np.sin(v))
           y_sphere = 5 * np.outer(np.sin(u), np.sin(v))
           z_sphere = 5 * np.outer(np.ones(np.size(u)), np.cos(v))
           
           self.widget_3d.add_surface(
               x=x_sphere,
               y=y_sphere,
               z=z_sphere,
               color='cyan',
               shading='smooth'
           )
           
           self.widget_3d.add_axes(size=10.0)
       
       def toggle_theme(self):
           """切换主题"""
           self.is_dark_theme = not self.is_dark_theme
           
           # 设置2D和3D控件主题
           self.widget_2d.set_theme(self.is_dark_theme)
           self.widget_3d.set_theme(self.is_dark_theme)
           
           theme_name = "暗色" if self.is_dark_theme else "亮色"
           self.status_label.setText(f"状态: 已切换到{theme_name}主题")
       
       def auto_range(self):
           """自动调整范围"""
           current_tab = self.tab_widget.currentIndex()
           
           if current_tab == 0:  # 2D
               self.widget_2d.auto_range()
               self.status_label.setText("状态: 2D图形已自动调整范围")
           else:  # 3D
               self.widget_3d.auto_range()
               self.status_label.setText("状态: 3D图形已自动调整范围")
       
       def export_data(self):
           """导出数据"""
           current_tab = self.tab_widget.currentIndex()
           
           if current_tab == 0:  # 2D
               self.status_label.setText("状态: 2D数据导出功能待实现")
           else:  # 3D
               self.status_label.setText("状态: 3D数据导出功能待实现")
       
       def on_2d_visual_added(self, visual_id):
           """2D图形元素添加处理"""
           self.visual_count_2d += 1
           print(f"2D图形元素已添加: {visual_id}")
       
       def on_2d_visual_removed(self, visual_id):
           """2D图形元素移除处理"""
           print(f"2D图形元素已移除: {visual_id}")
       
       def on_3d_visual_added(self, visual_id):
           """3D图形元素添加处理"""
           self.visual_count_3d += 1
           print(f"3D图形元素已添加: {visual_id}")
       
       def on_3d_visual_removed(self, visual_id):
           """3D图形元素移除处理"""
           print(f"3D图形元素已移除: {visual_id}")

最佳实践
--------

1. **主题管理** - 根据系统主题自动切换控件主题
2. **性能优化** - 合理控制图形元素数量
3. **信号处理** - 正确连接和处理图形元素信号
4. **内存管理** - 及时清理不需要的图形元素
5. **错误处理** - 妥善处理Vispy不可用的情况

注意事项
--------

- 需要安装vispy库才能正常工作
- 2D和3D控件使用不同的坐标系
- 图形元素ID是自动生成的唯一标识符
- 大量图形元素可能影响渲染性能
- 主题切换会影响所有图形元素
- 自动范围调整会考虑所有可见元素
- 3D控件支持多种相机模式和视角

相关模块
--------

- :doc:`components.vispy.vispy_canvas` - Vispy画布
- :doc:`components.vispy.vispy_visuals` - Vispy可视化元素
- :doc:`components.vispy.drawing` - 交互式绘图
- :doc:`common.theme` - 主题管理
- :doc:`common.style_sheet` - 样式表
