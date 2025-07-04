#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
模板管理器模块
负责管理和组织所有的代码模板文件
"""

import os
from pathlib import Path
from typing import Dict, List, Any


class TemplateManager:
    """模板管理器"""
    
    def __init__(self):
        # 获取模板目录路径
        current_dir = Path(__file__).parent
        self.templates_dir = current_dir / 'templates'
        
        # 确保模板目录存在
        self.templates_dir.mkdir(exist_ok=True)
        
        # 初始化模板结构
        self._init_template_structure()
    
    def _init_template_structure(self) -> None:
        """初始化模板目录结构"""
        template_dirs = [
            'maven',
            'java',
            'java/controller',
            'java/service',
            'java/service/impl',
            'java/mapper',
            'java/repository',
            'java/entity',
            'java/dto',
            'java/common',
            'java/config',
            'mybatis',
            'config',
            'docs',
            'git',
            'docker'
        ]
        
        for dir_name in template_dirs:
            dir_path = self.templates_dir / dir_name
            dir_path.mkdir(parents=True, exist_ok=True)
    
    def get_template_path(self, template_name: str) -> Path:
        """获取模板文件路径
        
        Args:
            template_name: 模板名称
            
        Returns:
            Path: 模板文件路径
        """
        return self.templates_dir / template_name
    
    def template_exists(self, template_name: str) -> bool:
        """检查模板是否存在
        
        Args:
            template_name: 模板名称
            
        Returns:
            bool: 模板是否存在
        """
        return self.get_template_path(template_name).exists()
    
    def list_templates(self) -> List[str]:
        """列出所有可用的模板
        
        Returns:
            List[str]: 模板名称列表
        """
        templates = []
        
        for root, dirs, files in os.walk(self.templates_dir):
            for file in files:
                if file.endswith(('.java', '.xml', '.yml', '.yaml', '.md', '.txt', '.properties')):
                    rel_path = os.path.relpath(os.path.join(root, file), self.templates_dir)
                    templates.append(rel_path.replace(os.sep, '/'))
        
        return sorted(templates)
    
    def get_template_info(self) -> Dict[str, Any]:
        """获取模板信息
        
        Returns:
            Dict[str, Any]: 模板信息字典
        """
        return {
            'templates_dir': str(self.templates_dir),
            'available_templates': self.list_templates(),
            'template_categories': {
                'maven': 'Maven配置文件模板',
                'java': 'Java源代码模板',
                'mybatis': 'MyBatis配置模板',
                'config': '应用配置文件模板',
                'docs': '文档模板',
                'git': 'Git配置模板',
                'docker': 'Docker配置模板'
            }
        }
    
    def create_default_templates(self) -> None:
        """创建默认模板文件"""
        # 这个方法将在后续实现中调用，用于创建所有默认模板
        pass