#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试新的目录结构和配置管理功能

这个脚本用于验证重构后的项目结构是否正常工作。
"""

import sys
import os
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def test_imports():
    """测试模块导入"""
    print("🔍 测试模块导入...")
    
    try:
        # 测试通用模块导入
        from common.config_manager import ConfigManager
        from common.utils.string_utils import to_camel_case, to_pascal_case
        from common.utils.file_utils import ensure_dir, file_exists
        from common.validators.project_validator import ProjectValidator
        from common.constants.project_constants import ProjectConstants
        print("✅ 通用模块导入成功")
        
        # 测试核心模块导入
        from spring_init.cli import cli
        from spring_init.generator import ProjectGenerator
        from spring_init.config import ProjectConfig, TechStack
        from spring_init.interactive import InteractiveConfig
        print("✅ 核心模块导入成功")
        
        return True
    except ImportError as e:
        print(f"❌ 模块导入失败: {e}")
        return False

def test_config_manager():
    """测试配置管理器"""
    print("\n🔧 测试配置管理器...")
    
    try:
        from common.config_manager import ConfigManager
        
        # 创建配置管理器实例
        config_manager = ConfigManager()
        print("✅ 配置管理器创建成功")
        
        # 测试默认配置创建
        default_config = config_manager.create_default_config()
        print(f"✅ 默认配置创建成功: {default_config['name']}")
        
        # 测试配置保存
        config_file = config_manager.save_config(default_config, "test-config")
        print(f"✅ 配置保存成功: {config_file}")
        
        # 测试配置加载
        loaded_config = config_manager.load_config("test-config")
        print(f"✅ 配置加载成功: {loaded_config['name']}")
        
        # 测试配置列表
        configs = config_manager.list_configs()
        print(f"✅ 配置列表获取成功: {len(configs)} 个配置")
        
        # 清理测试配置
        config_manager.delete_config("test-config")
        print("✅ 测试配置清理完成")
        
        return True
    except Exception as e:
        print(f"❌ 配置管理器测试失败: {e}")
        return False

def test_string_utils():
    """测试字符串工具"""
    print("\n📝 测试字符串工具...")
    
    try:
        from common.utils.string_utils import to_camel_case, to_pascal_case
        
        # 测试驼峰命名转换
        test_cases = [
            ("hello_world", "helloWorld", "HelloWorld"),
            ("my_project_name", "myProjectName", "MyProjectName"),
            ("user_service_impl", "userServiceImpl", "UserServiceImpl")
        ]
        
        for snake_case, expected_camel, expected_pascal in test_cases:
            camel_result = to_camel_case(snake_case)
            pascal_result = to_pascal_case(snake_case)
            
            if camel_result == expected_camel and pascal_result == expected_pascal:
                print(f"✅ {snake_case} -> {camel_result} / {pascal_result}")
            else:
                print(f"❌ {snake_case} -> 期望: {expected_camel}/{expected_pascal}, 实际: {camel_result}/{pascal_result}")
                return False
        
        return True
    except Exception as e:
        print(f"❌ 字符串工具测试失败: {e}")
        return False

def test_file_utils():
    """测试文件工具"""
    print("\n📁 测试文件工具...")
    
    try:
        from common.utils.file_utils import ensure_dir, file_exists, write_file, read_file
        
        # 测试目录创建
        test_dir = project_root / "test_temp"
        ensure_dir(str(test_dir))
        
        if test_dir.exists():
            print("✅ 目录创建成功")
        else:
            print("❌ 目录创建失败")
            return False
        
        # 测试文件写入和读取
        test_file = test_dir / "test.txt"
        test_content = "Hello, World!"
        
        write_file(str(test_file), test_content)
        if file_exists(str(test_file)):
            print("✅ 文件写入成功")
        else:
            print("❌ 文件写入失败")
            return False
        
        read_content = read_file(str(test_file))
        if read_content == test_content:
            print("✅ 文件读取成功")
        else:
            print("❌ 文件读取失败")
            return False
        
        # 清理测试文件
        import shutil
        shutil.rmtree(test_dir)
        print("✅ 测试文件清理完成")
        
        return True
    except Exception as e:
        print(f"❌ 文件工具测试失败: {e}")
        return False

def test_project_validator():
    """测试项目验证器"""
    print("\n🔍 测试项目验证器...")
    
    try:
        from common.validators.project_validator import ProjectValidator
        from common.config_manager import ConfigManager
        
        config_manager = ConfigManager()
        
        # 测试有效配置
        valid_config = config_manager.create_default_config()
        is_valid, errors = ProjectValidator.validate_project_config(valid_config)
        
        if is_valid:
            print("✅ 有效配置验证通过")
        else:
            print(f"❌ 有效配置验证失败: {errors}")
            return False
        
        # 测试无效配置
        invalid_config = valid_config.copy()
        invalid_config['name'] = ""  # 空项目名
        invalid_config['package'] = "invalid-package"  # 无效包名
        
        is_valid, errors = ProjectValidator.validate_project_config(invalid_config)
        
        if not is_valid and len(errors) > 0:
            print(f"✅ 无效配置验证正确识别错误: {len(errors)} 个错误")
        else:
            print("❌ 无效配置验证失败")
            return False
        
        return True
    except Exception as e:
        print(f"❌ 项目验证器测试失败: {e}")
        return False

def test_directory_structure():
    """测试目录结构"""
    print("\n📂 测试目录结构...")
    
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
    
    # 检查目录
    for dir_path in required_dirs:
        full_path = project_root / dir_path
        if full_path.exists() and full_path.is_dir():
            print(f"✅ 目录存在: {dir_path}")
        else:
            print(f"❌ 目录缺失: {dir_path}")
            return False
    
    # 检查文件
    for file_path in required_files:
        full_path = project_root / file_path
        if full_path.exists() and full_path.is_file():
            print(f"✅ 文件存在: {file_path}")
        else:
            print(f"❌ 文件缺失: {file_path}")
            return False
    
    return True

def main():
    """主测试函数"""
    print("🚀 开始测试新的项目结构...\n")
    
    tests = [
        ("目录结构", test_directory_structure),
        ("模块导入", test_imports),
        ("字符串工具", test_string_utils),
        ("文件工具", test_file_utils),
        ("配置管理器", test_config_manager),
        ("项目验证器", test_project_validator)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{'='*50}")
        print(f"测试: {test_name}")
        print(f"{'='*50}")
        
        try:
            if test_func():
                print(f"\n🎉 {test_name} 测试通过")
                passed += 1
            else:
                print(f"\n💥 {test_name} 测试失败")
        except Exception as e:
            print(f"\n💥 {test_name} 测试异常: {e}")
    
    print(f"\n{'='*60}")
    print(f"测试结果: {passed}/{total} 通过")
    print(f"{'='*60}")
    
    if passed == total:
        print("\n🎊 所有测试通过！新的项目结构工作正常。")
        return True
    else:
        print(f"\n⚠️  有 {total - passed} 个测试失败，请检查相关问题。")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)