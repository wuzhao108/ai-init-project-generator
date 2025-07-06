#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置管理CLI工具
提供命令行界面来管理系统配置、模板配置和历史配置
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

from config_manager_v2 import ConfigManagerV2
from config_migrator import ConfigMigrator


class ConfigCLI:
    """配置管理CLI"""
    
    def __init__(self):
        self.manager = ConfigManagerV2()
        self.migrator = ConfigMigrator()
    
    def run(self):
        """运行CLI"""
        parser = self._create_parser()
        args = parser.parse_args()
        
        if hasattr(args, 'func'):
            try:
                args.func(args)
            except Exception as e:
                print(f"错误: {e}")
                sys.exit(1)
        else:
            parser.print_help()
    
    def _create_parser(self) -> argparse.ArgumentParser:
        """创建命令行解析器"""
        parser = argparse.ArgumentParser(
            description="Spring Boot项目生成器配置管理工具",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
示例用法:
  %(prog)s system show                    # 显示系统配置
  %(prog)s template list                  # 列出所有模板
  %(prog)s template show spring-boot-basic # 显示指定模板
  %(prog)s history list                   # 列出历史配置
  %(prog)s history show project-20240101  # 显示指定历史配置
  %(prog)s migrate                        # 迁移旧配置
  %(prog)s search "spring boot"            # 搜索配置
"""
        )
        
        subparsers = parser.add_subparsers(dest='command', help='可用命令')
        
        # 系统配置命令
        self._add_system_commands(subparsers)
        
        # 模板配置命令
        self._add_template_commands(subparsers)
        
        # 历史配置命令
        self._add_history_commands(subparsers)
        
        # 迁移命令
        self._add_migration_commands(subparsers)
        
        # 搜索命令
        self._add_search_commands(subparsers)
        
        # 工具命令
        self._add_utility_commands(subparsers)
        
        return parser
    
    def _add_system_commands(self, subparsers):
        """添加系统配置命令"""
        system_parser = subparsers.add_parser('system', help='系统配置管理')
        system_subparsers = system_parser.add_subparsers(dest='system_action')
        
        # 显示系统配置
        show_parser = system_subparsers.add_parser('show', help='显示系统配置')
        show_parser.set_defaults(func=self.show_system_config)
        
        # 更新系统配置
        update_parser = system_subparsers.add_parser('update', help='更新系统配置')
        update_parser.add_argument('--output-dir', help='默认输出目录')
        update_parser.add_argument('--log-level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'], help='日志级别')
        update_parser.add_argument('--theme', help='UI主题')
        update_parser.add_argument('--language', help='界面语言')
        update_parser.set_defaults(func=self.update_system_config)
    
    def _add_template_commands(self, subparsers):
        """添加模板配置命令"""
        template_parser = subparsers.add_parser('template', help='模板配置管理')
        template_subparsers = template_parser.add_subparsers(dest='template_action')
        
        # 列出模板
        list_parser = template_subparsers.add_parser('list', help='列出所有模板')
        list_parser.add_argument('--format', choices=['table', 'json'], default='table', help='输出格式')
        list_parser.set_defaults(func=self.list_templates)
        
        # 显示模板详情
        show_parser = template_subparsers.add_parser('show', help='显示模板详情')
        show_parser.add_argument('template_id', help='模板ID')
        show_parser.add_argument('--format', choices=['yaml', 'json'], default='yaml', help='输出格式')
        show_parser.set_defaults(func=self.show_template)
        
        # 创建模板
        create_parser = template_subparsers.add_parser('create', help='创建新模板')
        create_parser.add_argument('template_id', help='模板ID')
        create_parser.add_argument('--name', required=True, help='模板名称')
        create_parser.add_argument('--description', help='模板描述')
        create_parser.add_argument('--author', default='AI Project Generator', help='作者')
        create_parser.add_argument('--config-file', help='配置文件路径')
        create_parser.set_defaults(func=self.create_template)
        
        # 删除模板
        delete_parser = template_subparsers.add_parser('delete', help='删除模板')
        delete_parser.add_argument('template_id', help='模板ID')
        delete_parser.add_argument('--force', action='store_true', help='强制删除')
        delete_parser.set_defaults(func=self.delete_template)
    
    def _add_history_commands(self, subparsers):
        """添加历史配置命令"""
        history_parser = subparsers.add_parser('history', help='历史配置管理')
        history_subparsers = history_parser.add_subparsers(dest='history_action')
        
        # 列出历史配置
        list_parser = history_subparsers.add_parser('list', help='列出历史配置')
        list_parser.add_argument('--limit', type=int, default=20, help='显示数量限制')
        list_parser.add_argument('--format', choices=['table', 'json'], default='table', help='输出格式')
        list_parser.set_defaults(func=self.list_history)
        
        # 显示历史配置详情
        show_parser = history_subparsers.add_parser('show', help='显示历史配置详情')
        show_parser.add_argument('config_id', help='配置ID')
        show_parser.add_argument('--format', choices=['yaml', 'json'], default='yaml', help='输出格式')
        show_parser.set_defaults(func=self.show_history)
        
        # 删除历史配置
        delete_parser = history_subparsers.add_parser('delete', help='删除历史配置')
        delete_parser.add_argument('config_id', help='配置ID')
        delete_parser.add_argument('--force', action='store_true', help='强制删除')
        delete_parser.set_defaults(func=self.delete_history)
        
        # 清理历史配置
        cleanup_parser = history_subparsers.add_parser('cleanup', help='清理历史配置')
        cleanup_parser.add_argument('--days', type=int, default=30, help='保留天数')
        cleanup_parser.add_argument('--dry-run', action='store_true', help='仅显示将要删除的配置')
        cleanup_parser.set_defaults(func=self.cleanup_history)
    
    def _add_migration_commands(self, subparsers):
        """添加迁移命令"""
        migrate_parser = subparsers.add_parser('migrate', help='配置迁移')
        migrate_subparsers = migrate_parser.add_subparsers(dest='migrate_action')
        
        # 执行迁移
        run_parser = migrate_subparsers.add_parser('run', help='执行配置迁移')
        run_parser.add_argument('--source', default='./configs', help='源配置目录')
        run_parser.add_argument('--target', default='./configs', help='目标配置目录')
        run_parser.add_argument('--backup', action='store_true', help='创建备份')
        run_parser.set_defaults(func=self.run_migration)
        
        # 回滚迁移
        rollback_parser = migrate_subparsers.add_parser('rollback', help='回滚迁移')
        rollback_parser.set_defaults(func=self.rollback_migration)
    
    def _add_search_commands(self, subparsers):
        """添加搜索命令"""
        search_parser = subparsers.add_parser('search', help='搜索配置')
        search_parser.add_argument('keyword', help='搜索关键词')
        search_parser.add_argument('--type', choices=['all', 'template', 'history'], default='all', help='搜索类型')
        search_parser.add_argument('--format', choices=['table', 'json'], default='table', help='输出格式')
        search_parser.set_defaults(func=self.search_configs)
    
    def _add_utility_commands(self, subparsers):
        """添加工具命令"""
        # 导出配置
        export_parser = subparsers.add_parser('export', help='导出配置')
        export_parser.add_argument('config_id', help='配置ID')
        export_parser.add_argument('config_type', choices=['template', 'history'], help='配置类型')
        export_parser.add_argument('--output', required=True, help='输出文件路径')
        export_parser.set_defaults(func=self.export_config)
        
        # 导入配置
        import_parser = subparsers.add_parser('import', help='导入配置')
        import_parser.add_argument('file_path', help='配置文件路径')
        import_parser.add_argument('config_type', choices=['template', 'history'], help='配置类型')
        import_parser.set_defaults(func=self.import_config)
        
        # 验证配置
        validate_parser = subparsers.add_parser('validate', help='验证配置')
        validate_parser.add_argument('--type', choices=['all', 'template', 'history'], default='all', help='验证类型')
        validate_parser.set_defaults(func=self.validate_configs)
    
    # ==================== 系统配置命令实现 ====================
    
    def show_system_config(self, args):
        """显示系统配置"""
        config = self.manager.load_system_config()
        
        print("=== 系统配置 ===")
        print(f"应用名称: {config.app_name}")
        print(f"版本: {config.version}")
        print(f"描述: {config.description}")
        print(f"默认输出目录: {config.output['default_dir']}")
        print(f"日志级别: {config.logging['level']}")
        print(f"UI主题: {config.ui['theme']}")
        print(f"界面语言: {config.ui['language']}")
        print(f"创建时间: {config.created_at}")
        print(f"更新时间: {config.updated_at}")
    
    def update_system_config(self, args):
        """更新系统配置"""
        config = self.manager.load_system_config()
        
        # 更新配置
        if args.output_dir:
            config.output['default_dir'] = args.output_dir
        if args.log_level:
            config.logging['level'] = args.log_level
        if args.theme:
            config.ui['theme'] = args.theme
        if args.language:
            config.ui['language'] = args.language
        
        # 保存配置
        if self.manager.save_system_config(config):
            print("系统配置更新成功")
        else:
            print("系统配置更新失败")
    
    # ==================== 模板配置命令实现 ====================
    
    def list_templates(self, args):
        """列出模板"""
        templates = self.manager.list_templates()
        
        if args.format == 'json':
            template_data = [{
                'template_id': t.template_id,
                'name': t.name,
                'version': t.version,
                'description': t.description,
                'created_at': t.created_at,
                'author': t.author
            } for t in templates]
            print(json.dumps(template_data, indent=2, ensure_ascii=False))
        else:
            print("=== 模板列表 ===")
            print(f"{'ID':<20} {'名称':<25} {'版本':<10} {'作者':<15} {'创建时间':<12}")
            print("-" * 85)
            for template in templates:
                print(f"{template.template_id:<20} {template.name:<25} {template.version:<10} {template.author:<15} {template.created_at:<12}")
    
    def show_template(self, args):
        """显示模板详情"""
        config = self.manager.load_template_config(args.template_id)
        if not config:
            print(f"模板 '{args.template_id}' 不存在")
            return
        
        if args.format == 'json':
            print(json.dumps(config, indent=2, ensure_ascii=False))
        else:
            import yaml
            print(f"=== 模板配置: {args.template_id} ===")
            print(yaml.dump(config, default_flow_style=False, allow_unicode=True))
    
    def create_template(self, args):
        """创建模板"""
        # 准备元数据
        metadata = {
            'template_id': args.template_id,
            'name': args.name,
            'description': args.description or '',
            'author': args.author,
            'version': '1.0.0'
        }
        
        # 准备配置
        if args.config_file:
            with open(args.config_file, 'r', encoding='utf-8') as f:
                if args.config_file.endswith('.json'):
                    config = json.load(f)
                else:
                    import yaml
                    config = yaml.safe_load(f)
        else:
            # 使用默认配置
            config = self._get_default_template_config()
        
        # 保存模板
        if self.manager.save_template_config(args.template_id, config, metadata):
            print(f"模板 '{args.template_id}' 创建成功")
        else:
            print(f"模板 '{args.template_id}' 创建失败")
    
    def delete_template(self, args):
        """删除模板"""
        if not args.force:
            confirm = input(f"确定要删除模板 '{args.template_id}' 吗？(y/N): ")
            if confirm.lower() != 'y':
                print("操作已取消")
                return
        
        template_file = Path(self.manager.templates_path) / f"{args.template_id}.md"
        if template_file.exists():
            template_file.unlink()
            print(f"模板 '{args.template_id}' 删除成功")
        else:
            print(f"模板 '{args.template_id}' 不存在")
    
    # ==================== 历史配置命令实现 ====================
    
    def list_history(self, args):
        """列出历史配置"""
        histories = self.manager.list_history_configs(args.limit)
        
        if args.format == 'json':
            history_data = [{
                'config_id': h.config_id,
                'project_name': h.project_name,
                'template_id': h.template_id,
                'project_type': h.project_type,
                'created_at': h.created_at,
                'creator': h.creator
            } for h in histories]
            print(json.dumps(history_data, indent=2, ensure_ascii=False))
        else:
            print("=== 历史配置列表 ===")
            print(f"{'配置ID':<25} {'项目名称':<20} {'项目类型':<15} {'模板':<20} {'创建时间':<12}")
            print("-" * 95)
            for history in histories:
                print(f"{history.config_id:<25} {history.project_name:<20} {history.project_type:<15} {history.template_id:<20} {history.created_at:<12}")
    
    def show_history(self, args):
        """显示历史配置详情"""
        config = self.manager.load_history_config(args.config_id)
        if not config:
            print(f"历史配置 '{args.config_id}' 不存在")
            return
        
        if args.format == 'json':
            print(json.dumps(config, indent=2, ensure_ascii=False))
        else:
            import yaml
            print(f"=== 历史配置: {args.config_id} ===")
            print(yaml.dump(config, default_flow_style=False, allow_unicode=True))
    
    def delete_history(self, args):
        """删除历史配置"""
        if not args.force:
            confirm = input(f"确定要删除历史配置 '{args.config_id}' 吗？(y/N): ")
            if confirm.lower() != 'y':
                print("操作已取消")
                return
        
        if self.manager.delete_history_config(args.config_id):
            print(f"历史配置 '{args.config_id}' 删除成功")
        else:
            print(f"历史配置 '{args.config_id}' 删除失败")
    
    def cleanup_history(self, args):
        """清理历史配置"""
        from datetime import timedelta
        
        cutoff_date = datetime.now() - timedelta(days=args.days)
        histories = self.manager.list_history_configs()
        
        to_delete = []
        for history in histories:
            try:
                created_date = datetime.fromisoformat(history.created_at.replace('Z', '+00:00'))
                if created_date < cutoff_date:
                    to_delete.append(history)
            except ValueError:
                continue
        
        if not to_delete:
            print(f"没有找到超过 {args.days} 天的历史配置")
            return
        
        print(f"找到 {len(to_delete)} 个超过 {args.days} 天的历史配置:")
        for history in to_delete:
            print(f"  - {history.config_id} ({history.created_at})")
        
        if args.dry_run:
            print("\n(这是预览模式，实际文件未被删除)")
            return
        
        confirm = input(f"\n确定要删除这 {len(to_delete)} 个配置吗？(y/N): ")
        if confirm.lower() != 'y':
            print("操作已取消")
            return
        
        deleted_count = 0
        for history in to_delete:
            if self.manager.delete_history_config(history.config_id):
                deleted_count += 1
        
        print(f"成功删除 {deleted_count} 个历史配置")
    
    # ==================== 迁移命令实现 ====================
    
    def run_migration(self, args):
        """执行迁移"""
        print("开始配置迁移...")
        
        migrator = ConfigMigrator(args.source, args.target)
        results = migrator.migrate_all()
        
        print(f"\n迁移完成: {'成功' if results['success'] else '失败'}")
        print(f"模板配置: {len(results['migrated_templates'])} 个")
        print(f"历史配置: {len(results['migrated_histories'])} 个")
        
        if results['errors']:
            print("\n错误信息:")
            for error in results['errors']:
                print(f"  - {error}")
        
        print(f"\n备份路径: {results['backup_path']}")
    
    def rollback_migration(self, args):
        """回滚迁移"""
        confirm = input("确定要回滚迁移吗？这将删除新配置并恢复备份。(y/N): ")
        if confirm.lower() != 'y':
            print("操作已取消")
            return
        
        if self.migrator.rollback():
            print("迁移回滚成功")
        else:
            print("迁移回滚失败")
    
    # ==================== 搜索命令实现 ====================
    
    def search_configs(self, args):
        """搜索配置"""
        results = self.manager.search_configs(args.keyword, args.type)
        
        if args.format == 'json':
            print(json.dumps(results, indent=2, ensure_ascii=False, default=str))
        else:
            print(f"=== 搜索结果: '{args.keyword}' ===")
            
            if results['templates']:
                print("\n模板配置:")
                for template in results['templates']:
                    print(f"  - {template.template_id}: {template.name}")
            
            if results['histories']:
                print("\n历史配置:")
                for history in results['histories']:
                    print(f"  - {history.config_id}: {history.project_name}")
            
            if not results['templates'] and not results['histories']:
                print("未找到匹配的配置")
    
    # ==================== 工具命令实现 ====================
    
    def export_config(self, args):
        """导出配置"""
        if self.manager.export_config(args.config_id, args.config_type, args.output):
            print(f"配置导出成功: {args.output}")
        else:
            print("配置导出失败")
    
    def import_config(self, args):
        """导入配置"""
        if self.manager.import_config(args.file_path, args.config_type):
            print("配置导入成功")
        else:
            print("配置导入失败")
    
    def validate_configs(self, args):
        """验证配置"""
        print("配置验证功能开发中...")
    
    def _get_default_template_config(self) -> Dict[str, Any]:
        """获取默认模板配置"""
        return {
            "project": {
                "name": "my-spring-boot-app",
                "package_name": "com.example.app",
                "version": "1.0.0",
                "description": "Spring Boot应用",
                "java_version": "17",
                "spring_boot_version": "3.2.0"
            },
            "tech_stack": {
                "database": "h2",
                "orm": "jpa",
                "cache": "none",
                "mq": "none",
                "documentation": False,
                "security": False,
                "web_framework": "spring-mvc",
                "testing": "junit5"
            },
            "generation": {
                "output_dir": "./output",
                "generate_examples": True,
                "generate_tests": True,
                "generate_docker": True
            }
        }


if __name__ == "__main__":
    cli = ConfigCLI()
    cli.run()