#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试用例 - 上下文生成器测试
"""

import unittest
import json
import tempfile
import shutil
from unittest.mock import patch, MagicMock
from pathlib import Path
import sys

# 添加项目路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from scripts.core.context_generator import ContextGenerator


class TestContextGenerator(unittest.TestCase):
    """上下文生成器测试类"""
    
    def setUp(self):
        """测试初始化"""
        # 创建临时目录用于测试
        self.temp_dir = tempfile.mkdtemp()
        self.generator = ContextGenerator()
        
        # 重写输出目录为临时目录
        self.generator.output_base_dir = Path(self.temp_dir) / "output"
        self.generator.templates_dir = Path(self.temp_dir) / "templates"
        
        # 创建目录
        self.generator.output_base_dir.mkdir(parents=True, exist_ok=True)
        self.generator.templates_dir.mkdir(parents=True, exist_ok=True)
        
        # 测试配置
        self.test_config = {
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
    
    def tearDown(self):
        """测试清理"""
        # 删除临时目录
        shutil.rmtree(self.temp_dir)
    
    def test_init(self):
        """测试初始化"""
        generator = ContextGenerator()
        self.assertTrue(generator.output_base_dir.exists())
        self.assertTrue(generator.templates_dir.exists())
    
    @patch('scripts.core.context_generator.console.print')
    def test_save_config(self, mock_print):
        """测试配置保存"""
        output_dir = self.generator.output_base_dir / "test"
        output_dir.mkdir(exist_ok=True)
        
        self.generator._save_config(self.test_config, output_dir)
        
        config_file = output_dir / "config.json"
        self.assertTrue(config_file.exists())
        
        # 验证配置内容
        with open(config_file, 'r', encoding='utf-8') as f:
            saved_config = json.load(f)
            self.assertEqual(saved_config['project_name'], 'test-project')
    
    def test_build_system_prompt(self):
        """测试系统提示词生成"""
        prompt = self.generator._build_system_prompt(self.test_config)
        
        self.assertIn('Java项目生成系统提示词', prompt)
        self.assertIn('test-project', prompt)
        self.assertIn('com.example.test', prompt)
        self.assertIn('Maven', prompt)
        self.assertIn('MySQL', prompt)
    
    def test_build_user_prompt(self):
        """测试用户提示词生成"""
        prompt = self.generator._build_user_prompt(self.test_config)
        
        self.assertIn('Java项目生成用户需求', prompt)
        self.assertIn('test-project', prompt)
        self.assertIn('重要说明', prompt)
    
    def test_format_modules_single_module(self):
        """测试单模块格式化"""
        result = self.generator._format_modules(self.test_config)
        self.assertEqual(result, "")
    
    def test_format_modules_multi_module(self):
        """测试多模块格式化"""
        config = self.test_config.copy()
        config['is_multi_module'] = True
        config['modules'] = [
            {'name': 'core', 'description': 'Core module'},
            {'name': 'web', 'description': 'Web module'}
        ]
        
        result = self.generator._format_modules(config)
        self.assertIn('模块配置', result)
        self.assertIn('core', result)
        self.assertIn('web', result)
    
    def test_format_tech_stack_integration(self):
        """测试技术栈集成格式化"""
        result = self.generator._format_tech_stack_integration(self.test_config)
        
        self.assertIn('MySQL', result)
        self.assertIn('MyBatis', result)
        self.assertIn('Redis', result)
        self.assertNotIn('无消息队列', result)  # 应该被过滤掉
    
    def test_build_gemini_commands(self):
        """测试Gemini命令生成"""
        commands = self.generator._build_gemini_commands(self.test_config)
        
        self.assertIn('Gemini CLI', commands)
        self.assertIn('/system', commands)
        self.assertIn('/user', commands)
        self.assertIn('test-project', commands)
    
    def test_build_readme(self):
        """测试README生成"""
        readme = self.generator._build_readme(self.test_config)
        
        self.assertIn('test-project', readme)
        self.assertIn('项目配置概览', readme)
        self.assertIn('使用方法', readme)
        self.assertIn('Maven', readme)
        self.assertIn('MySQL', readme)
    
    @patch('scripts.core.context_generator.console.print')
    def test_generate_full_context(self, mock_print):
        """测试完整上下文工程生成"""
        output_path = self.generator.generate(self.test_config)
        
        self.assertIsNotNone(output_path)
        output_dir = Path(output_path)
        self.assertTrue(output_dir.exists())
        
        # 验证生成的文件
        expected_files = [
            'config.json',
            'system_prompt.md',
            'user_prompt.md',
            'project_generator.gemini',
            'project_generator.claude',
            'execution_plan.md',
            'project_structure.md',
            'README.md'
        ]
        
        for file_name in expected_files:
            file_path = output_dir / file_name
            self.assertTrue(file_path.exists(), f"文件 {file_name} 应该存在")
            self.assertTrue(file_path.stat().st_size > 0, f"文件 {file_name} 不应该为空")


class TestContextGeneratorTemplateEngine(unittest.TestCase):
    """上下文生成器模板引擎测试"""
    
    def setUp(self):
        """测试初始化"""
        self.temp_dir = tempfile.mkdtemp()
        self.generator = ContextGenerator()
        
        # 重写模板目录
        self.generator.templates_dir = Path(self.temp_dir) / "templates"
        self.generator.templates_dir.mkdir(parents=True, exist_ok=True)
        
        # 创建模板文件
        template_content = """# {{project_name}} 系统提示词

项目名称: {{project_name}}
包名: {{package_name}}
JDK版本: {{jdk_version}}

{% if is_multi_module %}
这是多模块项目
{% else %}
这是单模块项目
{% endif %}
"""
        template_file = self.generator.templates_dir / "system_prompt_template.md"
        with open(template_file, 'w', encoding='utf-8') as f:
            f.write(template_content)
        
        # 重新初始化Jinja环境
        if hasattr(self.generator, 'jinja_env') and self.generator.jinja_env:
            from jinja2 import Environment, FileSystemLoader
            self.generator.jinja_env = Environment(
                loader=FileSystemLoader(str(self.generator.templates_dir)),
                trim_blocks=True,
                lstrip_blocks=True
            )
        
        self.test_config = {
            'project_name': 'test-project',
            'package_name': 'com.example.test',
            'jdk_version': '17',
            'is_multi_module': False
        }
    
    def tearDown(self):
        """测试清理"""
        shutil.rmtree(self.temp_dir)
    
    def test_template_rendering(self):
        """测试模板渲染"""
        if not hasattr(self.generator, 'jinja_env') or not self.generator.jinja_env:
            self.skipTest("Jinja2不可用，跳过模板测试")
        
        prompt = self.generator._build_system_prompt(self.test_config)
        
        self.assertIn('test-project 系统提示词', prompt)
        self.assertIn('com.example.test', prompt)
        self.assertIn('17', prompt)
        self.assertIn('单模块项目', prompt)


if __name__ == '__main__':
    unittest.main()