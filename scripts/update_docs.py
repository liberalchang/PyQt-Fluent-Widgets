#!/usr/bin/env python3
# coding: utf-8
"""
按顺序更新文档的脚本
"""

import re
from pathlib import Path

def read_record_file():
    """读取文档更新记录"""
    record_file = Path(__file__).parent.parent / 'docs' / '更新文档记录.md'
    with open(record_file, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def update_record_status(file_path, status):
    """更新文件状态"""
    record_file = Path(__file__).parent.parent / 'docs' / '更新文档记录.md'
    with open(record_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找并更新状态
    pattern = rf'(### {re.escape(file_path)}\n\n\*\*状态\*\*:\s*)`[^`]+`'
    replacement = f'\\1`{status}`'
    content = re.sub(pattern, replacement, content)
    
    with open(record_file, 'w', encoding='utf-8') as f:
        f.write(content)

def get_next_false_file():
    """获取下一个状态为false的文件"""
    content = read_record_file()
    lines = content.split('\n')
    
    current_file = None
    current_status = None
    
    for line in lines:
        if line.startswith('### '):
            current_file = line[4:].strip()
        elif line.startswith('**状态**:'):
            current_status = line.split(':')[1].strip()
            if current_status == '`false`' and current_file:
                return current_file
    
    return None

def main():
    """主函数"""
    next_file = get_next_false_file()
    
    if next_file:
        print(f"下一个需要更新的文件: {next_file}")
        
        # 检查文件是否存在
        file_path = Path(__file__).parent.parent / 'qfluentwidgets' / next_file
        if file_path.exists():
            print(f"文件路径: {file_path}")
            
            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            print(f"文件内容预览:")
            print(content[:500] + "..." if len(content) > 500 else content)
            
            return next_file
        else:
            print(f"文件不存在: {file_path}")
            return None
    else:
        print("所有文件都已更新完成！")
        return None

if __name__ == '__main__':
    next_file = main()
    if next_file:
        print(f"\n请为文件 {next_file} 更新文档，完成后运行:")
        print(f'python -c "from update_docs import update_record_status; update_record_status(\'{next_file}\', \'true\')"')
