#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试用例 - 配置收集器测试
"""

import unittest
import json
from unittest.mock import patch, MagicMock
from pathlib import Path
import sys

# 添加项目路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from scripts.core.config_collector import ConfigCollector


class TestConfigCollector(unittest.TestCase):
    """配置收集器测试类"""
    
    def setUp(self):
        """测试初始化"""
        self.collector = ConfigCollector()
    
    def test_init(self):
        """测试初始化"""
        self.assertIsInstance(self.collector.config, dict)
        self.assertIsInstance(self.collector.jdk_versions, list)
        self.assertIn("17", self.collector.jdk_versions)
        self.assertIn("Maven", self.collector.build_tools)
    
    @patch('scripts.core.config_collector.Prompt.ask')
    @patch('scripts.core.config_collector.Confirm.ask')
    @patch('scripts.core.config_collector.IntPrompt.ask')
    @patch('scripts.core.config_collector.console.print')
    def test_collect_basic_info(self, mock_print, mock_int_prompt, mock_confirm, mock_prompt):
        """测试基本信息收集"""
        # 模拟用户输入
        mock_prompt.side_effect = [
            'test-project',     # project_name
            'com.example.test', # package_name
            '1.0.0',           # version
            'Test project'     # description
        ]
        
        self.collector._collect_basic_info()
        
        self.assertEqual(self.collector.config['project_name'], 'test-project')
        self.assertEqual(self.collector.config['package_name'], 'com.example.test')
        self.assertEqual(self.collector.config['version'], '1.0.0')
        self.assertEqual(self.collector.config['description'], 'Test project')
    
    @patch('scripts.core.config_collector.IntPrompt.ask')
    @patch('scripts.core.config_collector.console.print')
    def test_collect_tech_versions(self, mock_print, mock_int_prompt):
        """测试技术版本收集"""
        # 模拟用户选择
        mock_int_prompt.side_effect = [3, 1, 1]  # JDK 17, Maven, Spring Boot 3.2.0
        
        self.collector._collect_tech_versions()
        
        self.assertEqual(self.collector.config['jdk_version'], '17')
        self.assertEqual(self.collector.config['build_tool'], 'Maven')
        self.assertEqual(self.collector.config['spring_boot_version'], '3.2.0')
    
    @patch('scripts.core.config_collector.Confirm.ask')
    @patch('scripts.core.config_collector.Prompt.ask')
    @patch('scripts.core.config_collector.console.print')
    def test_collect_project_structure_single_module(self, mock_print, mock_prompt, mock_confirm):
        """测试单模块项目结构收集"""
        mock_confirm.return_value = False  # 选择单模块
        
        self.collector._collect_project_structure()
        
        self.assertEqual(self.collector.config['is_multi_module'], False)
        self.assertEqual(self.collector.config['modules'], [])
    
    @patch('scripts.core.config_collector.Confirm.ask')
    @patch('scripts.core.config_collector.Prompt.ask')  
    @patch('scripts.core.config_collector.console.print')
    def test_collect_project_structure_multi_module(self, mock_print, mock_prompt, mock_confirm):
        """测试多模块项目结构收集"""
        mock_confirm.return_value = True  # 选择多模块
        mock_prompt.side_effect = [
            'core',           # 第一个模块名
            'Core module',    # 第一个模块描述
            'web',            # 第二个模块名
            'Web module',     # 第二个模块描述
            ''                # 结束输入
        ]
        
        self.collector._collect_project_structure()
        
        self.assertEqual(self.collector.config['is_multi_module'], True)
        self.assertEqual(len(self.collector.config['modules']), 2)
        self.assertEqual(self.collector.config['modules'][0]['name'], 'core')
        self.assertEqual(self.collector.config['modules'][1]['name'], 'web')
    
    @patch('scripts.core.config_collector.IntPrompt.ask')
    @patch('scripts.core.config_collector.Confirm.ask') 
    @patch('scripts.core.config_collector.console.print')
    def test_collect_tech_stack(self, mock_print, mock_confirm, mock_int_prompt):
        """测试技术栈收集"""
        # 模拟用户选择
        mock_int_prompt.side_effect = [1, 1, 1, 4]  # MySQL, MyBatis, Redis, 无消息队列
        mock_confirm.side_effect = [True, False, True]  # Swagger=True, Security=False, Actuator=True
        
        self.collector._collect_tech_stack()
        
        self.assertEqual(self.collector.config['database'], 'MySQL')
        self.assertEqual(self.collector.config['orm_framework'], 'MyBatis')
        self.assertEqual(self.collector.config['cache'], 'Redis')
        self.assertEqual(self.collector.config['message_queue'], '无消息队列')
        self.assertEqual(self.collector.config['include_swagger'], True)
        self.assertEqual(self.collector.config['include_security'], False)
        self.assertEqual(self.collector.config['include_actuator'], True)
    
    @patch('scripts.core.config_collector.Confirm.ask')
    @patch('scripts.core.config_collector.console.print')
    def test_collect_generation_options(self, mock_print, mock_confirm):
        """测试生成选项收集"""
        mock_confirm.side_effect = [True, True, True, True]  # 全部选择True
        
        self.collector._collect_generation_options()
        
        self.assertEqual(self.collector.config['generate_sample_code'], True)
        self.assertEqual(self.collector.config['generate_tests'], True)
        self.assertEqual(self.collector.config['generate_docker'], True)
        self.assertEqual(self.collector.config['generate_readme'], True)
        self.assertIn('created_at', self.collector.config)


class TestConfigCollectorValidation(unittest.TestCase):
    """配置收集器验证功能测试"""
    
    def setUp(self):
        """测试初始化"""
        self.collector = ConfigCollector()
        # 设置一个有效的基础配置
        self.collector.config = {
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
    
    @patch('scripts.core.config_collector.console.print')
    def test_validation_integration(self, mock_print):
        """测试验证集成功能"""
        # 设置不兼容的配置
        self.collector.config['jdk_version'] = '8'  # 与Spring Boot 3.2.0不兼容
        
        errors = self.collector.validator.validate_config(self.collector.config)
        self.assertTrue(len(errors) > 0)
        
        # 测试自动修复
        fixed_config = self.collector.validator.suggest_fixes(self.collector.config, errors)
        self.assertNotEqual(fixed_config['jdk_version'], '8')


if __name__ == '__main__':
    unittest.main()