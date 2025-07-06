#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
项目功能测试脚本
测试重构后的项目是否能正常运行
"""

import sys
import os
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def test_imports():
    """测试所有模块导入是否正常"""
    print("=== 测试模块导入 ===")
    
    try:
        # 测试scripts模块导入
        from scripts.core.config_manager import ConfigManager
        print("✓ ConfigManager 导入成功")
        
        from scripts.constants.project_constants import ProjectConstants
        print("✓ ProjectConstants 导入成功")
        
        from scripts.utils.file_utils import ensure_dir, write_json, read_json
        print("✓ file_utils 导入成功")
        
        from scripts.utils.string_utils import validate_project_name, to_camel_case
        print("✓ string_utils 导入成功")
        
        from scripts.validators.project_validator import ProjectValidator
        print("✓ ProjectValidator 导入成功")
        
        # 测试configs模块导入
        from configs.config_manager_v2 import ConfigManagerV2
        print("✓ ConfigManagerV2 导入成功")
        
        from configs.config_migrator import ConfigMigrator
        print("✓ ConfigMigrator 导入成功")
        
        # 测试spring_init模块导入
        from spring_init.cli import cli
        print("✓ CLI模块 导入成功")
        
        from spring_init.generator import ProjectGenerator
        print("✓ ProjectGenerator 导入成功")
        
        from spring_init.interactive import InteractiveConfig
        print("✓ InteractiveConfig 导入成功")
        
        print("\n所有模块导入测试通过！")
        return True
        
    except ImportError as e:
        print(f"❌ 导入失败: {e}")
        return False
    except Exception as e:
        print(f"❌ 其他错误: {e}")
        return False

def test_config_manager():
    """测试配置管理器功能"""
    print("\n=== 测试配置管理器 ===")
    
    try:
        from scripts.core.config_manager import ConfigManager
        
        # 创建配置管理器
        config_manager = ConfigManager()
        print("✓ ConfigManager 创建成功")
        
        # 测试创建默认配置
        default_config = config_manager.create_default_config()
        print("✓ 默认配置创建成功")
        
        # 测试列出配置
        configs = config_manager.list_configs()
        print(f"✓ 配置列表获取成功，共 {len(configs)} 个配置")
        
        return True
        
    except Exception as e:
        print(f"❌ 配置管理器测试失败: {e}")
        return False

def test_config_manager_v2():
    """测试新版配置管理器功能"""
    print("\n=== 测试新版配置管理器 ===")
    
    try:
        from configs.config_manager_v2 import ConfigManagerV2
        
        # 创建配置管理器
        config_manager = ConfigManagerV2()
        print("✓ ConfigManagerV2 创建成功")
        
        # 测试加载系统配置
        system_config = config_manager.load_system_config()
        print("✓ 系统配置加载成功")
        
        # 测试列出模板
        templates = config_manager.list_templates()
        print(f"✓ 模板列表获取成功，共 {len(templates)} 个模板")
        
        # 测试列出历史配置
        histories = config_manager.list_history_configs()
        print(f"✓ 历史配置列表获取成功，共 {len(histories)} 个配置")
        
        return True
        
    except Exception as e:
        print(f"❌ 新版配置管理器测试失败: {e}")
        return False

def test_project_constants():
    """测试项目常量"""
    print("\n=== 测试项目常量 ===")
    
    try:
        from scripts.constants.project_constants import ProjectConstants
        
        # 测试常量访问
        print(f"✓ 默认Java版本: {ProjectConstants.DEFAULT_JAVA_VERSION}")
        print(f"✓ 默认Spring Boot版本: {ProjectConstants.DEFAULT_SPRING_BOOT_VERSION}")
        print(f"✓ 支持的数据库: {ProjectConstants.DATABASES}")
        
        return True
        
    except Exception as e:
        print(f"❌ 项目常量测试失败: {e}")
        return False

def test_validators():
    """测试验证器功能"""
    print("\n=== 测试验证器 ===")
    
    try:
        from scripts.validators.project_validator import ProjectValidator
        
        # 测试项目名称验证
        valid, error = ProjectValidator.validate_project_name("my-test-project")
        print(f"✓ 项目名称验证: {valid}")
        
        # 测试包名验证
        valid, error = ProjectValidator.validate_package_name("com.example.test")
        print(f"✓ 包名验证: {valid}")
        
        # 测试版本号验证
        valid, error = ProjectValidator.validate_version("1.0.0")
        print(f"✓ 版本号验证: {valid}")
        
        return True
        
    except Exception as e:
        print(f"❌ 验证器测试失败: {e}")
        return False

def test_utils():
    """测试工具函数"""
    print("\n=== 测试工具函数 ===")
    
    try:
        from scripts.utils.string_utils import to_camel_case, to_pascal_case, validate_project_name
        from scripts.utils.file_utils import ensure_dir, file_exists
        
        # 测试字符串工具
        camel = to_camel_case("test_string")
        pascal = to_pascal_case("test_string")
        print(f"✓ 字符串转换: {camel}, {pascal}")
        
        # 测试项目名称验证
        valid = validate_project_name("my-test-project")
        print(f"✓ 项目名称验证: {valid}")
        
        # 测试文件工具
        test_dir = project_root / "tests" / "temp"
        ensure_dir(str(test_dir))
        exists = file_exists(str(test_dir / "nonexistent.txt"))
        print(f"✓ 文件工具测试: 目录创建成功, 文件存在检查: {exists}")
        
        return True
        
    except Exception as e:
        print(f"❌ 工具函数测试失败: {e}")
        return False

def main():
    """主测试函数"""
    print("开始项目功能测试...\n")
    
    tests = [
        test_imports,
        test_config_manager,
        test_config_manager_v2,
        test_project_constants,
        test_validators,
        test_utils
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ 测试执行失败: {e}")
    
    print(f"\n=== 测试结果 ===")
    print(f"总测试数: {total}")
    print(f"通过测试: {passed}")
    print(f"失败测试: {total - passed}")
    print(f"成功率: {passed/total*100:.1f}%")
    
    if passed == total:
        print("\n🎉 所有测试通过！项目重构成功！")
        return True
    else:
        print("\n⚠️ 部分测试失败，需要检查问题。")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)