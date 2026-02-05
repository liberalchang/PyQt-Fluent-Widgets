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
    
    # 生成 API 文档的目录
    api_source_path = project_root / "docs" / "source" / "api"
    api_source_path.mkdir(exist_ok=True)
    
    # 使用 sphinx-apidoc 生成 API 文档
    import subprocess
    
    cmd = [
        "sphinx-apidoc",
        "-f",  # 强制覆盖
        "-o", str(api_source_path),  # 输出目录
        str(qfluentwidgets_path),  # 源目录
        "--module-first",  # 按模块优先排序
        "--separate",  # 为每个模块创建单独的文件
    ]
    
    print(f"执行命令: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        if result.returncode == 0:
            print("API 文档生成成功")
            print(result.stdout)
        else:
            print(f"API 文档生成失败: {result.stderr}")
            return False
    except Exception as e:
        print(f"执行 sphinx-apidoc 时出错: {e}")
        return False
    
    return True

if __name__ == "__main__":
    generate_api_docs()
