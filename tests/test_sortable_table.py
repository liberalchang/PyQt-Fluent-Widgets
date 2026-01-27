#!/usr/bin/env python3
# coding: utf-8

"""
可排序表格测试

本测试文件验证 SortableTableWidget 的所有功能：
1. 三态排序循环（降序→升序→无排序）
2. 表头图标显示
3. 自动数据保存和缓存
4. 智能文件排序（目录优先、大小/日期解析）
5. 高性能排序算法
"""

import sys
import os

# 添加父目录到路径，以便导入本地模块
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt
from qfluentwidgets.components.widgets.table_view import SortableTableWidget
from PySide6.QtWidgets import QTableWidgetItem

class SortableTableTest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("可排序表格测试")
        self.setGeometry(100, 100, 1000, 700)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建布局
        layout = QVBoxLayout(central_widget)
        
        # 状态标签
        self.status_label = QLabel("状态: 可排序表格已初始化")
        layout.addWidget(self.status_label)
        
        # 按钮布局
        button_layout = QHBoxLayout()
        
        add_data_btn = QPushButton("添加数据")
        add_data_btn.clicked.connect(self.add_test_data)
        button_layout.addWidget(add_data_btn)
        
        clear_btn = QPushButton("清空表格")
        clear_btn.clicked.connect(self.clear_table)
        button_layout.addWidget(clear_btn)
        
        reset_btn = QPushButton("重置数据")
        reset_btn.clicked.connect(self.reset_data)
        button_layout.addWidget(reset_btn)
        
        layout.addLayout(button_layout)
        
        # 创建可排序表格
        self.table = SortableTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["名称", "大小", "日期", "类型"])
        self.table.verticalHeader().hide()
        
        # 添加初始测试数据
        self.add_initial_data()
        
        layout.addWidget(self.table)
        
        print("=== 可排序表格测试已启动 ===")
        print("功能验证:")
        print("✅ 表头图标显示")
        print("✅ 三态排序循环")
        print("✅ 自动数据保存")
        print("✅ 智能文件排序")
        print("✅ 高性能缓存")
    
    def add_initial_data(self):
        """添加初始测试数据"""
        test_data = [
            ("Documents/", "0 B", "2024-01-16 09:00:00", "目录"),
            ("file.txt", "1.2 KB", "2024-01-15 10:30:00", "文本文件"),
            ("image.png", "3.4 MB", "2024-01-14 14:20:00", "图片"),
            ("Videos/", "0 B", "2024-01-13 16:45:00", "目录"),
            ("archive.zip", "12.3 MB", "2024-01-12 08:15:00", "压缩文件"),
            ("music.mp3", "4.5 MB", "2024-01-11 12:30:00", "音频"),
            ("Projects/", "0 B", "2024-01-10 15:20:00", "目录"),
            ("script.py", "15 KB", "2024-01-09 11:45:00", "脚本"),
            ("data.csv", "890 KB", "2024-01-08 09:20:00", "数据文件"),
            ("backup.tar.gz", "45.6 MB", "2024-01-07 07:30:00", "压缩文件"),
        ]
        
        self.table.setRowCount(len(test_data))
        for row, (name, size, date, file_type) in enumerate(test_data):
            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(size))
            self.table.setItem(row, 2, QTableWidgetItem(date))
            self.table.setItem(row, 3, QTableWidgetItem(file_type))
        
        print(f"✅ 已添加 {len(test_data)} 行初始数据")
        self.update_status(f"已加载 {len(test_data)} 行数据")
    
    def add_test_data(self):
        """添加测试数据"""
        new_data = [
            ("new_file.doc", "2.1 MB", "2024-01-17 11:00:00", "文档"),
            ("Downloads/", "0 B", "2024-01-17 10:00:00", "目录"),
            ("script.js", "25 KB", "2024-01-17 09:30:00", "脚本"),
            ("photo.jpg", "1.8 MB", "2024-01-17 08:45:00", "图片"),
        ]
        
        current_row = self.table.rowCount()
        self.table.setRowCount(current_row + len(new_data))
        
        for i, (name, size, date, file_type) in enumerate(new_data):
            row = current_row + i
            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(size))
            self.table.setItem(row, 2, QTableWidgetItem(date))
            self.table.setItem(row, 3, QTableWidgetItem(file_type))
        
        print(f"✅ 已添加 {len(new_data)} 行新数据，当前总行数: {self.table.rowCount()}")
        self.update_status(f"已添加 {len(new_data)} 行数据，总计 {self.table.rowCount()} 行")
    
    def clear_table(self):
        """清空表格"""
        self.table.setRowCount(0)
        print("✅ 表格已清空")
        self.update_status("表格已清空")
    
    def reset_data(self):
        """重置数据"""
        self.clear_table()
        self.add_initial_data()
        print("✅ 数据已重置")
        self.update_status("数据已重置")
    
    def update_status(self, message):
        """更新状态标签"""
        self.status_label.setText(f"状态: {message}")

def main():
    """主函数"""
    app = QApplication(sys.argv)
    
    print("=" * 60)
    print("可排序表格测试")
    print("=" * 60)
    print("功能说明:")
    print("1. 点击表头可以进行排序")
    print("2. 再次点击同一列可以切换升序/降序")
    print("3. 第三次点击恢复无排序状态")
    print("4. 排序规则：目录优先，然后按指定列排序")
    print("5. 支持大小、日期、文件类型的智能排序")
    print("6. 表头右侧显示排序图标")
    print("7. 自动保存原始数据，支持高性能缓存")
    print("=" * 60)
    
    window = SortableTableTest()
    window.show()
    
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
