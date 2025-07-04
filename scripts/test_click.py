#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试 click 模块和其他依赖的可用性
"""

import sys
print(f"Python 版本: {sys.version}")
print(f"Python 路径: {sys.executable}")
print("\n=== 测试依赖模块 ===")

# 测试各个依赖模块
modules_to_test = [
    'click',
    'jinja2', 
    'questionary',
    'yaml',
    'colorama',
    'rich',
    'typing_extensions'
]

for module_name in modules_to_test:
    try:
        __import__(module_name)
        print(f"✓ {module_name} - 可用")
    except ImportError as e:
        print(f"✗ {module_name} - 不可用: {e}")

print("\n=== 测试项目模块 ===")

# 测试项目模块
project_modules = [
    'spring_init',
    'spring_init.cli',
    'common.config_manager'
]

for module_name in project_modules:
    try:
        __import__(module_name)
        print(f"✓ {module_name} - 可用")
    except ImportError as e:
        print(f"✗ {module_name} - 不可用: {e}")
    except Exception as e:
        print(f"✗ {module_name} - 错误: {e}")

print("\n=== 测试完成 ===")