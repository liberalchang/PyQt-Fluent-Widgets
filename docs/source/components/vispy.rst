Vispy 可视化组件 (Vispy)
=======================

本节介绍 PySide6-Fluent-Widgets 中的 Vispy 可视化组件。

VispyWidget2D
-------------

2D 可视化组件，基于 Vispy 库实现高性能 2D 图形渲染。

.. code-block:: python

   from qfluentwidgets import VispyWidget2D
   import numpy as np

   # 创建 2D 可视化组件
   vispy_2d = VispyWidget2D()
   vispy_2d.setFixedSize(600, 400)
   
   # 添加数据点
   x = np.linspace(0, 10, 100)
   y = np.sin(x)
   vispy_2d.plot(x, y, color='red', linewidth=2)

VispyWidget3D
-------------

3D 可视化组件，支持 3D 图形渲染。

.. code-block:: python

   from qfluentwidgets import VispyWidget3D
   import numpy as np

   # 创建 3D 可视化组件
   vispy_3d = VispyWidget3D()
   vispy_3d.setFixedSize(600, 400)
   
   # 添加 3D 散点图
   x = np.random.randn(100)
   y = np.random.randn(100)
   z = np.random.randn(100)
   vispy_3d.scatter(x, y, z, color='blue', size=5)

PointCloudViewer
----------------

点云查看器，专门用于显示和交互点云数据。

.. code-block:: python

   from qfluentwidgets import PointCloudViewer
   import numpy as np

   # 创建点云查看器
   point_viewer = PointCloudViewer()
   point_viewer.setFixedSize(800, 600)
   
   # 加载点云数据
   points = np.random.randn(1000, 3)  # 1000 个 3D 点
   colors = np.random.rand(1000, 3)    # 随机颜色
   point_viewer.setPointCloud(points, colors)

完整示例
--------

下面是一个完整的 Vispy 可视化组件使用示例：

.. code-block:: python

   import sys
   import numpy as np
   from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                                QWidget, QPushButton, QLabel, QTabWidget)
   from PySide6.QtCore import Qt
   from qfluentwidgets import *

   class VispyDemoWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           
           self.setWindowTitle('Vispy 可视化组件示例')
           self.resize(1000, 700)
           
           # 创建界面
           self.setup_ui()

       def setup_ui(self):
           """设置界面"""
           central_widget = QWidget()
           self.setCentralWidget(central_widget)
           
           layout = QVBoxLayout(central_widget)
           
           # 添加标题
           title = SubtitleLabel('Vispy 可视化组件示例')
           layout.addWidget(title)
           
           # 创建标签页
           tab_widget = QTabWidget()
           
           # 2D 可视化标签页
           self.setup_2d_tab(tab_widget)
           
           # 3D 可视化标签页
           self.setup_3d_tab(tab_widget)
           
           # 点云查看器标签页
           self.setup_pointcloud_tab(tab_widget)
           
           layout.addWidget(tab_widget)

       def setup_2d_tab(self, tab_widget):
           """设置 2D 可视化标签页"""
           tab = QWidget()
           tab_layout = QVBoxLayout(tab)
           
           # 创建 2D 可视化组件
           self.vispy_2d = VispyWidget2D()
           self.vispy_2d.setFixedSize(800, 500)
           tab_layout.addWidget(self.vispy_2d)
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           sin_btn = PrimaryPushButton('绘制正弦波')
           sin_btn.clicked.connect(self.plot_sine)
           
           scatter_btn = PushButton('绘制散点图')
           scatter_btn.clicked.connect(self.plot_scatter_2d)
           
           clear_btn = PushButton('清除')
           clear_btn.clicked.connect(self.clear_2d)
           
           button_layout.addWidget(sin_btn)
           button_layout.addWidget(scatter_btn)
           button_layout.addWidget(clear_btn)
           button_layout.addStretch()
           
           tab_layout.addLayout(button_layout)
           
           tab_widget.addTab(tab, '2D 可视化')

       def setup_3d_tab(self, tab_widget):
           """设置 3D 可视化标签页"""
           tab = QWidget()
           tab_layout = QVBoxLayout(tab)
           
           # 创建 3D 可视化组件
           self.vispy_3d = VispyWidget3D()
           self.vispy_3d.setFixedSize(800, 500)
           tab_layout.addWidget(self.vispy_3d)
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           surface_btn = PrimaryPushButton('绘制曲面')
           surface_btn.clicked.connect(self.plot_surface)
           
           scatter_3d_btn = PushButton('3D 散点图')
           scatter_3d_btn.clicked.connect(self.plot_scatter_3d)
           
           clear_3d_btn = PushButton('清除')
           clear_3d_btn.clicked.connect(self.clear_3d)
           
           button_layout.addWidget(surface_btn)
           button_layout.addWidget(scatter_3d_btn)
           button_layout.addWidget(clear_3d_btn)
           button_layout.addStretch()
           
           tab_layout.addLayout(button_layout)
           
           tab_widget.addTab(tab, '3D 可视化')

       def setup_pointcloud_tab(self, tab_widget):
           """设置点云查看器标签页"""
           tab = QWidget()
           tab_layout = QVBoxLayout(tab)
           
           # 创建点云查看器
           self.point_viewer = PointCloudViewer()
           self.point_viewer.setFixedSize(800, 500)
           tab_layout.addWidget(self.point_viewer)
           
           # 控制按钮
           button_layout = QHBoxLayout()
           
           load_btn = PrimaryPushButton('加载点云')
           load_btn.clicked.connect(self.load_pointcloud)
           
           random_btn = PushButton('随机点云')
           random_btn.clicked.connect(self.random_pointcloud)
           
           clear_pc_btn = PushButton('清除')
           clear_pc_btn.clicked.connect(self.clear_pointcloud)
           
           button_layout.addWidget(load_btn)
           button_layout.addWidget(random_btn)
           button_layout.addWidget(clear_pc_btn)
           button_layout.addStretch()
           
           tab_layout.addLayout(button_layout)
           
           tab_widget.addTab(tab, '点云查看器')

       def plot_sine(self):
           """绘制正弦波"""
           x = np.linspace(0, 4 * np.pi, 200)
           y = np.sin(x)
           
           self.vispy_2d.clear()
           self.vispy_2d.plot(x, y, color='blue', linewidth=2)
           self.vispy_2d.set_xlabel('X')
           self.vispy_2d.set_ylabel('Y')
           self.vispy_2d.set_title('正弦波')
           
           InfoBar.success('正弦波绘制完成', parent=self)

       def plot_scatter_2d(self):
           """绘制 2D 散点图"""
           x = np.random.randn(100)
           y = np.random.randn(100)
           colors = np.random.rand(100)
           
           self.vispy_2d.clear()
           self.vispy_2d.scatter(x, y, c=colors, s=50, cmap='viridis')
           self.vispy_2d.set_xlabel('X')
           self.vispy_2d.set_ylabel('Y')
           self.vispy_2d.set_title('2D 散点图')
           
           InfoBar.success('2D 散点图绘制完成', parent=self)

       def clear_2d(self):
           """清除 2D 图形"""
           self.vispy_2d.clear()
           InfoBar.info('2D 图形已清除', parent=self)

       def plot_surface(self):
           """绘制 3D 曲面"""
           x = np.linspace(-5, 5, 50)
           y = np.linspace(-5, 5, 50)
           X, Y = np.meshgrid(x, y)
           Z = np.sin(np.sqrt(X**2 + Y**2))
           
           self.vispy_3d.clear()
           self.vispy_3d.plot_surface(X, Y, Z, cmap='viridis')
           self.vispy_3d.set_xlabel('X')
           self.vispy_3d.set_ylabel('Y')
           self.vispy_3d.set_zlabel('Z')
           self.vispy_3d.set_title('3D 曲面')
           
           InfoBar.success('3D 曲面绘制完成', parent=self)

       def plot_scatter_3d(self):
           """绘制 3D 散点图"""
           x = np.random.randn(200)
           y = np.random.randn(200)
           z = np.random.randn(200)
           colors = np.random.rand(200)
           
           self.vispy_3d.clear()
           self.vispy_3d.scatter(x, y, z, c=colors, s=20, cmap='plasma')
           self.vispy_3d.set_xlabel('X')
           self.vispy_3d.set_ylabel('Y')
           self.vispy_3d.set_zlabel('Z')
           self.vispy_3d.set_title('3D 散点图')
           
           InfoBar.success('3D 散点图绘制完成', parent=self)

       def clear_3d(self):
           """清除 3D 图形"""
           self.vispy_3d.clear()
           InfoBar.info('3D 图形已清除', parent=self)

       def load_pointcloud(self):
           """加载点云数据"""
           # 模拟加载点云数据
           points = self.generate_sphere_pointcloud(1000)
           colors = np.random.rand(1000, 3)
           
           self.point_viewer.setPointCloud(points, colors)
           InfoBar.success('点云数据加载完成', parent=self)

       def random_pointcloud(self):
           """生成随机点云"""
           points = np.random.randn(500, 3) * 2
           colors = np.random.rand(500, 3)
           
           self.point_viewer.setPointCloud(points, colors)
           InfoBar.success('随机点云生成完成', parent=self)

       def clear_pointcloud(self):
           """清除点云"""
           self.point_viewer.clear()
           InfoBar.info('点云已清除', parent=self)

       def generate_sphere_pointcloud(self, n_points):
           """生成球面点云"""
           phi = np.random.uniform(0, 2 * np.pi, n_points)
           costheta = np.random.uniform(-1, 1, n_points)
           u = np.random.uniform(0, 1, n_points)
           
           theta = np.arccos(costheta)
           r = np.cbrt(u)
           
           x = r * np.sin(theta) * np.cos(phi)
           y = r * np.sin(theta) * np.sin(phi)
           z = r * np.cos(theta)
           
           return np.column_stack([x, y, z])

   if __name__ == '__main__':
       app = QApplication(sys.argv)
       window = VispyDemoWindow()
       window.show()
       sys.exit(app.exec())

最佳实践
--------

1. **性能优化**: 
   - 大量数据时使用适当的数据采样
   - 合理设置渲染参数
   - 避免频繁更新图形

2. **数据管理**: 
   - 使用 NumPy 数组处理数据
   - 合理设置数据范围和比例
   - 处理缺失值和异常值

3. **交互功能**: 
   - 支持鼠标缩放和平移
   - 提供坐标显示
   - 添加选择和高亮功能

4. **可视化设计**: 
   - 选择合适的颜色映射
   - 设置清晰的坐标轴标签
   - 添加图例和标题

依赖要求
--------

使用 Vispy 组件需要安装以下依赖：

.. code-block:: bash

   pip install vispy numpy
