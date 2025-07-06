#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
目录重组测试脚本
验证模板和配置文件路径调整后的功能
"""

import sys
import os
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from scripts.core.config_manager import ConfigManager
from scripts.core.template_manager import TemplateManager
from scripts.core.project_generator import ProjectGenerator

def test_config_manager():
    """测试配置管理器"""
    print("\n=== 测试配置管理器 ===")
    
    try:
        config_manager = ConfigManager()
        print(f"✓ 配置管理器初始化成功")
        print(f"✓ 配置目录: {config_manager.config_dir}")
        
        # 测试列出配置
        configs = config_manager.list_configs()
        print(f"✓ 配置列表获取成功，共 {len(configs)} 个配置")
        for config in configs:
            print(f"  - {config}")
        
        return True
    except Exception as e:
        print(f"❌ 配置管理器测试失败: {str(e)}")
        return False

def test_template_manager():
    """测试模板管理器"""
    print("\n=== 测试模板管理器 ===")
    
    try:
        template_manager = TemplateManager()
        print(f"✓ 模板管理器初始化成功")
        print(f"✓ 模板目录: {template_manager.templates_dir}")
        
        # 测试列出模板
        templates = template_manager.list_templates()
        print(f"✓ 模板列表获取成功，共 {len(templates)} 个模板")
        for template in templates:
            print(f"  - {template}")
        
        # 测试加载主模板
        if "spring-boot-templates" in templates:
            content = template_manager.load_template("spring-boot-templates")
            extracted = template_manager.extract_templates_from_markdown(content)
            print(f"✓ spring-boot-templates 加载成功，包含 {len(extracted)} 个子模板")
            for name in list(extracted.keys())[:5]:  # 只显示前5个
                print(f"  - {name}")
        
        return True
    except Exception as e:
        print(f"❌ 模板管理器测试失败: {str(e)}")
        return False

def test_project_generator():
    """测试项目生成器"""
    print("\n=== 测试项目生成器 ===")
    
    try:
        generator = ProjectGenerator()
        print(f"✓ 项目生成器初始化成功")
        print(f"✓ 加载的模板数量: {len(generator.templates)}")
        
        # 显示加载的模板
        for name in list(generator.templates.keys())[:5]:  # 只显示前5个
            print(f"  - {name}")
        
        return True
    except Exception as e:
        print(f"❌ 项目生成器测试失败: {str(e)}")
        return False

def test_directory_structure():
    """测试目录结构"""
    print("\n=== 测试目录结构 ===")
    
    project_root = Path(__file__).parent.parent
    
    # 检查templates目录
    templates_dir = project_root / "templates"
    if templates_dir.exists():
        print(f"✓ templates目录存在: {templates_dir}")
        template_files = list(templates_dir.glob("*.md"))
        print(f"✓ 模板文件数量: {len(template_files)}")
        for file in template_files:
            print(f"  - {file.name}")
    else:
        print(f"❌ templates目录不存在: {templates_dir}")
        return False
    
    # 检查scripts/configs_main目录
    configs_dir = project_root / "scripts" / "configs_main"
    if configs_dir.exists():
        print(f"✓ scripts/configs_main目录存在: {configs_dir}")
        config_files = list(configs_dir.glob("*.json"))
        print(f"✓ 配置文件数量: {len(config_files)}")
        for file in config_files:
            print(f"  - {file.name}")
    else:
        print(f"❌ scripts/configs_main目录不存在: {configs_dir}")
        return False
    
    # 检查旧的configs目录是否已移除
    old_configs_dir = project_root / "configs"
    if not old_configs_dir.exists():
        print(f"✓ 旧的configs目录已成功移除")
    else:
        print(f"⚠️ 旧的configs目录仍然存在: {old_configs_dir}")
    
    return True

def test_integration():
    """集成测试"""
    print("\n=== 集成测试 ===")
    
    try:
        # 创建配置管理器和模板管理器
        config_manager = ConfigManager()
        template_manager = TemplateManager()
        
        # 创建项目生成器
        generator = ProjectGenerator(
            config_manager=config_manager,
            template_manager=template_manager
        )
        
        print(f"✓ 集成初始化成功")
        print(f"✓ 配置目录: {config_manager.config_dir}")
        print(f"✓ 模板目录: {template_manager.templates_dir}")
        print(f"✓ 可用配置: {len(config_manager.list_configs())}")
        print(f"✓ 可用模板: {len(template_manager.list_templates())}")
        print(f"✓ 加载的模板: {len(generator.templates)}")
        
        return True
    except Exception as e:
        print(f"❌ 集成测试失败: {str(e)}")
        return False

def main():
    """主测试函数"""
    print("🧪 目录重组功能测试")
    print("=" * 50)
    
    tests = [
        ("目录结构", test_directory_structure),
        ("配置管理器", test_config_manager),
        ("模板管理器", test_template_manager),
        ("项目生成器", test_project_generator),
        ("集成测试", test_integration)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
                print(f"\n✅ {test_name} 测试通过")
            else:
                print(f"\n❌ {test_name} 测试失败")
        except Exception as e:
            print(f"\n💥 {test_name} 测试异常: {str(e)}")
    
    print("\n" + "=" * 50)
    print(f"📊 测试结果: {passed}/{total} 通过")
    
    if passed == total:
        print("🎉 所有测试通过！目录重组成功！")
        return True
    else:
        print("⚠️ 部分测试失败，请检查问题")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)