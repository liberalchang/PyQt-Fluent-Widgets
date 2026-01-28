# -*- coding: utf-8 -*-
from typing import List
from pathlib import Path
from PySide6.QtWidgets import (
    QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QSplitter, 
    QHeaderView, QFileDialog, QPushButton, QLabel, QSlider,
    QComboBox, QTableView, QAbstractItemView, QFrame, QColorDialog,
    QStyledItemDelegate, QStyle, QToolButton
)
from PySide6.QtCore import Signal, Qt, QEvent, QFile, QModelIndex, Slot
from PySide6.QtGui import QPainter, QColor

from app.common.logger import logger
from app.widgets.pcd import VispyPcdRenderer
from app.models.pcd.pcd_file_model import PcdFileModel
from app.common.icon import Icon
from app.core.managers.signal_manager import signalManager
from app.core.managers.params_manager import paramsManager

from app.common.style_sheet import StyleSheet

class ColorDelegate(QStyledItemDelegate):
    """自定义颜色列代理，防止选中时背景遮挡颜色"""
    def paint(self, painter: QPainter, option, index: QModelIndex):
        if index.column() == 3:
            painter.save()
            
            # 绘制背景 (处理选中状态)
            if option.state & QStyle.State_Selected:
                painter.fillRect(option.rect, option.palette.highlight())
            
            # 获取颜色
            color_brush = index.data(Qt.BackgroundRole)
            if color_brush:
                color = color_brush.color()
                # 绘制色块 (留出边距)
                rect = option.rect.adjusted(4, 4, -4, -4)
                painter.setBrush(color)
                painter.setPen(Qt.NoPen)
                painter.drawRoundedRect(rect, 2, 2)
            
            painter.restore()
        else:
            super().paint(painter, option, index)

class PcdControlPanel(QFrame):
    """点云查看器控制面板 (左侧) - 原生控件版本"""
    
    removeFileRequested = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumWidth(320)
        self.setObjectName("PcdControlPanel")
        
        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setContentsMargins(20, 20, 20, 20)
        self.vBoxLayout.setSpacing(15)
        
        # 1. 文件选择按钮
        self.addFilesBtn = QPushButton(self.tr("添加PCD/STL文件"), self)
        self.addFilesBtn.setMinimumHeight(36)
        self.addFilesBtn.setObjectName("addFilesBtn")
        
        self.addImagesBtn = QPushButton(self.tr("添加图片文件"), self)
        self.addImagesBtn.setMinimumHeight(36)
        self.addImagesBtn.setObjectName("addImagesBtn")
        
        # 2. 点大小控制
        self.pointSizeLabel = QLabel(self.tr("点大小: {value}").format(value=3), self)
        self.pointSizeSlider = QSlider(Qt.Horizontal, self)
        self.pointSizeSlider.setMinimum(1)
        self.pointSizeSlider.setMaximum(20)
        self.pointSizeSlider.setValue(3)
        self.pointSizeSlider.setFixedHeight(24)
        
        # 3. 颜色映射
        self.colorMappingLabel = QLabel(self.tr("颜色映射"), self)
        self.colorMappingCombo = QComboBox(self)
        self.colorMappingCombo.addItems([
            self.tr("强度"),
            self.tr("高度"),
            self.tr("RGB"),
            self.tr("单色")
        ])
        self.colorMappingCombo.setCurrentIndex(3)  # 默认设置为单色
        
        # 4. 加载模式
        self.loadModeLabel = QLabel(self.tr("加载模式"), self)
        self.loadModeCombo = QComboBox(self)
        self.loadModeCombo.addItems([
            self.tr("自动"),
            self.tr("降采样"),
            self.tr("完整加载")
        ])
        self.loadModeCombo.setCurrentIndex(0)
        
        # 5. 视图模式
        self.viewModeLabel = QLabel(self.tr("视图模式"), self)
        self.viewModeCombo = QComboBox(self)
        self.viewModeCombo.addItems([
            self.tr("自由视角"),
            self.tr("顶视图"),
            self.tr("前视图"),
            self.tr("侧视图")
        ])
        self.viewModeCombo.setCurrentIndex(0)
        
        # 6. 文件列表
        self.fileListLabel = QLabel(self.tr("文件列表"), self)
        self.fileTableView = QTableView(self)
        self.fileModel = PcdFileModel(self)
        self.fileTableView.setModel(self.fileModel)
        
        # 表格样式
        self.fileTableView.setShowGrid(False)
        self.fileTableView.verticalHeader().hide()
        self.fileTableView.verticalHeader().setDefaultSectionSize(38)  # 增加行高以完整显示按钮
        self.fileTableView.setItemDelegateForColumn(3, ColorDelegate(self.fileTableView))
        self.fileTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.fileTableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.fileTableView.setAlternatingRowColors(True)
        
        # 列宽调整
        header = self.fileTableView.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)  # 显示
        header.setSectionResizeMode(1, QHeaderView.Stretch)  # 文件名
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)  # 点数
        header.setSectionResizeMode(3, QHeaderView.Fixed)  # 色板
        self.fileTableView.setColumnWidth(3, 40)
        header.setSectionResizeMode(4, QHeaderView.Fixed)  # 操作
        self.fileTableView.setColumnWidth(4, 50)
        
        # 布局组装
        self.vBoxLayout.addWidget(self.addFilesBtn)
        self.vBoxLayout.addWidget(self.addImagesBtn)
        self.vBoxLayout.addSpacing(10)
        
        self.vBoxLayout.addWidget(self.pointSizeLabel)
        self.vBoxLayout.addWidget(self.pointSizeSlider)
        
        self.vBoxLayout.addWidget(self.colorMappingLabel)
        self.vBoxLayout.addWidget(self.colorMappingCombo)
        
        self.vBoxLayout.addWidget(self.loadModeLabel)
        self.vBoxLayout.addWidget(self.loadModeCombo)
        
        self.vBoxLayout.addWidget(self.viewModeLabel)
        self.vBoxLayout.addWidget(self.viewModeCombo)
        
        self.vBoxLayout.addWidget(self.fileListLabel)
        self.vBoxLayout.addWidget(self.fileTableView, 1)  # 文件列表占据剩余空间
        
        # 信号连接
        self.pointSizeSlider.valueChanged.connect(lambda v: self._on_point_size_changed(v))
        self.fileModel.rowsInserted.connect(lambda p, f, l: self._on_rows_inserted(p, f, l))
    
    @Slot(QModelIndex, int, int)
    def _on_rows_inserted(self, parent, first, last):
        """处理新行插入，添加删除按钮"""
        for row in range(first, last + 1):
            index = self.fileModel.index(row, 4)
            
            container = QWidget()
            layout = QHBoxLayout(container)
            layout.setContentsMargins(2, 2, 2, 2)
            layout.setAlignment(Qt.AlignCenter)
            
            btn = QToolButton(self)
            btn.setIcon(Icon.DELETE.icon())
            btn.setFixedSize(28, 28)
            btn.setObjectName("deleteFileBtn")
            btn.clicked.connect(lambda checked=False, b=btn: self._on_delete_btn_clicked(b))
            
            layout.addWidget(btn)
            self.fileTableView.setIndexWidget(index, container)

    @Slot()
    def _on_delete_btn_clicked(self, btn):
        """处理删除按钮点击"""
        # 获取按钮在表格中的位置
        pos = self.fileTableView.viewport().mapFromGlobal(btn.mapToGlobal(btn.rect().center()))
        index = self.fileTableView.indexAt(pos)
        if index.isValid():
            row = index.row()
            file_path = self.fileModel.get_file_path(row)
            if file_path:
                self.removeFileRequested.emit(file_path)
                self.fileModel.remove_file(row)
    
    @Slot(int)
    def _on_point_size_changed(self, value: int):
        """点大小变化处理"""
        self.pointSizeLabel.setText(self.tr("点大小: {value}").format(value=value))
    
    def changeEvent(self, event: QEvent):
        """语言变化事件"""
        if event.type() == QEvent.LanguageChange:
            self._retranslate()
        super().changeEvent(event)
    
    def _retranslate(self):
        """重新翻译界面"""
        self.addFilesBtn.setText(self.tr("添加PCD文件"))
        self.addImagesBtn.setText(self.tr("添加图片文件"))
        value = self.pointSizeSlider.value()
        self.pointSizeLabel.setText(self.tr("点大小: {value}").format(value=value))
        
        self.colorMappingLabel.setText(self.tr("颜色映射"))
        self.colorMappingCombo.setItemText(0, self.tr("强度"))
        self.colorMappingCombo.setItemText(1, self.tr("高度"))
        self.colorMappingCombo.setItemText(2, self.tr("RGB"))
        self.colorMappingCombo.setItemText(3, self.tr("单色"))
        
        self.loadModeLabel.setText(self.tr("加载模式"))
        self.loadModeCombo.setItemText(0, self.tr("自动"))
        self.loadModeCombo.setItemText(1, self.tr("降采样"))
        self.loadModeCombo.setItemText(2, self.tr("完整加载"))
        
        self.viewModeLabel.setText(self.tr("视图模式"))
        self.viewModeCombo.setItemText(0, self.tr("自由视角"))
        self.viewModeCombo.setItemText(1, self.tr("顶视图"))
        self.viewModeCombo.setItemText(2, self.tr("前视图"))
        self.viewModeCombo.setItemText(3, self.tr("侧视图"))
        
        self.fileListLabel.setText(self.tr("文件列表"))


class PcdWindow(QMainWindow):
    """ 独立的PCD查看窗口 - 原生控件版本 """
    
    # windowClosed = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(self.tr("3D Point Cloud Viewer"))
        self.setWindowIcon(Icon.PCD_VIEWER.icon())
        self.setObjectName("PcdWindow")
        self.resize(1200, 800)
        
        # 创建中心部件
        container = QWidget()
        self.setCentralWidget(container)
        
        # 主布局
        self.hBoxLayout = QHBoxLayout(container)
        self.hBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.hBoxLayout.setSpacing(0)
        
        # 创建分割器
        self.splitter = QSplitter(Qt.Horizontal, container)
        
        # 左侧控制面板
        self.controlPanel = PcdControlPanel(self.splitter)
        
        # 右侧渲染器
        self.renderer = VispyPcdRenderer()
        
        # 设置分割比例 (1:3)
        self.splitter.addWidget(self.controlPanel)
        self.splitter.addWidget(self.renderer)
        self.splitter.setStretchFactor(0, 1)
        self.splitter.setStretchFactor(1, 3)
        
        self.hBoxLayout.addWidget(self.splitter)
        
        # 初始化主题和样式
        self._init_theme_and_style()
        
        # 状态栏
        self.statusBar().showMessage(self.tr("就绪"))
        
        # 连接信号
        self._connect_signals()

    # def closeEvent(self, event):
    #     """窗口关闭事件"""
    #     self.windowClosed.emit()
    #     super().closeEvent(event)

    def _update_status_bar(self):
        """更新状态栏信息"""
        # 统计可见文件数和总点数
        visible_files = 0
        total_points = 0
        all_files = self.controlPanel.fileModel.get_all_files()
        for f in all_files:
            if f.is_visible and f.status == f.STATUS_LOADED:
                visible_files += 1
                total_points += f.point_count
        
        point_size = self.controlPanel.pointSizeSlider.value()
        color_map = self.controlPanel.colorMappingCombo.currentText()

        msg = self.tr("文件: {visible}/{total} | 总点数: {points} | 点大小: {size} | 颜色映射: {color}").format(
            visible=visible_files,
            total=len(all_files),
            points=total_points,
            size=point_size,
            color=color_map,
        )
        self.statusBar().showMessage(msg)
        
    def _init_theme_and_style(self):
        """ 初始化主题和加载独立样式表 """
        target_theme = paramsManager.get_config("themeMode")
        from qfluentwidgets import Theme, isDarkTheme
        
        if target_theme == Theme.AUTO:
            is_dark = isDarkTheme()
        else:
            is_dark = (target_theme == Theme.DARK)
        # self.renderer.set_theme(is_dark)
        self.renderer.set_theme(True)
        
        # 使用StyleSheet加载样式
        StyleSheet.PCD_WINDOW.apply(self)
        
    def _connect_signals(self):
        """连接信号槽"""
        # 添加文件按钮
        self.controlPanel.addFilesBtn.clicked.connect(lambda: self._on_add_files())
        self.controlPanel.addImagesBtn.clicked.connect(lambda: self._on_add_images())
        
        # 点大小滑块
        self.controlPanel.pointSizeSlider.valueChanged.connect(
            lambda v: self.renderer.set_point_size(v)
        )
        self.controlPanel.pointSizeSlider.valueChanged.connect(
            lambda: self._update_status_bar()
        )
        
        # 颜色映射下拉框
        self.controlPanel.colorMappingCombo.currentTextChanged.connect(
            lambda t: self.renderer.set_color_mapping(t)
        )
        self.controlPanel.colorMappingCombo.currentTextChanged.connect(
            lambda: self._update_status_bar()
        )
        
        # 视图模式下拉框
        self.controlPanel.viewModeCombo.currentTextChanged.connect(
            lambda t: self.renderer.set_view_mode(t)
        )
        
        # 渲染器加载信号 - 使用全局信号管理器
        signalManager.connect("pcdRendererLoaded", self._on_pcd_loaded)
        signalManager.connect("pcdRendererError", self._on_load_error)
        
        # 删除文件
        self.controlPanel.removeFileRequested.connect(lambda f: self.renderer.remove_file(f))

        # 加载模式
        self.controlPanel.loadModeCombo.currentTextChanged.connect(
            lambda t: self.renderer.set_load_mode(t)
        )
        
        # 文件列表交互
        self.controlPanel.fileModel.dataChanged.connect(lambda tl, br, r=[]: self._on_model_data_changed(tl, br, r))
        self.controlPanel.fileModel.rowsInserted.connect(lambda: self._update_status_bar())
        self.controlPanel.fileModel.rowsRemoved.connect(lambda: self._update_status_bar())
        self.controlPanel.fileTableView.doubleClicked.connect(lambda i: self._on_table_double_clicked(i))
        
    def _on_add_files(self):
        """添加文件按钮点击处理"""
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            self.tr("选择PCD/STL文件"),
            "",
            self.tr("3D Files (*.pcd *.stl);;PCD文件 (*.pcd);;STL文件 (*.stl);;所有文件 (*.*)")
        )
        
        if file_paths:
            self.load_pcd_files(file_paths)

    def _on_add_images(self):
        """添加图片按钮点击处理"""
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            self.tr("选择图片文件"),
            "",
            self.tr("图片文件 (*.png *.jpg *.jpeg *.bmp);;所有文件 (*.*)")
        )
        
        if file_paths:
            self.load_image_files(file_paths)
            
    def load_pcd_files(self, file_paths: List[str]):
        """加载文件 (支持 PCD 、图片、stl)"""
        if not file_paths:
            return
            
        logger.info(f"Loading {len(file_paths)} files")
        
        # 确保设置当前的加载模式
        self.renderer.set_load_mode(self.controlPanel.loadModeCombo.currentText())
        
        # 添加到文件模型和渲染器
        for path in file_paths:
            # 判断文件类型
            lower_path = path.lower()
            is_image = lower_path.endswith(('.png', '.jpg', '.jpeg', '.bmp'))
            is_stl = lower_path.endswith('.stl')
            
            # 检查是否已经在模型中
            # 如果已存在，先从模型中移除旧记录，以便 UI 刷新状态 (如从 Error -> Loading)
            existing_row = self.controlPanel.fileModel.find_file_row(path)
            if existing_row != -1:
                logger.info(f"File {path} already in list, removing old entry to reload.")
                self.controlPanel.fileModel.remove_file(existing_row)
            
            # 重新添加到模型
            row = self.controlPanel.fileModel.add_file(path)
            
            if is_image:
                self.controlPanel.fileModel.update_file_info(row, point_count=-1, status=self.controlPanel.fileModel.STATUS_LOADED)
                self.renderer.add_image_file(path)
            elif is_stl:
                self.controlPanel.fileModel.update_file_info(row, point_count=0, status=self.controlPanel.fileModel.STATUS_LOADING)
                file_info = self.controlPanel.fileModel.get_file_info(row)
                color = file_info.color if file_info else None
                self.renderer.add_stl_file(path, color=color)
            else:
                self.controlPanel.fileModel.update_file_info(row, point_count=0, status=self.controlPanel.fileModel.STATUS_LOADING)
                
                # 获取生成的随机颜色传递给渲染器，保持一致
                file_info = self.controlPanel.fileModel.get_file_info(row)
                color = file_info.color if file_info else None
                
                # 异步加载到渲染器 (渲染器内部现在会处理“已存在则移除重载”的逻辑)
                self.renderer.add_pcd_file(path, color=color)
            
        self._update_status_bar()

    def load_image_files(self, file_paths: List[str]):
        """加载图片文件"""
        if not file_paths:
            return
            
        logger.info(f"Loading {len(file_paths)} image files")
        
        for path in file_paths:
            # 添加到文件模型 (复用PCD模型，point_count设为-1表示图片)
            row = self.controlPanel.fileModel.add_file(path)
            self.controlPanel.fileModel.update_file_info(row, point_count=-1, status=self.controlPanel.fileModel.STATUS_LOADED)
            
            # 加载到渲染器
            self.renderer.add_image_file(path)
            
        self._update_status_bar()

    def _on_model_data_changed(self, topLeft: QModelIndex, bottomRight: QModelIndex, roles: List[int] = []):
        """模型数据变化处理"""
        if not roles or Qt.CheckStateRole in roles:
            # 处理可见性变化
            row = topLeft.row()
            file_info = self.controlPanel.fileModel.get_file_info(row)
            if file_info:
                self.renderer.set_file_visible(file_info.file_path, file_info.is_visible)
                self._update_status_bar()

    def _on_table_double_clicked(self, index: QModelIndex):
        """表格双击处理 - 更改颜色"""
        if not index.isValid():
            return
            
        if index.column() == 3:  # 色板列
            row = index.row()
            file_info = self.controlPanel.fileModel.get_file_info(row)
            if file_info:
                color = QColorDialog.getColor(file_info.color, self, self.tr("选择点云颜色"))
                if color.isValid():
                    self.controlPanel.fileModel.update_file_color(row, color)
                    self.renderer.set_file_color(file_info.file_path, color)
                    self._update_status_bar()
        
    def _on_pcd_loaded(self, file_path: str, point_count: int):
        """PCD加载成功回调"""
        for i in range(self.controlPanel.fileModel.rowCount()):
            file_info = self.controlPanel.fileModel.get_file_info(i)
            if file_info and file_info.file_path == file_path:
                self.controlPanel.fileModel.update_file_info(i, point_count=point_count, status=self.controlPanel.fileModel.STATUS_LOADED)
                # 注意：颜色已在加载时传递，此处不再调用 set_file_color，避免重置 RGB 模式
                # self.renderer.set_file_color(file_path, file_info.color)
                break
        self._update_status_bar()
                
    def _on_load_error(self, file_path: str, error: str):
        """PCD加载失败回调"""
        for i in range(self.controlPanel.fileModel.rowCount()):
            file_info = self.controlPanel.fileModel.get_file_info(i)
            if file_info and file_info.file_path == file_path:
                self.controlPanel.fileModel.update_file_info(i, status=self.controlPanel.fileModel.STATUS_ERROR)
                break
        logger.error(f"Failed to load {file_path}: {error}")
        
    def _retranslate_ui(self):
        """重新翻译界面"""
        self.setWindowTitle(self.tr("3D Point Cloud Viewer"))
        self._update_status_bar()
        
    def closeEvent(self, event):
        # self.windowClosed.emit()
        super().closeEvent(event)
