#!/usr/bin/env python3
"""
文档构建脚本
用于构建 PySide6-Fluent-Widgets 的中文文档
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def check_dependencies():
    """检查依赖是否已安装"""
    required_packages = [
        'sphinx',
        'sphinx_rtd_theme', 
        'sphinx_markdown_tables',
        'recommonmark'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"缺少依赖包: {', '.join(missing_packages)}")
        print("请运行以下命令安装:")
        print(f"pip install {' '.join(missing_packages)}")
        return False
    
    return True

def clean_build_dir():
    """清理构建目录"""
    build_dir = Path("docs/build")
    if build_dir.exists():
        shutil.rmtree(build_dir)
        print("已清理构建目录")

def generate_api_docs():
    """生成 API 文档"""
    print("正在生成 API 文档...")
    
    try:
        # 使用 sphinx-apidoc 生成 API 文档
        result = subprocess.run([
            "sphinx-apidoc", 
            "-o", "docs/source/api", 
            "qfluentwidgets", 
            "--force", 
            "--module-first"
        ], capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"API 文档生成失败: {result.stderr}")
            return False
        
        print("API 文档生成成功")
        return True
        
    except Exception as e:
        print(f"API 文档生成出错: {e}")
        return False

def build_html_docs():
    """构建 HTML 文档"""
    print("正在构建 HTML 文档...")
    
    try:
        # 切换到 docs 目录并构建
        result = subprocess.run([
            "sphinx-build", 
            "-b", "html", 
            "source", 
            "build"
        ], cwd="docs", capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"HTML 文档构建失败: {result.stderr}")
            return False
        
        print("HTML 文档构建成功")
        return True
        
    except Exception as e:
        print(f"HTML 文档构建出错: {e}")
        return False

def open_docs():
    """打开生成的文档"""
    index_file = Path("docs/build/index.html")
    if index_file.exists():
        import webbrowser
        webbrowser.open(str(index_file.absolute()))
        print("已在浏览器中打开文档")
    else:
        print("文档文件不存在")

def main():
    """主函数"""
    print("PySide6-Fluent-Widgets 文档构建脚本")
    print("=" * 50)
    
    # 检查依赖
    if not check_dependencies():
        sys.exit(1)
    
    # 清理构建目录
    clean_build_dir()
    
    # 生成 API 文档
    if not generate_api_docs():
        sys.exit(1)
    
    # 构建 HTML 文档
    if not build_html_docs():
        sys.exit(1)
    
    print("\n文档构建完成!")
    print(f"文档位置: {Path('docs/build').absolute()}")
    print("要查看文档，请在浏览器中打开 docs/build/index.html")
    
    # 询问是否打开文档
    try:
        response = input("\n是否在浏览器中打开文档? (y/n): ").strip().lower()
        if response in ['y', 'yes', '是']:
            open_docs()
    except KeyboardInterrupt:
        print("\n构建完成")

if __name__ == "__main__":
    main()
