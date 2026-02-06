Data Models 数据模型模块
============================

Data Models 模块定义交互式绘图框架中所有图元的数据结构，包括样式数据和各种图元数据类。
该模块提供完整的数据模型支持，适用于 2D 绘图和可视化应用。

主要功能
--------

- **样式数据** - 提供统一的样式定义和管理
- **图元基类** - 提供所有图元的通用属性和方法
- **具体图元** - 支持线条、贝塞尔曲线、圆弧、圆形、矩形、多边形等
- **标记点** - 提供散点标记的数据结构
- **图像数据** - 支持位图图像的显示
- **边界计算** - 提供统一的边界框计算方法

核心组件
--------

StyleData
~~~~~~~~~~

样式数据类，定义图元的视觉样式属性。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import StyleData
   
   # 创建样式数据
   style = StyleData(
       lineWidth=2.0,
       lineColor=(1.0, 0.0, 0.0, 1.0),  # 红色
       filled=True,
       fillColor=(0.5, 0.5, 0.5, 0.8),  # 半透明灰色
       showBorder=True,
       borderColor=(1.0, 1.0, 1.0, 1.0),  # 白色边框
       borderWidth=1.0,
       pointSize=6.0
   )
   
   # 复制样式
   style_copy = style.copy()

PrimitiveData
~~~~~~~~~~~~

图元数据基类，所有图元数据类的基类。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import PrimitiveData, StyleData
   
   # 创建基础图元数据
   primitive = PrimitiveData(
       name="示例图元",
       layer_id="layer1",
       type_name="primitive",
       style=StyleData(),
       visible=True,
       locked=False,
       with_handles=False,
       userData={"custom": "data"}
   )

PointData
~~~~~~~~~~

点数据类，表示单个点图元。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import PointData
   
   # 创建点数据
   point = PointData(
       x=10.0,
       y=20.0,
       radius=3.0,
       name="控制点"
   )
   
   # 获取边界框
   bounds = point.bounds

LineData
~~~~~~~~~~

线条数据类，表示直线或折线。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import LineData
   import numpy as np
   
   # 创建线条数据
   points = np.array([[0, 0], [10, 10], [20, 5]], dtype=np.float32)
   line = LineData(
       points=points,
       name="折线"
   )
   
   # 获取边界框
   bounds = line.bounds

BezierData
~~~~~~~~~~~~

贝塞尔曲线数据类，支持二阶和三阶贝塞尔曲线。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import BezierData
   import numpy as np
   
   # 创建二阶贝塞尔曲线
   control_points = np.array([[0, 0], [5, 10], [10, 0]], dtype=np.float32)
   bezier = BezierData(
       control_points=control_points,
       degree=2,
       name="贝塞尔曲线"
   )
   
   # 计算曲线上的点
   point = bezier.evaluate(0.5)
   
   # 采样曲线
   sampled_points = bezier.sample(num_points=50)

ArcData
~~~~~~~~~~

圆弧数据类，表示圆弧。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import ArcData
   
   # 创建圆弧数据
   arc = ArcData(
       center=(10, 10),
       radius=5.0,
       start_angle=0.0,
       end_angle=90.0,
       name="圆弧"
   )
   
   # 采样圆弧上的点
   sampled_points = arc.sample(num_points=30)

CircleData
~~~~~~~~~~

圆形数据类，表示圆形或椭圆。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import CircleData
   
   # 创建圆形
   circle = CircleData(
       center=(10, 10),
       radius=(5.0, 5.0),  # 正圆
       name="圆形"
   )
   
   # 创建椭圆
   ellipse = CircleData(
       center=(10, 10),
       radius=(8.0, 5.0),  # 椭圆
       name="椭圆"
   )
   
   # 检查是否为正圆
   is_circle = circle.is_circle

RectangleData
~~~~~~~~~~~~

矩形数据类，表示轴对齐的矩形。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import RectangleData
   
   # 创建矩形
   rect = RectangleData(
       pos=(0, 0),
       size=(100, 50),
       name="矩形"
   )
   
   # 获取中心点
   center = rect.center
   
   # 判断点是否在矩形内
   contains = rect.contains_point((50, 25))

PolygonData
~~~~~~~~~~

多边形数据类，表示任意多边形。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import PolygonData
   import numpy as np
   
   # 创建三角形
   vertices = np.array([[0, 0], [10, 0], [5, 8]], dtype=np.float32)
   triangle = PolygonData(
       vertices=vertices,
       name="三角形"
   )
   
   # 判断点是否在多边形内
   contains = triangle.contains_point((5, 3))

MarkersData
~~~~~~~~~~

标记点数据类，表示散点标记。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import MarkersData
   import numpy as np
   
   # 创建标记点
   positions = np.array([[1, 1], [2, 3], [3, 2]], dtype=np.float32)
   sizes = np.array([5.0, 8.0, 6.0])
   markers = MarkersData(
       positions=positions,
       sizes=sizes,
       symbol='o',
       name="散点"
   )

ImageData
~~~~~~~~~~

图像数据类，表示位图图像。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import ImageData
   import numpy as np
   
   # 创建图像数据
   image_data = np.random.rand(100, 100, 3)  # 随机彩色图像
   image = ImageData(
       data=image_data,
       pos=(0, 0),
       interpolation='nearest',
       image_path='path/to/image.png',
       name="图像"
   )
   
   # 获取图像尺寸
   size = image.size

实际应用
--------

基本图元创建
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import (
       StyleData, LineData, CircleData, RectangleData
   )
   from qfluentwidgets import CardWidget, Label
   from PySide6.QtWidgets import QVBoxLayout
   from PySide6.QtCore import Qt
   import numpy as np
   
   class BasicPrimitivesWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.create_primitives()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题
           title_label = Label("基本图元创建")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           # 显示当前状态
           self.status_label = Label("状态: 图元已创建")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addWidget(title_label)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def create_primitives(self):
           """创建基本图元"""
           # 创建样式
           line_style = StyleData(
               lineWidth=2.0,
               lineColor=(1.0, 0.0, 0.0, 1.0),  # 红色
               filled=False
           )
           
           fill_style = StyleData(
               lineWidth=1.0,
               lineColor=(0.0, 0.0, 1.0, 1.0),  # 蓝色边框
               filled=True,
               fillColor=(0.5, 0.5, 1.0, 0.5),  # 半透明蓝色
               showBorder=True
           )
           
           # 创建线条
           points = np.array([[10, 10], [50, 30], [90, 10]], dtype=np.float32)
           line = LineData(
               points=points,
               style=line_style,
               name="折线"
           )
           
           # 创建圆形
           circle = CircleData(
               center=(50, 50),
               radius=(20, 20),
               style=fill_style,
               name="圆形"
           )
           
           # 创建矩形
           rect = RectangleData(
               pos=(20, 70),
               size=(60, 30),
               style=fill_style,
               name="矩形"
           )
           
           # 显示图元信息
           self.display_primitive_info([line, circle, rect])
       
       def display_primitive_info(self, primitives):
           """显示图元信息"""
           info_lines = ["图元信息:"]
           
           for primitive in primitives:
               bounds = primitive.bounds
               info_lines.append(f"{primitive.name}: 边界 {bounds[0]} -> {bounds[1]}")
           
           self.status_label.setText("\n".join(info_lines))

高级图元应用
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import (
       StyleData, BezierData, ArcData, PolygonData, MarkersData
   )
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   import numpy as np
   
   class AdvancedPrimitivesWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.create_advanced_primitives()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("高级图元应用")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.sample_btn = PushButton("采样曲线")
           self.bounds_btn = PushButton("计算边界")
           self.contains_btn = PushButton("点包含测试")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.sample_btn)
           header_layout.addWidget(self.bounds_btn)
           header_layout.addWidget(self.contains_btn)
           
           # 显示当前状态
           self.status_label = Label("状态: 高级图元已创建")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def create_advanced_primitives(self):
           """创建高级图元"""
           # 创建贝塞尔曲线
           control_points = np.array([[0, 0], [25, 50], [50, 0]], dtype=np.float32)
           self.bezier = BezierData(
               control_points=control_points,
               degree=2,
               name="贝塞尔曲线"
           )
           
           # 创建圆弧
           self.arc = ArcData(
               center=(75, 25),
               radius=20,
               start_angle=0,
               end_angle=180,
               name="半圆弧"
           )
           
           # 创建多边形
           vertices = np.array([[100, 10], [120, 30], [110, 50], [90, 50], [80, 30]], dtype=np.float32)
           self.polygon = PolygonData(
               vertices=vertices,
               name="五边形"
           )
           
           # 创建标记点
           positions = np.array([[25, 75], [50, 85], [75, 75], [50, 65]], dtype=np.float32)
           self.markers = MarkersData(
               positions=positions,
               sizes=np.array([8.0, 10.0, 8.0, 6.0]),
               symbol='o',
               name="散点"
           )
       
       def setup_connections(self):
           """设置连接"""
           self.sample_btn.clicked.connect(self.sample_curves)
           self.bounds_btn.clicked.connect(self.calculate_bounds)
           self.contains_btn.clicked.connect(self.test_contains)
       
       def sample_curves(self):
           """采样曲线"""
           # 采样贝塞尔曲线
           bezier_points = self.bezier.sample(num_points=20)
           print(f"贝塞尔曲线采样点数: {len(bezier_points)}")
           
           # 采样圆弧
           arc_points = self.arc.sample(num_points=15)
           print(f"圆弧采样点数: {len(arc_points)}")
           
           self.status_label.setText(f"曲线采样完成：贝塞尔 {len(bezier_points)} 点，圆弧 {len(arc_points)} 点")
       
       def calculate_bounds(self):
           """计算边界"""
           primitives = [self.bezier, self.arc, self.polygon, self.markers]
           
           bounds_info = ["边界计算结果:"]
           for primitive in primitives:
               bounds = primitive.bounds
               width = bounds[1][0] - bounds[0][0]
               height = bounds[1][1] - bounds[0][1]
               bounds_info.append(f"{primitive.name}: 宽度={width:.1f}, 高度={height:.1f}")
           
           self.status_label.setText("\n".join(bounds_info))
       
       def test_contains(self):
           """测试点包含"""
           test_points = [(50, 25), (110, 35), (50, 75)]
           
           results = ["点包含测试:"]
           for i, point in enumerate(test_points):
               # 测试多边形包含
               in_polygon = self.polygon.contains_point(point)
               results.append(f"点{point}: 多边形内={in_polygon}")
           
           self.status_label.setText("\n".join(results))

最佳实践
--------

1. **样式复用** - 创建样式模板并在多个图元间复用
2. **数据验证** - 验证图元数据的有效性
3. **性能优化** - 使用 NumPy 数组提高计算性能
4. **内存管理** - 及时清理不需要的图元数据
5. **边界计算** - 统一使用 bounds 属性获取边界框

注意事项
--------

- 所有坐标和尺寸都使用浮点数
- 颜色值使用 RGBA 格式，范围 [0, 1]
- 边界框格式为 [[min_x, min_y], [max_x, max_y]]
- 贝塞尔曲线支持二阶和三阶
- 多边形使用射线法判断点包含
- 图像数据支持灰度和彩色图像

相关模块
--------

- :doc:`components.vispy.drawing` - 交互式绘图
- :doc:`components.vispy.drawing.coordinate_system` - 坐标系统
- :doc:`common.geometry` - 几何计算
- :doc:`common.color` - 颜色管理
