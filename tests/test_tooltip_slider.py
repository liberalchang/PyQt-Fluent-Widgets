#!/usr/bin/env python3
# coding: utf-8

"""
ToolTipSlider 测试

测试带工具提示的滑动条功能：
1. 拖动时显示数值
2. 自定义格式
3. 延迟显示
4. 水平和垂直方向
"""

import sys
import os

# 添加父目录到路径，以便导入本地模块
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QPushButton, QSpinBox
from PySide6.QtCore import Qt

from qfluentwidgets.components.widgets.slider import ToolTipSlider
from qfluentwidgets.components.widgets.label import BodyLabel, SubtitleLabel
from qfluentwidgets import setTheme, Theme


class ToolTipSliderTest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ToolTipSlider 测试")
        self.setGeometry(100, 100, 800, 600)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建布局
        layout = QVBoxLayout(central_widget)
        
        # 标题
        title = SubtitleLabel("ToolTipSlider 测试")
        layout.addWidget(title)
        
        # 说明
        description = BodyLabel("拖动滑动条时会在滑块上方显示当前数值")
        layout.addWidget(description)
        
        # 基本水平滑动条
        layout.addWidget(QLabel("基本水平滑动条:"))
        self.basic_slider = ToolTipSlider(Qt.Horizontal)
        self.basic_slider.setRange(0, 100)
        self.basic_slider.setValue(50)
        layout.addWidget(self.basic_slider)
        
        # 自定义格式的水平滑动条
        layout.addWidget(QLabel("百分比格式滑动条:"))
        self.percentage_slider = ToolTipSlider(Qt.Horizontal)
        self.percentage_slider.setRange(0, 100)
        self.percentage_slider.setValue(30)
        self.percentage_slider.setToolTipFormat("{:.1f}%")
        layout.addWidget(self.percentage_slider)
        
        # 带前缀的滑动条
        layout.addWidget(QLabel("带前缀的滑动条:"))
        self.prefix_slider = ToolTipSlider(Qt.Horizontal)
        self.prefix_slider.setRange(0, 255)
        self.prefix_slider.setValue(128)
        self.prefix_slider.setToolTipFormat("RGB: {}")
        layout.addWidget(self.prefix_slider)
        
        # 垂直滑动条
        h_layout = QHBoxLayout()
        
        # 基本垂直滑动条
        v_layout1 = QVBoxLayout()
        v_layout1.addWidget(QLabel("基本垂直滑动条:"))
        self.vertical_slider = ToolTipSlider(Qt.Vertical)
        self.vertical_slider.setRange(0, 100)
        self.vertical_slider.setValue(60)
        v_layout1.addWidget(self.vertical_slider)
        h_layout.addLayout(v_layout1)
        
        # 自定义格式的垂直滑动条
        v_layout2 = QVBoxLayout()
        v_layout2.addWidget(QLabel("音量格式:"))
        self.volume_slider = ToolTipSlider(Qt.Vertical)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(75)
        self.volume_slider.setToolTipFormat("音量: {}%")
        v_layout2.addWidget(self.volume_slider)
        h_layout.addLayout(v_layout2)
        
        layout.addLayout(h_layout)
        
        # 控制面板
        control_layout = QHBoxLayout()
        
        # 延迟设置
        delay_layout = QVBoxLayout()
        delay_layout.addWidget(QLabel("工具提示延迟 (ms):"))
        self.delay_spinbox = QSpinBox()
        self.delay_spinbox.setRange(0, 2000)
        self.delay_spinbox.setValue(500)
        self.delay_spinbox.setSingleStep(100)
        self.delay_spinbox.valueChanged.connect(self.update_delay)
        delay_layout.addWidget(self.delay_spinbox)
        control_layout.addLayout(delay_layout)
        
        # 重置按钮
        reset_btn = QPushButton("重置所有滑动条")
        reset_btn.clicked.connect(self.reset_sliders)
        control_layout.addWidget(reset_btn)
        
        layout.addLayout(control_layout)
        
        # 状态显示
        self.status_label = BodyLabel("状态: 已初始化")
        layout.addWidget(self.status_label)
        
        # 连接信号
        self.basic_slider.valueChanged.connect(self.update_status)
        self.percentage_slider.valueChanged.connect(self.update_status)
        self.prefix_slider.valueChanged.connect(self.update_status)
        self.vertical_slider.valueChanged.connect(self.update_status)
        self.volume_slider.valueChanged.connect(self.update_status)
        
        print("✅ ToolTipSlider 测试已启动")
        print("功能:")
        print("- 拖动滑动条时显示数值工具提示")
        print("- 支持自定义格式字符串")
        print("- 可调节工具提示显示延迟")
        print("- 支持水平和垂直方向")
    
    def update_delay(self, delay_ms):
        """更新工具提示延迟"""
        self.basic_slider.setToolTipDelay(delay_ms)
        self.percentage_slider.setToolTipDelay(delay_ms)
        self.prefix_slider.setToolTipDelay(delay_ms)
        self.vertical_slider.setToolTipDelay(delay_ms)
        self.volume_slider.setToolTipDelay(delay_ms)
        self.update_status()
    
    def reset_sliders(self):
        """重置所有滑动条"""
        self.basic_slider.setValue(50)
        self.percentage_slider.setValue(30)
        self.prefix_slider.setValue(128)
        self.vertical_slider.setValue(60)
        self.volume_slider.setValue(75)
        self.delay_spinbox.setValue(500)
        print("✅ 所有滑动条已重置")
    
    def update_status(self):
        """更新状态显示"""
        values = [
            f"基本: {self.basic_slider.value()}",
            f"百分比: {self.percentage_slider.value()}%",
            f"RGB: {self.prefix_slider.value()}",
            f"垂直: {self.vertical_slider.value()}",
            f"音量: {self.volume_slider.value()}%",
            f"延迟: {self.delay_spinbox.value()}ms"
        ]
        self.status_label.setText(f"状态: {' | '.join(values)}")

def main():
    """主函数"""
    app = QApplication(sys.argv)
    
    # 设置Fluent Design主题
    setTheme(Theme.LIGHT)
    
    print("=" * 60)
    print("ToolTipSlider 测试")
    print("=" * 60)
    print("测试说明:")
    print("1. 拖动任意滑动条，观察工具提示显示")
    print("2. 水平滑动条：工具提示显示在滑块正上方60像素处")
    print("3. 垂直滑动条：工具提示显示在滑块右侧25像素处，垂直居中对齐")
    print("4. 拖动过程中工具提示会持续跟随滑块移动")
    print("5. 工具提示采用Windows 11 Fluent Design风格")
    print("6. 不同滑动条使用不同的显示格式")
    print("7. 可以调节工具提示显示延迟")
    print("=" * 60)
    
    window = ToolTipSliderTest()
    window.show()
    
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
