# -*- coding: utf-8 -*-
"""
项目验证器模块
提供项目配置的验证功能
"""

import re
import os
from typing import List, Dict, Any, Optional, Tuple
from pathlib import Path


class ProjectValidator:
    """项目配置验证器"""
    
    @staticmethod
    def validate_project_name(name: str) -> Tuple[bool, Optional[str]]:
        """验证项目名称格式
        
        Args:
            name: 项目名称
            
        Returns:
            Tuple[bool, Optional[str]]: (是否有效, 错误信息)
        """
        if not name:
            return False, "项目名称不能为空"
        
        if len(name) < 2:
            return False, "项目名称长度不能少于2个字符"
        
        if len(name) > 50:
            return False, "项目名称长度不能超过50个字符"
        
        # 项目名称应该是小写字母、数字和连字符的组合
        pattern = r'^[a-z][a-z0-9-]*[a-z0-9]$'
        if not re.match(pattern, name):
            return False, "项目名称只能包含小写字母、数字和连字符，且必须以字母开头，以字母或数字结尾"
        
        # 不能包含连续的连字符
        if '--' in name:
            return False, "项目名称不能包含连续的连字符"
        
        return True, None
    
    @staticmethod
    def validate_package_name(package: str) -> Tuple[bool, Optional[str]]:
        """验证Java包名格式
        
        Args:
            package: 包名
            
        Returns:
            Tuple[bool, Optional[str]]: (是否有效, 错误信息)
        """
        if not package:
            return False, "包名不能为空"
        
        # Java包名格式：小写字母和数字，用点分隔
        pattern = r'^[a-z][a-z0-9]*(?:\.[a-z][a-z0-9]*)*$'
        if not re.match(pattern, package):
            return False, "包名格式不正确，应为小写字母和数字的组合，用点分隔，如：com.example.project"
        
        # 检查Java关键字
        java_keywords = {
            'abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch',
            'char', 'class', 'const', 'continue', 'default', 'do', 'double',
            'else', 'enum', 'extends', 'final', 'finally', 'float', 'for',
            'goto', 'if', 'implements', 'import', 'instanceof', 'int',
            'interface', 'long', 'native', 'new', 'package', 'private',
            'protected', 'public', 'return', 'short', 'static', 'strictfp',
            'super', 'switch', 'synchronized', 'this', 'throw', 'throws',
            'transient', 'try', 'void', 'volatile', 'while'
        }
        
        parts = package.split('.')
        for part in parts:
            if part in java_keywords:
                return False, f"包名不能包含Java关键字：{part}"
        
        return True, None
    
    @staticmethod
    def validate_version(version: str) -> Tuple[bool, Optional[str]]:
        """验证版本号格式
        
        Args:
            version: 版本号
            
        Returns:
            Tuple[bool, Optional[str]]: (是否有效, 错误信息)
        """
        if not version:
            return False, "版本号不能为空"
        
        # 支持语义化版本号格式：x.y.z 或 x.y.z-SNAPSHOT
        pattern = r'^\d+\.\d+\.\d+(?:-[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*)?$'
        if not re.match(pattern, version):
            return False, "版本号格式不正确，应为语义化版本号格式，如：1.0.0 或 1.0.0-SNAPSHOT"
        
        return True, None
    
    @staticmethod
    def validate_java_version(version: str) -> Tuple[bool, Optional[str]]:
        """验证Java版本
        
        Args:
            version: Java版本
            
        Returns:
            tuple[bool, Optional[str]]: (是否有效, 错误信息)
        """
        valid_versions = ['8', '11', '17', '21']
        if version not in valid_versions:
            return False, f"不支持的Java版本：{version}，支持的版本：{', '.join(valid_versions)}"
        
        return True, None
    
    @staticmethod
    def validate_spring_boot_version(version: str) -> Tuple[bool, Optional[str]]:
        """验证Spring Boot版本
        
        Args:
            version: Spring Boot版本
            
        Returns:
            tuple[bool, Optional[str]]: (是否有效, 错误信息)
        """
        valid_versions = ['2.7.18', '3.0.13', '3.1.8', '3.2.2', '3.3.0']
        if version not in valid_versions:
            return False, f"不支持的Spring Boot版本：{version}，支持的版本：{', '.join(valid_versions)}"
        
        return True, None
    
    @staticmethod
    def validate_output_directory(path: str) -> Tuple[bool, Optional[str]]:
        """验证输出目录
        
        Args:
            path: 输出目录路径
            
        Returns:
            tuple[bool, Optional[str]]: (是否有效, 错误信息)
        """
        if not path:
            return False, "输出目录不能为空"
        
        try:
            # 检查路径是否有效
            Path(path).resolve()
        except (OSError, ValueError) as e:
            return False, f"输出目录路径无效：{str(e)}"
        
        # 检查父目录是否存在
        parent_dir = os.path.dirname(path)
        if parent_dir and not os.path.exists(parent_dir):
            return False, f"输出目录的父目录不存在：{parent_dir}"
        
        # 检查是否有写权限
        if os.path.exists(path):
            if not os.access(path, os.W_OK):
                return False, f"没有输出目录的写权限：{path}"
        else:
            # 检查父目录的写权限
            if parent_dir and not os.access(parent_dir, os.W_OK):
                return False, f"没有创建输出目录的权限：{parent_dir}"
        
        return True, None
    
    @staticmethod
    def validate_tech_stack(tech_stack: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """验证技术栈配置
        
        Args:
            tech_stack: 技术栈配置
            
        Returns:
            Tuple[bool, List[str]]: (是否有效, 错误信息列表)
        """
        errors = []
        
        # 验证数据库类型
        valid_databases = ['mysql', 'postgresql', 'h2']
        database = tech_stack.get('database')
        if database and database not in valid_databases:
            errors.append(f"不支持的数据库类型：{database}，支持的类型：{', '.join(valid_databases)}")
        
        # 验证ORM框架
        valid_orms = ['mybatis', 'jpa']
        orm = tech_stack.get('orm')
        if orm and orm not in valid_orms:
            errors.append(f"不支持的ORM框架：{orm}，支持的框架：{', '.join(valid_orms)}")
        
        # 验证缓存类型
        valid_caches = ['redis', 'caffeine']
        cache = tech_stack.get('cache', [])
        if isinstance(cache, list):
            for c in cache:
                if c not in valid_caches:
                    errors.append(f"不支持的缓存类型：{c}，支持的类型：{', '.join(valid_caches)}")
        
        # 验证消息队列
        valid_mqs = ['rabbitmq', 'kafka']
        mq = tech_stack.get('mq', [])
        if isinstance(mq, list):
            for m in mq:
                if m not in valid_mqs:
                    errors.append(f"不支持的消息队列：{m}，支持的类型：{', '.join(valid_mqs)}")
        
        # 验证NoSQL数据库
        valid_nosqls = ['mongodb', 'elasticsearch']
        nosql = tech_stack.get('nosql', [])
        if isinstance(nosql, list):
            for n in nosql:
                if n not in valid_nosqls:
                    errors.append(f"不支持的NoSQL数据库：{n}，支持的类型：{', '.join(valid_nosqls)}")
        
        return len(errors) == 0, errors
    
    @staticmethod
    def validate_project_config(config: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """验证完整的项目配置
        
        Args:
            config: 项目配置
            
        Returns:
            tuple[bool, List[str]]: (是否有效, 错误信息列表)
        """
        errors = []
        
        # 验证项目名称
        name = config.get('name')
        is_valid, error = ProjectValidator.validate_project_name(name)
        if not is_valid:
            errors.append(f"项目名称验证失败：{error}")
        
        # 验证包名
        package = config.get('package')
        is_valid, error = ProjectValidator.validate_package_name(package)
        if not is_valid:
            errors.append(f"包名验证失败：{error}")
        
        # 验证版本号
        version = config.get('version')
        is_valid, error = ProjectValidator.validate_version(version)
        if not is_valid:
            errors.append(f"版本号验证失败：{error}")
        
        # 验证Java版本
        java_version = config.get('java_version')
        if java_version:
            is_valid, error = ProjectValidator.validate_java_version(java_version)
            if not is_valid:
                errors.append(f"Java版本验证失败：{error}")
        
        # 验证Spring Boot版本
        spring_boot_version = config.get('spring_boot_version')
        if spring_boot_version:
            is_valid, error = ProjectValidator.validate_spring_boot_version(spring_boot_version)
            if not is_valid:
                errors.append(f"Spring Boot版本验证失败：{error}")
        
        # 验证技术栈
        tech_stack = config.get('tech_stack', {})
        is_valid, tech_errors = ProjectValidator.validate_tech_stack(tech_stack)
        if not is_valid:
            errors.extend(tech_errors)
        
        return len(errors) == 0, errors