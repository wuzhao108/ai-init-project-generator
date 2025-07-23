#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置验证器 - 验证用户配置的有效性和兼容性

提供配置验证功能，包括：
- 项目名称和包名格式验证
- 技术栈版本兼容性验证
- 配置完整性验证
"""

import re
from typing import Dict, List, Any
from rich.console import Console

console = Console()


class ConfigValidator:
    """配置验证器类"""
    
    def __init__(self):
        # Spring Boot和JDK版本兼容性映射
        self.spring_jdk_compatibility = {
            "3.2.0": ["17", "21"],
            "3.1.6": ["17", "21"], 
            "3.0.13": ["17", "21"],
            "2.7.18": ["8", "11", "17", "21"]
        }
        
        # 数据库和ORM框架兼容性
        self.db_orm_compatibility = {
            "MySQL": ["MyBatis", "JPA/Hibernate", "MyBatis-Plus"],
            "PostgreSQL": ["MyBatis", "JPA/Hibernate", "MyBatis-Plus"],
            "H2": ["MyBatis", "JPA/Hibernate", "MyBatis-Plus"],
            "Oracle": ["MyBatis", "JPA/Hibernate", "MyBatis-Plus"],
            "SQL Server": ["MyBatis", "JPA/Hibernate", "MyBatis-Plus"],
            "无数据库": ["无ORM"]
        }
    
    def validate_config(self, config: Dict[str, Any]) -> List[str]:
        """
        验证配置的完整性和有效性
        
        Args:
            config: 用户配置字典
            
        Returns:
            List[str]: 验证错误列表，空列表表示验证通过
        """
        errors = []
        
        try:
            # 验证必需字段
            errors.extend(self._validate_required_fields(config))
            
            # 验证项目基本信息格式
            errors.extend(self._validate_project_info(config))
            
            # 验证技术栈兼容性
            errors.extend(self._validate_tech_compatibility(config))
            
            # 验证多模块配置
            if config.get('is_multi_module', False):
                errors.extend(self._validate_multi_module_config(config))
                
        except Exception as e:
            errors.append(f"配置验证过程中发生错误: {str(e)}")
        
        return errors
    
    def _validate_required_fields(self, config: Dict[str, Any]) -> List[str]:
        """验证必需字段是否存在"""
        errors = []
        required_fields = [
            'project_name', 'package_name', 'version', 'description',
            'jdk_version', 'build_tool', 'spring_boot_version',
            'database', 'orm_framework', 'cache', 'message_queue'
        ]
        
        for field in required_fields:
            if field not in config:
                errors.append(f"缺少必需字段: {field}")
            elif not config[field] or str(config[field]).strip() == '':
                errors.append(f"字段 {field} 不能为空")
        
        return errors
    
    def _validate_project_info(self, config: Dict[str, Any]) -> List[str]:
        """验证项目基本信息格式"""
        errors = []
        
        # 验证项目名称格式
        project_name = config.get('project_name', '')
        if project_name:
            if not re.match(r'^[a-zA-Z][a-zA-Z0-9-]*$', project_name):
                errors.append("项目名称格式不正确，应以字母开头，只能包含字母、数字和连字符")
            elif len(project_name) > 50:
                errors.append("项目名称长度不能超过50个字符")
        
        # 验证包名格式
        package_name = config.get('package_name', '')
        if package_name:
            if not re.match(r'^[a-z][a-z0-9]*(\.[a-z][a-z0-9]*)*$', package_name):
                errors.append("包名格式不正确，应为小写字母开头的标准Java包名格式")
            elif len(package_name) > 100:
                errors.append("包名长度不能超过100个字符")
        
        # 验证版本号格式
        version = config.get('version', '')
        if version:
            if not re.match(r'^\d+\.\d+\.\d+(-[a-zA-Z0-9]+)?$', version):
                errors.append("版本号格式不正确，应为 x.y.z 或 x.y.z-qualifier 格式")
        
        return errors
    
    def _validate_tech_compatibility(self, config: Dict[str, Any]) -> List[str]:
        """验证技术栈兼容性"""
        errors = []
        
        # 验证Spring Boot与JDK版本兼容性
        spring_version = config.get('spring_boot_version', '')
        jdk_version = config.get('jdk_version', '')
        
        if spring_version and jdk_version:
            compatible_jdks = self.spring_jdk_compatibility.get(spring_version, [])
            if compatible_jdks and jdk_version not in compatible_jdks:
                errors.append(f"Spring Boot {spring_version} 与 JDK {jdk_version} 不兼容，"
                            f"支持的JDK版本: {', '.join(compatible_jdks)}")
        
        # 验证数据库与ORM框架兼容性
        database = config.get('database', '')
        orm_framework = config.get('orm_framework', '')
        
        if database and orm_framework:
            compatible_orms = self.db_orm_compatibility.get(database, [])
            if compatible_orms and orm_framework not in compatible_orms:
                errors.append(f"数据库 {database} 与 ORM框架 {orm_framework} 配置不匹配，"
                            f"支持的ORM框架: {', '.join(compatible_orms)}")
        
        # 验证缓存配置合理性
        cache = config.get('cache', '')
        if cache == 'Redis' and config.get('generate_docker', False):
            # 如果使用Redis且生成Docker配置，这是合理的组合
            pass
        elif cache == 'Redis':
            console.print("[yellow]⚠️  使用Redis缓存建议同时启用Docker配置以便本地开发[/yellow]")
        
        return errors
    
    def _validate_multi_module_config(self, config: Dict[str, Any]) -> List[str]:
        """验证多模块项目配置"""
        errors = []
        
        modules = config.get('modules', [])
        if not modules:
            errors.append("多模块项目必须定义至少一个模块")
            return errors
        
        module_names = set()
        for i, module in enumerate(modules):
            if not isinstance(module, dict):
                errors.append(f"模块配置 {i+1} 格式不正确，应为字典类型")
                continue
            
            # 验证模块必需字段
            if 'name' not in module:
                errors.append(f"模块 {i+1} 缺少name字段")
            else:
                module_name = module['name']
                if module_name in module_names:
                    errors.append(f"模块名称重复: {module_name}")
                module_names.add(module_name)
                
                # 验证模块名称格式
                if not re.match(r'^[a-zA-Z][a-zA-Z0-9-]*$', module_name):
                    errors.append(f"模块名称 {module_name} 格式不正确")
            
            if 'description' not in module:
                errors.append(f"模块 {module.get('name', i+1)} 缺少description字段")
        
        return errors
    
    def suggest_fixes(self, config: Dict[str, Any], errors: List[str]) -> Dict[str, Any]:
        """
        根据验证错误提供修复建议并自动修复部分问题
        
        Args:
            config: 原始配置
            errors: 验证错误列表
            
        Returns:
            Dict[str, Any]: 修复后的配置
        """
        fixed_config = config.copy()
        
        # 自动修复Spring Boot与JDK版本兼容性问题
        spring_version = config.get('spring_boot_version', '')
        jdk_version = config.get('jdk_version', '')
        
        if spring_version and jdk_version:
            compatible_jdks = self.spring_jdk_compatibility.get(spring_version, [])
            if compatible_jdks and jdk_version not in compatible_jdks:
                # 选择最新的兼容JDK版本
                recommended_jdk = max(compatible_jdks, key=int)
                fixed_config['jdk_version'] = recommended_jdk
                console.print(f"[yellow]🔧 自动修复: JDK版本已从 {jdk_version} 调整为 {recommended_jdk}[/yellow]")
        
        # 自动修复数据库与ORM框架兼容性问题
        database = config.get('database', '')
        orm_framework = config.get('orm_framework', '')
        
        if database == '无数据库' and orm_framework != '无ORM':
            fixed_config['orm_framework'] = '无ORM'
            console.print(f"[yellow]🔧 自动修复: 无数据库时ORM框架已调整为'无ORM'[/yellow]")
        
        return fixed_config
    
    def print_validation_summary(self, errors: List[str]) -> bool:
        """
        打印验证结果摘要
        
        Args:
            errors: 验证错误列表
            
        Returns:
            bool: True表示验证通过，False表示有错误
        """
        if not errors:
            console.print("[green]✅ 配置验证通过[/green]")
            return True
        else:
            console.print(f"[red]❌ 发现 {len(errors)} 个配置错误:[/red]")
            for i, error in enumerate(errors, 1):
                console.print(f"  {i}. {error}")
            return False