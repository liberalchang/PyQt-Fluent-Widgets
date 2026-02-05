布局组件 (Layout)
=================

本节介绍 PySide6-Fluent-Widgets 中的布局相关组件。

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

VBoxLayout
----------

垂直盒子布局，优化的垂直布局。

.. code-block:: python

   from qfluentwidgets import VBoxLayout

   # 创建垂直盒子布局
   v_layout = VBoxLayout()
   v_layout.setSpacing(8)
   v_layout.setContentsMargins(16, 16, 16, 16)
   
   # 添加组件
   v_layout.addWidget(QLabel('标签1'))
   v_layout.addWidget(QPushButton('按钮1'))
   v_layout.addWidget(QLabel('标签2'))
   v_layout.addWidget(QPushButton('按钮2'))

FluentSplitter
---------------

Fluent风格分割器。

.. code-block:: python

   from qfluentwidgets import FluentSplitter

   # 创建分割器
   splitter = FluentSplitter(Qt.Horizontal)
   
   # 添加组件
   left_widget = QWidget()
   left_widget.setStyleSheet('background-color: #f0f0f0;')
   left_widget.setMinimumWidth(200)
   
   right_widget = QWidget()
   right_widget.setStyleSheet('background-color: #e0e0e0;')
   right_widget.setMinimumWidth(200)
   
   splitter.addWidget(left_widget)
   splitter.addWidget(right_widget)
   
   # 设置分割比例
   splitter.setStretchFactor(0, 1)
   splitter.setStretchFactor(1, 2)

FluentSplitterHandle
--------------------

Fluent风格分割器手柄。

.. code-block:: python

   from qfluentwidgets import FluentSplitterHandle

   # 创建分割器手柄
   handle = FluentSplitterHandle(Qt.Horizontal)
   handle.setFixedWidth(6)

CollapseButton
--------------

折叠按钮。

.. code-block:: python

   from qfluentwidgets import CollapseButton

   # 创建折叠按钮
   collapse_btn = CollapseButton()
   collapse_btn.setText('折叠/展开')
   
   # 连接信号
   collapse_btn.clicked.connect(lambda: print('折叠按钮被点击'))

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
           self.resize(1000, 800)
           
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
           self.add_vbox_layout_example(container_layout)
           self.add_expand_layout_example(container_layout)
           self.add_splitter_example(container_layout)
           
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

       def add_vbox_layout_example(self, layout):
           """添加垂直盒子布局示例"""
           group = QGroupBox('垂直盒子布局 (VBoxLayout)')
           group_layout = QVBoxLayout(group)
           
           # 创建垂直盒子布局容器
           vbox_container = QWidget()
           vbox_container.setStyleSheet("""
               QWidget {
                   background-color: #f0f8ff;
                   border: 1px solid #b0d4f1;
                   border-radius: 8px;
               }
           """)
           
           self.vbox_layout = VBoxLayout(vbox_container)
           self.vbox_layout.setSpacing(8)
           self.vbox_layout.setContentsMargins(15, 15, 15, 15)
           
           # 添加标签
           group_layout.addWidget(QLabel('垂直盒子布局提供优化的垂直排列功能'))
           group_layout.addWidget(vbox_container)
           
           # 添加控制按钮
           button_layout = QHBoxLayout()
           
           add_vbtn = PushButton('添加标签')
           add_vbtn.clicked.connect(self.add_vbox_item)
           
           clear_vbtn = PushButton('清空')
           clear_vbtn.clicked.connect(self.clear_vbox_layout)
           
           button_layout.addWidget(add_vbtn)
           button_layout.addWidget(clear_vbtn)
           button_layout.addStretch()
           
           group_layout.addLayout(button_layout)
           
           # 初始化添加一些标签
           for i in range(6):
               self.add_vbox_item()
           
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

       def add_splitter_example(self, layout):
           """添加分割器示例"""
           group = QGroupBox('分割器 (FluentSplitter)')
           group_layout = QVBoxLayout(group)
           
           # 创建水平分割器
           h_splitter = FluentSplitter(Qt.Horizontal)
           
           # 左侧面板
           left_panel = QWidget()
           left_panel.setStyleSheet('background-color: #f8f9fa; border: 1px solid #dee2e6; border-radius: 4px;')
           left_panel.setMinimumWidth(200)
           left_layout = QVBoxLayout(left_panel)
           left_layout.addWidget(QLabel('左侧面板'))
           left_layout.addWidget(PushButton('按钮1'))
           left_layout.addWidget(PushButton('按钮2'))
           
           # 右侧面板
           right_panel = QWidget()
           right_panel.setStyleSheet('background-color: #e9ecef; border: 1px solid #dee2e6; border-radius: 4px;')
           right_panel.setMinimumWidth(200)
           right_layout = QVBoxLayout(right_panel)
           right_layout.addWidget(QLabel('右侧面板'))
           right_layout.addWidget(PushButton('按钮3'))
           right_layout.addWidget(PushButton('按钮4'))
           
           h_splitter.addWidget(left_panel)
           h_splitter.addWidget(right_panel)
           h_splitter.setStretchFactor(0, 1)
           h_splitter.setStretchFactor(1, 2)
           
           group_layout.addWidget(QLabel('水平分割器:'))
           group_layout.addWidget(h_splitter)
           
           # 创建垂直分割器
           v_splitter = FluentSplitter(Qt.Vertical)
           
           # 上方面板
           top_panel = QWidget()
           top_panel.setStyleSheet('background-color: #fff3cd; border: 1px solid #ffeaa7; border-radius: 4px;')
           top_panel.setMinimumHeight(100)
           top_layout = QVBoxLayout(top_panel)
           top_layout.addWidget(QLabel('上方面板'))
           
           # 下方面板
           bottom_panel = QWidget()
           bottom_panel.setStyleSheet('background-color: #d1ecf1; border: 1px solid #bee5eb; border-radius: 4px;')
           bottom_panel.setMinimumHeight(100)
           bottom_layout = QVBoxLayout(bottom_panel)
           bottom_layout.addWidget(QLabel('下方面板'))
           
           v_splitter.addWidget(top_panel)
           v_splitter.addWidget(bottom_panel)
           v_splitter.setStretchFactor(0, 1)
           v_splitter.setStretchFactor(1, 1)
           
           group_layout.addWidget(QLabel('垂直分割器:'))
           group_layout.addWidget(v_splitter)
           
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

       def add_vbox_item(self):
           """添加垂直盒子布局项"""
           item_count = self.vbox_layout.count()
           label = QLabel(f'标签 {item_count + 1}')
           label.setStyleSheet("""
               QLabel {
                   background-color: #0078d4;
                   color: white;
                   padding: 8px 16px;
                   border-radius: 4px;
               }
           """)
           self.vbox_layout.addWidget(label)

       def clear_vbox_layout(self):
           """清空垂直盒子布局"""
           while self.vbox_layout.count():
               item = self.vbox_layout.takeAt(0)
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
   - VBoxLayout 适合垂直排列的标签列表
   - ExpandLayout 适合设置面板、分类内容
   - FluentSplitter 适合可调整大小的面板

2. **性能优化**: 
   - 大量子组件时考虑虚拟化
   - 合理设置间距和边距

3. **响应式设计**: 
   - 确保布局在不同窗口大小下正常工作
   - 处理最小尺寸限制

4. **用户体验**: 
   - 提供平滑的展开/折叠动画
   - 保持布局的一致性和可预测性

布局对比
--------

| 布局类型 | 用途 | 特点 |
|----------|------|------|
| FlowLayout | 流式排列 | 自动换行，适合标签云 |
| VBoxLayout | 垂直排列 | 优化的垂直布局 |
| ExpandLayout | 可展开内容 | 支持折叠/展开动画 |
| FluentSplitter | 分割面板 | 可调整大小比例 |
