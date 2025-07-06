#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
交互式配置模块
实现用户友好的交互式配置收集功能
"""

from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from typing import List, Optional

from .config import ProjectConfig, TechStack, ModuleConfig
from .utils import validate_project_name, validate_package_name
from scripts.core.config_manager import ConfigManager
from scripts.constants.project_constants import ProjectConstants

console = Console()


class InteractiveConfig:
    """交互式配置收集器"""
    
    def __init__(self, config_manager: ConfigManager = None):
        self.config = None
        self.config_manager = config_manager or ConfigManager()
    
    def collect_config(self, load_from_config: bool = False) -> ProjectConfig:
        """收集项目配置
        
        Args:
            load_from_config: 是否从已有配置文件加载
            
        Returns:
            ProjectConfig: 项目配置对象
        """
        try:
            console.print("\n[bold blue]🚀 欢迎使用SpringBoot项目脚手架生成器！[/bold blue]")
            console.print("请按照提示输入项目信息...\n")
            
            # 询问是否从已有配置加载
            if load_from_config or self._ask_load_from_config():
                config = self._load_existing_config()
                if config:
                    return config
            
            # 基本信息收集
            basic_info = self._collect_basic_info()
            
            # 技术版本选择
            versions = self._collect_versions()
            
            # 项目结构选择
            structure = self._collect_structure()
            
            # 技术栈选择
            tech_stack = self._collect_tech_stack()
            
            # 生成选项
            options = self._collect_options()
            
            # 创建配置对象
            config = ProjectConfig(
                name=basic_info['name'],
                package=basic_info['package'],
                version=basic_info['version'],
                description=basic_info['description'],
                java_version=versions['java_version'],
                spring_version=versions['spring_version'],
                multi_module=structure['multi_module'],
                modules=structure['modules'],
                tech_stack=tech_stack,
                output_dir=basic_info['output_dir'],
                generate_sample_code=options['generate_sample_code'],
                generate_tests=options['generate_tests'],
                generate_docker=options['generate_docker']
            )
            
            # 显示配置摘要
            self._show_config_summary(config)
            
            # 询问是否保存配置
            self._ask_save_config(config)
            
            # 确认配置
            if not Confirm.ask("确认以上配置并开始生成项目？"):
                console.print("[yellow]配置已取消[/yellow]")
                return None
            
            return config
            
        except Exception as e:
            import traceback
            console.print(f"[red]❌ 收集配置失败: {str(e)}[/red]")
            console.print(f"[red]详细错误信息: {traceback.format_exc()}[/red]")
            return None
    
    def _collect_basic_info(self) -> dict:
        """收集基本信息"""
        console.print(Panel.fit(
            Text("📋 基本信息配置", style="bold green"),
            border_style="green"
        ))
        
        # 项目名称
        while True:
            name = Prompt.ask("项目名称 (例: my-spring-app)")
            if validate_project_name(name):
                break
            else:
                console.print(f"[red]项目名称格式不正确，请使用小写字母、数字和连字符[/red]")
        
        # 基础包名
        while True:
            package = Prompt.ask("基础包名 (例: com.example.myapp)")
            if validate_package_name(package):
                break
            else:
                console.print(f"[red]包名格式不正确，请使用标准Java包名格式[/red]")
        
        # 项目版本
        version = Prompt.ask("项目版本", default="1.0.0")
        
        # 项目描述
        description = Prompt.ask("项目描述", default=f"{name} - SpringBoot项目")
        
        # 输出目录
        output_dir = Prompt.ask("输出目录", default=".")
        
        return {
            'name': name,
            'package': package,
            'version': version,
            'description': description,
            'output_dir': output_dir
        }
    
    def _collect_versions(self) -> dict:
        """收集技术版本信息"""
        console.print(Panel.fit(
            Text("🔧 技术版本选择", style="bold green"),
            border_style="green"
        ))
        
        # Java版本
        console.print("选择Java版本:")
        console.print("1. Java 8")
        console.print("2. Java 11 (推荐)")
        console.print("3. Java 17")
        console.print("4. Java 21")
        java_choice = Prompt.ask("请选择", choices=["1", "2", "3", "4"], default="2")
        java_version = {"1": "8", "2": "11", "3": "17", "4": "21"}[java_choice]
        
        # SpringBoot版本
        console.print("选择SpringBoot版本:")
        console.print("1. 2.7.18 (稳定版)")
        console.print("2. 3.0.13")
        console.print("3. 3.1.8")
        console.print("4. 3.2.2 (最新)")
        spring_choice = Prompt.ask("请选择", choices=["1", "2", "3", "4"], default="1")
        spring_version = {"1": "2.7.18", "2": "3.0.13", "3": "3.1.8", "4": "3.2.2"}[spring_choice]
        
        return {
            'java_version': java_version,
            'spring_version': spring_version
        }
    
    def _collect_structure(self) -> dict:
        """收集项目结构信息"""
        console.print(Panel.fit(
            Text("🏗️ 项目结构配置", style="bold green"),
            border_style="green"
        ))
        
        # 项目类型
        console.print("选择项目结构:")
        console.print("1. 单模块项目 (适合小型项目)")
        console.print("2. 多模块项目 (适合大型项目)")
        structure_choice = Prompt.ask("请选择", choices=["1", "2"], default="1")
        multi_module = structure_choice == "2"
        
        modules = []
        if multi_module:
            # 模块选择
            available_modules = [
                ('common', '公共模块'),
                ('api', 'API接口模块'),
                ('service', '业务服务模块'),
                ('dao', '数据访问模块'),
                ('web', 'Web控制器模块'),
                ('admin', '管理后台模块'),
                ('task', '定时任务模块'),
            ]
            
            console.print("选择要创建的模块 (输入数字，用逗号分隔，如: 1,2,3):")
            for i, (name, desc) in enumerate(available_modules, 1):
                console.print(f"{i}. {name} - {desc}")
            module_input = Prompt.ask("请选择模块", default="1,2,3,4,5")
            selected_indices = [int(x.strip()) for x in module_input.split(',') if x.strip().isdigit()]
            selected_modules = [available_modules[i-1][0] for i in selected_indices if 1 <= i <= len(available_modules)]
            
            modules = [ModuleConfig(name, dict(available_modules)[name]) for name in selected_modules]
        
        return {
            'multi_module': multi_module,
            'modules': modules
        }
    
    def _collect_tech_stack(self) -> TechStack:
        """收集技术栈信息"""
        console.print(Panel.fit(
            Text("🛠️ 技术栈配置", style="bold green"),
            border_style="green"
        ))
        
        # 数据库选择
        console.print("选择数据库:")
        console.print("1. MySQL")
        console.print("2. PostgreSQL")
        console.print("3. H2 (内存数据库)")
        db_choice = Prompt.ask("请选择", choices=["1", "2", "3"], default="1")
        database = {"1": "mysql", "2": "postgresql", "3": "h2"}[db_choice]
        
        # ORM框架
        console.print("选择ORM框架:")
        console.print("1. MyBatis (推荐)")
        console.print("2. JPA/Hibernate")
        orm_choice = Prompt.ask("请选择", choices=["1", "2"], default="1")
        orm = {"1": "mybatis", "2": "jpa"}[orm_choice]
        
        # 缓存组件
        console.print("选择缓存组件 (输入数字，用逗号分隔):")
        console.print("1. Redis")
        console.print("2. Caffeine (本地缓存)")
        cache_input = Prompt.ask("请选择缓存组件", default="1")
        cache_indices = [int(x.strip()) for x in cache_input.split(',') if x.strip().isdigit()]
        cache_options = {"1": "redis", "2": "caffeine"}
        cache = [cache_options[str(i)] for i in cache_indices if str(i) in cache_options]
        
        # 消息队列
        console.print("选择消息队列 (输入数字，用逗号分隔，留空表示不使用):")
        console.print("1. RabbitMQ")
        console.print("2. Apache Kafka")
        mq_input = Prompt.ask("请选择消息队列", default="")
        mq_indices = [int(x.strip()) for x in mq_input.split(',') if x.strip().isdigit()]
        mq_options = {"1": "rabbitmq", "2": "kafka"}
        mq = [mq_options[str(i)] for i in mq_indices if str(i) in mq_options]
        
        # 文档工具
        doc = Confirm.ask("集成Swagger API文档？", default=True)
        
        # 安全框架
        security = Confirm.ask("集成Spring Security？", default=False)
        
        # 其他组件
        mongodb = Confirm.ask("集成MongoDB？", default=False)
        
        elasticsearch = Confirm.ask("集成Elasticsearch？", default=False)
        
        # 监控组件
        actuator = Confirm.ask("集成Spring Boot Actuator监控？", default=True)
        
        return TechStack(
            database=database,
            orm=orm,
            cache=cache,
            mq=mq,
            doc=doc,
            security=security,
            mongodb=mongodb,
            elasticsearch=elasticsearch,
            actuator=actuator
        )
    
    def _collect_options(self) -> dict:
        """收集生成选项"""
        console.print(Panel.fit(
            Text("⚙️ 生成选项配置", style="bold green"),
            border_style="green"
        ))
        
        generate_sample_code = Confirm.ask("生成示例代码？", default=True)
        
        generate_tests = Confirm.ask("生成测试代码？", default=True)
        
        generate_docker = Confirm.ask("生成Docker配置？", default=True)
        
        return {
            'generate_sample_code': generate_sample_code,
            'generate_tests': generate_tests,
            'generate_docker': generate_docker
        }
    
    def _show_config_summary(self, config: ProjectConfig):
        """显示配置摘要"""
        console.print("\n" + "="*50)
        console.print(Panel.fit(
            Text("📋 配置摘要", style="bold yellow"),
            border_style="yellow"
        ))
        
        console.print(f"[bold]项目名称:[/bold] {config.name}")
        console.print(f"[bold]基础包名:[/bold] {config.package}")
        console.print(f"[bold]项目版本:[/bold] {config.version}")
        console.print(f"[bold]Java版本:[/bold] {config.java_version}")
        console.print(f"[bold]SpringBoot版本:[/bold] {config.spring_version}")
        console.print(f"[bold]项目类型:[/bold] {'多模块' if config.multi_module else '单模块'}")
        
        if config.multi_module:
            console.print(f"[bold]模块列表:[/bold] {', '.join([m.name for m in config.modules])}")
        
        console.print(f"[bold]数据库:[/bold] {config.tech_stack.database}")
        console.print(f"[bold]ORM框架:[/bold] {config.tech_stack.orm}")
        
        if config.tech_stack.cache and isinstance(config.tech_stack.cache, list):
            console.print(f"[bold]缓存组件:[/bold] {', '.join(config.tech_stack.cache)}")
        
        if config.tech_stack.mq and isinstance(config.tech_stack.mq, list):
            console.print(f"[bold]消息队列:[/bold] {', '.join(config.tech_stack.mq)}")
        
        console.print(f"[bold]API文档:[/bold] {'是' if config.tech_stack.doc else '否'}")
        console.print(f"[bold]安全框架:[/bold] {'是' if config.tech_stack.security else '否'}")
        console.print("="*50 + "\n")
    
    def _ask_load_from_config(self) -> bool:
        """询问是否从已有配置加载"""
        configs = self.config_manager.list_configs()
        if not configs:
            return False
        
        return Confirm.ask("\n是否从已有配置文件加载项目配置？", default=False)
    
    def _load_existing_config(self) -> Optional[ProjectConfig]:
        """加载已有配置"""
        configs = self.config_manager.list_configs()
        if not configs:
            console.print("[yellow]暂无已保存的配置文件[/yellow]")
            return None
        
        # 显示配置列表
        console.print("\n[green]📋 可用的配置文件:[/green]")
        choice_list = []
        for i, config_name in enumerate(configs):
            info = self.config_manager.get_config_info(config_name)
            if 'error' not in info:
                display_text = f"{config_name} - {info.get('project_name', 'Unknown')}"
                choice_list.append((display_text, config_name))
                console.print(f"{i+1}. {display_text}")
        
        if not choice_list:
            console.print("[yellow]没有可用的配置文件[/yellow]")
            return None
        
        # 选择配置
        console.print(f"{len(choice_list)+1}. 取消")
        
        choice_input = Prompt.ask("请选择", choices=[str(i) for i in range(1, len(choice_list)+2)], default=str(len(choice_list)+1))
        choice_index = int(choice_input) - 1
        
        if choice_index >= len(choice_list):
            selected = None
        else:
            selected = choice_list[choice_index][1]
        
        if not selected:
            return None
        
        try:
            config_dict = self.config_manager.load_config(selected)
            config = self._dict_to_config(config_dict)
            console.print(f"[green]✅ 已加载配置: {selected}[/green]")
            return config
        except Exception as e:
            console.print(f"[red]❌ 加载配置失败: {str(e)}[/red]")
            return None
    
    def _ask_save_config(self, config: ProjectConfig) -> None:
        """询问是否保存配置"""
        if Confirm.ask("\n是否保存此配置以便下次使用？", default=True):
            config_name = Prompt.ask("请输入配置名称", default=config.name)
            
            try:
                config_dict = self._config_to_dict(config)
                config_file = self.config_manager.save_config(config_dict, config_name)
                console.print(f"[green]✅ 配置已保存: {config_file}[/green]")
            except Exception as e:
                console.print(f"[red]❌ 保存配置失败: {str(e)}[/red]")
    
    def _config_to_dict(self, config: ProjectConfig) -> dict:
        """将ProjectConfig转换为字典"""
        return {
            'name': config.name,
            'package': config.package,
            'version': config.version,
            'description': config.description,
            'java_version': config.java_version,
            'spring_version': config.spring_version,
            'multi_module': config.multi_module,
            'tech_stack': {
                'database': config.tech_stack.database,
                'orm': config.tech_stack.orm,
                'cache': config.tech_stack.cache,
                'mq': config.tech_stack.mq,
                'doc': config.tech_stack.doc,
                'security': config.tech_stack.security,
                'mongodb': config.tech_stack.mongodb,
                'elasticsearch': config.tech_stack.elasticsearch,
                'web_framework': config.tech_stack.web_framework,
                'actuator': config.tech_stack.actuator,
                'test_framework': config.tech_stack.test_framework
            },
            'modules': [{
                'name': module.name,
                'description': module.description
            } for module in config.modules],
            'output_dir': getattr(config, 'output_dir', './output'),
            'generate_sample_code': getattr(config, 'generate_sample_code', True),
            'generate_tests': getattr(config, 'generate_tests', True),
            'generate_docker': getattr(config, 'generate_docker', True)
        }
    
    def _dict_to_config(self, config_dict: dict) -> ProjectConfig:
        """将字典转换为ProjectConfig对象"""
        # 创建技术栈配置
        tech_stack_dict = config_dict.get('tech_stack', {})
        
        # 确保cache和mq字段是列表类型
        cache = tech_stack_dict.get('cache', [])
        if not isinstance(cache, list):
            cache = []
        
        mq = tech_stack_dict.get('mq', [])
        if not isinstance(mq, list):
            mq = []
        
        # 确保test_framework字段是列表类型
        test_framework = tech_stack_dict.get('test_framework', ['junit5', 'mockito'])
        if not isinstance(test_framework, list):
            test_framework = ['junit5', 'mockito']
        
        tech_stack = TechStack(
            database=tech_stack_dict.get('database', 'mysql'),
            orm=tech_stack_dict.get('orm', 'mybatis'),
            cache=cache,
            mq=mq,
            doc=tech_stack_dict.get('doc', False),
            security=tech_stack_dict.get('security', False),
            mongodb=tech_stack_dict.get('mongodb', False),
            elasticsearch=tech_stack_dict.get('elasticsearch', False),
            web_framework=tech_stack_dict.get('web_framework', 'spring-web'),
            actuator=tech_stack_dict.get('actuator', True),
            test_framework=test_framework
        )
        
        # 创建模块配置
        modules = []
        for module_dict in config_dict.get('modules', []):
            modules.append(ModuleConfig(
                name=module_dict.get('name', ''),
                description=module_dict.get('description', '')
            ))
        
        # 创建项目配置
        return ProjectConfig(
            name=config_dict.get('name', 'my-spring-boot-project'),
            package=config_dict.get('package', 'com.example.project'),
            version=config_dict.get('version', '1.0.0'),
            description=config_dict.get('description', 'A Spring Boot project'),
            java_version=config_dict.get('java_version', '17'),
            spring_version=config_dict.get('spring_version', '3.2.2'),
            multi_module=config_dict.get('multi_module', False),
            modules=modules,
            tech_stack=tech_stack,
            output_dir=config_dict.get('output_dir', './output'),
            generate_sample_code=config_dict.get('generate_sample_code', True),
            generate_tests=config_dict.get('generate_tests', True),
            generate_docker=config_dict.get('generate_docker', True)
        )