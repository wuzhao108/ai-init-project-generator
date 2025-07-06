#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置显示功能修复测试脚本

测试目标：
1. 验证show_custom_config_details函数能正确处理字典类型配置
2. 验证show_custom_config_details函数能正确处理对象类型配置
3. 确保不再出现'dict' object has no attribute 'name'错误
"""

import sys
import os
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from main import show_custom_config_details
from scripts.core.config_manager import ConfigManager
from scripts.core.interactive_config import InteractiveConfig
from rich.console import Console

console = Console()

def test_dict_config_display():
    """测试字典类型配置的显示"""
    console.print("\n[blue]🧪 测试字典类型配置显示...[/blue]")
    
    # 创建字典类型的配置
    dict_config = {
        'name': 'test-project',
        'package': 'com.test.project',
        'version': '1.0.0',
        'description': '测试项目',
        'java_version': '17',
        'spring_version': '3.2.2',
        'multi_module': False,
        'tech_stack': {
            'database': 'mysql',
            'orm': 'mybatis',
            'cache': ['redis'],
            'mq': ['rabbitmq'],
            'doc': True,
            'security': False,
            'mongodb': False,
            'elasticsearch': False,
            'actuator': True
        },
        'output_dir': './output',
        'generate_sample_code': True,
        'generate_tests': True,
        'generate_docker': True
    }
    
    try:
        show_custom_config_details(dict_config)
        console.print("[green]✅ 字典类型配置显示测试通过[/green]")
        return True
    except Exception as e:
        console.print(f"[red]❌ 字典类型配置显示测试失败: {str(e)}[/red]")
        return False

def test_object_config_display():
    """测试对象类型配置的显示"""
    console.print("\n[blue]🧪 测试对象类型配置显示...[/blue]")
    
    # 创建一个简单的配置对象
    class MockTechStack:
        def __init__(self):
            self.database = 'h2'
            self.orm = 'jpa'
            self.cache = ['redis']
            self.mq = []
            self.doc = True
            self.security = False
            self.mongodb = False
            self.elasticsearch = False
            self.actuator = True
    
    class MockConfig:
        def __init__(self):
            self.name = 'mock-project'
            self.package = 'com.mock.project'
            self.version = '1.0.0'
            self.description = '模拟项目'
            self.java_version = '17'
            self.spring_version = '3.2.2'
            self.multi_module = False
            self.modules = []
            self.tech_stack = MockTechStack()
            self.output_dir = './output'
            self.generate_sample_code = True
            self.generate_tests = True
            self.generate_docker = True
    
    mock_config = MockConfig()
    
    try:
        show_custom_config_details(mock_config)
        console.print("[green]✅ 对象类型配置显示测试通过[/green]")
        return True
    except Exception as e:
        console.print(f"[red]❌ 对象类型配置显示测试失败: {str(e)}[/red]")
        return False

def test_loaded_config_display():
    """测试从配置文件加载的配置显示"""
    console.print("\n[blue]🧪 测试从配置文件加载的配置显示...[/blue]")
    
    try:
        config_manager = ConfigManager()
        configs = config_manager.list_configs()
        
        if not configs:
            console.print("[yellow]⚠️ 没有可用的配置文件，跳过此测试[/yellow]")
            return True
        
        # 加载第一个配置文件
        config = config_manager.load_config(configs[0])
        
        # 测试显示
        show_custom_config_details(config)
        console.print("[green]✅ 加载配置显示测试通过[/green]")
        return True
    except Exception as e:
        console.print(f"[red]❌ 加载配置显示测试失败: {str(e)}[/red]")
        return False

def test_edge_cases():
    """测试边界情况"""
    console.print("\n[blue]🧪 测试边界情况...[/blue]")
    
    # 测试空配置
    empty_config = {}
    
    try:
        show_custom_config_details(empty_config)
        console.print("[green]✅ 空配置测试通过[/green]")
    except Exception as e:
        console.print(f"[red]❌ 空配置测试失败: {str(e)}[/red]")
        return False
    
    # 测试部分缺失的配置
    partial_config = {
        'name': 'partial-project',
        'tech_stack': {
            'database': 'mysql'
        }
    }
    
    try:
        show_custom_config_details(partial_config)
        console.print("[green]✅ 部分配置测试通过[/green]")
        return True
    except Exception as e:
        console.print(f"[red]❌ 部分配置测试失败: {str(e)}[/red]")
        return False

def main():
    """主测试函数"""
    console.print("[bold blue]🧪 配置显示功能修复测试[/bold blue]")
    console.print("测试目标：验证show_custom_config_details函数能正确处理字典和对象类型配置")
    
    tests = [
        ("字典类型配置显示", test_dict_config_display),
        ("对象类型配置显示", test_object_config_display),
        ("加载配置显示", test_loaded_config_display),
        ("边界情况", test_edge_cases)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        console.print(f"\n[yellow]📋 运行测试: {test_name}[/yellow]")
        if test_func():
            passed += 1
    
    console.print(f"\n[bold]📊 测试结果: {passed}/{total} 通过[/bold]")
    
    if passed == total:
        console.print("[green]🎉 所有测试通过！配置显示功能修复成功！[/green]")
        return True
    else:
        console.print("[red]❌ 部分测试失败，需要进一步检查[/red]")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)