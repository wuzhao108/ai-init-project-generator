#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
项目生成器模块
负责根据配置生成完整的SpringBoot项目结构
"""

import os
import shutil
from pathlib import Path
from typing import Dict, Any, List
from jinja2 import Environment, FileSystemLoader, select_autoescape
from rich.console import Console
from rich.progress import Progress, TaskID
from rich.panel import Panel
from rich.tree import Tree
from rich.text import Text
from datetime import datetime

from .config import ProjectConfig, TechStack
from .template_manager import TemplateManager
from scripts.utils.string_utils import to_camel_case, to_pascal_case
from scripts.core.config_manager import ConfigManager
from scripts.utils.file_utils import ensure_dir, copy_directory
from scripts.constants.project_constants import ProjectConstants
from .utils import (
    get_java_package_path, project_name_to_class_name,
    to_snake_case, get_current_date,
    get_current_datetime, format_dependencies_xml
)

console = Console()


class ProjectGenerator:
    """项目生成器"""
    
    def __init__(self, config: ProjectConfig, config_manager: ConfigManager = None):
        self.config = config
        self.template_manager = TemplateManager()
        self.generated_files = []
        self.config_manager = config_manager or ConfigManager()
        
        # 设置Jinja2环境
        self.jinja_env = Environment(
            loader=FileSystemLoader(self.template_manager.templates_dir),
            autoescape=select_autoescape(['html', 'xml']),
            trim_blocks=True,
            lstrip_blocks=True
        )
        
        # 添加自定义过滤器
        self._setup_jinja_filters()
    
    def _setup_jinja_filters(self):
        """设置Jinja2自定义过滤器"""
        self.jinja_env.filters['camel_case'] = to_camel_case
        self.jinja_env.filters['pascal_case'] = to_pascal_case
        self.jinja_env.filters['snake_case'] = to_snake_case
        self.jinja_env.filters['package_path'] = get_java_package_path
        self.jinja_env.filters['class_name'] = project_name_to_class_name
        self.jinja_env.filters['format_dependencies'] = format_dependencies_xml
    
    def generate(self, output_dir: str = None, save_config: bool = True) -> str:
        """生成项目
        
        Args:
            output_dir: 输出目录，如果不提供则使用默认输出目录
            save_config: 是否保存配置到JSON文件
            
        Returns:
            str: 生成的项目路径
        """
        # 确定输出目录
        if output_dir is None:
            # 使用项目根目录下的output目录
            project_root = Path(__file__).parent.parent
            output_base = project_root / "output"
            ensure_dir(str(output_base))
            
            # 创建带时间戳的项目目录
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            project_dir_name = f"{self.config.name}_{timestamp}"
            self.config.output_dir = str(output_base / project_dir_name)
        else:
            self.config.output_dir = output_dir
        
        console.print(f"\n[bold green]🚀 开始生成项目: {self.config.name}[/bold green]")
        
        # 保存配置文件
        if save_config:
            try:
                config_dict = self._config_to_dict(self.config)
                config_file = self.config_manager.save_config(config_dict, self.config.name)
                console.print(f"[green]配置已保存:[/green] {config_file}")
            except Exception as e:
                console.print(f"[yellow]保存配置失败:[/yellow] {str(e)}")
        
        with Progress() as progress:
            task = progress.add_task("[green]生成项目文件...", total=100)
            
            # 创建项目目录
            self._create_project_structure(progress, task)
            progress.update(task, advance=20)
            
            # 生成Maven配置文件
            self._generate_maven_files(progress, task)
            progress.update(task, advance=20)
            
            # 生成Java源代码
            self._generate_java_sources(progress, task)
            progress.update(task, advance=30)
            
            # 生成配置文件
            self._generate_config_files(progress, task)
            progress.update(task, advance=15)
            
            # 生成文档和其他文件
            self._generate_docs_and_others(progress, task)
            progress.update(task, advance=15)
        
        console.print(f"\n[bold green]✅ 项目生成完成！[/bold green]")
        console.print(f"[bold]项目路径:[/bold] {self.config.project_path}")
        
        # 显示后续步骤
        self._show_next_steps()
        
        return self.config.project_path
    
    def preview(self) -> None:
        """预览项目结构"""
        console.print(f"\n[bold blue]📋 项目结构预览: {self.config.name}[/bold blue]")
        
        tree = Tree(f"📁 {self.config.name}/")
        
        if self.config.multi_module:
            self._add_multi_module_tree(tree)
        else:
            self._add_single_module_tree(tree)
        
        console.print(tree)
        
        # 显示技术栈信息
        self._show_tech_stack_info()
    
    def _create_project_structure(self, progress: Progress, task: TaskID) -> None:
        """创建项目目录结构"""
        project_path = self.config.project_path
        ensure_dir(project_path)
        
        if self.config.multi_module:
            # 多模块项目结构
            for module in self.config.modules:
                module_path = os.path.join(project_path, module.name)
                self._create_module_structure(module_path)
        else:
            # 单模块项目结构
            self._create_module_structure(project_path)
    
    def _create_module_structure(self, module_path: str) -> None:
        """创建模块目录结构"""
        # Maven标准目录结构
        dirs = [
            'src/main/java',
            'src/main/resources',
            'src/main/resources/static',
            'src/main/resources/templates',
            'src/test/java',
            'src/test/resources'
        ]
        
        for dir_path in dirs:
            ensure_dir(os.path.join(module_path, dir_path))
        
        # 创建包目录
        package_path = os.path.join(
            module_path, 'src/main/java', 
            get_java_package_path(self.config.package)
        )
        ensure_dir(package_path)
        
        # 创建测试包目录
        test_package_path = os.path.join(
            module_path, 'src/test/java',
            get_java_package_path(self.config.package)
        )
        ensure_dir(test_package_path)
    
    def _generate_maven_files(self, progress: Progress, task: TaskID) -> None:
        """生成Maven配置文件"""
        if self.config.multi_module:
            self._generate_parent_pom()
            for module in self.config.modules:
                self._generate_module_pom(module.name)
        else:
            self._generate_single_pom()
    
    def _generate_parent_pom(self) -> None:
        """生成父POM文件"""
        template = self.jinja_env.get_template('maven/parent-pom.xml')
        content = template.render(
            config=self.config,
            modules=[module.name for module in self.config.modules]
        )
        
        pom_path = os.path.join(self.config.project_path, 'pom.xml')
        self._write_file(pom_path, content)
    
    def _generate_module_pom(self, module_name: str) -> None:
        """生成模块POM文件"""
        template = self.jinja_env.get_template('maven/module-pom.xml')
        content = template.render(
            config=self.config,
            module_name=module_name,
            is_web_module=(module_name == 'web')
        )
        
        pom_path = os.path.join(self.config.project_path, module_name, 'pom.xml')
        self._write_file(pom_path, content)
    
    def _generate_single_pom(self) -> None:
        """生成单模块POM文件"""
        template = self.jinja_env.get_template('maven/single-pom.xml')
        content = template.render(config=self.config)
        
        pom_path = os.path.join(self.config.project_path, 'pom.xml')
        self._write_file(pom_path, content)
    
    def _generate_java_sources(self, progress: Progress, task: TaskID) -> None:
        """生成Java源代码"""
        if self.config.multi_module:
            # 多模块项目
            for module in self.config.modules:
                if module.name == 'web':
                    self._generate_main_application(module.name)
                self._generate_module_sources(module.name)
        else:
            # 单模块项目
            self._generate_main_application()
            self._generate_single_module_sources()
    
    def _generate_main_application(self, module_name: str = None) -> None:
        """生成SpringBoot主启动类"""
        template = self.jinja_env.get_template('java/Application.java')
        content = template.render(config=self.config)
        
        if module_name:
            java_path = os.path.join(
                self.config.project_path, module_name, 'src/main/java',
                get_java_package_path(self.config.package),
                f"{self.config.main_class_name}.java"
            )
        else:
            java_path = os.path.join(
                self.config.project_path, 'src/main/java',
                get_java_package_path(self.config.package),
                f"{self.config.main_class_name}.java"
            )
        
        self._write_file(java_path, content)
    
    def _generate_module_sources(self, module_name: str) -> None:
        """生成模块源代码"""
        if not self.config.generate_sample_code:
            return
        
        # 根据模块类型生成不同的代码
        if module_name == 'web':
            self._generate_controller_code(module_name)
        elif module_name == 'service':
            self._generate_service_code(module_name)
        elif module_name == 'dao':
            self._generate_dao_code(module_name)
        elif module_name == 'api':
            self._generate_api_code(module_name)
        elif module_name == 'common':
            self._generate_common_code(module_name)
    
    def _generate_single_module_sources(self) -> None:
        """生成单模块源代码"""
        if not self.config.generate_sample_code:
            return
        
        base_path = self.config.project_path
        
        # 生成各层代码
        self._generate_controller_code(base_path=base_path)
        self._generate_service_code(base_path=base_path)
        self._generate_dao_code(base_path=base_path)
        self._generate_common_code(base_path=base_path)
    
    def _generate_controller_code(self, module_name: str = None, base_path: str = None) -> None:
        """生成Controller代码"""
        template = self.jinja_env.get_template('java/controller/UserController.java')
        content = template.render(config=self.config)
        
        if base_path:
            java_path = os.path.join(
                base_path, 'src/main/java',
                get_java_package_path(self.config.package),
                'controller', 'UserController.java'
            )
        else:
            java_path = os.path.join(
                self.config.project_path, module_name, 'src/main/java',
                get_java_package_path(self.config.package),
                'controller', 'UserController.java'
            )
        
        ensure_dir(os.path.dirname(java_path))
        self._write_file(java_path, content)
    
    def _generate_service_code(self, module_name: str = None, base_path: str = None) -> None:
        """生成Service代码"""
        # 生成Service接口
        template = self.jinja_env.get_template('java/service/UserService.java')
        content = template.render(config=self.config)
        
        if base_path:
            java_path = os.path.join(
                base_path, 'src/main/java',
                get_java_package_path(self.config.package),
                'service', 'UserService.java'
            )
        else:
            java_path = os.path.join(
                self.config.project_path, module_name, 'src/main/java',
                get_java_package_path(self.config.package),
                'service', 'UserService.java'
            )
        
        ensure_dir(os.path.dirname(java_path))
        self._write_file(java_path, content)
        
        # 生成Service实现
        template = self.jinja_env.get_template('java/service/impl/UserServiceImpl.java')
        content = template.render(config=self.config)
        
        if base_path:
            impl_path = os.path.join(
                base_path, 'src/main/java',
                get_java_package_path(self.config.package),
                'service', 'impl', 'UserServiceImpl.java'
            )
        else:
            impl_path = os.path.join(
                self.config.project_path, module_name, 'src/main/java',
                get_java_package_path(self.config.package),
                'service', 'impl', 'UserServiceImpl.java'
            )
        
        ensure_dir(os.path.dirname(impl_path))
        self._write_file(impl_path, content)
    
    def _generate_dao_code(self, module_name: str = None, base_path: str = None) -> None:
        """生成DAO代码"""
        if self.config.tech_stack.orm == 'mybatis':
            self._generate_mybatis_code(module_name, base_path)
        elif self.config.tech_stack.orm == 'jpa':
            self._generate_jpa_code(module_name, base_path)
    
    def _generate_mybatis_code(self, module_name: str = None, base_path: str = None) -> None:
        """生成MyBatis代码"""
        # 生成Mapper接口
        template = self.jinja_env.get_template('java/mapper/UserMapper.java')
        content = template.render(config=self.config)
        
        if base_path:
            mapper_path = os.path.join(
                base_path, 'src/main/java',
                get_java_package_path(self.config.package),
                'mapper', 'UserMapper.java'
            )
        else:
            mapper_path = os.path.join(
                self.config.project_path, module_name, 'src/main/java',
                get_java_package_path(self.config.package),
                'mapper', 'UserMapper.java'
            )
        
        ensure_dir(os.path.dirname(mapper_path))
        self._write_file(mapper_path, content)
        
        # 生成Mapper XML
        template = self.jinja_env.get_template('mybatis/UserMapper.xml')
        content = template.render(config=self.config)
        
        if base_path:
            xml_path = os.path.join(
                base_path, 'src/main/resources',
                'mapper', 'UserMapper.xml'
            )
        else:
            xml_path = os.path.join(
                self.config.project_path, module_name, 'src/main/resources',
                'mapper', 'UserMapper.xml'
            )
        
        ensure_dir(os.path.dirname(xml_path))
        self._write_file(xml_path, content)
    
    def _generate_jpa_code(self, module_name: str = None, base_path: str = None) -> None:
        """生成JPA代码"""
        template = self.jinja_env.get_template('java/repository/UserRepository.java')
        content = template.render(config=self.config)
        
        if base_path:
            repo_path = os.path.join(
                base_path, 'src/main/java',
                get_java_package_path(self.config.package),
                'repository', 'UserRepository.java'
            )
        else:
            repo_path = os.path.join(
                self.config.project_path, module_name, 'src/main/java',
                get_java_package_path(self.config.package),
                'repository', 'UserRepository.java'
            )
        
        ensure_dir(os.path.dirname(repo_path))
        self._write_file(repo_path, content)
    
    def _generate_api_code(self, module_name: str) -> None:
        """生成API代码"""
        # 生成DTO
        template = self.jinja_env.get_template('java/dto/UserDTO.java')
        content = template.render(config=self.config)
        
        dto_path = os.path.join(
            self.config.project_path, module_name, 'src/main/java',
            get_java_package_path(self.config.package),
            'dto', 'UserDTO.java'
        )
        
        ensure_dir(os.path.dirname(dto_path))
        self._write_file(dto_path, content)
    
    def _generate_common_code(self, module_name: str = None, base_path: str = None) -> None:
        """生成公共代码"""
        # 生成实体类
        template = self.jinja_env.get_template('java/entity/User.java')
        content = template.render(config=self.config)
        
        if base_path:
            entity_path = os.path.join(
                base_path, 'src/main/java',
                get_java_package_path(self.config.package),
                'entity', 'User.java'
            )
        else:
            entity_path = os.path.join(
                self.config.project_path, module_name, 'src/main/java',
                get_java_package_path(self.config.package),
                'entity', 'User.java'
            )
        
        ensure_dir(os.path.dirname(entity_path))
        self._write_file(entity_path, content)
        
        # 生成统一响应结果
        template = self.jinja_env.get_template('java/common/Result.java')
        content = template.render(config=self.config)
        
        if base_path:
            result_path = os.path.join(
                base_path, 'src/main/java',
                get_java_package_path(self.config.package),
                'common', 'Result.java'
            )
        else:
            result_path = os.path.join(
                self.config.project_path, module_name, 'src/main/java',
                get_java_package_path(self.config.package),
                'common', 'Result.java'
            )
        
        ensure_dir(os.path.dirname(result_path))
        self._write_file(result_path, content)
    
    def _generate_config_files(self, progress: Progress, task: TaskID) -> None:
        """生成配置文件"""
        # 生成application.yml
        template = self.jinja_env.get_template('config/application.yml')
        content = template.render(config=self.config)
        
        if self.config.multi_module:
            config_path = os.path.join(
                self.config.project_path, 'web', 'src/main/resources', 'application.yml'
            )
        else:
            config_path = os.path.join(
                self.config.project_path, 'src/main/resources', 'application.yml'
            )
        
        self._write_file(config_path, content)
        
        # 生成多环境配置
        for env in ['dev', 'test', 'prod']:
            template = self.jinja_env.get_template(f'config/application-{env}.yml')
            content = template.render(config=self.config)
            
            if self.config.multi_module:
                env_config_path = os.path.join(
                    self.config.project_path, 'web', 'src/main/resources', f'application-{env}.yml'
                )
            else:
                env_config_path = os.path.join(
                    self.config.project_path, 'src/main/resources', f'application-{env}.yml'
                )
            
            self._write_file(env_config_path, content)
        
        # 生成logback配置
        template = self.jinja_env.get_template('config/logback-spring.xml')
        content = template.render(config=self.config)
        
        if self.config.multi_module:
            logback_path = os.path.join(
                self.config.project_path, 'web', 'src/main/resources', 'logback-spring.xml'
            )
        else:
            logback_path = os.path.join(
                self.config.project_path, 'src/main/resources', 'logback-spring.xml'
            )
        
        self._write_file(logback_path, content)
    
    def _generate_docs_and_others(self, progress: Progress, task: TaskID) -> None:
        """生成文档和其他文件"""
        # 生成README.md
        template = self.jinja_env.get_template('other/README.md')
        content = template.render(config=self.config)
        readme_path = os.path.join(self.config.project_path, 'README.md')
        self._write_file(readme_path, content)
        
        # 生成.gitignore
        template = self.jinja_env.get_template('git/gitignore')
        content = template.render(config=self.config)
        gitignore_path = os.path.join(self.config.project_path, '.gitignore')
        self._write_file(gitignore_path, content)
        
        # 生成Docker配置
        if self.config.generate_docker:
            template = self.jinja_env.get_template('docker/Dockerfile')
            content = template.render(config=self.config)
            dockerfile_path = os.path.join(self.config.project_path, 'Dockerfile')
            self._write_file(dockerfile_path, content)
            
            template = self.jinja_env.get_template('docker/docker-compose.yml')
            content = template.render(config=self.config)
            compose_path = os.path.join(self.config.project_path, 'docker-compose.yml')
            self._write_file(compose_path, content)
    
    def _write_file(self, file_path: str, content: str) -> None:
        """写入文件"""
        ensure_dir(os.path.dirname(file_path))
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        self.generated_files.append(file_path)
    
    def _add_multi_module_tree(self, tree: Tree) -> None:
        """添加多模块项目树结构"""
        tree.add("📄 pom.xml")
        tree.add("📄 README.md")
        tree.add("📄 .gitignore")
        
        if self.config.generate_docker:
            tree.add("🐳 Dockerfile")
            tree.add("🐳 docker-compose.yml")
        
        for module in self.config.modules:
            module_tree = tree.add(f"📁 {module.name}/")
            module_tree.add("📄 pom.xml")
            
            src_tree = module_tree.add("📁 src/")
            main_tree = src_tree.add("📁 main/")
            main_tree.add("📁 java/")
            main_tree.add("📁 resources/")
            
            test_tree = src_tree.add("📁 test/")
            test_tree.add("📁 java/")
            test_tree.add("📁 resources/")
    
    def _add_single_module_tree(self, tree: Tree) -> None:
        """添加单模块项目树结构"""
        tree.add("📄 pom.xml")
        tree.add("📄 README.md")
        tree.add("📄 .gitignore")
        
        if self.config.generate_docker:
            tree.add("🐳 Dockerfile")
            tree.add("🐳 docker-compose.yml")
        
        src_tree = tree.add("📁 src/")
        main_tree = src_tree.add("📁 main/")
        main_tree.add("📁 java/")
        main_tree.add("📁 resources/")
        
        test_tree = src_tree.add("📁 test/")
        test_tree.add("📁 java/")
        test_tree.add("📁 resources/")
    
    def _show_tech_stack_info(self) -> None:
        """显示技术栈信息"""
        console.print(Panel.fit(
            Text("🛠️ 技术栈信息", style="bold cyan"),
            border_style="cyan"
        ))
        
        console.print(f"[bold]Java版本:[/bold] {self.config.java_version}")
        console.print(f"[bold]SpringBoot版本:[/bold] {self.config.spring_version}")
        console.print(f"[bold]数据库:[/bold] {self.config.tech_stack.database}")
        console.print(f"[bold]ORM框架:[/bold] {self.config.tech_stack.orm}")
        
        if self.config.tech_stack.cache:
            console.print(f"[bold]缓存:[/bold] {', '.join(self.config.tech_stack.cache)}")
        
        if self.config.tech_stack.mq:
            console.print(f"[bold]消息队列:[/bold] {', '.join(self.config.tech_stack.mq)}")
    
    def _show_next_steps(self) -> None:
        """显示后续步骤"""
        console.print(Panel.fit(
            Text("📝 后续步骤", style="bold yellow"),
            border_style="yellow"
        ))
        
        steps = [
            f"1. 进入项目目录: cd {self.config.name}",
            "2. 导入IDE (推荐IntelliJ IDEA或Eclipse)",
            "3. 配置数据库连接信息",
            "4. 运行项目: mvn spring-boot:run",
            "5. 访问应用: http://localhost:8080"
        ]
        
        if self.config.tech_stack.doc:
            steps.append("6. 查看API文档: http://localhost:8080/swagger-ui.html")
        
        for step in steps:
            console.print(f"  {step}")
    
    def _config_to_dict(self, config: ProjectConfig) -> Dict[str, Any]:
        """将ProjectConfig转换为字典
        
        Args:
            config: 项目配置对象
            
        Returns:
            Dict[str, Any]: 配置字典
        """
        return {
            ProjectConstants.CONFIG_NAME: config.name,
            ProjectConstants.CONFIG_PACKAGE: config.package,
            ProjectConstants.CONFIG_VERSION: config.version,
            ProjectConstants.CONFIG_DESCRIPTION: config.description,
            ProjectConstants.CONFIG_JAVA_VERSION: config.java_version,
            ProjectConstants.CONFIG_SPRING_BOOT_VERSION: config.spring_version,
            ProjectConstants.CONFIG_PROJECT_TYPE: "multi-module" if config.multi_module else "single-module",
            ProjectConstants.CONFIG_TECH_STACK: {
                ProjectConstants.TECH_DATABASE: config.tech_stack.database,
                ProjectConstants.TECH_ORM: config.tech_stack.orm,
                ProjectConstants.TECH_CACHE: config.tech_stack.cache,
                ProjectConstants.TECH_MQ: config.tech_stack.mq,
                ProjectConstants.TECH_NOSQL: getattr(config.tech_stack, 'nosql', []),
                ProjectConstants.TECH_DOC: config.tech_stack.doc,
                ProjectConstants.TECH_SECURITY: getattr(config.tech_stack, 'security', []),
                ProjectConstants.TECH_MONITOR: getattr(config.tech_stack, 'monitoring', []),
                ProjectConstants.TECH_WEB_FRAMEWORK: getattr(config.tech_stack, 'web_framework', 'spring-mvc'),
                ProjectConstants.TECH_TEST_FRAMEWORKS: getattr(config.tech_stack, 'test_frameworks', ['junit'])
            },
            ProjectConstants.CONFIG_MODULES: [{
                "name": module.name,
                "type": getattr(module, 'type', 'common'),
                "description": getattr(module, 'description', '')
            } for module in config.modules],
            ProjectConstants.CONFIG_OUTPUT_DIR: "./output",
            ProjectConstants.CONFIG_PREVIEW_MODE: False
        }
    
    def generate_from_config_file(self, config_name: str, output_dir: str = None) -> str:
        """从配置文件生成项目
        
        Args:
            config_name: 配置文件名称
            output_dir: 输出目录
            
        Returns:
            str: 生成的项目路径
            
        Raises:
            FileNotFoundError: 配置文件不存在
            ValueError: 配置文件格式无效
        """
        # 加载配置
        config_dict = self.config_manager.load_config(config_name)
        
        # 转换为ProjectConfig对象
        config = self._dict_to_config(config_dict)
        
        # 更新当前配置
        self.config = config
        
        # 生成项目
        return self.generate(output_dir, save_config=False)
    
    def _dict_to_config(self, config_dict: Dict[str, Any]) -> ProjectConfig:
        """将字典转换为ProjectConfig对象
        
        Args:
            config_dict: 配置字典
            
        Returns:
            ProjectConfig: 项目配置对象
        """
        from .config import ModuleConfig, TechStack
        
        # 创建技术栈配置
        tech_stack_dict = config_dict.get(ProjectConstants.CONFIG_TECH_STACK, {})
        tech_stack = TechStack(
            database=tech_stack_dict.get(ProjectConstants.TECH_DATABASE, ProjectConstants.DEFAULT_DATABASE),
            orm=tech_stack_dict.get(ProjectConstants.TECH_ORM, ProjectConstants.DEFAULT_ORM),
            cache=tech_stack_dict.get(ProjectConstants.TECH_CACHE, []),
            mq=tech_stack_dict.get(ProjectConstants.TECH_MQ, []),
            doc=tech_stack_dict.get(ProjectConstants.TECH_DOC, [])
        )
        
        # 创建模块配置
        modules = []
        for module_dict in config_dict.get(ProjectConstants.CONFIG_MODULES, []):
            modules.append(ModuleConfig(
                name=module_dict.get("name", ""),
                type=module_dict.get("type", ""),
                description=module_dict.get("description", "")
            ))
        
        # 创建项目配置
        return ProjectConfig(
            name=config_dict.get(ProjectConstants.CONFIG_NAME, "my-spring-boot-project"),
            package=config_dict.get(ProjectConstants.CONFIG_PACKAGE, "com.example.project"),
            version=config_dict.get(ProjectConstants.CONFIG_VERSION, "1.0.0"),
            description=config_dict.get(ProjectConstants.CONFIG_DESCRIPTION, "A Spring Boot project"),
            java_version=config_dict.get(ProjectConstants.CONFIG_JAVA_VERSION, "17"),
            spring_version=config_dict.get(ProjectConstants.CONFIG_SPRING_BOOT_VERSION, "3.2.0"),
            multi_module=config_dict.get(ProjectConstants.CONFIG_PROJECT_TYPE) == "multi-module",
            tech_stack=tech_stack,
            modules=modules
        )