#!/usr/bin/env python3
# coding: utf-8
"""
扫描qfluentwidgets目录树，生成文档更新记录
"""

import os
import ast
from pathlib import Path

def scan_directory(directory, prefix='', is_last=False):
    """递归扫描目录结构"""
    lines = []
    
    # 获取目录中的所有项目并排序
    items = sorted(Path(directory).iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    
    for i, item in enumerate(items):
        # 跳过__pycache__目录
        if item.name == '__pycache__':
            continue
            
        # 判断是否是最后一个项目
        is_last_item = i == len(items) - 1
        
        # 构建前缀
        if prefix == '':
            current_prefix = ''
        else:
            current_prefix = prefix[:-1] + '└── ' if is_last_item else prefix[:-1] + '├── '
        
        # 添加项目
        if item.is_file() and item.suffix == '.py':
            lines.append(f"{current_prefix}{item.name}")
        elif item.is_dir():
            lines.append(f"{current_prefix}{item.name}/")
            
            # 递归扫描子目录
            new_prefix = prefix + ('    ' if is_last_item else '│   ')
            sub_lines = scan_directory(item, new_prefix, is_last_item)
            lines.extend(sub_lines)
    
    return lines

def get_all_python_files(directory):
    """获取所有Python文件"""
    python_files = []
    directory = Path(directory)
    
    for item in directory.rglob('*.py'):
        if '__pycache__' not in str(item):
            python_files.append(str(item))
    
    return sorted(python_files)

def extract_classes_from_file(file_path):
    """从Python文件中提取类名"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        classes = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                # 跳过私有类
                if not node.name.startswith('_'):
                    classes.append(node.name)
        
        return classes
    except Exception as e:
        print(f"解析文件 {file_path} 时出错: {e}")
        return []

def main():
    """主函数"""
    qfluentwidgets_dir = Path(__file__).parent.parent / 'qfluentwidgets'
    
    if not qfluentwidgets_dir.exists():
        print(f"目录不存在: {qfluentwidgets_dir}")
        return
    
    print("=== qfluentwidgets 目录结构 ===")
    tree_lines = scan_directory(qfluentwidgets_dir)
    for line in tree_lines:
        print(line)
    
    print("\n=== 所有Python文件 ===")
    python_files = get_all_python_files(qfluentwidgets_dir)
    for file_path in python_files:
        print(file_path)
    
    print("\n=== 生成文档更新记录 ===")
    # 生成文档更新记录
    record_file = Path(__file__).parent.parent / 'docs' / '更新文档记录.md'
    
    with open(record_file, 'w', encoding='utf-8') as f:
        f.write("# 文档更新记录\n\n")
        f.write("此文件记录所有需要文档更新的文件及其状态。\n\n")
        f.write("状态说明：\n")
        f.write("- `false`: 未更新文档\n")
        f.write("- `true`: 已更新文档\n\n")
        f.write("---\n\n")
        
        # 按目录分组
        current_dir = ""
        for file_path in python_files:
            # 获取相对路径
            rel_path = Path(file_path).relative_to(qfluentwidgets_dir)
            file_dir = str(rel_path.parent)
            
            # 添加目录标题
            if file_dir != current_dir:
                current_dir = file_dir
                if current_dir == '.':
                    f.write("## 根目录\n\n")
                else:
                    f.write(f"## {current_dir}\n\n")
            
            # 提取类名
            classes = extract_classes_from_file(file_path)
            
            # 写入文件记录
            f.write(f"### {rel_path}\n\n")
            f.write(f"**状态**: `false`\n\n")
            
            if classes:
                f.write(f"**包含的类**: {', '.join(classes)}\n\n")
            
            f.write("---\n\n")
    
    print(f"文档更新记录已生成: {record_file}")

if __name__ == '__main__':
    main()
