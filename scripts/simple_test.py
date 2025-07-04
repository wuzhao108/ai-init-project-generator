#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

print("=== 项目结构重构完成测试 ===")
print(f"项目根目录: {project_root}")
print()

# 检查目录结构
print("📂 检查目录结构:")
required_dirs = [
    "spring_init",
    "common",
    "common/utils", 
    "common/validators",
    "common/constants",
    "templates",
    "output",
    "configs"
]

for dir_path in required_dirs:
    full_path = project_root / dir_path
    status = "✅" if full_path.exists() else "❌"
    print(f"  {status} {dir_path}")

print()

# 检查关键文件
print("📄 检查关键文件:")
key_files = [
    "main.py",
    "README.md", 
    "spring_init/__init__.py",
    "spring_init/cli.py",
    "spring_init/generator.py",
    "common/config_manager.py",
    "common/utils/string_utils.py",
    "common/utils/file_utils.py",
    "common/validators/project_validator.py",
    "common/constants/project_constants.py"
]

for file_path in key_files:
    full_path = project_root / file_path
    status = "✅" if full_path.exists() else "❌"
    print(f"  {status} {file_path}")

print()

# 测试模块导入
print("🔧 测试模块导入:")
try:
    from common.config_manager import ConfigManager
    print("  ✅ ConfigManager 导入成功")
except Exception as e:
    print(f"  ❌ ConfigManager 导入失败: {e}")

try:
    from common.utils.string_utils import to_camel_case
    print("  ✅ string_utils 导入成功")
except Exception as e:
    print(f"  ❌ string_utils 导入失败: {e}")

try:
    from spring_init.cli import cli
    print("  ✅ CLI 模块导入成功")
except Exception as e:
    print(f"  ❌ CLI 模块导入失败: {e}")

print()

# 测试配置管理器基本功能
print("⚙️ 测试配置管理器:")
try:
    config_manager = ConfigManager()
    default_config = config_manager.create_default_config()
    print(f"  ✅ 默认配置创建成功: {default_config['name']}")
except Exception as e:
    print(f"  ❌ 配置管理器测试失败: {e}")

print()
print("🎉 项目结构重构测试完成!")
print()
print("📋 重构总结:")
print("  • 创建了 common/ 目录存放通用代码")
print("  • 创建了 output/ 目录存放生成结果")
print("  • 创建了 configs/ 目录存放JSON配置文件")
print("  • 实现了配置文件管理功能")
print("  • 更新了CLI命令支持配置管理")
print("  • 重构了项目生成器支持新的目录结构")
print()
print("🚀 可以使用以下命令开始使用:")
print("  python main.py create --help")
print("  python main.py list-configs")
print("  python main.py generate --help")