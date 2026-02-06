Layer Manager 层级管理器模块
===================================

Layer Manager 模块实现三级层级结构：图层 -> 类型分组 -> 图元。
该模块提供完整的图层管理功能，支持图元的组织、查找和导出。

主要功能
--------

- **三级结构** - 实现图层、类型分组、图元的三级层级
- **图元管理** - 提供图元的增删改查操作
- **图层管理** - 支持多图层的创建和管理
- **类型分组** - 按图元类型自动分组管理
- **可见性控制** - 支持图层和图元的可见性控制
- **数据导出** - 提供完整的层级数据导出功能

核心组件
--------

Primitive
~~~~~~~~~~

图元对象，封装单个图元的所有信息。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import Primitive
   from qfluentwidgets.components.vispy.drawing import PrimitiveData
   from qfluentwidgets.components.vispy_visuals import VisualEntry
   
   # 创建图元对象
   primitive = Primitive(
       id="primitive_001",
       data=primitive_data,  # PrimitiveData对象
       visual=visual_entry,  # VisualEntry对象
       selected=False,
       type_name="line",
       layer_id="layer_001"
   )

**主要属性：**
- ``id`` - 唯一标识符
- ``data`` - 图元数据
- ``visual`` - Visual渲染对象
- ``selected`` - 是否选中
- ``type_name`` - 类型名称
- ``layer_id`` - 所属图层ID

PrimitiveGroup
~~~~~~~~~~~~~~

类型分组类，管理同一类型的图元集合。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import PrimitiveGroup, Primitive
   
   # 创建类型分组
   group = PrimitiveGroup(type_name="line", layer_id="layer_001")
   
   # 添加图元
   group.addPrimitive(primitive)
   
   # 获取图元
   primitive = group.getPrimitive("primitive_001")
   
   # 获取所有图元
   all_primitives = group.getAllPrimitives()

**主要方法：**
- ``addPrimitive()`` - 添加图元
- ``removePrimitive()`` - 移除图元
- ``getPrimitive()`` - 获取图元
- ``getAllPrimitives()`` - 获取所有图元
- ``movePrimitive()`` - 移动图元位置
- ``clear()`` - 清空所有图元

Layer
~~~~~~

图层类，管理多个类型分组。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import Layer, Primitive
   
   # 创建图层
   layer = Layer(
       layer_id="layer_001",
       name="线条图层",
       zorder=1
   )
   
   # 添加图元
   layer.addPrimitive(primitive)
   
   # 设置可见性
   layer.setVisible(True)
   
   # 获取指定类型的图元
   lines = layer.getPrimitivesByType("line")

**主要方法：**
- ``addPrimitive()`` - 添加图元
- ``removePrimitive()`` - 移除图元
- ``getPrimitive()`` - 获取图元
- ``getAllPrimitives()`` - 获取所有图元
- ``getPrimitivesByType()`` - 获取指定类型的图元
- ``setVisible()`` - 设置可见性
- ``clear()`` - 清空图层

LayerManager
~~~~~~~~~~~~

图层管理器类，管理所有图层的顶层管理器。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import LayerManager, Primitive
   
   # 创建图层管理器
   manager = LayerManager()
   
   # 添加新图层
   new_layer = manager.addLayer("新图层", zorder=1)
   
   # 添加图元到指定图层
   manager.addPrimitive(primitive, new_layer.id)
   
   # 获取所有图元
   all_primitives = manager.getAllPrimitives()
   
   # 导出数据
   data = manager.exportData()

**主要方法：**
- ``addLayer()`` - 添加新图层
- ``removeLayer()`` - 移除图层
- ``getLayer()`` - 获取图层
- ``getAllLayers()`` - 获取所有图层
- ``addPrimitive()`` - 添加图元
- ``removePrimitive()`` - 移除图元
- ``getPrimitive()`` - 获取图元
- ``getAllPrimitives()`` - 获取所有图元
- ``movePrimitiveToLayer()`` - 移动图元到另一个图层
- ``clear()`` - 清空所有图层
- ``exportData()`` - 导出数据

实际应用
--------

基本层级管理
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import LayerManager
   from qfluentwidgets.components.vispy.drawing import PrimitiveData, LineData, CircleData
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   import numpy as np
   
   class BasicLayerWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_layer_manager()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("基本层级管理")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.add_layer_btn = PushButton("添加图层")
           self.add_line_btn = PushButton("添加线条")
           self.add_circle_btn = PushButton("添加圆形")
           self.clear_btn = PushButton("清空所有")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.add_layer_btn)
           header_layout.addWidget(self.add_line_btn)
           header_layout.addWidget(self.add_circle_btn)
           header_layout.addWidget(self.clear_btn)
           
           # 显示当前状态
           self.status_label = Label("状态: 层级管理器已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_layer_manager(self):
           """设置层级管理器"""
           self.layer_manager = LayerManager()
           
           # 创建示例图元（需要实际的visual对象）
           # 这里仅作示例，实际使用时需要传入正确的VisualEntry
           self.status_label.setText("状态: 层级管理器已设置")
       
       def setup_connections(self):
           """设置连接"""
           self.add_layer_btn.clicked.connect(self.add_layer)
           self.add_line_btn.clicked.connect(self.add_line)
           self.add_circle_btn.clicked.connect(self.add_circle)
           self.clear_btn.clicked.connect(self.clear_all)
       
       def add_layer(self):
           """添加新图层"""
           import random
           
           layer_name = f"图层_{random.randint(100, 999)}"
           zorder = len(self.layer_manager.getAllLayers())
           
           new_layer = self.layer_manager.addLayer(layer_name, zorder)
           self.status_label.setText(f"状态: 已添加图层 {layer_name}")
       
       def add_line(self):
           """添加线条图元"""
           import random
           
           # 创建线条数据
           points = np.array([
               [random.randint(10, 100), random.randint(10, 100)],
               [random.randint(100, 200), random.randint(10, 100)]
           ], dtype=np.float32)
           
           line_data = LineData(
               points=points,
               name=f"线条_{random.randint(100, 999)}"
           )
           
           # 这里需要创建实际的VisualEntry对象
           # 示例代码，实际使用时需要传入正确的对象
           self.status_label.setText("状态: 需要VisualEntry对象来创建图元")
       
       def add_circle(self):
           """添加圆形图元"""
           import random
           
           # 创建圆形数据
           circle_data = CircleData(
               center=(random.randint(50, 150), random.randint(50, 150)),
               radius=(random.randint(20, 40), random.randint(20, 40)),
               name=f"圆形_{random.randint(100, 999)}"
           )
           
           # 这里需要创建实际的VisualEntry对象
           self.status_label.setText("状态: 需要VisualEntry对象来创建图元")
       
       def clear_all(self):
           """清空所有图层"""
           self.layer_manager.clear()
           self.status_label.setText("状态: 所有图层已清空")

高级层级管理
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import LayerManager
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   
   class AdvancedLayerWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_layer_manager()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("高级层级管理")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.list_btn = PushButton("列出图层")
           self.export_btn = PushButton("导出数据")
           self.count_btn = PushButton("统计信息")
           self.move_btn = PushButton("移动图元")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.list_btn)
           header_layout.addWidget(self.export_btn)
           header_layout.addWidget(self.count_btn)
           header_layout.addWidget(self.move_btn)
           
           # 显示当前状态
           self.status_label = Label("状态: 高级层级管理器已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_layer_manager(self):
           """设置高级层级管理器"""
           self.layer_manager = LayerManager()
           
           # 添加几个示例图层
           self.layer_manager.addLayer("背景层", zorder=0)
           self.layer_manager.addLayer("绘图层", zorder=1)
           self.layer_manager.addLayer("标注层", zorder=2)
           
           self.status_label.setText("状态: 高级层级管理器已设置")
       
       def setup_connections(self):
           """设置连接"""
           self.list_btn.clicked.connect(self.list_layers)
           self.export_btn.clicked.connect(self.export_data)
           self.count_btn.clicked.connect(self.show_statistics)
           self.move_btn.clicked.connect(self.move_primitive_demo)
       
       def list_layers(self):
           """列出所有图层"""
           layers = self.layer_manager.getAllLayers()
           
           if layers:
               info_lines = [f"图层数量: {len(layers)}"]
               for layer in layers:
                   primitive_count = len(layer)
                   info_lines.append(f"- {layer.name} (ID: {layer.id[:8]}): {primitive_count} 个图元")
               
               self.status_label.setText("\n".join(info_lines))
           else:
               self.status_label.setText("状态: 没有图层")
       
       def export_data(self):
           """导出数据"""
           data = self.layer_manager.exportData()
           
           layer_count = len(data.get('layers', []))
           total_primitives = sum(len(layer.get('primitives', [])) for layer in data.get('layers', []))
           
           self.status_label.setText(f"状态: 数据已导出，{layer_count} 个图层，{total_primitives} 个图元")
           print(f"导出的数据结构: {list(data.keys())}")
       
       def show_statistics(self):
           """显示统计信息"""
           layers = self.layer_manager.getAllLayers()
           all_primitives = self.layer_manager.getAllPrimitives()
           
           # 按类型统计
           type_counts = {}
           for primitive in all_primitives:
               type_name = primitive.type_name
               type_counts[type_name] = type_counts.get(type_name, 0) + 1
           
           # 构建统计信息
           info_lines = [
               f"图层数量: {len(layers)}",
               f"图元总数: {len(all_primitives)}",
               "类型分布:"
           ]
           
           for type_name, count in type_counts.items():
               info_lines.append(f"  - {type_name}: {count} 个")
           
           self.status_label.setText("\n".join(info_lines))
       
       def move_primitive_demo(self):
           """移动图元演示"""
           layers = self.layer_manager.getAllLayers()
           
           if len(layers) < 2:
               self.status_label.setText("状态: 需要至少2个图层才能演示移动")
               return
           
           # 获取第一个和最后一个图层
           source_layer = layers[0]
           target_layer = layers[-1]
           
           # 查找源图层中的图元
           source_primitives = source_layer.getAllPrimitives()
           
           if source_primitives:
               # 移动第一个图元到目标图层
               primitive = source_primitives[0]
               success = self.layer_manager.movePrimitiveToLayer(
                   primitive.id, 
                   target_layer.id
               )
               
               if success:
                   self.status_label.setText(f"状态: 已将图元从 {source_layer.name} 移动到 {target_layer.name}")
               else:
                   self.status_label.setText("状态: 移动图元失败")
           else:
               self.status_label.setText(f"状态: {source_layer.name} 中没有图元可移动")

最佳实践
--------

1. **层级组织** - 合理规划图层结构和命名
2. **类型分组** - 利用自动类型分组功能
3. **可见性管理** - 正确使用图层可见性控制
4. **数据导出** - 定期导出重要的层级数据
5. **性能优化** - 避免在单个图层中放置过多图元

注意事项
--------

- 图层ID是自动生成的唯一标识符
- zorder值越大，图层越靠上显示
- 图元会自动按类型分组到对应的PrimitiveGroup
- 移除图元时需要提供正确的类型名称以提高效率
- 数据导出包含完整的层级结构和图元信息
- 图层锁定状态主要用于UI层面的控制

相关模块
--------

- :doc:`components.vispy.drawing.data_models` - 数据模型
- :doc:`components.vispy.drawing.drawing_canvas` - 绘图画布
- :doc:`components.vispy.drawing.selection_manager` - 选择管理
- :doc:`components.vispy.vispy_visuals` - Vispy可视化元素
- :doc:`common.data_structure` - 数据结构
