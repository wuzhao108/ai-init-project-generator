#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spring Boot项目生成器 - 交互式主入口文件

这是一个基于Python的交互式工具，用于快速生成Spring Boot项目模板。
支持多种技术栈配置、项目结构定制和配置文件管理。

使用方法:
    python main.py
"""

import sys
import os
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt, Confirm

# 添加项目根目录到Python路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

try:
    from scripts.core.interactive_config import InteractiveConfig
    from scripts.core.project_generator import ProjectGenerator
    from scripts.core.config_manager import ConfigManager
except ImportError as e:
    print(f"导入错误: {e}")
    print("请确保所有依赖已正确安装")
    sys.exit(1)

console = Console()


def main():
    """主入口函数"""
    try:
        # 确保必要的目录存在
        ensure_directories()
        
        # 显示欢迎界面
        show_welcome()
        
        # 启动交互式主菜单
        interactive_main_menu()
        
    except KeyboardInterrupt:
        console.print("\n\n[yellow]👋 再见！[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[red]❌ 发生错误: {e}[/red]")
        sys.exit(1)


def show_welcome():
    """显示欢迎界面"""
    console.print(Panel.fit(
        Text("🚀 SpringBoot项目脚手架生成器", style="bold blue"),
        subtitle="一个基于Python的交互式项目生成工具",
        border_style="blue"
    ))
    console.print()


def interactive_main_menu():
    """交互式主菜单"""
    while True:
        console.print("[bold green]📋 请选择操作:[/bold green]")
        console.print("1. 🆕 创建项目模板")
        console.print("2. 📁 从配置文件生成项目")
        console.print("3. 📋 查看已保存的配置")
        console.print("4. 📄 查看配置详情")
        console.print("5. 🗑️  删除配置文件")
        console.print("6. 📤 导出配置文件")
        console.print("7. 📥 导入配置文件")
        console.print("8. 📚 查看可用模板")
        console.print("9. 🚪 退出程序")
        console.print()
        
        choice = Prompt.ask("请选择操作", choices=["1", "2", "3", "4", "5", "6", "7", "8", "9"], default="1")
        console.print()
        
        if choice == "1":
            create_new_project()
        elif choice == "2":
            generate_from_config()
        elif choice == "3":
            list_configs()
        elif choice == "4":
            show_config_details()
        elif choice == "5":
            delete_config()
        elif choice == "6":
            export_config()
        elif choice == "7":
            import_config()
        elif choice == "8":
            show_templates()
        elif choice == "9":
            console.print("[yellow]👋 再见！[/yellow]")
            break
        
        console.print("\n" + "="*50 + "\n")


def create_new_project():
    """创建新项目的交互式流程"""
    console.print(Panel.fit(
        Text("🆕 创建项目模板", style="bold green"),
        border_style="green"
    ))
    
    try:
        # 询问用户选择默认模板还是自定义创建
        console.print("[bold blue]请选择创建方式:[/bold blue]")
        console.print("1. 📋 使用默认模板创建")
        console.print("2. ⚙️ 自定义配置创建")
        
        choice = Prompt.ask("请选择", choices=["1", "2"], default="1")
        
        if choice == "1":
            # 使用默认模板
            create_from_default_template()
        else:
            # 自定义创建
            create_with_custom_config()
        
    except Exception as e:
        console.print(f"[red]❌ 创建项目失败: {str(e)}[/red]")


def create_from_default_template():
    """使用默认模板创建项目"""
    console.print(Panel.fit(
        Text("📋 默认模板配置", style="bold blue"),
        border_style="blue"
    ))
    
    try:
        # 加载默认模板配置
        config_manager = ConfigManager()
        default_config_path = project_root / "configs" / "default_template.json"
        
        if not default_config_path.exists():
            console.print("[red]❌ 默认模板配置文件不存在[/red]")
            return
        
        # 读取默认配置
        import json
        with open(default_config_path, 'r', encoding='utf-8') as f:
            default_config = json.load(f)
        
        # 显示默认配置详情
        show_default_config_details(default_config)
        
        # 询问是否继续
        if Confirm.ask("\n是否使用以上默认配置创建项目？", default=True):
            # 直接生成项目到output目录
            output_dir = "./output"
            
            # 创建ProjectConfig对象
            interactive = InteractiveConfig()
            config = interactive._dict_to_config(default_config)
            
            # 生成项目
            generator = ProjectGenerator(config, config_manager)
            project_path = generator.generate(output_dir, True)
            console.print(f"[green]✅ 项目生成完成！路径: {project_path}[/green]")
        else:
            # 用户选择否，走自定义逻辑
            console.print("[yellow]切换到自定义配置模式...[/yellow]")
            create_with_custom_config()
    
    except Exception as e:
        console.print(f"[red]❌ 使用默认模板创建失败: {str(e)}[/red]")


def create_with_custom_config():
    """使用自定义配置创建项目"""
    console.print(Panel.fit(
        Text("⚙️ 自定义配置创建", style="bold green"),
        border_style="green"
    ))
    
    try:
        # 启动交互式配置收集
        interactive = InteractiveConfig()
        config = interactive.collect_config()
        
        if not config:
            console.print("[yellow]项目创建已取消[/yellow]")
            return
        
        # 显示用户选择后的详细配置
        show_custom_config_details(config)
        
        # 询问是否生成
        if Confirm.ask("\n确认以上配置并生成项目？", default=True):
            # 生成项目到output目录
            output_dir = "./output"
            
            config_manager = ConfigManager()
            generator = ProjectGenerator(config, config_manager)
            project_path = generator.generate(output_dir, True)
            console.print(f"[green]✅ 项目生成完成！路径: {project_path}[/green]")
        else:
            console.print("[yellow]项目生成已取消[/yellow]")
        
    except Exception as e:
        console.print(f"[red]❌ 自定义配置创建失败: {str(e)}[/red]")


def show_default_config_details(config):
    """显示默认配置详情"""
    console.print("\n[blue]📋 默认模板配置详情:[/blue]")
    console.print(f"[bold]项目名称:[/bold] {config.get('name')}")
    console.print(f"[bold]基础包名:[/bold] {config.get('package')}")
    console.print(f"[bold]项目版本:[/bold] {config.get('version')}")
    console.print(f"[bold]项目描述:[/bold] {config.get('description')}")
    console.print(f"[bold]Java版本:[/bold] {config.get('java_version')}")
    console.print(f"[bold]SpringBoot版本:[/bold] {config.get('spring_version')}")
    console.print(f"[bold]项目类型:[/bold] {'多模块' if config.get('multi_module') else '单模块'}")
    
    tech_stack = config.get('tech_stack', {})
    if tech_stack:
        console.print("\n[green]🔧 技术栈配置:[/green]")
        console.print(f"[bold]数据库:[/bold] {tech_stack.get('database')}")
        console.print(f"[bold]ORM框架:[/bold] {tech_stack.get('orm')}")
        
        cache = tech_stack.get('cache', [])
        if cache:
            console.print(f"[bold]缓存组件:[/bold] {', '.join(cache)}")
        
        mq = tech_stack.get('mq', [])
        if mq:
            console.print(f"[bold]消息队列:[/bold] {', '.join(mq)}")
        
        console.print(f"[bold]API文档:[/bold] {'是' if tech_stack.get('doc') else '否'}")
        console.print(f"[bold]安全框架:[/bold] {'是' if tech_stack.get('security') else '否'}")
        console.print(f"[bold]MongoDB:[/bold] {'是' if tech_stack.get('mongodb') else '否'}")
        console.print(f"[bold]Elasticsearch:[/bold] {'是' if tech_stack.get('elasticsearch') else '否'}")
        console.print(f"[bold]监控组件:[/bold] {'是' if tech_stack.get('actuator') else '否'}")
    
    console.print(f"\n[bold]输出目录:[/bold] {config.get('output_dir')}")
    console.print(f"[bold]生成示例代码:[/bold] {'是' if config.get('generate_sample_code') else '否'}")
    console.print(f"[bold]生成测试代码:[/bold] {'是' if config.get('generate_tests') else '否'}")
    console.print(f"[bold]生成Docker配置:[/bold] {'是' if config.get('generate_docker') else '否'}")


def show_custom_config_details(config):
    """显示自定义配置详情"""
    console.print("\n[blue]📋 您的自定义配置详情:[/blue]")
    console.print(f"[bold]项目名称:[/bold] {config.name}")
    console.print(f"[bold]基础包名:[/bold] {config.package}")
    console.print(f"[bold]项目版本:[/bold] {config.version}")
    console.print(f"[bold]项目描述:[/bold] {config.description}")
    console.print(f"[bold]Java版本:[/bold] {config.java_version}")
    console.print(f"[bold]SpringBoot版本:[/bold] {config.spring_version}")
    console.print(f"[bold]项目类型:[/bold] {'多模块' if config.multi_module else '单模块'}")
    
    if config.multi_module and config.modules:
        console.print(f"[bold]模块列表:[/bold] {', '.join([m.name for m in config.modules])}")
    
    console.print("\n[green]🔧 技术栈配置:[/green]")
    console.print(f"[bold]数据库:[/bold] {config.tech_stack.database}")
    console.print(f"[bold]ORM框架:[/bold] {config.tech_stack.orm}")
    
    if config.tech_stack.cache and isinstance(config.tech_stack.cache, list):
        console.print(f"[bold]缓存组件:[/bold] {', '.join(config.tech_stack.cache)}")
    
    if config.tech_stack.mq and isinstance(config.tech_stack.mq, list):
        console.print(f"[bold]消息队列:[/bold] {', '.join(config.tech_stack.mq)}")
    
    console.print(f"[bold]API文档:[/bold] {'是' if config.tech_stack.doc else '否'}")
    console.print(f"[bold]安全框架:[/bold] {'是' if config.tech_stack.security else '否'}")
    console.print(f"[bold]MongoDB:[/bold] {'是' if config.tech_stack.mongodb else '否'}")
    console.print(f"[bold]Elasticsearch:[/bold] {'是' if config.tech_stack.elasticsearch else '否'}")
    console.print(f"[bold]监控组件:[/bold] {'是' if config.tech_stack.actuator else '否'}")
    
    console.print(f"\n[bold]输出目录:[/bold] {config.output_dir}")
    console.print(f"[bold]生成示例代码:[/bold] {'是' if config.generate_sample_code else '否'}")
    console.print(f"[bold]生成测试代码:[/bold] {'是' if config.generate_tests else '否'}")
    console.print(f"[bold]生成Docker配置:[/bold] {'是' if config.generate_docker else '否'}")


def generate_from_config():
    """从配置文件生成项目"""
    console.print(Panel.fit(
        Text("📁 从配置文件生成项目", style="bold green"),
        border_style="green"
    ))
    
    try:
        config_manager = ConfigManager()
        configs = config_manager.list_configs()
        
        if not configs:
            console.print("[yellow]📝 暂无保存的配置文件[/yellow]")
            return
        
        # 显示配置列表
        console.print("[green]📋 可用的配置文件:[/green]")
        for i, config_name in enumerate(configs, 1):
            info = config_manager.get_config_info(config_name)
            if 'error' not in info:
                console.print(f"{i}. {config_name} - {info.get('project_name', 'Unknown')}")
            else:
                console.print(f"{i}. {config_name} - [red][错误: 无法读取][/red]")
        
        # 选择配置
        choice_input = Prompt.ask("请选择配置文件", choices=[str(i) for i in range(1, len(configs)+1)])
        selected_config = configs[int(choice_input) - 1]
        
        # 询问输出目录
        output_dir = Prompt.ask("请输入输出目录", default="./output")
        
        # 生成项目
        generator = ProjectGenerator(None, config_manager)
        project_path = generator.generate_from_config_file(selected_config, output_dir)
        
        console.print(f"[green]✅ 项目生成成功: {project_path}[/green]")
        
    except Exception as e:
        console.print(f"[red]❌ 生成项目失败: {str(e)}[/red]")


def list_configs():
    """列出所有配置文件"""
    console.print(Panel.fit(
        Text("📋 查看已保存的配置", style="bold green"),
        border_style="green"
    ))
    
    try:
        config_manager = ConfigManager()
        configs = config_manager.list_configs()
        
        if not configs:
            console.print("[yellow]📝 暂无保存的配置文件[/yellow]")
            return
        
        console.print("[green]📋 已保存的配置文件:[/green]")
        for config_name in configs:
            info = config_manager.get_config_info(config_name)
            if 'error' not in info:
                console.print(f"  • {config_name} - {info.get('project_name', 'Unknown')} (Java {info.get('java_version', 'Unknown')})")
            else:
                console.print(f"  • {config_name} - [red][错误: 无法读取][/red]")
        
    except Exception as e:
        console.print(f"[red]❌ 错误: {str(e)}[/red]")


def show_config_details():
    """显示配置文件详情"""
    console.print(Panel.fit(
        Text("📄 查看配置详情", style="bold green"),
        border_style="green"
    ))
    
    try:
        config_manager = ConfigManager()
        configs = config_manager.list_configs()
        
        if not configs:
            console.print("[yellow]📝 暂无保存的配置文件[/yellow]")
            return
        
        # 显示配置列表
        console.print("[green]📋 可用的配置文件:[/green]")
        for i, config_name in enumerate(configs, 1):
            console.print(f"{i}. {config_name}")
        
        # 选择配置
        choice_input = Prompt.ask("请选择要查看的配置文件", choices=[str(i) for i in range(1, len(configs)+1)])
        selected_config = configs[int(choice_input) - 1]
        
        # 显示配置详情
        config = config_manager.load_config(selected_config)
        
        console.print(f"\n[blue]📄 配置文件: {selected_config}[/blue]")
        console.print(f"项目名称: {config.get('name')}")
        console.print(f"包名: {config.get('package')}")
        console.print(f"版本: {config.get('version')}")
        console.print(f"描述: {config.get('description')}")
        console.print(f"Java版本: {config.get('java_version')}")
        console.print(f"Spring Boot版本: {config.get('spring_version')}")
        console.print(f"项目类型: {'多模块' if config.get('multi_module') else '单模块'}")
        
        tech_stack = config.get('tech_stack', {})
        if tech_stack:
            console.print("\n[green]🔧 技术栈:[/green]")
            for key, value in tech_stack.items():
                if value:
                    if isinstance(value, list):
                        value = ', '.join(value) if value else '无'
                    console.print(f"  {key}: {value}")
        
    except Exception as e:
        console.print(f"[red]❌ 错误: {str(e)}[/red]")


def delete_config():
    """删除配置文件"""
    console.print(Panel.fit(
        Text("🗑️ 删除配置文件", style="bold red"),
        border_style="red"
    ))
    
    try:
        config_manager = ConfigManager()
        configs = config_manager.list_configs()
        
        if not configs:
            console.print("[yellow]📝 暂无保存的配置文件[/yellow]")
            return
        
        # 显示配置列表
        console.print("[green]📋 可用的配置文件:[/green]")
        for i, config_name in enumerate(configs, 1):
            console.print(f"{i}. {config_name}")
        
        # 选择配置
        choice_input = Prompt.ask("请选择要删除的配置文件", choices=[str(i) for i in range(1, len(configs)+1)])
        selected_config = configs[int(choice_input) - 1]
        
        # 确认删除
        if Confirm.ask(f"确定要删除配置文件 '{selected_config}' 吗？", default=False):
            if config_manager.delete_config(selected_config):
                console.print(f"[green]✅ 配置文件已删除: {selected_config}[/green]")
            else:
                console.print(f"[red]❌ 删除配置文件失败: {selected_config}[/red]")
        else:
            console.print("[yellow]删除操作已取消[/yellow]")
        
    except Exception as e:
        console.print(f"[red]❌ 错误: {str(e)}[/red]")


def export_config():
    """导出配置文件"""
    console.print(Panel.fit(
        Text("📤 导出配置文件", style="bold green"),
        border_style="green"
    ))
    
    try:
        config_manager = ConfigManager()
        configs = config_manager.list_configs()
        
        if not configs:
            console.print("[yellow]📝 暂无保存的配置文件[/yellow]")
            return
        
        # 显示配置列表
        console.print("[green]📋 可用的配置文件:[/green]")
        for i, config_name in enumerate(configs, 1):
            console.print(f"{i}. {config_name}")
        
        # 选择配置
        choice_input = Prompt.ask("请选择要导出的配置文件", choices=[str(i) for i in range(1, len(configs)+1)])
        selected_config = configs[int(choice_input) - 1]
        
        # 输入导出路径
        export_path = Prompt.ask("请输入导出路径", default=f"./{selected_config}.json")
        
        # 导出配置
        config_manager.export_config(selected_config, export_path)
        console.print(f"[green]✅ 配置文件已导出: {export_path}[/green]")
        
    except Exception as e:
        console.print(f"[red]❌ 错误: {str(e)}[/red]")


def import_config():
    """导入配置文件"""
    console.print(Panel.fit(
        Text("📥 导入配置文件", style="bold green"),
        border_style="green"
    ))
    
    try:
        config_manager = ConfigManager()
        
        # 输入导入路径
        import_path = Prompt.ask("请输入要导入的配置文件路径")
        
        # 输入配置名称（可选）
        config_name = Prompt.ask("请输入配置名称（留空使用文件名）", default="")
        config_name = config_name if config_name else None
        
        # 导入配置
        config_file = config_manager.import_config(import_path, config_name)
        console.print(f"[green]✅ 配置文件已导入: {config_file}[/green]")
        
    except Exception as e:
        console.print(f"[red]❌ 错误: {str(e)}[/red]")


def show_templates():
    """显示可用模板"""
    console.print(Panel.fit(
        Text("📚 可用模板列表", style="bold green"),
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


def ensure_directories():
    """确保必要的目录存在"""
    directories = [
        project_root / "output",
        project_root / "configs",
        project_root / "common" / "utils",
        project_root / "common" / "validators",
        project_root / "common" / "constants"
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    main()