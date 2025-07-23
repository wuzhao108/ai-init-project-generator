#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
上下文工程生成器 - Java项目初始化上下文提示词生成工具 v3.1.0

这是一个基于Python的交互式工具，用于生成Java项目初始化的上下文提示词。
支持多种技术栈配置，智能配置验证，完整日志记录，生成系统提示词和用户提示词，
以及Gemini和Claude Code斜杠命令文件。

版本历史:
- v3.1.0 (2025-01-23): 代码审查优化和功能增强
  * 新增智能配置验证机制
  * 增强错误处理和日志系统
  * 支持多模块项目和模板化
  * 添加完整单元测试框架
- v3.0.0 (2025-01-07): 上下文工程生成器重构
- v2.1.0 (2025-07-06): 日志管理系统规范化
- v2.0.0 (2025-01-07): 配置管理系统V2重构

使用方法:
    python main.py
"""

import sys
import os
import logging
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt, Confirm
from datetime import datetime

# 添加项目根目录到Python路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# 配置日志系统
def setup_logging():
    """配置日志系统"""
    log_dir = Path("./logs")
    log_dir.mkdir(exist_ok=True)
    
    log_file = log_dir / f"app_{datetime.now().strftime('%Y%m%d')}.log"
    
    # 配置日志格式
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

# 初始化日志
logger = setup_logging()

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
        logger.info("程序启动")
        
        # 确保必要的目录存在
        ensure_directories()
        
        # 显示欢迎界面
        show_welcome()
        
        # 启动交互式主菜单
        interactive_main_menu()
        
        logger.info("程序正常结束")
        
    except KeyboardInterrupt:
        console.print("\n\n[yellow]👋 用户取消操作，再见！[/yellow]")
        logger.info("用户中断程序")
        sys.exit(0)
    except ImportError as e:
        error_msg = f"模块导入错误: {e}"
        console.print(f"\n[red]❌ {error_msg}[/red]")
        console.print("[yellow]💡 请检查以下事项:[/yellow]")
        console.print("  1. 是否正确安装了所有依赖包")
        console.print("  2. 运行 pip install -r requirements.txt")
        console.print("  3. 检查Python环境和包路径配置")
        logger.error(error_msg, exc_info=True)
        sys.exit(1)
    except FileNotFoundError as e:
        error_msg = f"文件或目录不存在: {e}"
        console.print(f"\n[red]❌ {error_msg}[/red]")
        console.print("[yellow]💡 请检查项目文件是否完整[/yellow]")
        logger.error(error_msg, exc_info=True)
        sys.exit(1)
    except PermissionError as e:
        error_msg = f"权限错误: {e}"
        console.print(f"\n[red]❌ {error_msg}[/red]")
        console.print("[yellow]💡 请检查文件和目录的读写权限[/yellow]")
        logger.error(error_msg, exc_info=True)
        sys.exit(1)
    except Exception as e:
        error_msg = f"未知错误: {e}"
        console.print(f"\n[red]❌ {error_msg}[/red]")
        console.print("[yellow]💡 详细错误信息已记录到日志文件中[/yellow]")
        logger.error(error_msg, exc_info=True)
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
        logger.info("开始生成上下文工程")
        
        # 收集用户配置
        collector = ConfigCollector()
        config = collector.collect_config()
        
        if not config:
            console.print("[yellow]操作已取消[/yellow]")
            logger.info("用户取消配置收集")
            return
        
        logger.info(f"配置收集完成，项目名称: {config.get('project_name', 'unknown')}")
        
        # 生成上下文工程
        generator = ContextGenerator()
        output_path = generator.generate(config)
        
        console.print(f"[green]✅ 上下文工程生成完成！[/green]")
        console.print(f"[green]📁 输出路径: {output_path}[/green]")
        logger.info(f"上下文工程生成成功，输出路径: {output_path}")
        
        # 显示生成的文件列表
        show_generated_files(output_path)
        
    except ValueError as e:
        error_msg = f"配置验证失败: {e}"
        console.print(f"[red]❌ {error_msg}[/red]")
        logger.error(error_msg)
    except FileNotFoundError as e:
        error_msg = f"文件或目录不存在: {e}"
        console.print(f"[red]❌ {error_msg}[/red]")
        console.print("[yellow]💡 请检查项目目录结构是否完整[/yellow]")
        logger.error(error_msg, exc_info=True)
    except PermissionError as e:
        error_msg = f"权限错误: {e}"
        console.print(f"[red]❌ {error_msg}[/red]")
        console.print("[yellow]💡 请检查输出目录的写入权限[/yellow]")
        logger.error(error_msg, exc_info=True)
    except Exception as e:
        error_msg = f"生成上下文工程失败: {str(e)}"
        console.print(f"[red]❌ {error_msg}[/red]")
        console.print("[yellow]💡 详细错误信息已记录到日志文件中[/yellow]")
        logger.error(error_msg, exc_info=True)


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