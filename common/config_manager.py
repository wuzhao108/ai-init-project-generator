# -*- coding: utf-8 -*-
"""
配置管理器模块
负责项目配置的保存、加载和管理
"""

import os
import json
from datetime import datetime
from typing import Dict, Any, Optional, List
from pathlib import Path

from .utils.file_utils import write_json, read_json, ensure_dir, file_exists
from .validators.project_validator import ProjectValidator
from .constants.project_constants import ProjectConstants


class ConfigManager:
    """配置管理器"""
    
    def __init__(self, config_dir: str = None):
        """
        初始化配置管理器
        
        Args:
            config_dir: 配置文件目录，默认为项目根目录下的configs目录
        """
        if config_dir is None:
            # 获取项目根目录
            project_root = Path(__file__).parent.parent
            config_dir = project_root / "configs"
        
        self.config_dir = Path(config_dir)
        ensure_dir(str(self.config_dir))
    
    def save_config(self, config: Dict[str, Any], config_name: str = None) -> str:
        """
        保存项目配置到JSON文件
        
        Args:
            config: 项目配置字典
            config_name: 配置文件名称，如果不提供则使用项目名称
            
        Returns:
            str: 配置文件路径
            
        Raises:
            ValueError: 配置验证失败
            IOError: 文件写入失败
        """
        # 验证配置
        is_valid, errors = ProjectValidator.validate_project_config(config)
        if not is_valid:
            raise ValueError(f"配置验证失败：{'; '.join(errors)}")
        
        # 添加时间戳
        config = config.copy()
        now = datetime.now().isoformat()
        if ProjectConstants.CONFIG_CREATED_AT not in config:
            config[ProjectConstants.CONFIG_CREATED_AT] = now
        config[ProjectConstants.CONFIG_UPDATED_AT] = now
        
        # 确定配置文件名
        if config_name is None:
            config_name = config.get(ProjectConstants.CONFIG_NAME, "default")
        
        # 确保配置文件名安全
        config_name = self._sanitize_filename(config_name)
        config_file = self.config_dir / f"{config_name}.json"
        
        try:
            write_json(str(config_file), config)
            return str(config_file)
        except Exception as e:
            raise IOError(f"保存配置文件失败：{str(e)}")
    
    def load_config(self, config_name: str) -> Dict[str, Any]:
        """
        从JSON文件加载项目配置
        
        Args:
            config_name: 配置文件名称（不包含.json扩展名）
            
        Returns:
            Dict[str, Any]: 项目配置字典
            
        Raises:
            FileNotFoundError: 配置文件不存在
            ValueError: 配置文件格式无效
        """
        config_name = self._sanitize_filename(config_name)
        config_file = self.config_dir / f"{config_name}.json"
        
        if not file_exists(str(config_file)):
            raise FileNotFoundError(f"配置文件不存在：{config_file}")
        
        try:
            config = read_json(str(config_file))
            
            # 验证配置
            is_valid, errors = ProjectValidator.validate_project_config(config)
            if not is_valid:
                raise ValueError(f"配置文件格式无效：{'; '.join(errors)}")
            
            return config
        except json.JSONDecodeError as e:
            raise ValueError(f"配置文件JSON格式错误：{str(e)}")
        except Exception as e:
            raise ValueError(f"加载配置文件失败：{str(e)}")
    
    def list_configs(self) -> List[str]:
        """
        列出所有可用的配置文件
        
        Returns:
            List[str]: 配置文件名称列表（不包含.json扩展名）
        """
        config_files = []
        if self.config_dir.exists():
            for file_path in self.config_dir.glob("*.json"):
                config_files.append(file_path.stem)
        return sorted(config_files)
    
    def delete_config(self, config_name: str) -> bool:
        """
        删除配置文件
        
        Args:
            config_name: 配置文件名称（不包含.json扩展名）
            
        Returns:
            bool: 是否删除成功
        """
        config_name = self._sanitize_filename(config_name)
        config_file = self.config_dir / f"{config_name}.json"
        
        if file_exists(str(config_file)):
            try:
                os.remove(str(config_file))
                return True
            except Exception:
                return False
        return False
    
    def config_exists(self, config_name: str) -> bool:
        """
        检查配置文件是否存在
        
        Args:
            config_name: 配置文件名称（不包含.json扩展名）
            
        Returns:
            bool: 配置文件是否存在
        """
        config_name = self._sanitize_filename(config_name)
        config_file = self.config_dir / f"{config_name}.json"
        return file_exists(str(config_file))
    
    def get_config_path(self, config_name: str) -> str:
        """
        获取配置文件的完整路径
        
        Args:
            config_name: 配置文件名称（不包含.json扩展名）
            
        Returns:
            str: 配置文件完整路径
        """
        config_name = self._sanitize_filename(config_name)
        config_file = self.config_dir / f"{config_name}.json"
        return str(config_file)
    
    def create_default_config(self) -> Dict[str, Any]:
        """
        创建默认配置
        
        Returns:
            Dict[str, Any]: 默认配置字典
        """
        return {
            ProjectConstants.CONFIG_NAME: "my-spring-boot-project",
            ProjectConstants.CONFIG_PACKAGE: "com.example.project",
            ProjectConstants.CONFIG_VERSION: ProjectConstants.DEFAULT_PROJECT_VERSION,
            ProjectConstants.CONFIG_DESCRIPTION: "A Spring Boot project generated by AI",
            ProjectConstants.CONFIG_JAVA_VERSION: ProjectConstants.DEFAULT_JAVA_VERSION,
            ProjectConstants.CONFIG_SPRING_BOOT_VERSION: ProjectConstants.DEFAULT_SPRING_BOOT_VERSION,
            ProjectConstants.CONFIG_PROJECT_TYPE: ProjectConstants.PROJECT_TYPE_SINGLE,
            ProjectConstants.CONFIG_TECH_STACK: {
                ProjectConstants.TECH_DATABASE: ProjectConstants.DEFAULT_DATABASE,
                ProjectConstants.TECH_ORM: ProjectConstants.DEFAULT_ORM,
                ProjectConstants.TECH_CACHE: ProjectConstants.DEFAULT_CACHE,
                ProjectConstants.TECH_MQ: [],
                ProjectConstants.TECH_NOSQL: [],
                ProjectConstants.TECH_DOC: [ProjectConstants.DOC_SWAGGER],
                ProjectConstants.TECH_SECURITY: [],
                ProjectConstants.TECH_MONITOR: [ProjectConstants.MONITOR_ACTUATOR],
                ProjectConstants.TECH_WEB_FRAMEWORK: ProjectConstants.DEFAULT_WEB_FRAMEWORK,
                ProjectConstants.TECH_TEST_FRAMEWORKS: ProjectConstants.DEFAULT_TEST_FRAMEWORKS
            },
            ProjectConstants.CONFIG_MODULES: [],
            ProjectConstants.CONFIG_OUTPUT_DIR: "./output",
            ProjectConstants.CONFIG_PREVIEW_MODE: False
        }
    
    def merge_configs(self, base_config: Dict[str, Any], override_config: Dict[str, Any]) -> Dict[str, Any]:
        """
        合并两个配置字典
        
        Args:
            base_config: 基础配置
            override_config: 覆盖配置
            
        Returns:
            Dict[str, Any]: 合并后的配置
        """
        merged = base_config.copy()
        
        for key, value in override_config.items():
            if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
                # 递归合并字典
                merged[key] = self.merge_configs(merged[key], value)
            else:
                # 直接覆盖
                merged[key] = value
        
        return merged
    
    def export_config(self, config_name: str, export_path: str) -> None:
        """
        导出配置文件到指定路径
        
        Args:
            config_name: 配置文件名称
            export_path: 导出路径
            
        Raises:
            FileNotFoundError: 配置文件不存在
            IOError: 导出失败
        """
        config = self.load_config(config_name)
        
        try:
            write_json(export_path, config)
        except Exception as e:
            raise IOError(f"导出配置文件失败：{str(e)}")
    
    def import_config(self, import_path: str, config_name: str = None) -> str:
        """
        从指定路径导入配置文件
        
        Args:
            import_path: 导入路径
            config_name: 配置文件名称，如果不提供则从配置中获取
            
        Returns:
            str: 保存的配置文件路径
            
        Raises:
            FileNotFoundError: 导入文件不存在
            ValueError: 配置文件格式无效
        """
        if not file_exists(import_path):
            raise FileNotFoundError(f"导入文件不存在：{import_path}")
        
        try:
            config = read_json(import_path)
            return self.save_config(config, config_name)
        except Exception as e:
            raise ValueError(f"导入配置文件失败：{str(e)}")
    
    def _sanitize_filename(self, filename: str) -> str:
        """
        清理文件名，移除不安全字符
        
        Args:
            filename: 原始文件名
            
        Returns:
            str: 清理后的文件名
        """
        # 移除不安全字符
        import re
        filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
        # 移除前后空格和点
        filename = filename.strip(' .')
        # 确保不为空
        if not filename:
            filename = "config"
        return filename
    
    def get_config_info(self, config_name: str) -> Dict[str, Any]:
        """
        获取配置文件信息
        
        Args:
            config_name: 配置文件名称
            
        Returns:
            Dict[str, Any]: 配置文件信息
        """
        config_file = self.get_config_path(config_name)
        
        if not file_exists(config_file):
            return {}
        
        try:
            config = self.load_config(config_name)
            stat = os.stat(config_file)
            
            return {
                "name": config_name,
                "path": config_file,
                "project_name": config.get(ProjectConstants.CONFIG_NAME, "Unknown"),
                "project_type": config.get(ProjectConstants.CONFIG_PROJECT_TYPE, "Unknown"),
                "java_version": config.get(ProjectConstants.CONFIG_JAVA_VERSION, "Unknown"),
                "spring_boot_version": config.get(ProjectConstants.CONFIG_SPRING_BOOT_VERSION, "Unknown"),
                "created_at": config.get(ProjectConstants.CONFIG_CREATED_AT, "Unknown"),
                "updated_at": config.get(ProjectConstants.CONFIG_UPDATED_AT, "Unknown"),
                "file_size": stat.st_size,
                "modified_time": datetime.fromtimestamp(stat.st_mtime).isoformat()
            }
        except Exception:
            return {
                "name": config_name,
                "path": config_file,
                "error": "Failed to load config"
            }