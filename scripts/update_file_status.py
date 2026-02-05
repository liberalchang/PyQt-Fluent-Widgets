#!/usr/bin/env python3
# coding: utf-8
"""
更新文档记录，为每个文件添加两个状态
"""

import re
from pathlib import Path

def update_single_file_status(file_path, api_status, usage_status):
    """更新单个文件的状态"""
    record_file = Path(__file__).parent.parent / 'docs' / '更新文档记录.md'
    
    with open(record_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找文件部分
    file_pattern = rf'(### {re.escape(file_path)}\n\n)(.*?)(?=### |\Z)'
    file_match = re.search(file_pattern, content, re.DOTALL)
    
    if file_match:
        file_section = file_match.group(2)
        
        # 更新API文档状态
        api_pattern = r'\*\*API文档状态\*\*:\s*`[^`]+`'
        api_replacement = f'**API文档状态**: `{api_status}`'
        file_section = re.sub(api_pattern, api_replacement, file_section)
        
        # 更新组件使用状态
        usage_pattern = r'\*\*组件使用状态\*\*:\s*`[^`]+`'
        usage_replacement = f'**组件使用状态**: `{usage_status}`'
        file_section = re.sub(usage_pattern, usage_replacement, file_section)
        
        # 如果没有找到状态行，添加它们
        if '**API文档状态**:' not in file_section:
            file_section = f'**API文档状态**: `{api_status}`\n**组件使用状态**: `{usage_status}`\n\n' + file_section
        
        # 替换整个文件部分
        new_content = content[:file_match.start(1)] + file_match.group(1) + file_section + content[file_match.end():]
        
        with open(record_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"已更新 {file_path}: API={api_status}, Usage={usage_status}")
    else:
        print(f"未找到文件: {file_path}")

def main():
    """主函数 - 更新一些关键文件的状态"""
    
    # 更新一些已完成组件使用文档的文件
    completed_files = [
        ('components/widgets/label_line_edit.py', 'true', 'true'),  # API文档已生成，使用文档已添加
        ('components/widgets/__init__.py', 'true', 'true'),  # API文档已生成，使用文档已覆盖
        ('components/widgets/button.py', 'true', 'true'),  # API文档已生成，使用文档已覆盖
        ('components/widgets/line_edit.py', 'true', 'true'),  # API文档已生成，使用文档已覆盖
        ('components/widgets/table_view.py', 'true', 'true'),  # API文档已生成，使用文档已覆盖
        ('components/navigation/__init__.py', 'true', 'true'),  # API文档已生成，使用文档已覆盖
        ('components/dialog_box/__init__.py', 'true', 'true'),  # API文档已生成，使用文档已覆盖
        ('components/settings/__init__.py', 'true', 'true'),  # API文档已生成，使用文档已覆盖
        ('components/material/__init__.py', 'true', 'true'),  # API文档已生成，使用文档已覆盖
        ('components/charts/__init__.py', 'true', 'true'),  # API文档已生成，使用文档已覆盖
        ('components/date_time/__init__.py', 'true', 'true'),  # API文档已生成，使用文档已覆盖
        ('components/layout/__init__.py', 'true', 'true'),  # API文档已生成，使用文档已覆盖
        ('components/vispy/__init__.py', 'true', 'true'),  # API文档已生成，使用文档已覆盖
        ('multimedia/__init__.py', 'true', 'true'),  # API文档已生成，使用文档已覆盖
        ('window/__init__.py', 'true', 'true'),  # API文档已生成，使用文档已覆盖
    ]
    
    for file_path, api_status, usage_status in completed_files:
        update_single_file_status(file_path, api_status, usage_status)
    
    print("\n状态更新完成！")

if __name__ == '__main__':
    main()
