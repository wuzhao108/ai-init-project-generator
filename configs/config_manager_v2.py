#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置管理器 V2
支持系统配置、模板配置和历史配置的统一管理
"""

import os
import json
import yaml
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from pathlib import Path
import re


@dataclass
class SystemConfig:
    """系统级配置"""
    version: str
    app_name: str
    description: str
    output: Dict[str, str]
    templates: Dict[str, Any]
    logging: Dict[str, Any]
    generator: Dict[str, Any]
    ui: Dict[str, str]
    validation: Dict[str, bool]
    created_at: str
    updated_at: str


@dataclass
class TemplateMetadata:
    """模板元数据"""
    template_id: str
    name: str
    version: str
    description: str
    created_at: str
    updated_at: str
    author: str
    file_path: str


@dataclass
class HistoryMetadata:
    """历史配置元数据"""
    config_id: str
    project_name: str
    template_id: str
    created_at: str
    updated_at: str
    creator: str
    project_type: str
    file_path: str


class ConfigManagerV2:
    """配置管理器 V2"""
    
    def __init__(self, base_path: str = "./configs"):
        self.base_path = Path(base_path)
        self.system_path = self.base_path / "system"
        self.templates_path = self.base_path / "templates"
        self.history_path = self.base_path / "history"
        
        # 确保目录存在
        self._ensure_directories()
    
    def _ensure_directories(self):
        """确保配置目录存在"""
        for path in [self.system_path, self.templates_path, self.history_path]:
            path.mkdir(parents=True, exist_ok=True)
    
    # ==================== 系统配置管理 ====================
    
    def load_system_config(self) -> SystemConfig:
        """加载系统配置"""
        config_file = self.system_path / "system.json"
        if not config_file.exists():
            return self._create_default_system_config()
        
        with open(config_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        return SystemConfig(**data)
    
    def save_system_config(self, config: SystemConfig) -> bool:
        """保存系统配置"""
        try:
            config.updated_at = datetime.now().isoformat()
            config_file = self.system_path / "system.json"
            
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(asdict(config), f, indent=2, ensure_ascii=False)
            
            return True
        except Exception as e:
            print(f"保存系统配置失败: {e}")
            return False
    
    def _create_default_system_config(self) -> SystemConfig:
        """创建默认系统配置"""
        now = datetime.now().isoformat()
        config = SystemConfig(
            version="1.0.0",
            app_name="Spring Boot Project Generator",
            description="AI驱动的Spring Boot项目生成器",
            output={
                "default_dir": "./output",
                "backup_dir": "./backup",
                "temp_dir": "./temp"
            },
            templates={
                "base_path": "./spring_init/templates",
                "cache_enabled": True,
                "cache_ttl": 3600
            },
            logging={
                "level": "INFO",
                "file": "./logs/generator.log",
                "max_size": "10MB",
                "backup_count": 5
            },
            generator={
                "max_concurrent_tasks": 4,
                "timeout_seconds": 300,
                "auto_backup": True
            },
            ui={
                "theme": "default",
                "language": "zh-CN",
                "show_progress": "true"
            },
            validation={
                "strict_mode": False,
                "check_dependencies": True,
                "validate_package_name": True
            },
            created_at=now,
            updated_at=now
        )
        
        self.save_system_config(config)
        return config
    
    # ==================== 模板配置管理 ====================
    
    def list_templates(self) -> List[TemplateMetadata]:
        """列出所有模板配置"""
        templates = []
        
        for md_file in self.templates_path.glob("*.md"):
            metadata = self._parse_template_metadata(md_file)
            if metadata:
                templates.append(metadata)
        
        return sorted(templates, key=lambda x: x.created_at, reverse=True)
    
    def load_template_config(self, template_id: str) -> Optional[Dict[str, Any]]:
        """加载模板配置"""
        md_file = self.templates_path / f"{template_id}.md"
        if not md_file.exists():
            return None
        
        return self._parse_template_config(md_file)
    
    def save_template_config(self, template_id: str, config: Dict[str, Any], 
                           metadata: Dict[str, str]) -> bool:
        """保存模板配置"""
        try:
            md_file = self.templates_path / f"{template_id}.md"
            content = self._generate_template_markdown(config, metadata)
            
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        except Exception as e:
            print(f"保存模板配置失败: {e}")
            return False
    
    def _parse_template_metadata(self, md_file: Path) -> Optional[TemplateMetadata]:
        """解析模板元数据"""
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 提取元数据
            template_id = md_file.stem
            name = self._extract_field(content, "模板名称")
            version = self._extract_field(content, "版本")
            description = self._extract_field(content, "描述")
            created_at = self._extract_field(content, "创建时间")
            updated_at = self._extract_field(content, "更新时间")
            author = self._extract_field(content, "作者")
            
            return TemplateMetadata(
                template_id=template_id,
                name=name or template_id,
                version=version or "1.0.0",
                description=description or "",
                created_at=created_at or "",
                updated_at=updated_at or "",
                author=author or "",
                file_path=str(md_file)
            )
        except Exception as e:
            print(f"解析模板元数据失败 {md_file}: {e}")
            return None
    
    def _parse_template_config(self, md_file: Path) -> Dict[str, Any]:
        """解析模板配置"""
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        config = {}
        
        # 提取YAML配置块
        yaml_blocks = re.findall(r'```yaml\n(.*?)\n```', content, re.DOTALL)
        for block in yaml_blocks:
            try:
                yaml_config = yaml.safe_load(block)
                if isinstance(yaml_config, dict):
                    config.update(yaml_config)
            except yaml.YAMLError:
                continue
        
        return config
    
    def _generate_template_markdown(self, config: Dict[str, Any], 
                                  metadata: Dict[str, str]) -> str:
        """生成模板Markdown内容"""
        now = datetime.now().strftime("%Y-%m-%d")
        
        content = f"""# {metadata.get('name', '未命名模板')}配置

## 模板信息

- **模板名称**: {metadata.get('name', '未命名模板')}
- **模板ID**: `{metadata.get('template_id', '')}`
- **版本**: `{metadata.get('version', '1.0.0')}`
- **描述**: {metadata.get('description', '')}
- **创建时间**: {metadata.get('created_at', now)}
- **更新时间**: {now}
- **作者**: {metadata.get('author', 'AI Project Generator')}

## 项目配置

```yaml
{yaml.dump(config, default_flow_style=False, allow_unicode=True)}
```

## 使用说明

请根据实际需求调整配置参数。
"""
        
        return content
    
    # ==================== 历史配置管理 ====================
    
    def list_history_configs(self, limit: int = 50) -> List[HistoryMetadata]:
        """列出历史配置"""
        histories = []
        
        for md_file in self.history_path.glob("*.md"):
            metadata = self._parse_history_metadata(md_file)
            if metadata:
                histories.append(metadata)
        
        # 按创建时间倒序排列
        histories.sort(key=lambda x: x.created_at, reverse=True)
        
        return histories[:limit]
    
    def load_history_config(self, config_id: str) -> Optional[Dict[str, Any]]:
        """加载历史配置"""
        md_file = self.history_path / f"{config_id}.md"
        if not md_file.exists():
            return None
        
        return self._parse_history_config(md_file)
    
    def save_history_config(self, project_name: str, config: Dict[str, Any], 
                          metadata: Dict[str, str]) -> str:
        """保存历史配置"""
        try:
            # 生成配置ID
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            config_id = f"{project_name}-{timestamp}"
            
            md_file = self.history_path / f"{config_id}.md"
            content = self._generate_history_markdown(config_id, config, metadata)
            
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return config_id
        except Exception as e:
            print(f"保存历史配置失败: {e}")
            return ""
    
    def delete_history_config(self, config_id: str) -> bool:
        """删除历史配置"""
        try:
            md_file = self.history_path / f"{config_id}.md"
            if md_file.exists():
                md_file.unlink()
                return True
            return False
        except Exception as e:
            print(f"删除历史配置失败: {e}")
            return False
    
    def _parse_history_metadata(self, md_file: Path) -> Optional[HistoryMetadata]:
        """解析历史配置元数据"""
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            config_id = md_file.stem
            project_name = self._extract_field(content, "项目名称")
            template_id = self._extract_field(content, "使用模板")
            created_at = self._extract_field(content, "创建时间")
            updated_at = self._extract_field(content, "更新时间")
            creator = self._extract_field(content, "创建者")
            project_type = self._extract_field(content, "项目类型")
            
            return HistoryMetadata(
                config_id=config_id,
                project_name=project_name or config_id,
                template_id=template_id or "",
                created_at=created_at or "",
                updated_at=updated_at or "",
                creator=creator or "",
                project_type=project_type or "",
                file_path=str(md_file)
            )
        except Exception as e:
            print(f"解析历史配置元数据失败 {md_file}: {e}")
            return None
    
    def _parse_history_config(self, md_file: Path) -> Dict[str, Any]:
        """解析历史配置"""
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        config = {}
        
        # 提取YAML配置块
        yaml_blocks = re.findall(r'```yaml\n(.*?)\n```', content, re.DOTALL)
        for block in yaml_blocks:
            try:
                yaml_config = yaml.safe_load(block)
                if isinstance(yaml_config, dict):
                    config.update(yaml_config)
            except yaml.YAMLError:
                continue
        
        return config
    
    def _generate_history_markdown(self, config_id: str, config: Dict[str, Any], 
                                 metadata: Dict[str, str]) -> str:
        """生成历史配置Markdown内容"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        content = f"""# 项目配置历史记录

## 项目基本信息

- **项目名称**: {metadata.get('project_name', '')}
- **配置ID**: `{config_id}`
- **创建时间**: {now}
- **更新时间**: {now}
- **创建者**: {metadata.get('creator', '')}
- **项目类型**: {metadata.get('project_type', '')}
- **使用模板**: {metadata.get('template_id', '')}

## 项目配置详情

### 基础配置
```yaml
{yaml.dump(config, default_flow_style=False, allow_unicode=True)}
```

## 配置说明

{metadata.get('description', '此配置用于生成Spring Boot项目。')}

## 配置变更记录

| 时间 | 变更内容 | 变更原因 | 操作人 |
|------|----------|----------|--------|
| {now} | 初始配置创建 | 项目启动 | {metadata.get('creator', '')} |

## 备注

- 本配置基于{metadata.get('template_id', '')}模板创建
- 可根据实际需求进行配置调整
"""
        
        return content
    
    # ==================== 工具方法 ====================
    
    def _extract_field(self, content: str, field_name: str) -> str:
        """从Markdown内容中提取字段值"""
        pattern = rf"\*\*{field_name}\*\*:?\s*([^\n]+)"
        match = re.search(pattern, content)
        if match:
            value = match.group(1).strip()
            # 移除markdown格式
            value = re.sub(r'`([^`]+)`', r'\1', value)
            return value
        return ""
    
    def search_configs(self, keyword: str, config_type: str = "all") -> Dict[str, List]:
        """搜索配置"""
        results = {
            "templates": [],
            "histories": []
        }
        
        if config_type in ["all", "template"]:
            for template in self.list_templates():
                if (keyword.lower() in template.name.lower() or 
                    keyword.lower() in template.description.lower()):
                    results["templates"].append(template)
        
        if config_type in ["all", "history"]:
            for history in self.list_history_configs():
                if (keyword.lower() in history.project_name.lower() or 
                    keyword.lower() in history.project_type.lower()):
                    results["histories"].append(history)
        
        return results
    
    def export_config(self, config_id: str, config_type: str, 
                     export_path: str) -> bool:
        """导出配置"""
        try:
            if config_type == "template":
                source_file = self.templates_path / f"{config_id}.md"
            elif config_type == "history":
                source_file = self.history_path / f"{config_id}.md"
            else:
                return False
            
            if not source_file.exists():
                return False
            
            import shutil
            shutil.copy2(source_file, export_path)
            return True
        except Exception as e:
            print(f"导出配置失败: {e}")
            return False
    
    def import_config(self, import_path: str, config_type: str) -> bool:
        """导入配置"""
        try:
            import_file = Path(import_path)
            if not import_file.exists():
                return False
            
            if config_type == "template":
                target_dir = self.templates_path
            elif config_type == "history":
                target_dir = self.history_path
            else:
                return False
            
            import shutil
            shutil.copy2(import_file, target_dir / import_file.name)
            return True
        except Exception as e:
            print(f"导入配置失败: {e}")
            return False


if __name__ == "__main__":
    # 测试代码
    manager = ConfigManagerV2()
    
    # 测试系统配置
    system_config = manager.load_system_config()
    print(f"系统配置: {system_config.app_name}")
    
    # 测试模板列表
    templates = manager.list_templates()
    print(f"模板数量: {len(templates)}")
    for template in templates:
        print(f"  - {template.name} ({template.template_id})")
    
    # 测试历史配置列表
    histories = manager.list_history_configs()
    print(f"历史配置数量: {len(histories)}")
    for history in histories:
        print(f"  - {history.project_name} ({history.config_id})")