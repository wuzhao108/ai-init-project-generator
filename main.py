#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
上下文工程生成器 - Java项目初始化上下文提示词生成工具

这是一个基于Python的交互式工具，用于生成Java项目初始化的上下文提示词。
支持多种技术栈配置，生成系统提示词和用户提示词，以及Gemini斜杠命令文件。

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
from datetime import datetime

# 添加项目根目录到Python路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

try:
    from scripts.core.context_generator import ContextGenerator
    from scripts.core.config_collector import ConfigCollector
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
        Text("🚀 Java项目上下文工程生成器", style="bold blue"),
        subtitle="生成项目初始化的上下文提示词和Gemini斜杠命令",
        border_style="blue"
    ))
    console.print()


def interactive_main_menu():
    """交互式主菜单"""
    while True:
        console.print("[bold green]📋 请选择操作:[/bold green]")
        console.print("1. 🆕 生成上下文工程")
        console.print("2. 📋 查看历史配置")
        console.print("3. 🚪 退出程序")
        console.print()
        
        choice = Prompt.ask("请选择操作", choices=["1", "2", "3"], default="1")
        console.print()
        
        if choice == "1":
            generate_context_project()
        elif choice == "2":
            show_history_configs()
        elif choice == "3":
            console.print("[yellow]👋 再见！[/yellow]")
            break
        
        console.print("\n" + "="*50 + "\n")


def generate_context_project():
    """生成上下文工程"""
    console.print(Panel.fit(
        Text("🆕 生成上下文工程", style="bold green"),
        border_style="green"
    ))
    
    try:
        # 收集用户配置
        collector = ConfigCollector()
        config = collector.collect_config()
        
        if not config:
            console.print("[yellow]操作已取消[/yellow]")
            return
        
        # 生成上下文工程
        generator = ContextGenerator()
        output_path = generator.generate(config)
        
        console.print(f"[green]✅ 上下文工程生成完成！[/green]")
        console.print(f"[green]📁 输出路径: {output_path}[/green]")
        
        # 显示生成的文件列表
        show_generated_files(output_path)
        
    except Exception as e:
        console.print(f"[red]❌ 生成上下文工程失败: {str(e)}[/red]")


def show_generated_files(output_path):
    """显示生成的文件列表"""
    console.print("\n[blue]📄 生成的文件:[/blue]")
    output_dir = Path(output_path)
    
    if output_dir.exists():
        for file_path in output_dir.rglob("*"):
            if file_path.is_file():
                relative_path = file_path.relative_to(output_dir)
                console.print(f"  📄 {relative_path}")


def show_history_configs():
    """显示历史配置"""
    console.print(Panel.fit(
        Text("📋 历史配置", style="bold blue"),
        border_style="blue"
    ))
    
    # 查找output目录下的历史配置
    output_dir = Path("./output")
    if not output_dir.exists():
        console.print("[yellow]暂无历史配置[/yellow]")
        return
    
    configs = []
    for item in output_dir.iterdir():
        if item.is_dir():
            config_file = item / "config.json"
            if config_file.exists():
                configs.append(item.name)
    
    if not configs:
        console.print("[yellow]暂无历史配置[/yellow]")
        return
    
    console.print("[green]历史配置列表:[/green]")
    for i, config in enumerate(configs, 1):
        console.print(f"  {i}. {config}")


def ensure_directories():
    """确保必要的目录存在"""
    directories = [
        "./output",
        "./scripts",
        "./scripts/core",
        "./scripts/templates"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    main()