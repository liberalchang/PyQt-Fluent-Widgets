# coding:utf-8
"""
测试FluentSplitter组件
"""
import sys
from pathlib import Path

# 添加项目路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLabel

from qfluentwidgets import FluentSplitter, setTheme, Theme, PushButton, BodyLabel


class TestSplitterWindow(QWidget):
    """分割器测试窗口"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("FluentSplitter 测试示例")
        self.resize(1000, 700)
        
        # 主布局
        mainLayout = QVBoxLayout(self)
        mainLayout.setContentsMargins(20, 20, 20, 20)
        mainLayout.setSpacing(20)
        
        # 标题
        titleLabel = BodyLabel("Fluent Design 分割器测试")
        titleLabel.setStyleSheet("font-size: 24px; font-weight: bold;")
        mainLayout.addWidget(titleLabel)
        
        # 主题切换按钮
        self.themeButton = PushButton("切换深色模式")
        self.themeButton.clicked.connect(self.toggleTheme)
        mainLayout.addWidget(self.themeButton)
        
        # 水平分割器测试
        hLabel = BodyLabel("水平分割器 (拖动手柄或点击折叠按钮)")
        hLabel.setStyleSheet("font-size: 16px; font-weight: bold;")
        mainLayout.addWidget(hLabel)
        
        self.hSplitter = FluentSplitter(Qt.Horizontal)
        self.hSplitter.setMinimumHeight(200)
        
        # 添加水平分割器的面板
        leftPanel = self._createPanel("左侧面板", "这是左侧面板的内容\n支持拖动手柄调整大小\n点击手柄上的折叠按钮可以折叠/展开")
        centerPanel = self._createPanel("中间面板", "这是中间面板的内容\n主题色手柄\n悬停时会高亮并增加宽度")
        rightPanel = self._createPanel("右侧面板", "这是右侧面板的内容\n符合Fluent Design规范\n支持浅色和深色主题")
        
        self.hSplitter.addWidget(leftPanel)
        self.hSplitter.addWidget(centerPanel)
        self.hSplitter.addWidget(rightPanel)
        
        # 设置初始比例
        self.hSplitter.setSizes([250, 400, 250])
        
        mainLayout.addWidget(self.hSplitter)
        
        # 垂直分割器测试
        vLabel = BodyLabel("垂直分割器 (拖动手柄或点击折叠按钮)")
        vLabel.setStyleSheet("font-size: 16px; font-weight: bold;")
        mainLayout.addWidget(vLabel)
        
        self.vSplitter = FluentSplitter(Qt.Vertical)
        self.vSplitter.setMinimumHeight(200)
        
        # 添加垂直分割器的面板
        topPanel = self._createPanel("顶部面板", "这是顶部面板的内容\n垂直方向分割")
        bottomPanel = self._createPanel("底部面板", "这是底部面板的内容\n支持上下折叠")
        
        self.vSplitter.addWidget(topPanel)
        self.vSplitter.addWidget(bottomPanel)
        
        # 设置初始比例
        self.vSplitter.setSizes([100, 100])
        
        mainLayout.addWidget(self.vSplitter)
        
        self._isDark = False

    def _createPanel(self, title: str, content: str) -> QWidget:
        """创建测试面板"""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(10, 10, 10, 10)
        
        # 标题
        titleLabel = BodyLabel(title)
        titleLabel.setStyleSheet("font-size: 14px; font-weight: bold; color: #0078D4;")
        layout.addWidget(titleLabel)
        
        # 内容
        textEdit = QTextEdit()
        textEdit.setPlainText(content)
        textEdit.setStyleSheet("""
            QTextEdit {
                border: 1px solid rgba(0, 0, 0, 0.1);
                border-radius: 6px;
                padding: 10px;
                background: rgba(255, 255, 255, 0.7);
            }
        """)
        layout.addWidget(textEdit)
        
        return panel

    def toggleTheme(self):
        """切换主题"""
        self._isDark = not self._isDark
        if self._isDark:
            setTheme(Theme.DARK)
            self.themeButton.setText("切换浅色模式")
        else:
            setTheme(Theme.LIGHT)
            self.themeButton.setText("切换深色模式")


if __name__ == '__main__':
    # 启用高DPI支持 (PySide6 6.0+ 自动处理高DPI,无需手动设置)
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )
    
    app = QApplication(sys.argv)
    
    window = TestSplitterWindow()
    window.show()
    
    sys.exit(app.exec())
