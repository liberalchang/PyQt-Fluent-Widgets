Coordinate System 坐标系统模块
===================================

Coordinate System 模块提供屏幕坐标与世界坐标的双向转换功能，集成 vispy 相机的变换矩阵。
该模块支持像素坐标与逻辑坐标之间的转换，适用于 2D 绘图和可视化应用。

主要功能
--------

- **坐标转换** - 提供屏幕坐标与世界坐标的双向转换
- **批量转换** - 支持数组形式的批量坐标转换
- **视口管理** - 提供视口边界获取和管理功能
- **距离转换** - 支持屏幕距离与世界坐标距离的转换
- **相机集成** - 集成 vispy 相机的变换矩阵

核心组件
--------

CoordinateSystem
~~~~~~~~~~~~~~

坐标系统类，管理屏幕坐标与世界坐标之间的转换。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import CoordinateSystem
   
   # 创建坐标系统
   coord_system = CoordinateSystem(
       view=vispy_view,
       canvas=vispy_canvas,
       scale_factor=1.0,
       origin_offset=(0.0, 0.0)
   )
   
   # 初始化视图
   coord_system.initialize_view()
   
   # 坐标转换
   world_x, world_y = coord_system.screenToWorld(100, 100)
   screen_x, screen_y = coord_system.worldToScreen(0, 0)

**主要方法：**
- ``screenToWorld()`` - 屏幕坐标转世界坐标
- ``worldToScreen()`` - 世界坐标转屏幕坐标
- ``screenToWorldArray()`` - 批量屏幕坐标转世界坐标
- ``worldToScreenArray()`` - 批量世界坐标转屏幕坐标
- ``getViewBounds()`` - 获取视口边界
- ``distanceScreenToWorld()`` - 屏幕距离转世界距离
- ``distanceWorldToScreen()`` - 世界距离转屏幕距离

实际应用
--------

基本坐标转换
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import CoordinateSystem
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   import numpy as np
   
   class BasicCoordinateWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_coordinate_system()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("基本坐标转换")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 显示当前状态
           self.status_label = Label("状态: 坐标系统已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_coordinate_system(self):
           """设置坐标系统"""
           # 这里需要实际的 vispy view 和 canvas
           # 示例代码，实际使用时需要传入正确的对象
           self.coord_system = CoordinateSystem(
               view=None,  # 需要传入 vispy view
               canvas=None,  # 需要传入 vispy canvas
               scale_factor=1.0,
               origin_offset=(0.0, 0.0)
           )
           
           # 测试坐标转换
           self.test_coordinate_conversion()
       
       def test_coordinate_conversion(self):
           """测试坐标转换"""
           # 测试屏幕坐标转世界坐标
           screen_points = [(100, 100), (200, 200), (300, 300)]
           
           # 单点转换
           for screen_x, screen_y in screen_points:
               world_x, world_y = self.coord_system.screenToWorld(screen_x, screen_y)
               print(f"屏幕坐标 ({screen_x}, {screen_y}) -> 世界坐标 ({world_x:.2f}, {world_y:.2f})")
           
           # 批量转换
           screen_array = np.array(screen_points)
           world_array = self.coord_system.screenToWorldArray(screen_array)
           print(f"批量转换结果: {world_array}")
           
           # 测试世界坐标转屏幕坐标
           world_points = [(0, 0), (50, 50), (100, 100)]
           for world_x, world_y in world_points:
               screen_x, screen_y = self.coord_system.worldToScreen(world_x, world_y)
               print(f"世界坐标 ({world_x}, {world_y}) -> 屏幕坐标 ({screen_x:.2f}, {screen_y:.2f})")
           
           self.status_label.setText("坐标转换测试完成")

高级坐标管理
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import CoordinateSystem
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   import numpy as np
   
   class AdvancedCoordinateWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_coordinate_system()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("高级坐标管理")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.test_btn = PushButton("测试转换")
           self.bounds_btn = PushButton("获取边界")
           self.distance_btn = PushButton("距离转换")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.test_btn)
           header_layout.addWidget(self.bounds_btn)
           header_layout.addWidget(self.distance_btn)
           
           # 显示当前状态
           self.status_label = Label("状态: 坐标系统已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_coordinate_system(self):
           """设置坐标系统"""
           self.coord_system = CoordinateSystem(
               view=None,  # 需要传入 vispy view
               canvas=None,  # 需要传入 vispy canvas
               scale_factor=2.0,  # 1像素 = 2物理单位
               origin_offset=(-100, 100)  # 屏幕原点对应世界坐标
           )
       
       def setup_connections(self):
           """设置连接"""
           self.test_btn.clicked.connect(self.test_conversions)
           self.bounds_btn.clicked.connect(self.get_view_bounds)
           self.distance_btn.clicked.connect(self.test_distance_conversion)
       
       def test_conversions(self):
           """测试坐标转换"""
           # 创建测试点
           test_points = [
               (50, 50),    # 左上角
               (200, 50),   # 右上角
               (50, 200),   # 左下角
               (200, 200),  # 右下角
               (125, 125)   # 中心点
           ]
           
           print("=== 坐标转换测试 ===")
           
           # 屏幕坐标转世界坐标
           screen_array = np.array(test_points)
           world_array = self.coord_system.screenToWorldArray(screen_array)
           
           for i, (screen, world) in enumerate(zip(test_points, world_array)):
               print(f"点{i+1}: 屏幕{screen} -> 世界({world[0]:.2f}, {world[1]:.2f})")
           
           # 世界坐标转屏幕坐标（反向验证）
           screen_back = self.coord_system.worldToScreenArray(world_array)
           
           for i, (world, screen) in enumerate(zip(world_array, screen_back)):
               print(f"点{i+1}: 世界({world[0]:.2f}, {world[1]:.2f}) -> 屏幕({screen[0]:.2f}, {screen[1]:.2f})")
           
           self.status_label.setText("坐标转换测试完成")
       
       def get_view_bounds(self):
           """获取视口边界"""
           bounds = self.coord_system.getViewBounds()
           
           if bounds:
               min_x, min_y, max_x, max_y = bounds
               print(f"视口边界: ({min_x:.2f}, {min_y:.2f}) -> ({max_x:.2f}, {max_y:.2f})")
               print(f"视口宽度: {max_x - min_x:.2f}, 高度: {max_y - min_y:.2f}")
               self.status_label.setText(f"视口边界: ({min_x:.1f}, {min_y:.1f}) -> ({max_x:.1f}, {max_y:.1f})")
           else:
               print("无法获取视口边界")
               self.status_label.setText("无法获取视口边界")
       
       def test_distance_conversion(self):
           """测试距离转换"""
           print("=== 距离转换测试 ===")
           
           # 测试屏幕距离转世界距离
           screen_distances = [10, 50, 100, 200]
           
           for screen_dist in screen_distances:
               world_dist = self.coord_system.distanceScreenToWorld(screen_dist)
               print(f"屏幕距离 {screen_dist}px -> 世界距离 {world_dist:.2f}")
           
           # 测试世界距离转屏幕距离
           world_distances = [5, 10, 25, 50]
           
           for world_dist in world_distances:
               screen_dist = self.coord_system.distanceWorldToScreen(world_dist)
               print(f"世界距离 {world_dist} -> 屏幕距离 {screen_dist:.2f}px")
           
           self.status_label.setText("距离转换测试完成")

绘图坐标应用
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import CoordinateSystem
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   import numpy as np
   
   class DrawingCoordinateWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_drawing_coordinate()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("绘图坐标应用")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 显示当前状态
           self.status_label = Label("状态: 绘图坐标系统已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_drawing_coordinate(self):
           """设置绘图坐标系统"""
           self.coord_system = CoordinateSystem(
               view=None,  # 需要传入 vispy view
               canvas=None,  # 需要传入 vispy canvas
               scale_factor=1.0,
               origin_offset=(0.0, 0.0)
           )
           
           # 模拟绘图坐标转换
           self.simulate_drawing_coordinates()
       
       def simulate_drawing_coordinates(self):
           """模拟绘图坐标转换"""
           print("=== 绘图坐标应用 ===")
           
           # 模拟鼠标点击事件（屏幕坐标）
           mouse_clicks = [
               (100, 100),  # 第一次点击
               (150, 120),  # 第二次点击
               (200, 100),  # 第三次点击
               (175, 150),  # 第四次点击
               (125, 150)   # 第五次点击
           ]
           
           # 转换为世界坐标（用于绘图）
           world_points = []
           for screen_x, screen_y in mouse_clicks:
               world_x, world_y = self.coord_system.screenToWorld(screen_x, screen_y)
               world_points.append((world_x, world_y))
               print(f"鼠标点击 ({screen_x}, {screen_y}) -> 绘图坐标 ({world_x:.2f}, {world_y:.2f})")
           
           # 计算绘制的多边形面积（世界坐标系）
           if len(world_points) >= 3:
               area = self.calculate_polygon_area(world_points)
               print(f"绘制的多边形面积: {area:.2f} 平方单位")
           
           # 计算绘制的线条长度（世界坐标系）
           if len(world_points) >= 2:
               total_length = 0
               for i in range(len(world_points) - 1):
                   p1 = world_points[i]
                   p2 = world_points[i + 1]
                   length = np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
                   total_length += length
               print(f"绘制的线条总长度: {total_length:.2f} 单位")
           
           self.status_label.setText(f"绘图坐标应用完成，{len(world_points)} 个点")
       
       def calculate_polygon_area(self, points):
           """计算多边形面积（使用鞋带公式）"""
           if len(points) < 3:
               return 0
           
           area = 0
           n = len(points)
           
           for i in range(n):
               j = (i + 1) % n
               area += points[i][0] * points[j][1]
               area -= points[j][0] * points[i][1]
           
           return abs(area) / 2

最佳实践
--------

1. **初始化管理** - 正确初始化 view 和 canvas 对象
2. **错误处理** - 处理坐标转换中的异常情况
3. **性能优化** - 使用批量转换提高性能
4. **精度控制** - 注意浮点数精度问题
5. **坐标系统一** - 保持坐标系的统一性

注意事项
--------

- 坐标系统需要有效的 vispy view 和 canvas 对象
- 屏幕坐标以像素为单位，原点在左上角，Y轴向下
- 世界坐标为逻辑坐标，原点和方向由相机控制
- 转换过程中可能出现精度损失
- 批量转换比单点转换更高效
- 需要处理无效输入和异常情况

相关模块
--------

- :doc:`components.vispy.vispy_canvas` - Vispy 画布
- :doc:`components.vispy.vispy_widget` - Vispy 控件
- :doc:`components.vispy.drawing` - 交互式绘图
- :doc:`common.geometry` - 几何计算
