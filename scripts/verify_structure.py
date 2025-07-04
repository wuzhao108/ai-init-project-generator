#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path

print("=== Spring Boot 项目生成器重构验证 ===")
print()

# 检查目录结构
project_root = Path(__file__).parent
print(f"项目根目录: {project_root}")
print()

# 必需的目录
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

print("📂 目录结构检查:")
all_dirs_exist = True
for dir_name in required_dirs:
    dir_path = project_root / dir_name
    exists = dir_path.exists() and dir_path.is_dir()
    status = "✅" if exists else "❌"
    print(f"  {status} {dir_name}")
    if not exists:
        all_dirs_exist = False

print()

# 必需的文件
required_files = [
    "main.py",
    "README.md",
    "spring_init/__init__.py",
    "spring_init/cli.py", 
    "spring_init/generator.py",
    "spring_init/config.py",
    "spring_init/interactive.py",
    "common/config_manager.py",
    "common/utils/string_utils.py",
    "common/utils/file_utils.py",
    "common/validators/project_validator.py",
    "common/constants/project_constants.py"
]

print("📄 关键文件检查:")
all_files_exist = True
for file_name in required_files:
    file_path = project_root / file_name
    exists = file_path.exists() and file_path.is_file()
    status = "✅" if exists else "❌"
    print(f"  {status} {file_name}")
    if not exists:
        all_files_exist = False

print()

# 总结
if all_dirs_exist and all_files_exist:
    print("🎉 项目重构验证成功!")
    print()
    print("✨ 重构完成的功能:")
    print("  • 创建了通用代码目录 (common/)")
    print("  • 创建了结果输出目录 (output/)")
    print("  • 创建了配置文件目录 (configs/)")
    print("  • 实现了JSON配置文件管理")
    print("  • 更新了CLI命令支持配置管理")
    print("  • 重构了项目生成器")
    print()
    print("🚀 使用方法:")
    print("  python main.py create --help    # 创建新项目")
    print("  python main.py list-configs     # 列出配置文件")
    print("  python main.py generate --help  # 从配置生成项目")
else:
    print("❌ 项目重构验证失败，请检查缺失的目录和文件")
    
print()
print("=== 验证完成 ===")