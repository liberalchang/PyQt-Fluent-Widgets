@echo off
chcp 65001 >nul
echo PySide6-Fluent-Widgets 文档构建脚本
echo ========================================

REM 激活 conda 环境
call conda activate pyside6dev

REM 运行 Python 构建脚本
python build_docs.py

pause
