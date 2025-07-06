#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configs模块
包含配置管理相关的功能
"""

__version__ = "2.0.0"
__author__ = "AI Project Generator"

# 导出主要类
from .config_manager_v2 import ConfigManagerV2
from .config_migrator import ConfigMigrator

__all__ = [
    'ConfigManagerV2',
    'ConfigMigrator'
]