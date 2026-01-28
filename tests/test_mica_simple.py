# coding:utf-8
"""
简单测试：验证云母效果最大化修复
"""

import sys
import os

# Add parent directory to sys.path to import qfluentwidgets
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtCore import Qt, QEvent
from PySide6.QtWidgets import QApplication, QLabel

from qfluentwidgets.window.fluent_window import FluentWidget


class SimpleMicaTest(FluentWidget):
    """简单的云母效果测试窗口"""

    def __init__(self):
        super().__init__()
        
        # 设置窗口属性
        self.resize(600, 400)
        self.setWindowTitle('云母效果测试')
        
        # 添加标签
        self.label = QLabel("请尝试最大化窗口\n观察云母效果变化", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
            font-size: 18px; 
            color: white; 
            background: transparent;
            padding: 20px;
        """)
        
        # 启用云母效果
        print("启用云母效果...")
        self.setMicaEffectEnabled(True)
        
        print(f"初始化完成 - 云母效果: {self.isMicaEffectEnabled()}")
        print(f"WA_TranslucentBackground: {self.testAttribute(Qt.WA_TranslucentBackground)}")

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # 居中标签
        self.label.setGeometry(0, 0, self.width(), self.height())

    def changeEvent(self, event):
        super().changeEvent(event)
        
        if event.type() == QEvent.WindowStateChange:
            print(f"\n--- 窗口状态变化 ---")
            print(f"新状态: {self.windowState()}")
            print(f"云母效果: {self.isMicaEffectEnabled()}")
            print(f"WA_TranslucentBackground: {self.testAttribute(Qt.WA_TranslucentBackground)}")
            
            if self.isMaximized():
                print("✓ 窗口最大化，云母效果应该重新应用")
                self.label.setText("窗口已最大化\n云母效果应该有效")
            else:
                print("窗口还原")
                self.label.setText("窗口已还原\n云母效果正常")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    print("=" * 50)
    print("云母效果最大化修复测试")
    print("=" * 50)
    
    w = SimpleMicaTest()
    w.show()
    
    print("测试窗口已创建")
    print("请尝试最大化窗口观察效果")
    
    sys.exit(app.exec())
