#!/usr/bin/env python3
"""
API 文档生成脚本
自动扫描 qfluentwidgets 包并生成 API 文档
"""

import os
import sys
from pathlib import Path

# 添加项目根目录到 Python 路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def generate_api_docs():
    """生成 API 文档"""
    
    # 获取 qfluentwidgets 包路径
    qfluentwidgets_path = project_root / "qfluentwidgets"
    
    if not qfluentwidgets_path.exists():
        print(f"错误: 找不到 qfluentwidgets 包路径: {qfluentwidgets_path}")
        return False
    
    print(f"正在扫描 qfluentwidgets 包: {qfluentwidgets_path}")
    
    # 扫描主要模块
    modules = [
        "qfluentwidgets",
        "qfluentwidgets.common",
        "qfluentwidgets.components", 
        "qfluentwidgets.window",
        "qfluentwidgets.multimedia"
    ]
    
    # 扫描子模块
    submodules = []
    for module in modules:
        module_path = qfluentwidgets_path / module.replace("qfluentwidgets.", "")
        if module_path.is_dir():
            for item in module_path.iterdir():
                if item.is_file() and item.suffix == '.py' and item.name != '__init__.py':
                    submodules.append(f"{module}.{item.stem}")
                elif item.is_dir() and (item / '__init__.py').exists():
                    submodules.append(f"{module}.{item.name}")
    
    all_modules = modules + submodules
    
    print(f"发现 {len(all_modules)} 个模块")
    
    # 生成 API 文档
    docs_source_path = project_root / "docs" / "source"
    
    for module in all_modules:
        try:
            # 尝试导入模块以验证其存在性
            __import__(module)
            print(f"✓ {module}")
        except ImportError as e:
            print(f"✗ {module}: {e}")
    
    return True

if __name__ == "__main__":
    generate_api_docs()
