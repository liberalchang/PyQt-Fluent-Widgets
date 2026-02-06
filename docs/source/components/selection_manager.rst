Selection Manager 选择管理器模块
====================================

Selection Manager 模块实现图元的选择功能，提供点选检测、框选检测和高亮渲染。
该模块支持多种图元类型的精确碰撞检测和选择状态管理。

主要功能
--------

- **点选检测** - 支持鼠标点击选中图元
- **框选检测** - 支持拖拽矩形框选中多个图元
- **高亮渲染** - 为选中的图元添加高亮效果
- **碰撞检测** - 支持多种图元类型的精确碰撞检测
- **选择管理** - 提供完整的选择状态管理
- **信号系统** - 提供选择变化的通知机制

核心组件
--------

SelectionManager
~~~~~~~~~~~~~~~

选择管理器类，管理图元的选择状态。

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import SelectionManager
   from qfluentwidgets.components.vispy.drawing import LayerManager, CoordinateSystem
   
   # 创建选择管理器
   layer_manager = LayerManager()
   coord_system = CoordinateSystem(view, canvas)
   
   manager = SelectionManager(
       layer_manager=layer_manager,
       coordinate_system=coord_system,
       parent_view=view
   )
   
   # 连接信号
   manager.selectionChanged.connect(self.on_selection_changed)
   
   # 点选图元
   primitive_id = manager.pickPrimitive(100, 100)
   if primitive_id:
       manager.selectPrimitive(primitive_id)
   
   # 框选图元
   selected_ids = manager.boxSelect(50, 50, 200, 200)

**主要信号：**
- ``selectionChanged`` - 选中的图元ID列表变化信号

**主要方法：**
- ``selectPrimitive()`` - 选中图元
- ``deselectPrimitive()`` - 取消选中图元
- ``clearSelection()`` - 清除所有选择
- ``getSelectedPrimitives()`` - 获取当前选中的图元ID列表
- ``isSelected()`` - 判断图元是否被选中
- ``pickPrimitive()`` - 点选检测
- ``boxSelect()`` - 框选检测
- ``setSelectionThreshold()`` - 设置点选阈值
- ``updateHighlights()`` - 更新高亮效果

实际应用
--------

基本选择管理
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import SelectionManager
   from qfluentwidgets.components.vispy.drawing import LayerManager, CoordinateSystem
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   
   class BasicSelectionWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_selection_manager()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("基本选择管理")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.pick_btn = PushButton("点选测试")
           self.box_btn = PushButton("框选测试")
           self.clear_btn = PushButton("清除选择")
           self.threshold_btn = PushButton("设置阈值")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.pick_btn)
           header_layout.addWidget(self.box_btn)
           header_layout.addWidget(self.clear_btn)
           header_layout.addWidget(self.threshold_btn)
           
           # 显示当前状态
           self.status_label = Label("状态: 选择管理器已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_selection_manager(self):
           """设置选择管理器"""
           # 这里需要实际的图层管理器和坐标系统
           # 示例代码，实际使用时需要传入正确的对象
           self.layer_manager = LayerManager()
           self.coord_system = None  # 需要传入 CoordinateSystem
           self.view = None  # 需要传入 vispy view
           
           if self.coord_system and self.view:
               self.selection_manager = SelectionManager(
                   self.layer_manager,
                   self.coord_system,
                   self.view
               )
               
               # 连接信号
               self.selection_manager.selectionChanged.connect(self.on_selection_changed)
               
               self.status_label.setText("状态: 选择管理器已设置")
           else:
               self.status_label.setText("状态: 需要坐标系统和视图对象")
       
       def setup_connections(self):
           """设置连接"""
           self.pick_btn.clicked.connect(self.test_pick_selection)
           self.box_btn.clicked.connect(self.test_box_selection)
           self.clear_btn.clicked.connect(self.clear_selection)
           self.threshold_btn.clicked.connect(self.set_threshold)
       
       def test_pick_selection(self):
           """测试点选"""
           if hasattr(self, 'selection_manager'):
               # 模拟点选测试
               test_points = [(100, 100), (150, 150), (200, 100)]
               
               for x, y in test_points:
                   primitive_id = self.selection_manager.pickPrimitive(x, y)
                   if primitive_id:
                       self.selection_manager.selectPrimitive(primitive_id)
                       self.status_label.setText(f"状态: 已选中图元 {primitive_id[:8]}")
                       break
               else:
                   self.status_label.setText(f"状态: 点 ({x}, {y}) 未命中任何图元")
           else:
               self.status_label.setText("状态: 选择管理器未初始化")
       
       def test_box_selection(self):
           """测试框选"""
           if hasattr(self, 'selection_manager'):
               # 模拟框选测试
               x1, y1 = 50, 50
               x2, y2 = 200, 200
               
               selected_ids = self.selection_manager.boxSelect(x1, y1, x2, y2)
               
               if selected_ids:
                   self.status_label.setText(f"状态: 框选选中 {len(selected_ids)} 个图元")
               else:
                   self.status_label.setText("状态: 框选未命中任何图元")
           else:
               self.status_label.setText("状态: 选择管理器未初始化")
       
       def clear_selection(self):
           """清除选择"""
           if hasattr(self, 'selection_manager'):
               self.selection_manager.clearSelection()
               self.status_label.setText("状态: 已清除所有选择")
           else:
               self.status_label.setText("状态: 选择管理器未初始化")
       
       def set_threshold(self):
           """设置选择阈值"""
           if hasattr(self, 'selection_manager'):
               # 设置较大的阈值便于选择
               self.selection_manager.setSelectionThreshold(10.0)
               self.status_label.setText("状态: 已设置选择阈值为 10.0 像素")
           else:
               self.status_label.setText("状态: 选择管理器未初始化")
       
       def on_selection_changed(self, selected_ids):
           """选择变化处理"""
           if selected_ids:
               print(f"当前选中的图元: {selected_ids}")
           else:
               print("已清除所有选择")

高级选择管理
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import SelectionManager
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   
   class AdvancedSelectionWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_selection_manager()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("高级选择管理")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.multi_btn = PushButton("多选测试")
           self.append_btn = PushButton("追加选择")
           self.highlight_btn = PushButton("更新高亮")
           self.info_btn = PushButton("选择信息")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.multi_btn)
           header_layout.addWidget(self.append_btn)
           header_layout.addWidget(self.highlight_btn)
           header_layout.addWidget(self.info_btn)
           
           # 显示当前状态
           self.status_label = Label("状态: 高级选择管理器已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_selection_manager(self):
           """设置高级选择管理器"""
           # 这里需要实际的图层管理器和坐标系统
           self.layer_manager = LayerManager()
           self.coord_system = None  # 需要传入 CoordinateSystem
           self.view = None  # 需要传入 vispy view
           
           if self.coord_system and self.view:
               self.selection_manager = SelectionManager(
                   self.layer_manager,
                   self.coord_system,
                   self.view
               )
               
               # 连接信号
               self.selection_manager.selectionChanged.connect(self.on_selection_changed)
               
               self.status_label.setText("状态: 高级选择管理器已设置")
           else:
               self.status_label.setText("状态: 需要坐标系统和视图对象")
       
       def setup_connections(self):
           """设置连接"""
           self.multi_btn.clicked.connect(self.test_multi_selection)
           self.append_btn.clicked.connect(self.test_append_selection)
           self.highlight_btn.clicked.connect(self.update_highlights)
           self.info_btn.clicked.connect(self.show_selection_info)
       
       def test_multi_selection(self):
           """测试多选"""
           if hasattr(self, 'selection_manager'):
               # 清除现有选择
               self.selection_manager.clearSelection()
               
               # 模拟多次点选
               test_points = [(80, 80), (120, 120), (160, 80)]
               
               selected_count = 0
               for x, y in test_points:
                   primitive_id = self.selection_manager.pickPrimitive(x, y)
                   if primitive_id:
                       # 追加选择（不清除之前的选择）
                       self.selection_manager.selectPrimitive(primitive_id, append=True)
                       selected_count += 1
               
               self.status_label.setText(f"状态: 多选测试完成，选中 {selected_count} 个图元")
           else:
               self.status_label.setText("状态: 选择管理器未初始化")
       
       def test_append_selection(self):
           """测试追加选择"""
           if hasattr(self, 'selection_manager'):
               # 先选择一个图元
               primitive_id = self.selection_manager.pickPrimitive(100, 100)
               if primitive_id:
                   self.selection_manager.selectPrimitive(primitive_id, append=False)
                   
                   # 再追加选择另一个图元
                   primitive_id2 = self.selection_manager.pickPrimitive(150, 150)
                   if primitive_id2:
                       self.selection_manager.selectPrimitive(primitive_id2, append=True)
                       self.status_label.setText("状态: 追加选择测试完成")
                   else:
                       self.status_label.setText("状态: 未找到第二个图元")
               else:
                   self.status_label.setText("状态: 未找到第一个图元")
           else:
               self.status_label.setText("状态: 选择管理器未初始化")
       
       def update_highlights(self):
           """更新高亮效果"""
           if hasattr(self, 'selection_manager'):
               self.selection_manager.updateHighlights()
               self.status_label.setText("状态: 高亮效果已更新")
           else:
               self.status_label.setText("状态: 选择管理器未初始化")
       
       def show_selection_info(self):
           """显示选择信息"""
           if hasattr(self, 'selection_manager'):
               selected_ids = self.selection_manager.getSelectedPrimitives()
               
               if selected_ids:
                   info_lines = [f"当前选择: {len(selected_ids)} 个图元"]
                   for i, primitive_id in enumerate(selected_ids, 1):
                       info_lines.append(f"  {i}. {primitive_id[:8]}")
                   
                   self.status_label.setText("\n".join(info_lines))
               else:
                   self.status_label.setText("状态: 当前无选择")
           else:
               self.status_label.setText("状态: 选择管理器未初始化")
       
       def on_selection_changed(self, selected_ids):
           """选择变化处理"""
           if selected_ids:
               print(f"选择已变化: {len(selected_ids)} 个图元")
           else:
               print("选择已清空")

碰撞检测应用
~~~~~~~~~~~~

.. code-block:: python

   from qfluentwidgets.components.vispy.drawing import SelectionManager
   from qfluentwidgets import CardWidget, Label, PushButton
   from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout
   from PySide6.QtCore import Qt
   
   class CollisionTestWidget(CardWidget):
       def __init__(self):
           super().__init__()
           self.setup_ui()
           self.setup_selection_manager()
       
       def setup_ui(self):
           layout = QVBoxLayout()
           
           # 创建标题和控制按钮
           header_layout = QHBoxLayout()
           
           title_label = Label("碰撞检测应用")
           title_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")
           
           self.line_btn = PushButton("线条检测")
           self.circle_btn = PushButton("圆形检测")
           self.rect_btn = PushButton("矩形检测")
           self.distance_btn = PushButton("距离计算")
           
           header_layout.addWidget(title_label)
           header_layout.addStretch()
           header_layout.addWidget(self.line_btn)
           header_layout.addWidget(self.circle_btn)
           header_layout.addWidget(self.rect_btn)
           header_layout.addWidget(self.distance_btn)
           
           # 显示当前状态
           self.status_label = Label("状态: 碰撞检测应用已初始化")
           self.status_label.setStyleSheet("padding: 10px;")
           
           layout.addLayout(header_layout)
           layout.addWidget(self.status_label)
           self.setLayout(layout)
       
       def setup_selection_manager(self):
           """设置碰撞检测"""
           self.layer_manager = LayerManager()
           self.coord_system = None  # 需要传入 CoordinateSystem
           self.view = None  # 需要传入 vispy view
           
           if self.coord_system and self.view:
               self.selection_manager = SelectionManager(
                   self.layer_manager,
                   self.coord_system,
                   self.view
               )
               
               self.status_label.setText("状态: 碰撞检测已设置")
           else:
               self.status_label.setText("状态: 需要坐标系统和视图对象")
       
       def setup_connections(self):
           """设置连接"""
           self.line_btn.clicked.connect(self.test_line_collision)
           self.circle_btn.clicked.connect(self.test_circle_collision)
           self.rect_btn.clicked.connect(self.test_rectangle_collision)
           self.distance_btn.clicked.connect(self.test_distance_calculation)
       
       def test_line_collision(self):
           """测试线条碰撞检测"""
           if hasattr(self, 'selection_manager'):
               # 测试多个点的线条碰撞
               test_points = [(100, 100), (110, 110), (120, 100), (130, 130)]
               
               hit_results = []
               for x, y in test_points:
                   primitive_id = self.selection_manager.pickPrimitive(x, y)
                   if primitive_id:
                       hit_results.append(f"点({x},{y}) 命中 {primitive_id[:8]}")
                   else:
                       hit_results.append(f"点({x},{y}) 未命中")
               
               self.status_label.setText("\n".join(hit_results))
           else:
               self.status_label.setText("状态: 选择管理器未初始化")
       
       def test_circle_collision(self):
           """测试圆形碰撞检测"""
           if hasattr(self, 'selection_manager'):
               # 测试圆形区域内的碰撞
               center_x, center_y = 150, 150
               test_radius = 30
               
               # 在圆形边界上测试多个点
               import math
               hit_count = 0
               total_tests = 8
               
               for i in range(total_tests):
                   angle = 2 * math.pi * i / total_tests
                   x = center_x + test_radius * math.cos(angle)
                   y = center_y + test_radius * math.sin(angle)
                   
                   primitive_id = self.selection_manager.pickPrimitive(x, y)
                   if primitive_id:
                       hit_count += 1
               
               self.status_label.setText(f"状态: 圆形碰撞测试，{hit_count}/{total_tests} 个点命中")
           else:
               self.status_label.setText("状态: 选择管理器未初始化")
       
       def test_rectangle_collision(self):
           """测试矩形碰撞检测"""
           if hasattr(self, 'selection_manager'):
               # 测试矩形区域内的碰撞
               x1, y1 = 50, 50
               x2, y2 = 200, 150
               
               selected_ids = self.selection_manager.boxSelect(x1, y1, x2, y2)
               
               self.status_label.setText(f"状态: 矩形框选命中 {len(selected_ids)} 个图元")
           else:
               self.status_label.setText("状态: 选择管理器未初始化")
       
       def test_distance_calculation(self):
           """测试距离计算"""
           if hasattr(self, 'selection_manager'):
               # 使用静态方法计算点到线段的距离
               from qfluentwidgets.components.vispy.drawing.selection_manager import SelectionManager
               
               # 测试点到线段的距离
               px, py = 100, 100
               x1, y1 = 50, 50
               x2, y2 = 150, 150
               
               distance = SelectionManager._pointToSegmentDistance(px, py, x1, y1, x2, y2)
               
               self.status_label.setText(f"状态: 点({px},{py}) 到线段({x1},{y1})-({x2},{y2}) 的距离: {distance:.2f}")
           else:
               self.status_label.setText("状态: 选择管理器未初始化")

最佳实践
--------

1. **阈值设置** - 根据图元密度合理设置选择阈值
2. **性能优化** - 避免过于频繁的选择检测
3. **高亮管理** - 及时更新和清理高亮效果
4. **信号处理** - 正确连接和处理选择变化信号
5. **碰撞精度** - 根据需求选择合适的碰撞检测精度

注意事项
--------

- 选择管理器需要有效的图层管理器和坐标系统
- 点选阈值以像素为单位，会自动转换为世界坐标
- 框选使用世界坐标系进行计算
- 高亮效果需要 vispy 环境支持
- 锁定的图元无法被选中
- 不可见的图元不会被检测到
- 碰撞检测的精度影响选择准确性

相关模块
--------

- :doc:`components.vispy.drawing.layer_manager` - 图层管理
- :doc:`components.vispy.drawing.coordinate_system` - 坐标系统
- :doc:`components.vispy.drawing.data_models` - 数据模型
- :doc:`components.vispy.drawing.interaction_manager` - 交互管理
- :doc:`common.geometry` - 几何计算
