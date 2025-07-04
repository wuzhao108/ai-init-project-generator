#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
工具函数模块
提供各种辅助功能如验证、字符串处理等
"""

import re
import os
from pathlib import Path
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
    
    # 项目名称应该是小写字母、数字和连字符的组合
    pattern = r'^[a-z][a-z0-9-]*[a-z0-9]$'
    return bool(re.match(pattern, name)) and len(name) >= 2


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
    return bool(re.match(pattern, package))


def to_camel_case(snake_str: str) -> str:
    """将下划线命名转换为驼峰命名
    
    Args:
        snake_str: 下划线命名的字符串
        
    Returns:
        str: 驼峰命名的字符串
    """
    components = snake_str.split('_')
    return components[0] + ''.join(word.capitalize() for word in components[1:])


def to_pascal_case(snake_str: str) -> str:
    """将下划线命名转换为帕斯卡命名（首字母大写的驼峰命名）
    
    Args:
        snake_str: 下划线命名的字符串
        
    Returns:
        str: 帕斯卡命名的字符串
    """
    components = snake_str.split('_')
    return ''.join(word.capitalize() for word in components)


def to_snake_case(camel_str: str) -> str:
    """将驼峰命名转换为下划线命名
    
    Args:
        camel_str: 驼峰命名的字符串
        
    Returns:
        str: 下划线命名的字符串
    """
    # 在大写字母前插入下划线
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def to_kebab_case(snake_str: str) -> str:
    """将下划线命名转换为连字符命名
    
    Args:
        snake_str: 下划线命名的字符串
        
    Returns:
        str: 连字符命名的字符串
    """
    return snake_str.replace('_', '-')


def project_name_to_class_name(project_name: str) -> str:
    """将项目名称转换为Java类名
    
    Args:
        project_name: 项目名称（连字符命名）
        
    Returns:
        str: Java类名（帕斯卡命名）
    """
    # 将连字符替换为下划线，然后转换为帕斯卡命名
    snake_name = project_name.replace('-', '_')
    return to_pascal_case(snake_name)


def ensure_dir(path: str) -> None:
    """确保目录存在，如果不存在则创建
    
    Args:
        path: 目录路径
    """
    Path(path).mkdir(parents=True, exist_ok=True)


def get_java_package_path(package_name: str) -> str:
    """获取Java包的文件系统路径
    
    Args:
        package_name: Java包名
        
    Returns:
        str: 文件系统路径
    """
    return package_name.replace('.', os.sep)


def format_xml_dependency(dependency: Dict[str, Any]) -> str:
    """格式化Maven依赖为XML格式
    
    Args:
        dependency: 依赖信息字典
        
    Returns:
        str: XML格式的依赖
    """
    xml = "        <dependency>\n"
    xml += f"            <groupId>{dependency['groupId']}</groupId>\n"
    xml += f"            <artifactId>{dependency['artifactId']}</artifactId>\n"
    
    if 'version' in dependency and dependency['version']:
        xml += f"            <version>{dependency['version']}</version>\n"
    
    if 'scope' in dependency and dependency['scope']:
        xml += f"            <scope>{dependency['scope']}</scope>\n"
    
    xml += "        </dependency>"
    return xml


def format_dependencies_xml(dependencies: List[Dict[str, Any]]) -> str:
    """格式化多个Maven依赖为XML格式
    
    Args:
        dependencies: 依赖信息列表
        
    Returns:
        str: XML格式的依赖列表
    """
    return "\n".join(format_xml_dependency(dep) for dep in dependencies)


def get_spring_boot_version_properties(version: str) -> Dict[str, str]:
    """获取SpringBoot版本相关的属性
    
    Args:
        version: SpringBoot版本
        
    Returns:
        Dict[str, str]: 版本属性字典
    """
    properties = {
        'spring.boot.version': version,
        'maven.compiler.source': '11',
        'maven.compiler.target': '11',
        'project.build.sourceEncoding': 'UTF-8',
        'project.reporting.outputEncoding': 'UTF-8',
        'java.version': '11'
    }
    
    # 根据SpringBoot版本调整Java版本
    if version.startswith('3.'):
        properties['maven.compiler.source'] = '17'
        properties['maven.compiler.target'] = '17'
        properties['java.version'] = '17'
    
    return properties


def get_file_extension(filename: str) -> str:
    """获取文件扩展名
    
    Args:
        filename: 文件名
        
    Returns:
        str: 文件扩展名（不包含点）
    """
    return Path(filename).suffix.lstrip('.')


def is_text_file(filename: str) -> bool:
    """判断是否为文本文件
    
    Args:
        filename: 文件名
        
    Returns:
        bool: 是否为文本文件
    """
    text_extensions = {
        'java', 'xml', 'yml', 'yaml', 'properties', 'txt', 'md',
        'json', 'sql', 'sh', 'bat', 'cmd', 'gitignore', 'dockerfile'
    }
    
    ext = get_file_extension(filename).lower()
    return ext in text_extensions or not ext  # 无扩展名的文件也当作文本文件


def clean_empty_lines(content: str) -> str:
    """清理多余的空行
    
    Args:
        content: 文件内容
        
    Returns:
        str: 清理后的内容
    """
    # 将多个连续的空行替换为单个空行
    return re.sub(r'\n\s*\n\s*\n', '\n\n', content)


def format_java_imports(imports: List[str]) -> str:
    """格式化Java导入语句
    
    Args:
        imports: 导入语句列表
        
    Returns:
        str: 格式化后的导入语句
    """
    if not imports:
        return ""
    
    # 去重并排序
    unique_imports = sorted(set(imports))
    
    # 分组：java.*, javax.*, org.*, com.*, 其他
    java_imports = []
    javax_imports = []
    org_imports = []
    com_imports = []
    other_imports = []
    
    for imp in unique_imports:
        if imp.startswith('java.'):
            java_imports.append(imp)
        elif imp.startswith('javax.'):
            javax_imports.append(imp)
        elif imp.startswith('org.'):
            org_imports.append(imp)
        elif imp.startswith('com.'):
            com_imports.append(imp)
        else:
            other_imports.append(imp)
    
    # 组合导入语句
    result = []
    for group in [java_imports, javax_imports, org_imports, com_imports, other_imports]:
        if group:
            result.extend([f"import {imp};" for imp in group])
            result.append("")  # 添加空行分隔
    
    # 移除最后的空行
    if result and result[-1] == "":
        result.pop()
    
    return "\n".join(result)


def get_current_year() -> str:
    """获取当前年份
    
    Returns:
        str: 当前年份
    """
    from datetime import datetime
    return str(datetime.now().year)


def get_current_date() -> str:
    """获取当前日期
    
    Returns:
        str: 当前日期（YYYY-MM-DD格式）
    """
    from datetime import datetime
    return datetime.now().strftime('%Y-%m-%d')


def get_current_datetime() -> str:
    """获取当前日期时间
    
    Returns:
        str: 当前日期时间（YYYY-MM-DD HH:MM:SS格式）
    """
    from datetime import datetime
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')