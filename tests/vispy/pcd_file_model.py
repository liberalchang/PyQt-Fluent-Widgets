# -*- coding: utf-8 -*-
"""
PCD文件表格模型模块

提供PCD文件列表的表格数据模型。
"""
from typing import List, Optional
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide6.QtGui import QColor, QBrush

from app.common.logger import logger
import random


class PcdFileInfo:
    """PCD文件信息"""

    STATUS_NOT_LOADED = "not_loaded"
    STATUS_LOADING = "loading"
    STATUS_LOADED = "loaded"
    STATUS_ERROR = "error"
    
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.filename = file_path.split('/')[-1].split('\\')[-1]
        self.point_count = 0
        self.status = self.STATUS_NOT_LOADED
        self.is_visible = True
        # 随机分配一个颜色
        self.color = QColor(
            random.randint(100, 255),
            random.randint(100, 255),
            random.randint(100, 255)
        )
        
    def __repr__(self):
        return f"PcdFileInfo({self.filename}, {self.point_count} points, {self.status})"


class PcdFileModel(QAbstractTableModel):
    """
    PCD文件表格模型
    
    列: 显示 | 文件名 | 点数 | 色板
    """
    
    STATUS_NOT_LOADED = PcdFileInfo.STATUS_NOT_LOADED
    STATUS_LOADING = PcdFileInfo.STATUS_LOADING
    STATUS_LOADED = PcdFileInfo.STATUS_LOADED
    STATUS_ERROR = PcdFileInfo.STATUS_ERROR

    HEADERS = ["visible", "filename", "points", "color", "action"]
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._files: List[PcdFileInfo] = []
    
    def rowCount(self, parent=QModelIndex()):
        return len(self._files)
    
    def columnCount(self, parent=QModelIndex()):
        return len(self.HEADERS)
    
    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        
        row = index.row()
        col = index.column()
        
        if row >= len(self._files):
            return None
        
        file_info = self._files[row]
        
        if role == Qt.DisplayRole:
            if col == 1:  # 文件名
                return file_info.filename
            elif col == 2:  # 点数
                if file_info.point_count == -1:
                    return "Image"
                return str(file_info.point_count) if file_info.point_count > 0 else "-"
            # Col 0 (Display) and Col 3 (Color) and Col 4 (Action) have no text
            return ""
        
        elif role == Qt.CheckStateRole:
            if col == 0:  # 显示复选框
                return Qt.Checked if file_info.is_visible else Qt.Unchecked
        
        elif role == Qt.BackgroundRole:
            if col == 3:  # 色板
                return QBrush(file_info.color)
        
        elif role == Qt.TextAlignmentRole:
            if col == 2:  # 点数居中
                return Qt.AlignCenter
            return Qt.AlignLeft | Qt.AlignVCenter
            
        elif role == Qt.ToolTipRole:
            if col == 1:
                return file_info.file_path
        
        return None
    
    def setData(self, index: QModelIndex, value, role=Qt.EditRole):
        if not index.isValid():
            return False
            
        row = index.row()
        col = index.column()
        
        if role == Qt.CheckStateRole and col == 0:
            self._files[row].is_visible = (value == Qt.Checked.value)
            self.dataChanged.emit(index, index, [Qt.CheckStateRole])
            return True
            
        return False
        
    def flags(self, index: QModelIndex):
        if not index.isValid():
            return Qt.NoItemFlags
            
        flags = super().flags(index)
        if index.column() == 0:
            flags |= Qt.ItemIsUserCheckable
        return flags
    
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            if section < len(self.HEADERS):
                headers = [
                    self.tr("显示"),
                    self.tr("文件名"),
                    self.tr("点数"),
                    self.tr("色板"),
                    self.tr("操作"),
                ]
                return headers[section]
        return None
    
    def add_file(self, file_path: str) -> int:
        """
        添加文件到模型
        
        Returns:
            添加的文件索引
        """
        # 检查是否已存在
        for i, f in enumerate(self._files):
            if f.file_path == file_path:
                logger.warning(f"File already exists: {file_path}")
                return i
        
        row = len(self._files)
        self.beginInsertRows(QModelIndex(), row, row)
        self._files.append(PcdFileInfo(file_path))
        self.endInsertRows()
        
        logger.debug(f"Added file to model: {file_path}")
        return row
    
    def add_files(self, file_paths: List[str]):
        """批量添加文件"""
        for path in file_paths:
            self.add_file(path)
    
    def remove_file(self, row: int):
        """移除文件"""
        if 0 <= row < len(self._files):
            self.beginRemoveRows(QModelIndex(), row, row)
            removed = self._files.pop(row)
            self.endRemoveRows()
            logger.debug(f"Removed file from model: {removed.filename}")
    
    def clear(self):
        """清空所有文件"""
        if self._files:
            self.beginResetModel()
            self._files.clear()
            self.endResetModel()
            logger.debug("Cleared all files from model")
    
    def update_file_info(self, row: int, point_count: int = None, status: str = None):
        """更新文件信息"""
        if 0 <= row < len(self._files):
            file_info = self._files[row]
            if point_count is not None:
                file_info.point_count = point_count
            if status is not None:
                file_info.status = status
            
            # 通知视图更新
            start_index = self.index(row, 0)
            end_index = self.index(row, len(self.HEADERS) - 1)
            self.dataChanged.emit(start_index, end_index)

    def update_file_color(self, row: int, color: QColor):
        """更新文件颜色"""
        if 0 <= row < len(self._files):
            self._files[row].color = color
            index = self.index(row, 3)  # Color column
            self.dataChanged.emit(index, index)

    def set_file_visible(self, row: int, visible: bool):
        """设置文件可见性"""
        if 0 <= row < len(self._files):
            self._files[row].is_visible = visible
            index = self.index(row, 0)
            self.dataChanged.emit(index, index)
    
    def get_file_info(self, row: int) -> Optional[PcdFileInfo]:
        """获取文件信息"""
        if 0 <= row < len(self._files):
            return self._files[row]
        return None
    
    def get_all_files(self) -> List[PcdFileInfo]:
        """获取所有文件信息"""
        return self._files.copy()
    
    def get_file_path(self, row: int) -> Optional[str]:
        """获取文件路径"""
        if 0 <= row < len(self._files):
            return self._files[row].file_path
        return None

    def find_file_row(self, file_path: str) -> int:
        """查找文件所在的行号，未找到返回 -1"""
        for i, f in enumerate(self._files):
            if f.file_path == file_path:
                return i
        return -1
