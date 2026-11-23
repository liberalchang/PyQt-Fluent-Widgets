# pip 打包与本地安装

统一在项目根目录、`.venv` 环境中操作。产物在 `dist/`（已由 `.gitignore` 忽略）。

## 1. 准备环境

```shell
python -m venv .venv
.venv\Scripts\activate
pip install -U pip setuptools wheel build twine
pip install -r requirements.txt
```

## 2. 确认版本号

打包前检查并按需修改：

| 文件 | 字段 |
| --- | --- |
| `setup.py` | `version=` |
| `qfluentwidgets/__init__.py` | `__version__` |

当前约定示例：`1.11.3-liber.1`（与官方对齐主版本，后缀标识二次开发）。

## 3. 构建分发包

推荐使用 `build`（PEP 517）：

```shell
# 在项目根目录
python -m build
```

等价的旧写法（仍可用）：

```shell
python setup.py sdist bdist_wheel
```

成功后 `dist/` 下会有：

- `PySide6_Fluent_Widgets-<version>.tar.gz`（源码包 sdist）
- `PySide6_Fluent_Widgets-<version>-py3-none-any.whl`（wheel）

## 4. 本地安装验证

从刚打好的包安装（不要用已安装的 editable 混测时，可先卸载）：

```shell
pip uninstall -y PySide6-Fluent-Widgets
pip install dist\PySide6_Fluent_Widgets-*-py3-none-any.whl
```

完整版 extras：

```shell
pip install "dist\PySide6_Fluent_Widgets-*-py3-none-any.whl[full]"
```

开发期也可直接可编辑安装，无需每次打包：

```shell
pip install -e .
# 或
pip install -e ".[full]"
```

验证：

```shell
python -c "import qfluentwidgets as q; print(q.__version__)"
cd examples\gallery
python demo.py
```

## 5. 发布到 PyPI（可选）

先做检查，再上传。测试通道建议先走 TestPyPI：

```shell
twine check dist\*
twine upload --repository testpypi dist\*
# 确认无误后再：
# twine upload dist\*
```

上传正式 PyPI 前请确认包名、版本未被占用，且许可证/元数据正确。

## 6. 常用清理

```shell
rmdir /s /q build dist
rmdir /s /q PySide6_Fluent_Widgets.egg-info
```

PowerShell：

```powershell
Remove-Item -Recurse -Force build, dist, PySide6_Fluent_Widgets.egg-info -ErrorAction SilentlyContinue
```
