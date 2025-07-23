#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试用例 - 配置验证器测试
"""

import unittest
import json
from unittest.mock import patch, MagicMock
from pathlib import Path
import sys

# 添加项目路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from scripts.validators.config_validator import ConfigValidator


class TestConfigValidator(unittest.TestCase):
    """配置验证器测试类"""
    
    def setUp(self):
        """测试初始化"""
        self.validator = ConfigValidator()
        self.valid_config = {
            'project_name': 'test-project',
            'package_name': 'com.example.test',
            'version': '1.0.0',
            'description': 'Test project',
            'jdk_version': '17',
            'build_tool': 'Maven',
            'spring_boot_version': '3.2.0',
            'database': 'MySQL',
            'orm_framework': 'MyBatis',
            'cache': 'Redis',
            'message_queue': '无消息队列',
            'include_swagger': True,
            'include_security': False,
            'include_actuator': True,
            'generate_sample_code': True,
            'generate_tests': True,
            'generate_docker': True,
            'generate_readme': True,
            'is_multi_module': False,
            'modules': []
        }
    
    def test_validate_valid_config(self):
        """测试有效配置验证"""
        errors = self.validator.validate_config(self.valid_config)
        self.assertEqual(len(errors), 0, "有效配置不应产生验证错误")
    
    def test_validate_project_name_format(self):
        """测试项目名称格式验证"""
        # 测试无效的项目名称
        invalid_names = ['123project', 'project name', 'project@name', '']
        
        for invalid_name in invalid_names:
            with self.subTest(name=invalid_name):
                config = self.valid_config.copy()
                config['project_name'] = invalid_name
                errors = self.validator.validate_config(config)
                self.assertTrue(any('项目名称' in error for error in errors))
    
    def test_validate_package_name_format(self):
        """测试包名格式验证"""
        # 测试无效的包名
        invalid_packages = ['Com.example', 'com.Example', '123.example', 'com..example']
        
        for invalid_package in invalid_packages:
            with self.subTest(package=invalid_package):
                config = self.valid_config.copy()
                config['package_name'] = invalid_package
                errors = self.validator.validate_config(config)
                self.assertTrue(any('包名' in error for error in errors))
    
    def test_validate_spring_jdk_compatibility(self):
        """测试Spring Boot与JDK版本兼容性"""
        # 测试不兼容的版本组合
        incompatible_combinations = [
            ('3.2.0', '8'),   # Spring Boot 3.x 不支持 JDK 8
            ('3.1.6', '11'),  # Spring Boot 3.x 不支持 JDK 11
        ]
        
        for spring_version, jdk_version in incompatible_combinations:
            with self.subTest(spring=spring_version, jdk=jdk_version):
                config = self.valid_config.copy()
                config['spring_boot_version'] = spring_version
                config['jdk_version'] = jdk_version
                errors = self.validator.validate_config(config)
                self.assertTrue(any('不兼容' in error for error in errors))
    
    def test_validate_database_orm_compatibility(self):
        """测试数据库与ORM框架兼容性"""
        # 测试不匹配的组合
        config = self.valid_config.copy()
        config['database'] = '无数据库'
        config['orm_framework'] = 'MyBatis'
        
        errors = self.validator.validate_config(config)
        self.assertTrue(any('配置不匹配' in error for error in errors))
    
    def test_validate_multi_module_config(self):
        """测试多模块项目配置验证"""
        config = self.valid_config.copy()
        config['is_multi_module'] = True
        config['modules'] = []  # 空模块列表
        
        errors = self.validator.validate_config(config)
        self.assertTrue(any('至少一个模块' in error for error in errors))
    
    def test_suggest_fixes(self):
        """测试自动修复功能"""
        config = self.valid_config.copy()
        config['spring_boot_version'] = '3.2.0'
        config['jdk_version'] = '8'  # 不兼容版本
        
        errors = self.validator.validate_config(config)
        self.assertTrue(len(errors) > 0)
        
        # 测试自动修复
        with patch('builtins.print'):  # 模拟console.print
            fixed_config = self.validator.suggest_fixes(config, errors)
            self.assertNotEqual(fixed_config['jdk_version'], '8')
            self.assertIn(fixed_config['jdk_version'], ['17', '21'])
    
    def test_missing_required_fields(self):
        """测试必需字段缺失验证"""
        config = self.valid_config.copy()
        del config['project_name']  # 删除必需字段
        
        errors = self.validator.validate_config(config)
        self.assertTrue(any('缺少必需字段' in error for error in errors))
    
    def test_empty_fields(self):
        """测试空字段验证"""
        config = self.valid_config.copy()
        config['project_name'] = ''  # 空字段
        
        errors = self.validator.validate_config(config)
        self.assertTrue(any('不能为空' in error for error in errors))


if __name__ == '__main__':
    unittest.main()