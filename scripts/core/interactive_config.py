# -*- coding: utf-8 -*-
"""
交互式配置收集器模块
提供用户友好的交互式配置收集功能
"""

from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.text import Text
from typing import Dict, Any, List, Optional

from .config_manager import ConfigManager
from ..validators.project_validator import ProjectValidator
from ..constants.project_constants import ProjectConstants

console = Console()


class InteractiveConfig:
    """交互式配置收集器"""
    
    def __init__(self, config_manager: ConfigManager = None):
        """
        初始化交互式配置收集器
        
        Args:
            config_manager: 配置管理器实例
        """
        self.config_manager = config_manager or ConfigManager()
    
    def collect_config(self, load_from_existing: bool = False) -> Optional[Dict[str, Any]]:
        """
        收集项目配置
        
        Args:
            load_from_existing: 是否从已有配置文件加载
            
        Returns:
            Optional[Dict[str, Any]]: 项目配置字典，如果用户取消则返回None
        """
        try:
            console.print("\n[bold blue]🚀 欢迎使用SpringBoot项目脚手架生成器！[/bold blue]")
            console.print("请按照提示输入项目信息...\n")
            
            # 询问是否从已有配置加载
            if load_from_existing or self._ask_load_from_existing():
                config = self._load_existing_config()
                if config:
                    return config
            
            # 收集基本信息
            basic_info = self._collect_basic_info()
            if not basic_info:
                return None
            
            # 收集技术版本
            versions = self._collect_versions()
            if not versions:
                return None
            
            # 收集项目结构
            structure = self._collect_structure()
            if not structure:
                return None
            
            # 收集技术栈
            tech_stack = self._collect_tech_stack()
            if not tech_stack:
                return None
            
            # 收集生成选项
            options = self._collect_options()
            if not options:
                return None
            
            # 构建配置字典
            config = {
                ProjectConstants.CONFIG_NAME: basic_info['name'],
                ProjectConstants.CONFIG_PACKAGE: basic_info['package'],
                ProjectConstants.CONFIG_VERSION: basic_info['version'],
                ProjectConstants.CONFIG_DESCRIPTION: basic_info['description'],
                ProjectConstants.CONFIG_JAVA_VERSION: versions['java_version'],
                ProjectConstants.CONFIG_SPRING_BOOT_VERSION: versions['spring_version'],
                ProjectConstants.CONFIG_PROJECT_TYPE: structure['project_type'],
                ProjectConstants.CONFIG_MODULES: structure['modules'],
                ProjectConstants.CONFIG_TECH_STACK: tech_stack,
                ProjectConstants.CONFIG_OUTPUT_DIR: basic_info['output_dir'],
                ProjectConstants.CONFIG_GENERATE_SAMPLE_CODE: options['generate_sample_code'],
                ProjectConstants.CONFIG_GENERATE_TESTS: options['generate_tests'],
                ProjectConstants.CONFIG_GENERATE_DOCKER: options['generate_docker']
            }
            
            # 显示配置摘要
            self._show_config_summary(config)
            
            # 询问是否保存配置
            self._ask_save_config(config)
            
            # 确认配置
            if not Confirm.ask("确认以上配置并开始生成项目？"):
                console.print("[yellow]配置已取消[/yellow]")
                return None
            
            return config
            
        except KeyboardInterrupt:
            console.print("\n[yellow]用户取消操作[/yellow]")
            return None
        except Exception as e:
            console.print(f"[red]❌ 收集配置失败: {str(e)}[/red]")
            return None
    
    def collect_config_without_save(self, load_from_existing: bool = False) -> Optional[Dict[str, Any]]:
        """
        收集项目配置（不包含保存逻辑）
        
        Args:
            load_from_existing: 是否从已有配置文件加载
            
        Returns:
            Optional[Dict[str, Any]]: 项目配置字典，如果用户取消则返回None
        """
        try:
            console.print("\n[bold blue]🚀 欢迎使用SpringBoot项目脚手架生成器！[/bold blue]")
            console.print("请按照提示输入项目信息...\n")
            
            # 询问是否从已有配置加载
            if load_from_existing or self._ask_load_from_existing():
                config = self._load_existing_config()
                if config:
                    return config
            
            # 收集基本信息
            basic_info = self._collect_basic_info()
            if not basic_info:
                return None
            
            # 收集技术版本
            versions = self._collect_versions()
            if not versions:
                return None
            
            # 收集项目结构
            structure = self._collect_structure()
            if not structure:
                return None
            
            # 收集技术栈
            tech_stack = self._collect_tech_stack()
            if not tech_stack:
                return None
            
            # 收集生成选项
            options = self._collect_options()
            if not options:
                return None
            
            # 构建配置字典
            config = {
                ProjectConstants.CONFIG_NAME: basic_info['name'],
                ProjectConstants.CONFIG_PACKAGE: basic_info['package'],
                ProjectConstants.CONFIG_VERSION: basic_info['version'],
                ProjectConstants.CONFIG_DESCRIPTION: basic_info['description'],
                ProjectConstants.CONFIG_JAVA_VERSION: versions['java_version'],
                ProjectConstants.CONFIG_SPRING_BOOT_VERSION: versions['spring_version'],
                ProjectConstants.CONFIG_PROJECT_TYPE: structure['project_type'],
                ProjectConstants.CONFIG_MODULES: structure['modules'],
                ProjectConstants.CONFIG_TECH_STACK: tech_stack,
                ProjectConstants.CONFIG_OUTPUT_DIR: basic_info['output_dir'],
                ProjectConstants.CONFIG_GENERATE_SAMPLE_CODE: options['generate_sample_code'],
                ProjectConstants.CONFIG_GENERATE_TESTS: options['generate_tests'],
                ProjectConstants.CONFIG_GENERATE_DOCKER: options['generate_docker']
            }
            
            return config
            
        except KeyboardInterrupt:
            console.print("\n[yellow]用户取消操作[/yellow]")
            return None
        except Exception as e:
            console.print(f"[red]❌ 收集配置失败: {str(e)}[/red]")
            return None
    
    def _collect_basic_info(self) -> Optional[Dict[str, str]]:
        """
        收集基本信息
        
        Returns:
            Optional[Dict[str, str]]: 基本信息字典
        """
        console.print(Panel.fit(
            Text("📋 基本信息配置", style="bold green"),
            border_style="green"
        ))
        
        try:
            # 项目名称
            while True:
                name = Prompt.ask("项目名称 (例: my-spring-app)")
                if ProjectValidator.validate_project_name(name):
                    break
                else:
                    console.print("[red]项目名称格式不正确，请使用小写字母、数字和连字符[/red]")
            
            # 基础包名
            while True:
                package = Prompt.ask("基础包名 (例: com.example.myapp)")
                if ProjectValidator.validate_package_name(package):
                    break
                else:
                    console.print("[red]包名格式不正确，请使用标准Java包名格式[/red]")
            
            # 项目版本
            version = Prompt.ask("项目版本", default="1.0.0")
            
            # 项目描述
            description = Prompt.ask("项目描述", default=f"{name} - SpringBoot项目")
            
            # 输出目录
            output_dir = Prompt.ask("输出目录", default="./output")
            
            return {
                'name': name,
                'package': package,
                'version': version,
                'description': description,
                'output_dir': output_dir
            }
        
        except KeyboardInterrupt:
            return None
    
    def _collect_versions(self) -> Optional[Dict[str, str]]:
        """
        收集技术版本信息
        
        Returns:
            Optional[Dict[str, str]]: 版本信息字典
        """
        console.print(Panel.fit(
            Text("🔧 技术版本选择", style="bold green"),
            border_style="green"
        ))
        
        try:
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
        
        except KeyboardInterrupt:
            return None
    
    def _collect_structure(self) -> Optional[Dict[str, Any]]:
        """
        收集项目结构信息
        
        Returns:
            Optional[Dict[str, Any]]: 项目结构信息字典
        """
        console.print(Panel.fit(
            Text("🏗️ 项目结构配置", style="bold green"),
            border_style="green"
        ))
        
        try:
            # 项目类型
            console.print("选择项目结构:")
            console.print("1. 单模块项目 (适合小型项目)")
            console.print("2. 多模块项目 (适合大型项目)")
            structure_choice = Prompt.ask("请选择", choices=["1", "2"], default="1")
            
            project_type = ProjectConstants.PROJECT_TYPE_SINGLE if structure_choice == "1" else ProjectConstants.PROJECT_TYPE_MULTI
            modules = []
            
            if project_type == ProjectConstants.PROJECT_TYPE_MULTI:
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
                selected_modules = [available_modules[i-1] for i in selected_indices if 1 <= i <= len(available_modules)]
                
                modules = [{
                    "name": name,
                    "description": desc
                } for name, desc in selected_modules]
            
            return {
                'project_type': project_type,
                'modules': modules
            }
        
        except KeyboardInterrupt:
            return None
    
    def _collect_tech_stack(self) -> Optional[Dict[str, Any]]:
        """
        收集技术栈信息
        
        Returns:
            Optional[Dict[str, Any]]: 技术栈信息字典
        """
        console.print(Panel.fit(
            Text("🛠️ 技术栈配置", style="bold green"),
            border_style="green"
        ))
        
        try:
            # 数据库选择
            console.print("选择数据库:")
            console.print("1. MySQL")
            console.print("2. PostgreSQL")
            console.print("3. H2 (内存数据库)")
            console.print("4. 不使用数据库")
            db_choice = Prompt.ask("请选择", choices=["1", "2", "3", "4"], default="1")
            database = {"1": "mysql", "2": "postgresql", "3": "h2", "4": "none"}[db_choice]
            
            # ORM框架（仅在使用数据库时选择）
            orm = "none"
            if database != "none":
                console.print("选择ORM框架:")
                console.print("1. MyBatis (推荐)")
                console.print("2. JPA/Hibernate")
                orm_choice = Prompt.ask("请选择", choices=["1", "2"], default="1")
                orm = {"1": "mybatis", "2": "jpa"}[orm_choice]
            
            # 缓存组件
            console.print("选择缓存组件 (输入数字，用逗号分隔，留空表示不使用):")
            console.print("1. Redis")
            console.print("2. Caffeine (本地缓存)")
            cache_input = Prompt.ask("请选择缓存组件", default="")
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
            
            # NoSQL数据库
            nosql = []
            if Confirm.ask("集成MongoDB？", default=False):
                nosql.append("mongodb")
            if Confirm.ask("集成Elasticsearch？", default=False):
                nosql.append("elasticsearch")
            
            # 文档工具
            doc = []
            if Confirm.ask("集成Swagger API文档？", default=True):
                doc.append("swagger")
            
            # 安全框架
            security = []
            if Confirm.ask("集成Spring Security？", default=False):
                security.append("spring-security")
            
            # 监控组件
            monitor = []
            if Confirm.ask("集成Spring Boot Actuator监控？", default=True):
                monitor.append("actuator")
            
            return {
                ProjectConstants.TECH_DATABASE: database,
                ProjectConstants.TECH_ORM: orm,
                ProjectConstants.TECH_CACHE: cache,
                ProjectConstants.TECH_MQ: mq,
                ProjectConstants.TECH_NOSQL: nosql,
                ProjectConstants.TECH_DOC: doc,
                ProjectConstants.TECH_SECURITY: security,
                ProjectConstants.TECH_MONITOR: monitor,
                ProjectConstants.TECH_WEB_FRAMEWORK: ProjectConstants.DEFAULT_WEB_FRAMEWORK,
                ProjectConstants.TECH_TEST_FRAMEWORKS: ProjectConstants.DEFAULT_TEST_FRAMEWORKS
            }
        
        except KeyboardInterrupt:
            return None
    
    def _collect_options(self) -> Optional[Dict[str, bool]]:
        """
        收集生成选项
        
        Returns:
            Optional[Dict[str, bool]]: 生成选项字典
        """
        console.print(Panel.fit(
            Text("⚙️ 生成选项配置", style="bold green"),
            border_style="green"
        ))
        
        try:
            generate_sample_code = Confirm.ask("生成示例代码？", default=True)
            generate_tests = Confirm.ask("生成测试代码？", default=True)
            generate_docker = Confirm.ask("生成Docker配置？", default=True)
            
            return {
                'generate_sample_code': generate_sample_code,
                'generate_tests': generate_tests,
                'generate_docker': generate_docker
            }
        
        except KeyboardInterrupt:
            return None
    
    def _show_config_summary(self, config: Dict[str, Any]) -> None:
        """
        显示配置摘要
        
        Args:
            config: 项目配置字典
        """
        console.print("\n" + "="*50)
        console.print(Panel.fit(
            Text("📋 配置摘要", style="bold yellow"),
            border_style="yellow"
        ))
        
        console.print(f"[bold]项目名称:[/bold] {config.get(ProjectConstants.CONFIG_NAME)}")
        console.print(f"[bold]基础包名:[/bold] {config.get(ProjectConstants.CONFIG_PACKAGE)}")
        console.print(f"[bold]项目版本:[/bold] {config.get(ProjectConstants.CONFIG_VERSION)}")
        console.print(f"[bold]Java版本:[/bold] {config.get(ProjectConstants.CONFIG_JAVA_VERSION)}")
        console.print(f"[bold]SpringBoot版本:[/bold] {config.get(ProjectConstants.CONFIG_SPRING_BOOT_VERSION)}")
        
        project_type = config.get(ProjectConstants.CONFIG_PROJECT_TYPE)
        console.print(f"[bold]项目类型:[/bold] {'多模块' if project_type == ProjectConstants.PROJECT_TYPE_MULTI else '单模块'}")
        
        modules = config.get(ProjectConstants.CONFIG_MODULES, [])
        if modules:
            module_names = [module.get('name', '') for module in modules]
            console.print(f"[bold]模块列表:[/bold] {', '.join(module_names)}")
        
        tech_stack = config.get(ProjectConstants.CONFIG_TECH_STACK, {})
        console.print(f"[bold]数据库:[/bold] {tech_stack.get(ProjectConstants.TECH_DATABASE)}")
        console.print(f"[bold]ORM框架:[/bold] {tech_stack.get(ProjectConstants.TECH_ORM)}")
        
        cache = tech_stack.get(ProjectConstants.TECH_CACHE, [])
        if cache:
            console.print(f"[bold]缓存组件:[/bold] {', '.join(cache)}")
        
        mq = tech_stack.get(ProjectConstants.TECH_MQ, [])
        if mq:
            console.print(f"[bold]消息队列:[/bold] {', '.join(mq)}")
        
        doc = tech_stack.get(ProjectConstants.TECH_DOC, [])
        console.print(f"[bold]API文档:[/bold] {'是' if doc else '否'}")
        
        security = tech_stack.get(ProjectConstants.TECH_SECURITY, [])
        console.print(f"[bold]安全框架:[/bold] {'是' if security else '否'}")
        
        console.print("="*50 + "\n")
    
    def _ask_load_from_existing(self) -> bool:
        """
        询问是否从已有配置加载
        
        Returns:
            bool: 是否从已有配置加载
        """
        configs = self.config_manager.list_configs()
        if not configs:
            return False
        
        return Confirm.ask("\n是否从已有配置文件加载项目配置？", default=False)
    
    def _load_existing_config(self) -> Optional[Dict[str, Any]]:
        """
        加载已有配置
        
        Returns:
            Optional[Dict[str, Any]]: 配置字典
        """
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
        
        try:
            choice_input = Prompt.ask("请选择", choices=[str(i) for i in range(1, len(choice_list)+2)], default=str(len(choice_list)+1))
            choice_index = int(choice_input) - 1
            
            if choice_index >= len(choice_list):
                return None
            
            selected = choice_list[choice_index][1]
            config = self.config_manager.load_config(selected)
            console.print(f"[green]✅ 已加载配置: {selected}[/green]")
            return config
        
        except Exception as e:
            console.print(f"[red]❌ 加载配置失败: {str(e)}[/red]")
            return None
    
    def _ask_save_config(self, config: Dict[str, Any]) -> None:
        """
        询问是否保存配置
        
        Args:
            config: 项目配置字典
        """
        if Confirm.ask("\n是否保存此配置以便下次使用？", default=True):
            config_name = Prompt.ask("请输入配置名称", default=config.get(ProjectConstants.CONFIG_NAME))
            
            try:
                config_file = self.config_manager.save_config(config, config_name)
                console.print(f"[green]✅ 配置已保存: {config_file}[/green]")
            except Exception as e:
                console.print(f"[red]❌ 保存配置失败: {str(e)}[/red]")
    
    def _dict_to_config(self, config_dict: Dict[str, Any]) -> 'InteractiveConfig':
        """
        将字典配置转换为InteractiveConfig对象
        
        Args:
            config_dict: 配置字典
            
        Returns:
            InteractiveConfig: 配置对象
        """
        # 创建一个新的InteractiveConfig实例
        new_config = InteractiveConfig(self.config_manager)
        
        # 将字典中的配置项设置到新实例中
        for key, value in config_dict.items():
            setattr(new_config, key, value)
        
        return new_config