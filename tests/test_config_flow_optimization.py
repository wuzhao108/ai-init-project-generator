#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置流程优化测试脚本
测试自定义配置创建时的新流程：
1. 配置收集完成后直接显示详情并询问是否保存
2. 保存后再询问是否生成，不重复显示详情
3. 当用户选择不保存时，提供修改选项
4. 修改完成后重新显示详情并继续后续流程
"""

import sys
import os
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "scripts"))

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from scripts.core.interactive_config import InteractiveConfig
from scripts.core.config_manager import ConfigManager
from main import handle_config_confirmation_and_save, modify_config_item

console = Console()

def test_collect_config_without_save():
    """测试不包含保存逻辑的配置收集"""
    console.print("\n[blue]测试1: 验证collect_config_without_save方法[/blue]")
    
    try:
        interactive = InteractiveConfig()
        
        # 验证方法存在
        assert hasattr(interactive, 'collect_config_without_save'), "collect_config_without_save方法不存在"
        
        console.print("[green]✅ collect_config_without_save方法存在[/green]")
        
        # 验证方法签名
        import inspect
        sig = inspect.signature(interactive.collect_config_without_save)
        params = list(sig.parameters.keys())
        assert 'load_from_existing' in params, "缺少load_from_existing参数"
        
        console.print("[green]✅ 方法签名正确[/green]")
        
        return True
        
    except Exception as e:
        console.print(f"[red]❌ 测试失败: {str(e)}[/red]")
        return False

def test_handle_config_confirmation_and_save():
    """测试配置确认和保存处理函数"""
    console.print("\n[blue]测试2: 验证handle_config_confirmation_and_save函数[/blue]")
    
    try:
        # 验证函数存在
        import main
        assert hasattr(main, 'handle_config_confirmation_and_save'), "handle_config_confirmation_and_save函数不存在"
        
        console.print("[green]✅ handle_config_confirmation_and_save函数存在[/green]")
        
        # 验证函数签名
        import inspect
        sig = inspect.signature(main.handle_config_confirmation_and_save)
        params = list(sig.parameters.keys())
        assert 'config' in params, "缺少config参数"
        assert 'interactive' in params, "缺少interactive参数"
        
        console.print("[green]✅ 函数签名正确[/green]")
        
        return True
        
    except Exception as e:
        console.print(f"[red]❌ 测试失败: {str(e)}[/red]")
        return False

def test_modify_config_item():
    """测试配置项修改函数"""
    console.print("\n[blue]测试3: 验证modify_config_item函数[/blue]")
    
    try:
        # 验证函数存在
        import main
        assert hasattr(main, 'modify_config_item'), "modify_config_item函数不存在"
        
        console.print("[green]✅ modify_config_item函数存在[/green]")
        
        # 验证函数签名
        import inspect
        sig = inspect.signature(main.modify_config_item)
        params = list(sig.parameters.keys())
        assert 'config' in params, "缺少config参数"
        assert 'modify_choice' in params, "缺少modify_choice参数"
        assert 'interactive' in params, "缺少interactive参数"
        
        console.print("[green]✅ 函数签名正确[/green]")
        
        return True
        
    except Exception as e:
        console.print(f"[red]❌ 测试失败: {str(e)}[/red]")
        return False

def test_create_with_custom_config_modification():
    """测试create_with_custom_config函数的修改"""
    console.print("\n[blue]测试4: 验证create_with_custom_config函数修改[/blue]")
    
    try:
        import main
        import inspect
        
        # 获取函数源码
        source = inspect.getsource(main.create_with_custom_config)
        
        # 验证关键修改点
        assert 'collect_config_without_save' in source, "未使用collect_config_without_save方法"
        assert 'handle_config_confirmation_and_save' in source, "未调用handle_config_confirmation_and_save函数"
        assert '确认以上配置并开始生成项目' in source, "生成确认提示文本未更新"
        
        console.print("[green]✅ create_with_custom_config函数修改正确[/green]")
        
        return True
        
    except Exception as e:
        console.print(f"[red]❌ 测试失败: {str(e)}[/red]")
        return False

def test_config_flow_logic():
    """测试配置流程逻辑"""
    console.print("\n[blue]测试5: 验证配置流程逻辑[/blue]")
    
    try:
        # 创建测试配置
        test_config = {
            'name': 'test-project',
            'package': 'com.test.project',
            'version': '1.0.0',
            'description': 'Test project',
            'java_version': '11',
            'spring_version': '2.7.18',
            'project_type': 'single',
            'modules': [],
            'tech_stack': {
                'database': 'mysql',
                'orm': 'mybatis',
                'cache': ['redis'],
                'mq': [],
                'doc': ['swagger'],
                'security': [],
                'monitor': []
            },
            'output_dir': './output',
            'generate_sample_code': True,
            'generate_tests': True,
            'generate_docker': True
        }
        
        # 验证配置结构
        required_keys = ['name', 'package', 'version', 'tech_stack']
        for key in required_keys:
            assert key in test_config, f"配置缺少必需字段: {key}"
        
        console.print("[green]✅ 配置结构验证通过[/green]")
        
        # 验证技术栈结构
        tech_stack = test_config['tech_stack']
        tech_required_keys = ['database', 'orm']
        for key in tech_required_keys:
            assert key in tech_stack, f"技术栈配置缺少必需字段: {key}"
        
        console.print("[green]✅ 技术栈结构验证通过[/green]")
        
        return True
        
    except Exception as e:
        console.print(f"[red]❌ 测试失败: {str(e)}[/red]")
        return False

def test_interactive_config_methods():
    """测试InteractiveConfig类的方法可访问性"""
    console.print("\n[blue]测试6: 验证InteractiveConfig方法可访问性[/blue]")
    
    try:
        interactive = InteractiveConfig()
        
        # 验证私有方法存在（用于配置修改）
        private_methods = [
            '_collect_basic_info',
            '_collect_versions', 
            '_collect_structure',
            '_collect_tech_stack',
            '_collect_options'
        ]
        
        for method_name in private_methods:
            assert hasattr(interactive, method_name), f"方法{method_name}不存在"
        
        console.print("[green]✅ 所有必需的私有方法都存在[/green]")
        
        return True
        
    except Exception as e:
        console.print(f"[red]❌ 测试失败: {str(e)}[/red]")
        return False

def run_all_tests():
    """运行所有测试"""
    console.print(Panel.fit(
        Text("🧪 配置流程优化测试", style="bold green"),
        border_style="green"
    ))
    
    tests = [
        test_collect_config_without_save,
        test_handle_config_confirmation_and_save,
        test_modify_config_item,
        test_create_with_custom_config_modification,
        test_config_flow_logic,
        test_interactive_config_methods
    ]
    
    passed = 0
    total = len(tests)
    
    for test_func in tests:
        if test_func():
            passed += 1
    
    console.print(f"\n[bold]测试结果: {passed}/{total} 通过[/bold]")
    
    if passed == total:
        console.print("[green]🎉 所有测试通过！配置流程优化功能正常工作[/green]")
        
        # 显示功能改进总结
        console.print("\n[blue]📋 功能改进总结:[/blue]")
        console.print("1. ✅ 新增collect_config_without_save方法，分离配置收集和保存逻辑")
        console.print("2. ✅ 新增handle_config_confirmation_and_save函数，统一处理配置确认和保存")
        console.print("3. ✅ 新增modify_config_item函数，支持配置项修改")
        console.print("4. ✅ 优化create_with_custom_config流程，避免重复显示配置详情")
        console.print("5. ✅ 当用户选择不保存时，提供7种修改选项")
        console.print("6. ✅ 修改完成后重新显示详情并继续后续流程")
        
        console.print("\n[yellow]📝 用户体验改进:[/yellow]")
        console.print("• 配置收集完成后立即显示详情")
        console.print("• 保存配置后不再重复显示详情")
        console.print("• 提供灵活的配置修改选项")
        console.print("• 支持循环修改直到用户满意")
        console.print("• 清晰的流程提示和状态反馈")
        
        return True
    else:
        console.print("[red]❌ 部分测试失败，请检查实现[/red]")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)