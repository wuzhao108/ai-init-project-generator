#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置收集器 - 交互式收集Java项目配置信息

负责通过交互式界面收集用户的Java项目配置，包括：
- 基本项目信息
- JDK版本选择
- Maven/Gradle构建工具
- Spring Boot版本
- 技术栈选择
- 项目结构配置
"""

import json
from pathlib import Path
from rich.console import Console
from rich.prompt import Prompt, Confirm, IntPrompt
from rich.panel import Panel
from rich.text import Text
from datetime import datetime

console = Console()


class ConfigCollector:
    """配置收集器类"""
    
    def __init__(self):
        self.config = {}
        
        # 预定义的选项
        self.jdk_versions = [
            "8", "11", "17", "21"
        ]
        
        self.build_tools = [
            "Maven", "Gradle"
        ]
        
        self.spring_versions = [
            "3.2.0", "3.1.6", "3.0.13", "2.7.18"
        ]
        
        self.databases = [
            "MySQL", "PostgreSQL", "H2", "Oracle", "SQL Server", "无数据库"
        ]
        
        self.orm_frameworks = [
            "MyBatis", "JPA/Hibernate", "MyBatis-Plus", "无ORM"
        ]
        
        self.cache_options = [
            "Redis", "Caffeine", "Ehcache", "无缓存"
        ]
        
        self.mq_options = [
            "RabbitMQ", "Apache Kafka", "RocketMQ", "无消息队列"
        ]
    
    def collect_config(self):
        """收集完整的项目配置"""
        try:
            console.print(Panel.fit(
                Text("📋 Java项目配置收集", style="bold green"),
                subtitle="请按照提示输入项目配置信息",
                border_style="green"
            ))
            console.print()
            
            # 收集基本信息
            self._collect_basic_info()
            
            # 收集技术版本
            self._collect_tech_versions()
            
            # 设置为单模块项目（简化配置）
            self.config.update({
                "is_multi_module": False,
                "modules": []
            })
            
            # 收集技术栈
            self._collect_tech_stack()
            
            # 收集生成选项
            self._collect_generation_options()
            
            # 显示配置摘要并确认
            if self._confirm_config():
                return self.config
            else:
                return None
                
        except KeyboardInterrupt:
            console.print("\n[yellow]配置收集已取消[/yellow]")
            return None
        except Exception as e:
            console.print(f"\n[red]配置收集失败: {str(e)}[/red]")
            return None
    
    def _collect_basic_info(self):
        """收集基本项目信息"""
        console.print("[bold blue]📋 基本项目信息[/bold blue]")
        
        # 项目名称
        project_name = Prompt.ask(
            "项目名称",
            default="my-java-app"
        )
        
        # 包名
        package_name = Prompt.ask(
            "基础包名",
            default=f"com.example.{project_name.replace('-', '').lower()}"
        )
        
        # 项目版本
        version = Prompt.ask(
            "项目版本",
            default="1.0.0"
        )
        
        # 项目描述
        description = Prompt.ask(
            "项目描述",
            default=f"{project_name} - Java应用程序"
        )
        
        self.config.update({
            "project_name": project_name,
            "package_name": package_name,
            "version": version,
            "description": description
        })
        
        console.print("[green]✅ 基本信息收集完成[/green]\n")
    
    def _collect_tech_versions(self):
        """收集技术版本信息"""
        console.print("[bold blue]🔧 技术版本选择[/bold blue]")
        
        # JDK版本选择
        console.print("可选JDK版本:")
        for i, version in enumerate(self.jdk_versions, 1):
            console.print(f"  {i}. Java {version}")
        
        jdk_choice = IntPrompt.ask(
            "请选择JDK版本",
            choices=[str(i) for i in range(1, len(self.jdk_versions) + 1)],
            default=3  # Java 17
        )
        jdk_version = self.jdk_versions[jdk_choice - 1]
        
        # 构建工具选择
        console.print("\n可选构建工具:")
        for i, tool in enumerate(self.build_tools, 1):
            console.print(f"  {i}. {tool}")
        
        build_choice = IntPrompt.ask(
            "请选择构建工具",
            choices=[str(i) for i in range(1, len(self.build_tools) + 1)],
            default=1  # Maven
        )
        build_tool = self.build_tools[build_choice - 1]
        
        # Spring Boot版本选择
        console.print("\n可选Spring Boot版本:")
        for i, version in enumerate(self.spring_versions, 1):
            console.print(f"  {i}. Spring Boot {version}")
        
        spring_choice = IntPrompt.ask(
            "请选择Spring Boot版本",
            choices=[str(i) for i in range(1, len(self.spring_versions) + 1)],
            default=1  # 最新版本
        )
        spring_version = self.spring_versions[spring_choice - 1]
        
        self.config.update({
            "jdk_version": jdk_version,
            "build_tool": build_tool,
            "spring_boot_version": spring_version
        })
        
        console.print("[green]✅ 技术版本选择完成[/green]\n")
    

    
    def _collect_tech_stack(self):
        """收集技术栈信息"""
        console.print("[bold blue]🛠️ 技术栈选择[/bold blue]")
        
        # 数据库选择
        console.print("可选数据库:")
        for i, db in enumerate(self.databases, 1):
            console.print(f"  {i}. {db}")
        
        db_choice = IntPrompt.ask(
            "请选择数据库",
            choices=[str(i) for i in range(1, len(self.databases) + 1)],
            default=1  # MySQL
        )
        database = self.databases[db_choice - 1]
        
        # ORM框架选择
        orm_framework = "无ORM"
        if database != "无数据库":
            console.print("\n可选ORM框架:")
            for i, orm in enumerate(self.orm_frameworks, 1):
                console.print(f"  {i}. {orm}")
            
            orm_choice = IntPrompt.ask(
                "请选择ORM框架",
                choices=[str(i) for i in range(1, len(self.orm_frameworks) + 1)],
                default=1  # MyBatis
            )
            orm_framework = self.orm_frameworks[orm_choice - 1]
        
        # 缓存选择
        console.print("\n可选缓存组件:")
        for i, cache in enumerate(self.cache_options, 1):
            console.print(f"  {i}. {cache}")
        
        cache_choice = IntPrompt.ask(
            "请选择缓存组件",
            choices=[str(i) for i in range(1, len(self.cache_options) + 1)],
            default=1  # Redis
        )
        cache = self.cache_options[cache_choice - 1]
        
        # 消息队列选择
        console.print("\n可选消息队列:")
        for i, mq in enumerate(self.mq_options, 1):
            console.print(f"  {i}. {mq}")
        
        mq_choice = IntPrompt.ask(
            "请选择消息队列",
            choices=[str(i) for i in range(1, len(self.mq_options) + 1)],
            default=4  # 无消息队列
        )
        message_queue = self.mq_options[mq_choice - 1]
        
        # 其他组件选择
        include_swagger = Confirm.ask("\n是否包含Swagger API文档？", default=True)
        include_security = Confirm.ask("是否包含Spring Security？", default=False)
        include_actuator = Confirm.ask("是否包含Spring Boot Actuator监控？", default=True)
        
        self.config.update({
            "database": database,
            "orm_framework": orm_framework,
            "cache": cache,
            "message_queue": message_queue,
            "include_swagger": include_swagger,
            "include_security": include_security,
            "include_actuator": include_actuator
        })
        
        console.print("[green]✅ 技术栈选择完成[/green]\n")
    
    def _collect_generation_options(self):
        """收集生成选项"""
        console.print("[bold blue]⚙️ 生成选项配置[/bold blue]")
        
        generate_sample_code = Confirm.ask(
            "是否生成示例代码？",
            default=True
        )
        
        generate_tests = Confirm.ask(
            "是否生成测试代码？",
            default=True
        )
        
        generate_docker = Confirm.ask(
            "是否生成Docker配置？",
            default=True
        )
        
        generate_readme = Confirm.ask(
            "是否生成README文档？",
            default=True
        )
        
        self.config.update({
            "generate_sample_code": generate_sample_code,
            "generate_tests": generate_tests,
            "generate_docker": generate_docker,
            "generate_readme": generate_readme,
            "created_at": datetime.now().isoformat()
        })
        
        console.print("[green]✅ 生成选项配置完成[/green]\n")
    
    def _confirm_config(self):
        """显示配置摘要并确认"""
        console.print(Panel.fit(
            Text("📋 配置摘要", style="bold blue"),
            border_style="blue"
        ))
        
        # 显示基本信息
        console.print("[bold]基本信息:[/bold]")
        console.print(f"  项目名称: {self.config['project_name']}")
        console.print(f"  包名: {self.config['package_name']}")
        console.print(f"  版本: {self.config['version']}")
        console.print(f"  描述: {self.config['description']}")
        
        # 显示技术版本
        console.print("\n[bold]技术版本:[/bold]")
        console.print(f"  JDK版本: {self.config['jdk_version']}")
        console.print(f"  构建工具: {self.config['build_tool']}")
        console.print(f"  Spring Boot版本: {self.config['spring_boot_version']}")
        
        # 显示项目结构
        console.print("\n[bold]项目结构:[/bold]")
        console.print(f"  项目类型: 单模块项目")
        
        # 显示技术栈
        console.print("\n[bold]技术栈:[/bold]")
        console.print(f"  数据库: {self.config['database']}")
        console.print(f"  ORM框架: {self.config['orm_framework']}")
        console.print(f"  缓存: {self.config['cache']}")
        console.print(f"  消息队列: {self.config['message_queue']}")
        console.print(f"  Swagger文档: {'是' if self.config['include_swagger'] else '否'}")
        console.print(f"  Spring Security: {'是' if self.config['include_security'] else '否'}")
        console.print(f"  监控组件: {'是' if self.config['include_actuator'] else '否'}")
        
        # 显示生成选项
        console.print("\n[bold]生成选项:[/bold]")
        console.print(f"  示例代码: {'是' if self.config['generate_sample_code'] else '否'}")
        console.print(f"  测试代码: {'是' if self.config['generate_tests'] else '否'}")
        console.print(f"  Docker配置: {'是' if self.config['generate_docker'] else '否'}")
        console.print(f"  README文档: {'是' if self.config['generate_readme'] else '否'}")
        
        console.print()
        return Confirm.ask("确认以上配置并生成上下文工程？", default=True)