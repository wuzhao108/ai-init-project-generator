#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CLI主入口模块
提供命令行界面和主要的命令处理逻辑
"""

import click
import os
import sys
from pathlib import Path
from typing import Optional
import json
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from .generator import ProjectGenerator
from .config import ProjectConfig
from .interactive import InteractiveConfig
from .utils import validate_project_name, validate_package_name
from ..common.config_manager import ConfigManager
from ..common.constants.project_constants import ProjectConstants

console = Console()


@click.group()
@click.version_option(version="1.0.0")
def cli():
    """SpringBoot项目脚手架生成器
    
    一个基于Python的CLI命令行工具，用于自动生成标准化的Java SpringBoot项目脚手架。
    """
    pass


@cli.command()
@click.option('--name', '-n', help='项目名称')
@click.option('--package', '-p', help='基础包名')
@click.option('--version', '-v', default='1.0.0', help='项目版本号')
@click.option('--description', '-d', help='项目描述')
@click.option('--java-version', type=click.Choice(['8', '11', '17', '21']), help='Java版本')
@click.option('--spring-version', type=click.Choice(['2.7.18', '3.0.13', '3.1.8', '3.2.2']), help='SpringBoot版本')
@click.option('--multi-module', is_flag=True, help='创建多模块项目')
@click.option('--output', '-o', default='.', help='输出目录')
@click.option('--preview', is_flag=True, help='预览模式，不实际生成文件')
@click.option('--save-config', is_flag=True, default=True, help='保存配置到JSON文件')
@click.option('--config-name', help='配置文件名称')
def create(name, package, version, description, java_version, spring_version, multi_module, output, preview, save_config, config_name):
    """创建SpringBoot项目"""
    
    console.print(Panel.fit(
        Text("SpringBoot项目脚手架生成器", style="bold blue"),
        border_style="blue"
    ))
    
    try:
        # 如果没有提供必要参数，启动交互式配置
        if not name or not package:
            interactive = InteractiveConfig()
            config = interactive.collect_config()
        else:
            # 验证输入参数
            if not validate_project_name(name):
                console.print("[red]错误: 项目名称格式不正确[/red]")
                sys.exit(1)
                
            if not validate_package_name(package):
                console.print("[red]错误: 包名格式不正确[/red]")
                sys.exit(1)
            
            config = ProjectConfig(
                name=name,
                package=package,
                version=version,
                description=description or f"{name} - SpringBoot项目",
                java_version=java_version or '11',
                spring_version=spring_version or '2.7.18',
                multi_module=multi_module,
                output_dir=output
            )
        
        # 生成项目
        config_manager = ConfigManager()
        generator = ProjectGenerator(config, config_manager)
        
        if preview:
            generator.preview()
        else:
            project_path = generator.generate(output, save_config)
            
        console.print("[green]✅ 项目生成完成！[/green]")
        
    except KeyboardInterrupt:
        console.print("\n[yellow]操作已取消[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[red]错误: {str(e)}[/red]")
        sys.exit(1)


@cli.command()
def templates():
    """查看可用的模板列表"""
    console.print(Panel.fit(
        Text("可用模板列表", style="bold green"),
        border_style="green"
    ))
    
    templates_info = [
        "📁 单模块项目模板",
        "📁 多模块项目模板",
        "🔧 MyBatis集成模板",
        "🔧 JPA集成模板",
        "🔧 Redis集成模板",
        "🔧 RabbitMQ集成模板",
        "🔧 Kafka集成模板",
        "📚 Swagger文档模板",
        "🔒 Spring Security模板",
    ]
    
    for template in templates_info:
        console.print(f"  {template}")


@cli.command()
@click.argument('config_name')
@click.option('--output', '-o', help='输出目录')
def generate(config_name, output):
    """从配置文件生成项目"""
    try:
        config_manager = ConfigManager()
        
        # 检查配置文件是否存在
        if not config_manager.config_exists(config_name):
            console.print(f"[red]❌ 配置文件不存在: {config_name}[/red]")
            return
        
        # 从配置文件生成项目
        generator = ProjectGenerator(None, config_manager)
        project_path = generator.generate_from_config_file(config_name, output)
        
        console.print(f"[green]✅ 项目生成成功: {project_path}[/green]")
        
    except Exception as e:
        console.print(f"[red]❌ 错误: {str(e)}[/red]")


@cli.command()
def list_configs():
    """列出所有配置文件"""
    try:
        config_manager = ConfigManager()
        configs = config_manager.list_configs()
        
        if not configs:
            console.print("[yellow]📝 暂无保存的配置文件[/yellow]")
            return
        
        console.print("\n[green]📋 已保存的配置文件:[/green]")
        for config_name in configs:
            info = config_manager.get_config_info(config_name)
            if 'error' not in info:
                console.print(f"  • {config_name} - {info.get('project_name', 'Unknown')} (Java {info.get('java_version', 'Unknown')})")
            else:
                console.print(f"  • {config_name} - [red][错误: 无法读取][/red]")
        
    except Exception as e:
        console.print(f"[red]❌ 错误: {str(e)}[/red]")


@cli.command()
@click.argument('config_name')
def show_config(config_name):
    """显示配置文件详情"""
    try:
        config_manager = ConfigManager()
        
        if not config_manager.config_exists(config_name):
            console.print(f"[red]❌ 配置文件不存在: {config_name}[/red]")
            return
        
        config = config_manager.load_config(config_name)
        
        console.print(f"\n[blue]📄 配置文件: {config_name}[/blue]")
        console.print(f"项目名称: {config.get(ProjectConstants.CONFIG_NAME)}")
        console.print(f"包名: {config.get(ProjectConstants.CONFIG_PACKAGE)}")
        console.print(f"版本: {config.get(ProjectConstants.CONFIG_VERSION)}")
        console.print(f"描述: {config.get(ProjectConstants.CONFIG_DESCRIPTION)}")
        console.print(f"Java版本: {config.get(ProjectConstants.CONFIG_JAVA_VERSION)}")
        console.print(f"Spring Boot版本: {config.get(ProjectConstants.CONFIG_SPRING_BOOT_VERSION)}")
        console.print(f"项目类型: {config.get(ProjectConstants.CONFIG_PROJECT_TYPE)}")
        
        tech_stack = config.get(ProjectConstants.CONFIG_TECH_STACK, {})
        if tech_stack:
            console.print("\n[green]🔧 技术栈:[/green]")
            for key, value in tech_stack.items():
                if value:
                    if isinstance(value, list):
                        value = ', '.join(value) if value else '无'
                    console.print(f"  {key}: {value}")
        
    except Exception as e:
        console.print(f"[red]❌ 错误: {str(e)}[/red]")


@cli.command()
@click.argument('config_name')
@click.confirmation_option(prompt='确定要删除此配置文件吗?')
def delete_config(config_name):
    """删除配置文件"""
    try:
        config_manager = ConfigManager()
        
        if not config_manager.config_exists(config_name):
            console.print(f"[red]❌ 配置文件不存在: {config_name}[/red]")
            return
        
        if config_manager.delete_config(config_name):
            console.print(f"[green]✅ 配置文件已删除: {config_name}[/green]")
        else:
            console.print(f"[red]❌ 删除配置文件失败: {config_name}[/red]")
        
    except Exception as e:
        console.print(f"[red]❌ 错误: {str(e)}[/red]")


@cli.command()
@click.argument('config_name')
@click.argument('export_path')
def export_config(config_name, export_path):
    """导出配置文件"""
    try:
        config_manager = ConfigManager()
        
        if not config_manager.config_exists(config_name):
            console.print(f"[red]❌ 配置文件不存在: {config_name}[/red]")
            return
        
        config_manager.export_config(config_name, export_path)
        console.print(f"[green]✅ 配置文件已导出: {export_path}[/green]")
        
    except Exception as e:
        console.print(f"[red]❌ 错误: {str(e)}[/red]")


@cli.command()
@click.argument('import_path')
@click.option('--config-name', help='配置文件名称')
def import_config(import_path, config_name):
    """导入配置文件"""
    try:
        config_manager = ConfigManager()
        
        config_file = config_manager.import_config(import_path, config_name)
        console.print(f"[green]✅ 配置文件已导入: {config_file}[/green]")
        
    except Exception as e:
        console.print(f"[red]❌ 错误: {str(e)}[/red]")


@cli.command()
@click.argument('project_path', type=click.Path(exists=True))
def update(project_path):
    """更新已有项目的配置"""
    console.print(f"[yellow]更新项目: {project_path}[/yellow]")
    console.print("[red]此功能正在开发中...[/red]")


def main():
    """主入口函数"""
    cli()


if __name__ == '__main__':
    main()