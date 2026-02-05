#!/usr/bin/env python3
# coding: utf-8
"""
更新文档记录结构，为每个文件添加两个状态
"""

import re
from pathlib import Path

def update_record_structure():
    """更新文档记录结构"""
    record_file = Path(__file__).parent.parent / 'docs' / '更新文档记录.md'
    
    with open(record_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    new_lines = []
    
    for line in lines:
        if line.startswith('### ') and '.py' in line:
            file_path = line[4:].strip()
            new_lines.append(line)
            new_lines.append('')
            new_lines.append('**API文档状态**: `false`')
            new_lines.append('**组件使用状态**: `false`')
        elif line.startswith('**状态**:'):
            # 跳过旧的状态行
            continue
        else:
            new_lines.append(line)
    
    new_content = '\n'.join(new_lines)
    
    with open(record_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("文档记录结构已更新")

if __name__ == '__main__':
    update_record_structure()
