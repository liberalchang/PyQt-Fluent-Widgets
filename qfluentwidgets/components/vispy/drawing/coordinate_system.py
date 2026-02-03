# coding:utf-8
"""
坐标系统模块

实现屏幕坐标与世界坐标的双向转换，集成 vispy 相机的变换矩阵。
"""
import numpy as np
from typing import Tuple, Optional


class CoordinateSystem:
    """坐标系统类
    
    管理屏幕坐标（像素坐标）与世界坐标（逻辑坐标）之间的转换。
    
    - 屏幕坐标：以像素为单位，原点在左上角，Y轴向下
    - 世界坐标：逻辑坐标，支持缩放和平移，原点和方向由相机控制
    """
    
    def __init__(self, view=None, canvas=None, scale_factor=1.0, origin_offset=(0.0, 0.0)):
        """初始化坐标系统
        
        Args:
            view: vispy ViewBox 对象
            canvas: vispy Canvas 对象
            scale_factor: 像素与物理尺寸比例 (1像素 = N物理单位)
            origin_offset: 原点世界坐标值 (Screen(0,0)对应的世界坐标)
        """
        self.view = view
        self.canvas = canvas
        self.scale_factor = scale_factor
        self.origin_offset = origin_offset
        self._initialized = False
        
    def initialize_view(self):
        """根据配置初始化相机视图"""
        if self._initialized:
            return
            
        if self.view is None or self.canvas is None:
            return
            
        try:
            # 获取 Canvas 尺寸
            canvas_size = self.canvas.size
            if canvas_size is None or len(canvas_size) != 2:
                return
                
            w, h = canvas_size
            if w <= 0 or h <= 0:
                return
                
            # 设置相机范围
            # Screen(0,0) -> Top-Left -> World(Ox, Oy)
            # Screen(w,h) -> Bottom-Right -> World(Ox + w*scale, Oy - h*scale)
            # Camera Rect (x, y, w, h) 通常定义 Bottom-Left, Width, Height
            
            ox, oy = self.origin_offset
            scale = self.scale_factor
            
            # Rect Bottom-Left
            rect_x = ox
            rect_y = oy - h * scale
            rect_w = w * scale
            rect_h = h * scale
            
            if hasattr(self.view, 'camera'):
                self.view.camera.rect = (rect_x, rect_y, rect_w, rect_h)
                self._initialized = True
                
        except Exception as e:
            print(f"初始化视图失败: {e}")

    def setView(self, view):
        """设置 ViewBox
        
        Args:
            view: vispy ViewBox 对象
        """
        self.view = view
        
    def setCanvas(self, canvas):
        """设置 Canvas
        
        Args:
            canvas: vispy Canvas 对象
        """
        self.canvas = canvas
        
    def screenToWorld(self, x: float, y: float) -> Tuple[float, float]:
        """将屏幕坐标转换为世界坐标
        
        Args:
            x: 屏幕 X 坐标（像素）
            y: 屏幕 Y 坐标（像素）
            
        Returns:
            世界坐标 (world_x, world_y)
        """
        if self.view is None or self.canvas is None:
            # 降级处理：直接返回屏幕坐标
            return (x, y)
            
        try:
            # 获取 Canvas 尺寸
            canvas_size = self.canvas.size
            if canvas_size is None or len(canvas_size) != 2:
                return (x, y)
                
            canvas_width, canvas_height = canvas_size
            
            # 检查画布尺寸是否有效
            if canvas_width <= 0 or canvas_height <= 0:
                print(f"无效的画布尺寸: {canvas_width}x{canvas_height}")
                return (x, y)
            
            # 归一化设备坐标 (NDC)：范围 [-1, 1]
            # vispy 坐标系统：左下角为原点，Y轴向上
            ndc_x = (2.0 * x / canvas_width) - 1.0
            ndc_y = 1.0 - (2.0 * y / canvas_height)  # 翻转 Y 轴
            
            # 使用简化的坐标转换，但考虑相机的基本变换
            # 世界坐标系：原点在画布中心，X轴向右，Y轴向上
            # 基础转换：屏幕坐标到以画布中心为原点的坐标系
            base_x = x - canvas_width / 2
            base_y = canvas_height / 2 - y  # 翻转 Y 轴
            
            # 尝试获取相机的基本变换参数
            if hasattr(self.view, 'camera'):
                camera = self.view.camera
                
                # 对于PanZoomCamera，尝试获取实际的视口信息
                if hasattr(camera, 'rect'):
                    rect = camera.rect
                    # 使用rect来调整坐标
                    # rect通常表示当前可见的矩形区域
                    if hasattr(rect, 'left') and hasattr(rect, 'width'):
                        # 简单的线性映射
                        world_x = rect.left + (x / canvas_width) * rect.width
                        world_y = rect.bottom + (1.0 - y / canvas_height) * rect.height
                        return (world_x, world_y)
                
                # 如果有center和scale信息，使用它们
                if hasattr(camera, 'center') and hasattr(camera, 'scale_factor'):
                    center = camera.center
                    scale = camera.scale_factor if hasattr(camera, 'scale_factor') else 1.0
                    
                    # 处理scale可能是单个值或元组的情况
                    if isinstance(scale, (tuple, list)) and len(scale) >= 2:
                        scale_x, scale_y = scale[0], scale[1]
                    else:
                        scale_x = scale_y = float(scale)
                    
                    # 应用缩放和平移
                    world_x = base_x * scale_x + center[0]
                    world_y = base_y * scale_y + center[1]
                    return (world_x, world_y)
            
            # 默认情况：使用基础转换
            return (base_x, base_y)
            
        except Exception as e:
            print(f"screenToWorld 转换错误: {e}")
            return (x, y)
            
    def worldToScreen(self, world_x: float, world_y: float) -> Tuple[float, float]:
        """将世界坐标转换为屏幕坐标
        
        Args:
            world_x: 世界 X 坐标
            world_y: 世界 Y 坐标
            
        Returns:
            屏幕坐标 (screen_x, screen_y)
        """
        if self.view is None or self.canvas is None:
            # 降级处理：直接返回世界坐标
            return (world_x, world_y)
            
        try:
            # 获取 Canvas 尺寸
            canvas_size = self.canvas.size
            if canvas_size is None or len(canvas_size) != 2:
                return (world_x, world_y)
                
            canvas_width, canvas_height = canvas_size
            
            # 使用相机的变换矩阵
            if hasattr(self.view, 'camera') and hasattr(self.view.camera, 'transform'):
                transform = self.view.camera.transform
                
                # 创建世界坐标的齐次坐标 (x, y, 0, 1)
                world_point = np.array([world_x, world_y, 0.0, 1.0])
                
                # 应用变换
                try:
                    ndc_point = transform.map(world_point)
                    ndc_x = ndc_point[0]
                    ndc_y = ndc_point[1]
                    
                    # NDC 转屏幕坐标
                    screen_x = (ndc_x + 1.0) * canvas_width / 2.0
                    screen_y = (1.0 - ndc_y) * canvas_height / 2.0  # 翻转 Y 轴
                    
                    return (float(screen_x), float(screen_y))
                except Exception:
                    pass
            
            # 降级方法：使用相机的 center 和 scale_factor
            if hasattr(self.view.camera, 'center') and hasattr(self.view.camera, 'scale_factor'):
                center = self.view.camera.center
                scale = self.view.camera.scale_factor if hasattr(self.view.camera, 'scale_factor') else 1.0
                
                # 世界坐标转 NDC
                ndc_x = (world_x - center[0]) / scale
                ndc_y = (world_y - center[1]) / scale
                
                # NDC 转屏幕坐标
                screen_x = (ndc_x + 1.0) * canvas_width / 2.0
                screen_y = (1.0 - ndc_y) * canvas_height / 2.0
                
                return (screen_x, screen_y)
            
            # 最终降级：假设简单的比例关系
            return (world_x, world_y)
            
        except Exception as e:
            print(f"worldToScreen 转换错误: {e}")
            return (world_x, world_y)
            
    def screenToWorldArray(self, points: np.ndarray) -> np.ndarray:
        """批量将屏幕坐标转换为世界坐标
        
        Args:
            points: 屏幕坐标数组，形状 (N, 2)
            
        Returns:
            世界坐标数组，形状 (N, 2)
        """
        world_points = np.array([self.screenToWorld(p[0], p[1]) for p in points])
        return world_points
        
    def worldToScreenArray(self, points: np.ndarray) -> np.ndarray:
        """批量将世界坐标转换为屏幕坐标
        
        Args:
            points: 世界坐标数组，形状 (N, 2)
            
        Returns:
            屏幕坐标数组，形状 (N, 2)
        """
        screen_points = np.array([self.worldToScreen(p[0], p[1]) for p in points])
        return screen_points
        
    def getViewBounds(self) -> Optional[Tuple[float, float, float, float]]:
        """获取当前视口的世界坐标边界
        
        Returns:
            边界 (min_x, min_y, max_x, max_y) 或 None
        """
        if self.canvas is None:
            return None
            
        try:
            canvas_size = self.canvas.size
            if canvas_size is None:
                return None
                
            width, height = canvas_size
            
            # 将四个角的屏幕坐标转换为世界坐标
            top_left = self.screenToWorld(0, 0)
            top_right = self.screenToWorld(width, 0)
            bottom_left = self.screenToWorld(0, height)
            bottom_right = self.screenToWorld(width, height)
            
            # 计算边界
            all_x = [top_left[0], top_right[0], bottom_left[0], bottom_right[0]]
            all_y = [top_left[1], top_right[1], bottom_left[1], bottom_right[1]]
            
            min_x = min(all_x)
            max_x = max(all_x)
            min_y = min(all_y)
            max_y = max(all_y)
            
            return (min_x, min_y, max_x, max_y)
            
        except Exception as e:
            print(f"getViewBounds 错误: {e}")
            return None
            
    def distanceScreenToWorld(self, screen_distance: float) -> float:
        """将屏幕距离转换为世界坐标距离
        
        Args:
            screen_distance: 屏幕距离（像素）
            
        Returns:
            世界坐标距离
        """
        if self.canvas is None or self.view is None:
            return screen_distance
            
        try:
            # 使用两个点的转换来计算距离比例
            p1_screen = (0.0, 0.0)
            p2_screen = (screen_distance, 0.0)
            
            p1_world = self.screenToWorld(*p1_screen)
            p2_world = self.screenToWorld(*p2_screen)
            
            world_distance = np.sqrt((p2_world[0] - p1_world[0])**2 + (p2_world[1] - p1_world[1])**2)
            return world_distance
            
        except Exception:
            return screen_distance
            
    def distanceWorldToScreen(self, world_distance: float) -> float:
        """将世界坐标距离转换为屏幕距离
        
        Args:
            world_distance: 世界坐标距离
            
        Returns:
            屏幕距离（像素）
        """
        if self.canvas is None or self.view is None:
            return world_distance
            
        try:
            # 使用两个点的转换来计算距离比例
            p1_world = (0.0, 0.0)
            p2_world = (world_distance, 0.0)
            
            p1_screen = self.worldToScreen(*p1_world)
            p2_screen = self.worldToScreen(*p2_world)
            
            screen_distance = np.sqrt((p2_screen[0] - p1_screen[0])**2 + (p2_screen[1] - p1_screen[1])**2)
            return screen_distance
            
        except Exception:
            return world_distance
