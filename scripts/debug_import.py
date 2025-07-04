#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import traceback
from pathlib import Path

print("=== 调试导入问题 ===")
print(f"Python版本: {sys.version}")
print(f"当前工作目录: {Path.cwd()}")
print(f"Python路径: {sys.path[:3]}...")  # 只显示前3个路径
print()

try:
    print("尝试导入 spring_init...")
    import spring_init
    print("✅ spring_init 导入成功!")
    print(f"版本: {spring_init.__version__}")
    print(f"作者: {spring_init.__author__}")
except Exception as e:
    print(f"❌ spring_init 导入失败: {e}")
    print("详细错误信息:")
    traceback.print_exc()
    print()

try:
    print("尝试导入 spring_init.cli...")
    from spring_init.cli import cli
    print("✅ CLI 导入成功!")
except Exception as e:
    print(f"❌ CLI 导入失败: {e}")
    print("详细错误信息:")
    traceback.print_exc()
    print()

try:
    print("尝试导入 common 模块...")
    from common.config_manager import ConfigManager
    print("✅ ConfigManager 导入成功!")
except Exception as e:
    print(f"❌ ConfigManager 导入失败: {e}")
    print("详细错误信息:")
    traceback.print_exc()
    print()

print("=== 调试完成 ===")