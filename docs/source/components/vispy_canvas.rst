Vispy Canvas Vispy画布模块
=================================

Vispy Canvas 模块负责创建和管理 Vispy SceneCanvas，处理 OpenGL 上下文、相机控制、主题管理。
该模块提供2D和3D画布的完整实现，支持网格显示和自动范围调整。

主要功能
--------

- **OpenGL管理** - 创建和管理OpenGL上下文
- **相机控制** - 支持多种相机模式和视角控制
- **主题管理** - 支持亮色/暗色主题切换
- **网格显示** - 提供2D和3D网格背景
- **视觉元素** - 管理Visual元素的生命周期
- **自动范围** - 自动调整相机以适应场景

核心组件
--------

initialize_vispy
~~~~~~~~~~~~~~~~

初始化Vispy后端函数。

.. code-block:: python

   from qfluentwidgets.components.vispy.vispy_canvas import initialize_vispy
   
   # 初始化Vispy后端
   initialize_vispy()

VispyCanvasBase
~~~~~~~~~~~~~~~

Vispy Canvas基类，管理SceneCanvas、相机、网格、主题等基础功能。

.. code-block:: python

   from qfluentwidgets.components.vispy.vispy_canvas import VispyCanvasBase
   from qfluentwidgets.components.vispy.vispy_visuals import VisualEntry
   
   # 创建画布基类
   canvas = VispyCanvasBase(camera_mode='panzoom')
   
   # 添加视觉元素
   visual = VisualEntry(canvas.view, "visual_001")
   canvas.add_visual(visual)
   
   # 设置主题
   canvas.set_theme(is_dark=True)
   
   # 自动调整范围
   canvas.auto_range()

**主要方法：**
- ``set_theme()`` - 设置主题
- ``add_visual()`` - 添加Visual元素
- ``remove_visual()`` - 移除Visual元素
- ``set_visible()`` - 设置Visual元素可见性
- ``update_visual()`` - 更新Visual元素数据
- ``clear_all()`` - 清空所有Visual元素
- ``auto_range()`` - 自动调整相机以适应场景范围

VispyCanvas2D
~~~~~~~~~~~~~~

2D Vispy Canvas，相机模式为PanZoomCamera。

.. code-block:: python

   from qfluentwidgets.components.vispy.vispy_canvas import VispyCanvas2D
   
   # 创建2D画布
   canvas_2d = VispyCanvas2D(
       grid_size=100.0,
       grid_spacing=10.0
   )
   
   # 获取原生控件
   native_widget = canvas_2d.native_widget
   
   # 更新网格
   canvas_2d.update_grid(scale=(2.0, 2.0))

**主要方法：**
- ``update_grid()`` - 更新网格范围和间距

VispyCanvas3D
~~~~~~~~~~~~~~

3D Vispy Canvas，相机模式为TurntableCamera或ArcballCamera。

.. code-block:: python

   from qfluentwidgets.components.vispy.vispy_canvas import VispyCanvas3D
   
   # 创建3D画布
   canvas_3d = VispyCanvas3D(camera_mode='turntable')
   
   # 设置视角
   canvas_3d.set_view('top')
   
   # 更新网格
   canvas_3d.update_grid(scale=(1.0, 1.0, 1.0))

**主要方法：**
- ``set_view()`` - 设置相机视角
- ``update_grid()`` - 更新网格范围和间距

实际应用
--------

基本2D画布应用
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.vispy_canvas import VispyCanvas2D
   from qfluentwidgets.components.vispy.vispy_visuals import VisualEntry
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   
   class Basic2DCanvasWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_canvas()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("基本2D画布应用")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.theme_btn = PushButton("切换主题")
           self.range_btn = PushButton("自动范围")
           self.clear_btn = PushButton("清空画布")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.theme_btn)
           header_layout.addWidget(self.range_btn)
           header_layout.addWidget(self.clear_btn)
           
           # 创建2D画布
           self.canvas = VispyCanvas2D(
               grid_size=100.0,
               grid_spacing=10.0
           )
           
           # 显示当前状态
           self.status_label = Label("状态: 2D画布已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.canvas.native_widget)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_canvas(self):
           """设置画布"""
           # 连接信号（这里主要是展示功能）
           self.status_label.setText("状态: 2D画布已设置")
       
       def setup_connections(self):
           """设置连接"""
           self.theme_btn.clicked.connect(self.toggle_theme)
           self.range_btn.clicked.connect(self.auto_range)
           self.clear_btn.clicked.connect(self.clear_canvas)
       
       def toggle_theme(self):
           """切换主题"""
           # 这里需要获取当前主题状态
           # 示例：切换到暗色主题
           self.canvas.set_theme(is_dark=True)
           self.status_label.setText("状态: 已切换到暗色主题")
       
       def auto_range(self):
           """自动调整范围"""
           self.canvas.auto_range()
           self.status_label.setText("状态: 已自动调整范围")
       
       def clear_canvas(self):
           """清空画布"""
           self.canvas.clear_all()
           self.status_label.setText("状态: 画布已清空")

高级3D画布应用
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.vispy_canvas import VispyCanvas3D
   from qfluentwidgets.components.vispy.vispy_visuals import VisualEntry
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   
   class Advanced3DCanvasWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_canvas()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("高级3D画布应用")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.view_btn = PushButton("切换视角")
           self.grid_btn = PushButton("更新网格")
           self.camera_btn = PushButton("相机信息")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.view_btn)
           header_layout.addWidget(self.grid_btn)
           header_layout.addWidget(self.camera_btn)
           
           # 创建3D画布
           self.canvas = VispyCanvas3D(camera_mode='turntable')
           
           # 显示当前状态
           self.status_label = Label("状态: 3D画布已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.canvas.native_widget)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_canvas(self):
           """设置画布"""
           # 连接信号（这里主要是展示功能）
           self.status_label.setText("状态: 3D画布已设置")
           self.current_view_index = 0
       
       def setup_connections(self):
           """设置连接"""
           self.view_btn.clicked.connect(self.cycle_views)
           self.grid_btn.clicked.connect(self.update_grid)
           self.camera_btn.clicked.connect(self.show_camera_info)
       
       def cycle_views(self):
           """循环切换视角"""
           views = ['free', 'top', 'front', 'side']
           self.current_view_index = (self.current_view_index + 1) % len(views)
           current_view = views[self.current_view_index]
           
           self.canvas.set_view(current_view)
           self.status_label.setText(f"状态: 已切换到 {current_view} 视角")
       
       def update_grid(self):
           """更新网格"""
           import random
           
           # 随机缩放因子
           scale = (random.uniform(0.5, 2.0), random.uniform(0.5, 2.0), random.uniform(0.5, 2.0))
           self.canvas.update_grid(scale=scale)
           
           self.status_label.setText(f"状态: 网格已更新，缩放: {scale}")
       
       def show_camera_info(self):
           """显示相机信息"""
           if self.canvas.view and self.canvas.view.camera:
               camera = self.canvas.view.camera
               
               info_lines = [
                   f"相机类型: {type(camera).__name__}",
                   f"FOV: {getattr(camera, 'fov', 'N/A')}",
                   f"距离: {getattr(camera, 'distance', 'N/A')}",
                   f"仰角: {getattr(camera, 'elevation', 'N/A')}",
                   f"方位角: {getattr(camera, 'azimuth', 'N/A')}"
               ]
               
               self.status_label.setText("\n".join(info_lines))
           else:
               self.status_label.setText("状态: 相机信息不可用")

视觉元素管理应用
~~~~~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.vispy_canvas import VispyCanvas2D
   from qfluentwidgets.components.vispy.vispy_visuals import VisualEntry
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   import numpy as np
   
   class VisualManagementWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_canvas()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("视觉元素管理应用")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.add_btn = PushButton("添加元素")
           self.remove_btn = PushButton("移除元素")
           self.update_btn = PushButton("更新元素")
           self.list_btn = PushButton("列出元素")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.add_btn)
           header_layout.addWidget(self.remove_btn)
           header_layout.addWidget(self.update_btn)
           header_layout.addWidget(self.list_btn)
           
           # 创建2D画布
           self.canvas = VispyCanvas2D()
           
           # 显示当前状态
           self.status_label = Label("状态: 视觉元素管理已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.canvas.native_widget)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_canvas(self):
           """设置画布和视觉元素管理"""
           self.visual_counter = 0
           self.visual_elements = {}
           self.status_label.setText("状态: 视觉元素管理已设置")
       
       def setup_connections(self):
           """设置连接"""
           self.add_btn.clicked.connect(self.add_visual)
           self.remove_btn.clicked.connect(self.remove_visual)
           self.update_btn.clicked.connect(self.update_visual)
           self.list_btn.clicked.connect(self.list_visuals)
       
       def add_visual(self):
           """添加视觉元素"""
           # 这里需要实际的VisualEntry对象
           # 示例代码，实际使用时需要传入正确的对象
           self.visual_counter += 1
           visual_id = f"visual_{self.visual_counter}"
           
           # 模拟添加视觉元素
           self.visual_elements[visual_id] = {
               'id': visual_id,
               'created_time': '现在',
               'visible': True
           }
           
           self.status_label.setText(f"状态: 已添加视觉元素 {visual_id}")
       
       def remove_visual(self):
           """移除视觉元素"""
           if self.visual_elements:
               # 获取第一个元素ID
               visual_id = list(self.visual_elements.keys())[0]
               
               # 从画布移除
               success = self.canvas.remove_visual(visual_id)
               
               if success:
                   del self.visual_elements[visual_id]
                   self.status_label.setText(f"状态: 已移除视觉元素 {visual_id}")
               else:
                   self.status_label.setText(f"状态: 移除失败，元素 {visual_id} 不存在")
           else:
               self.status_label.setText("状态: 没有可移除的视觉元素")
       
       def update_visual(self):
           """更新视觉元素"""
           if self.visual_elements:
               # 获取第一个元素ID
               visual_id = list(self.visual_elements.keys())[0]
               
               # 模拟更新
               self.visual_elements[visual_id]['updated_time'] = '现在'
               
               # 这里需要实际的更新参数
               # success = self.canvas.update_visual(visual_id, param1=value1, param2=value2)
               
               self.status_label.setText(f"状态: 已更新视觉元素 {visual_id}")
           else:
               self.status_label.setText("状态: 没有可更新的视觉元素")
       
       def list_visuals(self):
           """列出所有视觉元素"""
           if self.visual_elements:
               info_lines = [f"视觉元素总数: {len(self.visual_elements)}"]
               
               for i, (visual_id, info) in enumerate(self.visual_elements.items(), 1):
                   info_lines.append(f"  {i}. {visual_id} - 可见: {info.get('visible', 'Unknown')}")
               
               self.status_label.setText("\n".join(info_lines))
           else:
               self.status_label.setText("状态: 没有视觉元素")

最佳实践
--------

1. **环境检查** - 始终检查VISPY_AVAILABLE状态
2. **主题管理** - 根据系统主题自动切换画布主题
3. **性能优化** - 合理控制视觉元素数量
4. **相机控制** - 提供直观的相机操作接口
5. **错误处理** - 妥善处理OpenGL初始化失败的情况

注意事项
--------

- 需要安装vispy库才能正常工作
- 画布创建时会自动初始化OpenGL上下文
- 相机模式影响用户交互方式
- 网格显示有助于理解空间关系
- 自动范围调整会考虑所有可见元素
- 3D画布支持多种视角模式
- 视觉元素的ID需要保持唯一性

相关模块
--------

- :doc:`components.vispy.vispy_visuals` - Vispy可视化元素
- :doc:`components.vispy.vispy_widget` - Vispy控件
- :doc:`components.vispy.drawing` - 交互式绘图
- :doc:`common.theme` - 主题管理
- :doc:`common.geometry` - 几何计算
