@echo off
chcp 65001 >nul
echo PySide6-Fluent-Widgets 文档构建脚本
echo ========================================

REM 统一使用项目根目录 .venv（不再使用 conda）
if not exist ".venv\Scripts\python.exe" (
  echo [错误] 未找到 .venv，请先在项目根目录创建虚拟环境：
  echo   python -m venv .venv
  echo   .venv\Scripts\python -m pip install -U pip
  echo   .venv\Scripts\python -m pip install -r requirements.txt
  echo   .venv\Scripts\python -m pip install sphinx sphinx-rtd-theme sphinx-markdown-tables recommonmark
  pause
  exit /b 1
)

call ".venv\Scripts\activate.bat"
python build_docs.py
set EXITCODE=%ERRORLEVEL%

pause
exit /b %EXITCODE%
