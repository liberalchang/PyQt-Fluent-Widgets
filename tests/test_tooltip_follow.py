#!/usr/bin/env python3
# coding: utf-8

"""
简单的工具提示跟随测试
专门测试工具提示是否能跟随滑块移动
"""

import sys
import os

# 添加父目录到路径，以便导入本地模块
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import Qt
from qfluentwidgets.components.widgets.slider import ToolTipSlider
from qfluentwidgets import setTheme, Theme, FluentIcon


class SimpleTooltipTest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("工具提示跟随测试")
        self.setGeometry(100, 100, 600, 200)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建布局
        layout = QVBoxLayout(central_widget)
        
        # 说明
        layout.addWidget(QLabel("拖动滑动条，观察工具提示是否跟随滑块移动"))
        
        # 水平滑动条
        layout.addWidget(QLabel("水平滑动条:"))
        self.h_slider = ToolTipSlider(Qt.Horizontal)
        self.h_slider.setRange(0, 100)
        self.h_slider.setValue(50)
        self.h_slider.setToolTipDelay(0)  # 无延迟
        layout.addWidget(self.h_slider)
        
        # 垂直滑动条
        layout.addWidget(QLabel("垂直滑动条:"))
        self.v_slider = ToolTipSlider(Qt.Vertical)
        self.v_slider.setRange(0, 100)
        self.v_slider.setValue(50)
        self.v_slider.setToolTipDelay(0)  # 无延迟
        layout.addWidget(self.v_slider)
        
        print("✅ 简单测试已启动")
        print("请拖动滑动条并观察工具提示是否跟随移动")


def main():
    app = QApplication(sys.argv)
    
    # 设置Fluent Design主题
    setTheme(Theme.LIGHT)
    
    print("=" * 50)
    print("工具提示跟随测试")
    print("=" * 50)
    print("测试说明:")
    print("1. 拖动水平滑动条，工具提示应该在滑块正上方60像素处跟随移动")
    print("2. 拖动垂直滑动条，工具提示应该在滑块右侧25像素处跟随移动")
    print("3. 工具提示应该实时更新数值")
    print("4. 垂直滑动条工具提示应该与滑块垂直居中对齐")
    print("=" * 50)
    
    window = SimpleTooltipTest()
    window.show()
    
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
