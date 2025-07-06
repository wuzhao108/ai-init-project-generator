#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
工具函数模块
提供项目生成过程中需要的各种工具函数
"""

import re
from datetime import datetime
from typing import List, Dict, Any


def validate_project_name(name: str) -> bool:
    """验证项目名称格式
    
    Args:
        name: 项目名称
        
    Returns:
        bool: 是否有效
    """
    if not name:
        return False
    
    if len(name) < 2 or len(name) > 50:
        return False
    
    # 项目名称应该是小写字母、数字和连字符的组合
    pattern = r'^[a-z][a-z0-9-]*[a-z0-9]$'
    if not re.match(pattern, name):
        return False
    
    # 不能包含连续的连字符
    if '--' in name:
        return False
    
    return True


def validate_package_name(package: str) -> bool:
    """验证Java包名格式
    
    Args:
        package: 包名
        
    Returns:
        bool: 是否有效
    """
    if not package:
        return False
    
    # Java包名格式：小写字母和数字，用点分隔
    pattern = r'^[a-z][a-z0-9]*(?:\.[a-z][a-z0-9]*)*$'
    if not re.match(pattern, package):
        return False
    
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
            return False
    
    return True


def get_java_package_path(package: str) -> str:
    """将Java包名转换为文件路径
    
    Args:
        package: Java包名，如 com.example.project
        
    Returns:
        str: 文件路径，如 com/example/project
    """
    return package.replace('.', '/')


def project_name_to_class_name(project_name: str) -> str:
    """将项目名转换为Java类名
    
    Args:
        project_name: 项目名，如 my-spring-boot-project
        
    Returns:
        str: Java类名，如 MySpringBootProject
    """
    # 将连字符和下划线替换为空格，然后转换为驼峰命名
    words = project_name.replace('-', ' ').replace('_', ' ').split()
    return ''.join(word.capitalize() for word in words)


def to_snake_case(text: str) -> str:
    """转换为蛇形命名法
    
    Args:
        text: 输入文本
        
    Returns:
        str: 蛇形命名的文本
    """
    # 在大写字母前插入下划线
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    # 在小写字母和大写字母之间插入下划线
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def get_current_date() -> str:
    """获取当前日期
    
    Returns:
        str: 当前日期，格式为 YYYY-MM-DD
    """
    return datetime.now().strftime('%Y-%m-%d')


def get_current_datetime() -> str:
    """获取当前日期时间
    
    Returns:
        str: 当前日期时间，格式为 YYYY-MM-DD HH:MM:SS
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def format_dependencies_xml(dependencies: List[Dict[str, Any]]) -> str:
    """格式化Maven依赖为XML
    
    Args:
        dependencies: 依赖列表
        
    Returns:
        str: 格式化的XML字符串
    """
    if not dependencies:
        return ''
    
    xml_lines = []
    for dep in dependencies:
        xml_lines.append('        <dependency>')
        xml_lines.append(f'            <groupId>{dep["groupId"]}</groupId>')
        xml_lines.append(f'            <artifactId>{dep["artifactId"]}</artifactId>')
        
        if dep.get('version'):
            xml_lines.append(f'            <version>{dep["version"]}</version>')
        
        if dep.get('scope'):
            xml_lines.append(f'            <scope>{dep["scope"]}</scope>')
        
        xml_lines.append('        </dependency>')
    
    return '\n'.join(xml_lines)