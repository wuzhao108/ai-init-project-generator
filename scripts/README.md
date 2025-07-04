# Scripts 目录

本目录包含项目的各种测试、调试和验证脚本。

## 脚本说明

### 测试脚本

- **`test_click.py`** - 测试 click 模块和其他依赖的可用性
  - 检查 Python 版本和路径
  - 验证所有依赖模块是否正确安装
  - 测试项目模块的导入功能

- **`simple_test.py`** - 简单的项目结构测试
  - 验证项目目录结构
  - 检查关键文件是否存在
  - 测试基本模块导入

- **`test_new_structure.py`** - 新项目结构测试
  - 测试重构后的项目结构
  - 验证新增功能模块

### 调试脚本

- **`debug_import.py`** - 导入问题调试脚本
  - 详细的模块导入测试
  - 错误信息收集和分析
  - 用于诊断导入相关问题

### 验证脚本

- **`verify_structure.py`** - 项目结构验证脚本
  - 验证项目重构是否成功
  - 检查必需的目录和文件
  - 总结重构完成的功能

## 使用方法

在项目根目录下运行脚本：

```bash
# 测试依赖安装
python scripts/test_click.py

# 验证项目结构
python scripts/verify_structure.py

# 调试导入问题
python scripts/debug_import.py

# 简单测试
python scripts/simple_test.py
```

## 注意事项

- 运行脚本前请确保已安装所有依赖：`pip install -r requirements.txt`
- 某些脚本可能需要在项目根目录下运行以正确导入模块
- 如果遇到导入错误，请先运行 `test_click.py` 检查依赖安装情况