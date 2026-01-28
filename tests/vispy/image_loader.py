# -*- coding: utf-8 -*-
"""
图片加载工具模块
"""
import numpy as np
from typing import Optional
from PySide6.QtGui import QImage
from app.common.logger import logger

class ImageLoader:
    """图片加载器"""
    
    @staticmethod
    def load(file_path: str) -> Optional[np.ndarray]:
        """
        使用 QImage 加载图片并转换为 numpy 数组
        
        Args:
            file_path: 图片文件路径
            
        Returns:
            Optional[np.ndarray]: (H, W, 4) uint8 RGBA array, or None if failed
        """
        try:
            # 优先读取文件内容到内存，再加载，避免 Windows 下中文路径或特殊字符导致的问题
            with open(file_path, 'rb') as f:
                data = f.read()
                image = QImage()
                if not image.loadFromData(data):
                    logger.warning(f"Failed to load image from data: {file_path}")
                    return None
            
            if image.isNull():
                logger.warning(f"Loaded image is null: {file_path}")
                return None
            
            image = image.convertToFormat(QImage.Format_RGBA8888)
            width = image.width()
            height = image.height()
            
            ptr = image.constBits()
            bytes_per_line = image.bytesPerLine()
            
            # 使用 frombuffer 避免直接复制，并正确处理 padding
            arr = np.frombuffer(ptr, dtype=np.uint8)
            arr = arr.reshape(height, bytes_per_line)
            
            # 裁剪掉 padding (如果有)
            if bytes_per_line > width * 4:
                arr = arr[:, :width*4]
            
            arr = arr.reshape(height, width, 4)
            # 垂直翻转图片，使得图片在3D场景中方向正确 (Top at Z-high)
            # 原始: Row 0 (Top) -> Y=0 -> Z=0 (Upside down)
            # 翻转后: Row 0 (Bottom) -> Y=0 -> Z=0 (Correct)
            return arr[::-1].copy()
            
        except Exception as e:
            logger.error(f"Error loading image {file_path}: {e}")
            return None
