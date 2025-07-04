#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spring Boot项目生成器 - 主入口文件

这是一个基于Python的CLI工具，用于快速生成Spring Boot项目模板。
支持多种技术栈配置、项目结构定制和配置文件管理。

使用方法:
    python main.py create --help
    python main.py list-configs
    python main.py generate <config_name>
"""

import sys
import os
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

try:
    from spring_init.cli import cli
except ImportError as e:
    print(f"导入错误: {e}")
    print("请确保所有依赖已正确安装")
    sys.exit(1)


def main():
    """主入口函数"""
    try:
        # 确保必要的目录存在
        ensure_directories()
        
        # 启动CLI应用
        cli()
    except KeyboardInterrupt:
        print("\n\n👋 再见！")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        sys.exit(1)


def ensure_directories():
    """确保必要的目录存在"""
    directories = [
        project_root / "output",
        project_root / "configs",
        project_root / "common" / "utils",
        project_root / "common" / "validators",
        project_root / "common" / "constants"
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    main()