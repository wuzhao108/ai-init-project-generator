#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置迁移工具
将现有的JSON配置迁移到新的配置架构中
"""

import os
import json
import yaml
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
from .config_manager_v2 import ConfigManagerV2


class ConfigMigrator:
    """配置迁移器"""
    
    def __init__(self, old_configs_path: str = "./configs", 
                 new_configs_path: str = "./configs"):
        self.old_path = Path(old_configs_path)
        self.new_path = Path(new_configs_path)
        self.config_manager = ConfigManagerV2(str(self.new_path))
        
        # 备份目录
        self.backup_path = self.old_path / "backup" / datetime.now().strftime("%Y%m%d_%H%M%S")
        self.backup_path.mkdir(parents=True, exist_ok=True)
    
    def migrate_all(self) -> Dict[str, Any]:
        """迁移所有配置"""
        results = {
            "success": True,
            "migrated_templates": [],
            "migrated_histories": [],
            "errors": [],
            "backup_path": str(self.backup_path)
        }
        
        try:
            # 1. 备份原有配置
            self._backup_old_configs()
            
            # 2. 迁移模板配置
            template_results = self._migrate_templates()
            results["migrated_templates"] = template_results
            
            # 3. 迁移历史配置
            history_results = self._migrate_histories()
            results["migrated_histories"] = history_results
            
            # 4. 生成迁移报告
            self._generate_migration_report(results)
            
        except Exception as e:
            results["success"] = False
            results["errors"].append(f"迁移过程中发生错误: {str(e)}")
        
        return results
    
    def _backup_old_configs(self):
        """备份原有配置文件"""
        import shutil
        
        for json_file in self.old_path.glob("*.json"):
            backup_file = self.backup_path / json_file.name
            shutil.copy2(json_file, backup_file)
            print(f"备份配置文件: {json_file.name} -> {backup_file}")
    
    def _migrate_templates(self) -> List[Dict[str, str]]:
        """迁移模板配置"""
        migrated = []
        
        # 识别模板配置文件
        template_files = [
            "default_template.json",
            "template.json"
        ]
        
        for template_file in template_files:
            json_path = self.old_path / template_file
            if not json_path.exists():
                continue
            
            try:
                # 加载原配置
                with open(json_path, 'r', encoding='utf-8') as f:
                    old_config = json.load(f)
                
                # 转换配置格式
                new_config = self._convert_to_new_format(old_config)
                
                # 生成模板ID和元数据
                template_id = self._generate_template_id(template_file, old_config)
                metadata = self._generate_template_metadata(template_file, old_config)
                
                # 保存新格式配置
                success = self.config_manager.save_template_config(
                    template_id, new_config, metadata
                )
                
                if success:
                    migrated.append({
                        "source_file": template_file,
                        "template_id": template_id,
                        "status": "success"
                    })
                    print(f"成功迁移模板配置: {template_file} -> {template_id}.md")
                else:
                    migrated.append({
                        "source_file": template_file,
                        "template_id": template_id,
                        "status": "failed",
                        "error": "保存失败"
                    })
                
            except Exception as e:
                migrated.append({
                    "source_file": template_file,
                    "template_id": "",
                    "status": "error",
                    "error": str(e)
                })
                print(f"迁移模板配置失败 {template_file}: {e}")
        
        return migrated
    
    def _migrate_histories(self) -> List[Dict[str, str]]:
        """迁移历史配置"""
        migrated = []
        
        # 查找所有项目配置文件（排除模板文件）
        exclude_files = {"default_template.json", "template.json"}
        
        for json_file in self.old_path.glob("*.json"):
            if json_file.name in exclude_files:
                continue
            
            try:
                # 加载原配置
                with open(json_file, 'r', encoding='utf-8') as f:
                    old_config = json.load(f)
                
                # 转换配置格式
                new_config = self._convert_to_new_format(old_config)
                
                # 生成历史配置元数据
                metadata = self._generate_history_metadata(json_file.stem, old_config)
                
                # 保存历史配置
                config_id = self.config_manager.save_history_config(
                    json_file.stem, new_config, metadata
                )
                
                if config_id:
                    migrated.append({
                        "source_file": json_file.name,
                        "config_id": config_id,
                        "status": "success"
                    })
                    print(f"成功迁移历史配置: {json_file.name} -> {config_id}.md")
                else:
                    migrated.append({
                        "source_file": json_file.name,
                        "config_id": "",
                        "status": "failed",
                        "error": "保存失败"
                    })
                
            except Exception as e:
                migrated.append({
                    "source_file": json_file.name,
                    "config_id": "",
                    "status": "error",
                    "error": str(e)
                })
                print(f"迁移历史配置失败 {json_file.name}: {e}")
        
        return migrated
    
    def _convert_to_new_format(self, old_config: Dict[str, Any]) -> Dict[str, Any]:
        """将旧格式配置转换为新格式"""
        new_config = {
            "project": {
                "name": old_config.get("project_name", ""),
                "package_name": old_config.get("package_name", ""),
                "version": old_config.get("version", "1.0.0"),
                "description": old_config.get("description", ""),
                "java_version": old_config.get("java_version", "17"),
                "spring_boot_version": old_config.get("spring_boot_version", "3.2.0")
            },
            "tech_stack": {},
            "generation": {
                "output_dir": old_config.get("output_dir", "./output"),
                "generate_examples": old_config.get("generate_examples", True),
                "generate_tests": old_config.get("generate_tests", True),
                "generate_docker": old_config.get("generate_docker", True)
            }
        }
        
        # 转换技术栈配置
        tech_stack = old_config.get("tech_stack", {})
        if tech_stack:
            new_config["tech_stack"] = {
                "database": tech_stack.get("database", "h2"),
                "orm": tech_stack.get("orm", "jpa"),
                "cache": tech_stack.get("cache", "none"),
                "mq": tech_stack.get("mq", "none"),
                "nosql": {
                    "mongodb": tech_stack.get("mongodb", False),
                    "elasticsearch": tech_stack.get("elasticsearch", False)
                },
                "documentation": tech_stack.get("doc", False),
                "security": tech_stack.get("security", False),
                "web_framework": tech_stack.get("web_framework", "spring-mvc"),
                "monitoring": {
                    "actuator": tech_stack.get("actuator", False)
                },
                "testing": tech_stack.get("testing_framework", "junit5")
            }
        
        # 处理模块配置（如果存在）
        if "modules" in old_config:
            new_config["modules"] = old_config["modules"]
        
        # 处理多模块配置
        if "multi_module" in old_config:
            new_config["project"]["multi_module"] = old_config["multi_module"]
        
        return new_config
    
    def _generate_template_id(self, filename: str, config: Dict[str, Any]) -> str:
        """生成模板ID"""
        if "default" in filename.lower():
            return "spring-boot-basic"
        elif "template" in filename.lower():
            # 根据配置内容判断模板类型
            if config.get("multi_module", False):
                return "spring-boot-microservice"
            else:
                return "spring-boot-web"
        else:
            return filename.replace(".json", "")
    
    def _generate_template_metadata(self, filename: str, config: Dict[str, Any]) -> Dict[str, str]:
        """生成模板元数据"""
        template_id = self._generate_template_id(filename, config)
        
        metadata_map = {
            "spring-boot-basic": {
                "name": "Spring Boot 基础模板",
                "description": "适用于单体应用的基础Spring Boot项目模板",
                "author": "AI Project Generator"
            },
            "spring-boot-microservice": {
                "name": "Spring Boot 微服务模板",
                "description": "适用于微服务架构的Spring Boot项目模板",
                "author": "AI Project Generator"
            },
            "spring-boot-web": {
                "name": "Spring Boot Web模板",
                "description": "适用于Web应用的Spring Boot项目模板",
                "author": "AI Project Generator"
            }
        }
        
        default_metadata = {
            "name": f"Spring Boot {template_id.replace('-', ' ').title()}模板",
            "description": "Spring Boot项目模板",
            "author": "AI Project Generator"
        }
        
        metadata = metadata_map.get(template_id, default_metadata)
        metadata.update({
            "template_id": template_id,
            "version": "1.0.0",
            "created_at": datetime.now().strftime("%Y-%m-%d"),
            "updated_at": datetime.now().strftime("%Y-%m-%d")
        })
        
        return metadata
    
    def _generate_history_metadata(self, project_name: str, config: Dict[str, Any]) -> Dict[str, str]:
        """生成历史配置元数据"""
        # 根据配置判断项目类型
        project_type = "单体应用"
        if config.get("multi_module", False):
            project_type = "微服务"
        elif config.get("tech_stack", {}).get("web_framework") == "spring-webflux":
            project_type = "响应式Web应用"
        
        # 判断使用的模板
        template_id = "spring-boot-basic"
        if config.get("multi_module", False):
            template_id = "spring-boot-microservice"
        
        return {
            "project_name": project_name,
            "creator": "系统迁移",
            "project_type": project_type,
            "template_id": template_id,
            "description": f"从{project_name}.json迁移的项目配置"
        }
    
    def _generate_migration_report(self, results: Dict[str, Any]):
        """生成迁移报告"""
        report_path = self.backup_path / "migration_report.md"
        
        content = f"""# 配置迁移报告

## 迁移概览

- **迁移时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **迁移状态**: {'成功' if results['success'] else '失败'}
- **备份路径**: `{results['backup_path']}`

## 模板配置迁移

| 源文件 | 模板ID | 状态 | 错误信息 |
|--------|--------|------|----------|
"""
        
        for template in results["migrated_templates"]:
            error = template.get("error", "")
            content += f"| {template['source_file']} | {template['template_id']} | {template['status']} | {error} |\n"
        
        content += f"\n## 历史配置迁移\n\n| 源文件 | 配置ID | 状态 | 错误信息 |\n|--------|--------|------|----------|\n"
        
        for history in results["migrated_histories"]:
            error = history.get("error", "")
            content += f"| {history['source_file']} | {history['config_id']} | {history['status']} | {error} |\n"
        
        if results["errors"]:
            content += f"\n## 错误信息\n\n"
            for error in results["errors"]:
                content += f"- {error}\n"
        
        content += f"\n## 迁移后目录结构\n\n```\nconfigs/\n├── system/\n│   └── system.json\n├── templates/\n│   ├── spring-boot-basic.md\n│   ├── spring-boot-microservice.md\n│   └── spring-boot-web.md\n└── history/\n    ├── project1-20240101-120000.md\n    └── project2-20240102-130000.md\n```\n\n## 使用新配置管理器\n\n```python\nfrom configs.config_manager_v2 import ConfigManagerV2\n\n# 创建配置管理器\nmanager = ConfigManagerV2()\n\n# 加载系统配置\nsystem_config = manager.load_system_config()\n\n# 列出模板\ntemplates = manager.list_templates()\n\n# 列出历史配置\nhistories = manager.list_history_configs()\n```\n"""
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"迁移报告已生成: {report_path}")
    
    def rollback(self) -> bool:
        """回滚迁移（恢复备份）"""
        try:
            import shutil
            
            # 删除新生成的配置目录
            for subdir in ["system", "templates", "history"]:
                target_dir = self.new_path / subdir
                if target_dir.exists():
                    shutil.rmtree(target_dir)
            
            # 恢复备份文件
            for backup_file in self.backup_path.glob("*.json"):
                target_file = self.old_path / backup_file.name
                shutil.copy2(backup_file, target_file)
            
            print("配置迁移已回滚")
            return True
        except Exception as e:
            print(f"回滚失败: {e}")
            return False


if __name__ == "__main__":
    # 执行迁移
    migrator = ConfigMigrator()
    results = migrator.migrate_all()
    
    print("\n=== 迁移结果 ===")
    print(f"迁移状态: {'成功' if results['success'] else '失败'}")
    print(f"模板配置: {len(results['migrated_templates'])} 个")
    print(f"历史配置: {len(results['migrated_histories'])} 个")
    
    if results["errors"]:
        print("\n错误信息:")
        for error in results["errors"]:
            print(f"  - {error}")
    
    print(f"\n备份路径: {results['backup_path']}")
    print("迁移报告已生成，请查看备份目录中的 migration_report.md")