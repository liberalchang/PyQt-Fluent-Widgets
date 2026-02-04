布局组件 (Layout)
=================

本节介绍 PySide6-Fluent-Widgets 中的布局相关组件。

FlowLayout
----------

流式布局，自动排列子组件。

.. code-block:: python

   from qfluentwidgets import FlowLayout
   from PySide6.QtWidgets import QPushButton, QLabel

   # 创建流式布局
   flow_layout = FlowLayout()
   flow_layout.setSpacing(10)
   flow_layout.setContentsMargins(20, 20, 20, 20)
   
   # 添加组件
   for i in range(10):
       btn = QPushButton(f'按钮 {i+1}')
       flow_layout.addWidget(btn)

VFlowLayout
-----------

垂直流式布局，垂直方向自动排列。

.. code-block:: python

   from qfluentwidgets import VFlowLayout

   # 创建垂直流式布局
   vflow_layout = VFlowLayout()
   vflow_layout.setSpacing(8)
   vflow_layout.setContentsMargins(16, 16, 16, 16)
   
   # 添加组件
   for i in range(8):
       label = QLabel(f'标签 {i+1}')
       label.setFixedHeight(30)
       vflow_layout.addWidget(label)

ExpandLayout
------------

可展开布局，支持折叠/展开功能。

.. code-block:: python

   from qfluentwidgets import ExpandLayout

   # 创建可展开布局
   expand_layout = ExpandLayout()
   
   # 添加可折叠的内容
   content1 = QWidget()
   content1_layout = QVBoxLayout(content1)
   content1_layout.addWidget(QLabel('内容1'))
   content1_layout.addWidget(QPushButton('按钮1'))
   
   expand_layout.addWidget(content1, '标题1', True)  # 默认展开
   
   content2 = QWidget()
   content2_layout = QVBoxLayout(content2)
   content2_layout.addWidget(QLabel('内容2'))
   content2_layout.addWidget(QPushButton('按钮2'))
   
   expand_layout.addWidget(content2, '标题2', False)  # 默认折叠

完整示例
--------

下面是一个完整的布局组件使用示例：

.. code-block:: python

   import sys
   from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                                QWidget, QLabel, QPushButton, QGroupBox, QScrollArea)
   from PySide6.QtCore import Qt
   from qfluentwidgets import *

   class LayoutDemoWindow(QMainWindow):
       def __init__(self):
           super().__init__()
           
           self.setWindowTitle('布局组件示例')
           self.resize(800, 600)
           
           # 创建界面
           self.setup_ui()

       def setup_ui(self):
           """设置界面"""
           # 创建滚动区域
           scroll_area = QScrollArea()
           scroll_area.setWidgetResizable(True)
           scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
           
           # 创建主容器
           container = QWidget()
           container_layout = QVBoxLayout(container)
           container_layout.setSpacing(20)
           container_layout.setContentsMargins(20, 20, 20, 20)
           
           # 添加标题
           title = SubtitleLabel('布局组件示例')
           container_layout.addWidget(title)
           
           # 添加各种布局示例
           self.add_flow_layout_example(container_layout)
           self.add_vflow_layout_example(container_layout)
           self.add_expand_layout_example(container_layout)
           
           # 添加弹性空间
           container_layout.addStretch()
           
           scroll_area.setWidget(container)
           self.setCentralWidget(scroll_area)

       def add_flow_layout_example(self, layout):
           """添加流式布局示例"""
           group = QGroupBox('流式布局 (FlowLayout)')
           group_layout = QVBoxLayout(group)
           
           # 创建流式布局容器
           flow_container = QWidget()
           flow_container.setStyleSheet("""
               QWidget {
                   background-color: #f5f5f5;
                   border: 1px solid #ddd;
                   border-radius: 8px;
               }
           """)
           
           self.flow_layout = FlowLayout(flow_container)
           self.flow_layout.setSpacing(10)
           self.flow_layout.setContentsMargins(15, 15, 15, 15)
           
           # 添加标签
           group_layout.addWidget(QLabel('流式布局会自动排列子组件，当空间不足时自动换行'))
           group_layout.addWidget(flow_container)
           
           # 添加控制按钮
           button_layout = QHBoxLayout()
           
           add_btn = PushButton('添加按钮')
           add_btn.clicked.connect(self.add_flow_button)
           
           clear_btn = PushButton('清空')
           clear_btn.clicked.connect(self.clear_flow_layout)
           
           button_layout.addWidget(add_btn)
           button_layout.addWidget(clear_btn)
           button_layout.addStretch()
           
           group_layout.addLayout(button_layout)
           
           # 初始化添加一些按钮
           for i in range(8):
               self.add_flow_button()
           
           layout.addWidget(group)

       def add_vflow_layout_example(self, layout):
           """添加垂直流式布局示例"""
           group = QGroupBox('垂直流式布局 (VFlowLayout)')
           group_layout = QVBoxLayout(group)
           
           # 创建垂直流式布局容器
           vflow_container = QWidget()
           vflow_container.setStyleSheet("""
               QWidget {
                   background-color: #f0f8ff;
                   border: 1px solid #b0d4f1;
                   border-radius: 8px;
               }
           """)
           
           self.vflow_layout = VFlowLayout(vflow_container)
           self.vflow_layout.setSpacing(8)
           self.vflow_layout.setContentsMargins(15, 15, 15, 15)
           
           # 添加标签
           group_layout.addWidget(QLabel('垂直流式布局在垂直方向自动排列子组件'))
           group_layout.addWidget(vflow_container)
           
           # 添加控制按钮
           button_layout = QHBoxLayout()
           
           add_vbtn = PushButton('添加标签')
           add_vbtn.clicked.connect(self.add_vflow_item)
           
           clear_vbtn = PushButton('清空')
           clear_vbtn.clicked.connect(self.clear_vflow_layout)
           
           button_layout.addWidget(add_vbtn)
           button_layout.addWidget(clear_vbtn)
           button_layout.addStretch()
           
           group_layout.addLayout(button_layout)
           
           # 初始化添加一些标签
           for i in range(6):
               self.add_vflow_item()
           
           layout.addWidget(group)

       def add_expand_layout_example(self, layout):
           """添加可展开布局示例"""
           group = QGroupBox('可展开布局 (ExpandLayout)')
           group_layout = QVBoxLayout(group)
           
           # 创建可展开布局
           self.expand_layout = ExpandLayout()
           
           # 添加可展开的内容
           self.add_expand_section('基础设置', self.create_basic_settings())
           self.add_expand_section('高级设置', self.create_advanced_settings())
           self.add_expand_section('网络设置', self.create_network_settings())
           
           group_layout.addWidget(self.expand_layout)
           
           layout.addWidget(group)

       def add_expand_section(self, title, content):
           """添加可展开部分"""
           self.expand_layout.addWidget(content, title, True)

       def create_basic_settings(self):
           """创建基础设置内容"""
           widget = QWidget()
           layout = QVBoxLayout(widget)
           
           layout.addWidget(QLabel('这是基础设置的内容'))
           layout.addWidget(SwitchSettingCard(FluentIcon.BRIGHTNESS, '启用通知', '接收系统通知'))
           layout.addWidget(RangeSettingCard(FluentIcon.VOLUME, '音量', '调整系统音量'))
           
           return widget

       def create_advanced_settings(self):
           """创建高级设置内容"""
           widget = QWidget()
           layout = QVBoxLayout(widget)
           
           layout.addWidget(QLabel('这是高级设置的内容'))
           layout.addWidget(ComboBoxSettingCard(FluentIcon.LANGUAGE, '语言', '选择界面语言'))
           layout.addWidget(ColorSettingCard(FluentIcon.PALETTE, '主题颜色', '选择主题颜色'))
           
           return widget

       def create_network_settings(self):
           """创建网络设置内容"""
           widget = QWidget()
           layout = QVBoxLayout(widget)
           
           layout.addWidget(QLabel('这是网络设置的内容'))
           layout.addWidget(SwitchSettingCard(FluentIcon.WIFI, 'Wi-Fi', '启用无线网络'))
           layout.addWidget(SwitchSettingCard(FluentIcon.BLUETOOTH, '蓝牙', '启用蓝牙'))
           
           return widget

       def add_flow_button(self):
           """添加流式布局按钮"""
           btn_count = self.flow_layout.count()
           btn = PushButton(f'按钮 {btn_count + 1}')
           self.flow_layout.addWidget(btn)

       def clear_flow_layout(self):
           """清空流式布局"""
           while self.flow_layout.count():
               item = self.flow_layout.takeAt(0)
               if item.widget():
                   item.widget().deleteLater()

       def add_vflow_item(self):
           """添加垂直流式布局项"""
           item_count = self.vflow_layout.count()
           label = QLabel(f'标签 {item_count + 1}')
           label.setStyleSheet("""
               QLabel {
                   background-color: #0078d4;
                   color: white;
                   padding: 8px 16px;
                   border-radius: 4px;
               }
           """)
           self.vflow_layout.addWidget(label)

       def clear_vflow_layout(self):
           """清空垂直流式布局"""
           while self.vflow_layout.count():
               item = self.vflow_layout.takeAt(0)
               if item.widget():
                   item.widget().deleteLater()

   if __name__ == '__main__':
       app = QApplication(sys.argv)
       window = LayoutDemoWindow()
       window.show()
       sys.exit(app.exec())

最佳实践
--------

1. **布局选择**: 
   - FlowLayout 适合标签云、按钮组等
   - VFlowLayout 适合垂直排列的标签列表
   - ExpandLayout 适合设置面板、分类内容

2. **性能优化**: 
   - 大量子组件时考虑虚拟化
   - 合理设置间距和边距

3. **响应式设计**: 
   - 确保布局在不同窗口大小下正常工作
   - 处理最小尺寸限制

4. **用户体验**: 
   - 提供平滑的展开/折叠动画
   - 保持布局的一致性和可预测性
