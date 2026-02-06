Drawing Visuals 绘图可视化元素模块
=======================================

Drawing Visuals 模块扩展 vispy_visuals 模块，添加交互式绘图需要的新图元类型。
该模块提供贝塞尔曲线、圆弧、带样式控制的多边形、矩形和椭圆等可视化元素。

主要功能
--------

- **贝塞尔曲线** - 支持二阶和三阶贝塞尔曲线渲染
- **圆弧元素** - 提供圆弧的可视化渲染
- **样式多边形** - 支持独立填充和边缘线条控制的多边形
- **样式矩形** - 提供带样式控制的矩形元素
- **样式椭圆** - 支持圆形和椭圆的样式控制
- **动态更新** - 支持图元数据的实时更新

核心组件
--------

BezierCurveEntry
~~~~~~~~~~~~~~~~

贝塞尔曲线元素，支持二阶和三阶贝塞尔曲线。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import BezierCurveEntry
   import numpy as np
   
   # 创建贝塞尔曲线
   control_points = np.array([[0, 0], [50, 100], [100, 0]], dtype=np.float32)
   bezier = BezierCurveEntry(
       parent_view=view,
       visual_id="bezier_1",
       control_points=control_points,
       degree=2,
       color='red',
       width=2.0,
       num_samples=50
   )
   
   # 更新控制点
   bezier.update_data(control_points=new_points)

**主要方法：**
- ``set_visible()`` - 设置可见性
- ``update_data()`` - 更新数据
- ``destroy()`` - 销毁元素

ArcEntry
~~~~~~~~~~

圆弧元素，通过参数方程采样生成圆弧上的点。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import ArcEntry
   
   # 创建圆弧
   arc = ArcEntry(
       parent_view=view,
       visual_id="arc_1",
       center=(50, 50),
       radius=30.0,
       start_angle=0.0,
       end_angle=90.0,
       color='blue',
       width=2.0,
       num_samples=50
   )
   
   # 更新圆弧参数
   arc.update_data(center=(60, 60), radius=40.0)

StyledPolygonEntry
~~~~~~~~~~~~~~~~~~

带样式控制的多边形元素，支持独立的填充和边缘线条控制。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import StyledPolygonEntry
   import numpy as np
   
   # 创建多边形
   vertices = np.array([[0, 0], [100, 0], [50, 80]], dtype=np.float32)
   polygon = StyledPolygonEntry(
       parent_view=view,
       visual_id="polygon_1",
       vertices=vertices,
       fill_color=(0.5, 0.5, 1.0, 0.8),
       border_color=(1.0, 1.0, 1.0, 1.0),
       border_width=2.0,
       filled=True,
       show_border=True
   )
   
   # 更新样式
   polygon.update_data(fill_color=(1.0, 0.5, 0.5, 0.8))

StyledRectangleEntry
~~~~~~~~~~~~~~~~~~~~

带样式控制的矩形元素，支持独立的填充和边缘线条控制。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import StyledRectangleEntry
   
   # 创建矩形
   rect = StyledRectangleEntry(
       parent_view=view,
       visual_id="rect_1",
       pos=(10, 10),
       size=(80, 60),
       fill_color=(0.5, 1.0, 0.5, 0.8),
       border_color=(0.0, 1.0, 0.0, 1.0),
       border_width=2.0,
       filled=True,
       show_border=True
   )
   
   # 更新矩形
   rect.update_data(pos=(20, 20), size=(100, 80))

StyledEllipseEntry
~~~~~~~~~~~~~~~~~~

带样式控制的圆形/椭圆元素。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import StyledEllipseEntry
   
   # 创建圆形
   circle = StyledEllipseEntry(
       parent_view=view,
       visual_id="circle_1",
       center=(50, 50),
       radius=30.0,
       fill_color=(1.0, 0.5, 0.5, 0.8),
       border_color=(1.0, 0.0, 0.0, 1.0),
       border_width=2.0,
       filled=True,
       show_border=True
   )
   
   # 创建椭圆
   ellipse = StyledEllipseEntry(
       parent_view=view,
       visual_id="ellipse_1",
       center=(100, 50),
       radius=(40, 20),
       fill_color=(0.5, 1.0, 1.0, 0.8),
       border_color=(0.0, 1.0, 1.0, 1.0),
       border_width=2.0,
       filled=True,
       show_border=True
   )

实际应用
--------

基本可视化元素
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import (
       BezierCurveEntry, ArcEntry, StyledPolygonEntry, StyledRectangleEntry, StyledEllipseEntry
   )
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   import numpy as np
   
   class BasicVisualsWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.create_visuals()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("基本可视化元素")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 显示当前状态
           self.status_label = Label("状态: 可视化元素已创建")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def create_visuals(self):
           """创建可视化元素"""
           # 这里需要实际的 vispy view 对象
           # 示例代码，实际使用时需要传入正确的 view
           view = None  # 需要传入 vispy view
           
           if view is None:
               self.status_label.setText("状态: 需要 vispy view 对象")
               return
           
           # 创建贝塞尔曲线
           control_points = np.array([[10, 10], [50, 50], [90, 10]], dtype=np.float32)
           self.bezier = BezierCurveEntry(
               parent_view=view,
               visual_id="bezier_demo",
               control_points=control_points,
               degree=2,
               color='red',
               width=2.0
           )
           
           # 创建圆弧
           self.arc = ArcEntry(
               parent_view=view,
               visual_id="arc_demo",
               center=(150, 30),
               radius=20.0,
               start_angle=0.0,
               end_angle=180.0,
               color='blue',
               width=2.0
           )
           
           # 创建多边形
           vertices = np.array([[200, 10], [250, 30], [230, 50], [180, 50]], dtype=np.float32)
           self.polygon = StyledPolygonEntry(
               parent_view=view,
               visual_id="polygon_demo",
               vertices=vertices,
               fill_color=(0.5, 0.5, 1.0, 0.8),
               border_color=(1.0, 1.0, 1.0, 1.0),
               border_width=2.0
           )
           
           # 创建矩形
           self.rect = StyledRectangleEntry(
               parent_view=view,
               visual_id="rect_demo",
               pos=(10, 80),
               size=(80, 60),
               fill_color=(0.5, 1.0, 0.5, 0.8),
               border_color=(0.0, 1.0, 0.0, 1.0),
               border_width=2.0
           )
           
           # 创建椭圆
           self.ellipse = StyledEllipseEntry(
               parent_view=view,
               visual_id="ellipse_demo",
               center=(150, 110),
               radius=(30, 20),
               fill_color=(1.0, 0.5, 0.5, 0.8),
               border_color=(1.0, 0.0, 0.0, 1.0),
               border_width=2.0
           )
           
           self.status_label.setText("状态: 所有可视化元素已创建")

高级可视化应用
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import StyledRectangleEntry, StyledEllipseEntry
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   import numpy as np
   
   class AdvancedVisualsWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.create_visuals()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("高级可视化应用")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.update_btn = PushButton("更新样式")
           self.animate_btn = PushButton("动画效果")
           self.hide_btn = PushButton("隐藏/显示")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.update_btn)
           header_layout.addWidget(self.animate_btn)
           header_layout.addWidget(self.hide_btn)
           
           # 显示当前状态
           self.status_label = Label("状态: 高级可视化已创建")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def create_visuals(self):
           """创建高级可视化元素"""
           # 这里需要实际的 vispy view 对象
           view = None  # 需要传入 vispy view
           
           if view is None:
               self.status_label.setText("状态: 需要 vispy view 对象")
               return
           
           # 创建多个矩形
           self.rectangles = []
           colors = [
               (1.0, 0.0, 0.0, 0.8),  # 红色
               (0.0, 1.0, 0.0, 0.8),  # 绿色
               (0.0, 0.0, 1.0, 0.8),  # 蓝色
               (1.0, 1.0, 0.0, 0.8),  # 黄色
           ]
           
           for i, color in enumerate(colors):
               rect = StyledRectangleEntry(
                   parent_view=view,
                   visual_id=f"rect_{i}",
                   pos=(10 + i * 60, 20),
                   size=(50, 50),
                   fill_color=color,
                   border_color=(1.0, 1.0, 1.0, 1.0),
                   border_width=2.0,
                   filled=True,
                   show_border=True
               )
               self.rectangles.append(rect)
           
           # 创建多个椭圆
           self.ellipses = []
           for i in range(4):
               ellipse = StyledEllipseEntry(
                   parent_view=view,
                   visual_id=f"ellipse_{i}",
                   center=(40 + i * 60, 100),
                   radius=(25, 15),
                   fill_color=(0.5, 0.5, 1.0, 0.8),
                   border_color=(0.0, 0.0, 1.0, 1.0),
                   border_width=2.0,
                   filled=True,
                   show_border=True
               )
               self.ellipses.append(ellipse)
           
           self.visible_state = True
           self.status_label.setText("状态: 高级可视化元素已创建")
       
       def setup_connections(self):
           """设置连接"""
           self.update_btn.clicked.connect(self.update_styles)
           self.animate_btn.clicked.connect(self.animate_elements)
           self.hide_btn.clicked.connect(self.toggle_visibility)
       
       def update_styles(self):
           """更新样式"""
           import random
           
           # 更新矩形颜色
           for rect in self.rectangles:
               new_color = (random.random(), random.random(), random.random(), 0.8)
               rect.update_data(fill_color=new_color)
           
           # 更新椭圆大小
           for i, ellipse in enumerate(self.ellipses):
               new_radius = (20 + random.randint(0, 20), 10 + random.randint(0, 15))
               ellipse.update_data(radius=new_radius)
           
           self.status_label.setText("状态: 样式已更新")
       
       def animate_elements(self):
           """动画效果"""
           import random
           
           # 随机移动矩形
           for rect in self.rectangles:
               new_x = random.randint(10, 200)
               new_y = random.randint(10, 100)
               rect.update_data(pos=(new_x, new_y))
           
           # 随机移动椭圆
           for ellipse in self.ellipses:
               new_center = (random.randint(20, 250), random.randint(80, 150))
               ellipse.update_data(center=new_center)
           
           self.status_label.setText("状态: 动画效果已应用")
       
       def toggle_visibility(self):
           """切换可见性"""
           self.visible_state = not self.visible_state
           
           # 切换所有元素的可见性
           for rect in self.rectangles:
               rect.set_visible(self.visible_state)
           
           for ellipse in self.ellipses:
               ellipse.set_visible(self.visible_state)
           
           state_text = "显示" if self.visible_state else "隐藏"
           self.status_label.setText(f"状态: 所有元素已{state_text}")

最佳实践
--------

1. **性能优化** - 合理设置采样点数量，避免过度采样
2. **样式管理** - 统一管理颜色和样式参数
3. **内存管理** - 及时销毁不需要的可视化元素
4. **批量更新** - 使用批量更新提高性能
5. **错误处理** - 处理 vispy 环境不可用的情况

注意事项
--------

- 所有可视化元素都需要有效的 vispy view 对象
- 采样点数量影响渲染质量和性能
- 颜色值使用 RGBA 格式，范围 [0, 1]
- 样式元素支持独立的填充和边缘控制
- 需要正确处理元素的生命周期
- 大量元素可能影响渲染性能

相关模块
--------

- :doc:`components.vispy.vispy_visuals` - Vispy 可视化元素
- :doc:`components.vispy.drawing` - 交互式绘图
- :doc:`components.vispy.drawing.data_models` - 数据模型
- :doc:`components.vispy.drawing.drawing_canvas` - 绘图画布
- :doc:`common.color` - 颜色管理
