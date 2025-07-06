# -*- coding: utf-8 -*-
"""
项目生成器模块
负责根据配置生成Spring Boot项目
"""

import os
import shutil
from pathlib import Path
from typing import Dict, Any, Optional
from jinja2 import Environment, DictLoader, select_autoescape
import yaml
import re

from .config_manager import ConfigManager
from .template_manager import TemplateManager
from ..utils.file_utils import ensure_dir, write_file
from ..constants.project_constants import ProjectConstants
from ..validators.project_validator import ProjectValidator


class ProjectGenerator:
    """项目生成器"""
    
    def __init__(self, config=None, config_manager: ConfigManager = None, template_manager: TemplateManager = None):
        """
        初始化项目生成器
        
        Args:
            config: 项目配置对象或字典（可选）
            config_manager: 配置管理器实例
            template_manager: 模板管理器实例
        """
        self.config = config
        self.config_manager = config_manager or ConfigManager()
        self.template_manager = template_manager or TemplateManager()
        
        # 获取项目根目录
        self.project_root = Path(__file__).parent.parent.parent
        
        # 从模板管理器加载模板内容
        self.templates = self._load_templates_from_manager()
        
        # 初始化Jinja2环境
        self.jinja_env = Environment(
            loader=DictLoader(self.templates),
            autoescape=select_autoescape(['html', 'xml']),
            trim_blocks=True,
            lstrip_blocks=True
        )
        
        # 添加自定义过滤器
        self._setup_filters()
    
    def generate_from_config_file(self, config_name: str, output_dir: str = None) -> str:
        """
        从配置文件生成项目
        
        Args:
            config_name: 配置文件名称
            output_dir: 输出目录，如果不提供则使用配置中的输出目录
            
        Returns:
            str: 生成的项目路径
            
        Raises:
            FileNotFoundError: 配置文件不存在
            ValueError: 配置验证失败
        """
        # 加载配置
        config = self.config_manager.load_config(config_name)
        
        # 使用提供的输出目录或配置中的输出目录
        if output_dir:
            config[ProjectConstants.CONFIG_OUTPUT_DIR] = output_dir
        
        return self.generate_from_config(config)
    
    def generate(self, output_dir: str, use_sequential_naming: bool = True) -> str:
        """
        生成项目（兼容main.py调用）
        
        Args:
            output_dir: 输出目录
            use_sequential_naming: 是否使用序号命名避免覆盖
            
        Returns:
            str: 生成的项目路径
        """
        # 从配置对象获取配置字典
        if hasattr(self, 'config') and self.config:
            # 如果是配置对象，转换为字典
            if hasattr(self.config, '__dict__'):
                config = self._config_to_dict(self.config)
            else:
                config = self.config
        else:
            raise ValueError("未提供项目配置")
        
        # 设置输出目录
        config[ProjectConstants.CONFIG_OUTPUT_DIR] = output_dir
        
        return self.generate_from_config(config, use_sequential_naming)
    
    def generate_from_config(self, config: Dict[str, Any], use_sequential_naming: bool = True) -> str:
        """
        从配置字典生成项目
        
        Args:
            config: 项目配置字典
            use_sequential_naming: 是否使用序号命名避免覆盖
            
        Returns:
            str: 生成的项目路径
            
        Raises:
            ValueError: 配置验证失败
        """
        # 验证配置
        is_valid, errors = ProjectValidator.validate_project_config(config)
        if not is_valid:
            raise ValueError(f"配置验证失败：{'; '.join(errors)}")
        
        # 确定项目输出路径
        output_dir = config.get(ProjectConstants.CONFIG_OUTPUT_DIR, "./output")
        project_name = config.get(ProjectConstants.CONFIG_NAME)
        
        if use_sequential_naming:
            project_path = self._get_sequential_project_path(output_dir, project_name)
        else:
            project_path = Path(output_dir) / project_name
        
        # 创建项目目录
        ensure_dir(str(project_path))
        
        # 生成项目结构
        self._generate_project_structure(config, project_path)
        
        # 生成Maven配置文件
        self._generate_maven_files(config, project_path)
        
        # 生成Java源代码
        self._generate_java_sources(config, project_path)
        
        # 生成配置文件
        self._generate_config_files(config, project_path)
        
        # 生成文档文件
        self._generate_documentation(config, project_path)
        
        # 生成Docker配置（如果启用）
        if config.get(ProjectConstants.CONFIG_GENERATE_DOCKER, False):
            self._generate_docker_files(config, project_path)
        
        return str(project_path)
    
    def _get_sequential_project_path(self, output_dir: str, project_name: str) -> Path:
        """
        获取带序号的项目路径，避免覆盖已有文件
        
        Args:
            output_dir: 输出目录
            project_name: 项目名称
            
        Returns:
            Path: 带序号的项目路径
        """
        output_path = Path(output_dir)
        
        # 确保输出目录存在
        ensure_dir(str(output_path))
        
        # 查找已存在的项目文件夹，获取最大序号
        max_sequence = 0
        pattern_prefix = f"{project_name}"
        
        if output_path.exists():
            for item in output_path.iterdir():
                if item.is_dir():
                    folder_name = item.name
                    # 检查是否匹配 "序号-项目名称" 或 "项目名称" 格式
                    if folder_name == project_name:
                        max_sequence = max(max_sequence, 1)
                    elif folder_name.endswith(f"-{project_name}"):
                        try:
                            # 提取序号部分
                            sequence_part = folder_name[:-len(f"-{project_name}")]
                            if sequence_part.isdigit():
                                sequence = int(sequence_part)
                                max_sequence = max(max_sequence, sequence)
                        except (ValueError, IndexError):
                            continue
        
        # 生成新的序号
        new_sequence = max_sequence + 1
        new_folder_name = f"{new_sequence}-{project_name}"
        
        return output_path / new_folder_name
    
    def _config_to_dict(self, config_obj) -> Dict[str, Any]:
        """
        将配置对象转换为字典
        
        Args:
            config_obj: 配置对象
            
        Returns:
            Dict[str, Any]: 配置字典
        """
        config_dict = {}
        
        # 基本配置
        config_dict[ProjectConstants.CONFIG_NAME] = getattr(config_obj, 'name', 'demo-project')
        config_dict[ProjectConstants.CONFIG_PACKAGE] = getattr(config_obj, 'package', 'com.example.demo')
        config_dict[ProjectConstants.CONFIG_VERSION] = getattr(config_obj, 'version', '1.0.0')
        config_dict[ProjectConstants.CONFIG_DESCRIPTION] = getattr(config_obj, 'description', 'Demo project')
        config_dict[ProjectConstants.CONFIG_JAVA_VERSION] = getattr(config_obj, 'java_version', '17')
        config_dict[ProjectConstants.CONFIG_SPRING_BOOT_VERSION] = getattr(config_obj, 'spring_boot_version', '3.2.2')
        config_dict[ProjectConstants.CONFIG_OUTPUT_DIR] = getattr(config_obj, 'output_dir', './output')
        config_dict[ProjectConstants.CONFIG_GENERATE_SAMPLE_CODE] = getattr(config_obj, 'generate_sample_code', True)
        config_dict[ProjectConstants.CONFIG_GENERATE_TESTS] = getattr(config_obj, 'generate_tests', True)
        config_dict[ProjectConstants.CONFIG_GENERATE_DOCKER] = getattr(config_obj, 'generate_docker', False)
        
        # 项目类型
        if getattr(config_obj, 'multi_module', False):
            config_dict[ProjectConstants.CONFIG_PROJECT_TYPE] = ProjectConstants.PROJECT_TYPE_MULTI
            # 处理模块列表
            modules = getattr(config_obj, 'modules', [])
            if modules:
                config_dict[ProjectConstants.CONFIG_MODULES] = [
                    {'name': module.name, 'description': getattr(module, 'description', '')}
                    for module in modules
                ]
        else:
            config_dict[ProjectConstants.CONFIG_PROJECT_TYPE] = ProjectConstants.PROJECT_TYPE_SINGLE
        
        # 技术栈配置
        tech_stack_obj = getattr(config_obj, 'tech_stack', None)
        tech_stack = {}
        if tech_stack_obj:
            tech_stack[ProjectConstants.TECH_DATABASE] = getattr(tech_stack_obj, 'database', ProjectConstants.DEFAULT_DATABASE)
            tech_stack[ProjectConstants.TECH_ORM] = getattr(tech_stack_obj, 'orm', ProjectConstants.DEFAULT_ORM)
            tech_stack[ProjectConstants.TECH_CACHE] = getattr(tech_stack_obj, 'cache', [])
            tech_stack[ProjectConstants.TECH_MQ] = getattr(tech_stack_obj, 'mq', [])
            tech_stack[ProjectConstants.TECH_DOC] = getattr(tech_stack_obj, 'doc', [])
            tech_stack[ProjectConstants.TECH_SECURITY] = getattr(tech_stack_obj, 'security', [])
            tech_stack[ProjectConstants.TECH_MONGODB] = getattr(tech_stack_obj, 'mongodb', False)
            tech_stack[ProjectConstants.TECH_ELASTICSEARCH] = getattr(tech_stack_obj, 'elasticsearch', False)
            tech_stack[ProjectConstants.TECH_ACTUATOR] = getattr(tech_stack_obj, 'actuator', True)
        else:
            # 使用默认技术栈配置
            tech_stack[ProjectConstants.TECH_DATABASE] = 'h2'
            tech_stack[ProjectConstants.TECH_ORM] = 'jpa'
            tech_stack[ProjectConstants.TECH_CACHE] = []
            tech_stack[ProjectConstants.TECH_MQ] = []
            tech_stack[ProjectConstants.TECH_DOC] = ['swagger']
            tech_stack[ProjectConstants.TECH_SECURITY] = []
            tech_stack[ProjectConstants.TECH_MONGODB] = False
            tech_stack[ProjectConstants.TECH_ELASTICSEARCH] = False
            tech_stack[ProjectConstants.TECH_ACTUATOR] = True
        
        config_dict[ProjectConstants.CONFIG_TECH_STACK] = tech_stack
        
        return config_dict
    
    def _generate_project_structure(self, config: Dict[str, Any], project_path: Path) -> None:
        """
        生成项目目录结构
        
        Args:
            config: 项目配置
            project_path: 项目路径
        """
        # 基本目录结构
        dirs_to_create = [
            "src/main/java",
            "src/main/resources",
            "src/main/resources/static",
            "src/main/resources/templates",
            "src/test/java",
            "src/test/resources"
        ]
        
        # 如果是多模块项目，创建模块目录
        if config.get(ProjectConstants.CONFIG_PROJECT_TYPE) == ProjectConstants.PROJECT_TYPE_MULTI:
            modules = config.get(ProjectConstants.CONFIG_MODULES, [])
            for module in modules:
                module_name = module.get("name")
                if module_name:
                    for base_dir in dirs_to_create:
                        dirs_to_create.append(f"{module_name}/{base_dir}")
        
        # 创建目录
        for dir_path in dirs_to_create:
            ensure_dir(str(project_path / dir_path))
    
    def _generate_maven_files(self, config: Dict[str, Any], project_path: Path) -> None:
        """
        生成Maven配置文件
        
        Args:
            config: 项目配置
            project_path: 项目路径
        """
        # 生成主pom.xml
        pom_template = self.jinja_env.get_template("pom.xml.j2")
        pom_content = pom_template.render(config=config)
        write_file(str(project_path / "pom.xml"), pom_content)
        
        # 如果是多模块项目，生成子模块的pom.xml
        if config.get(ProjectConstants.CONFIG_PROJECT_TYPE) == ProjectConstants.PROJECT_TYPE_MULTI:
            modules = config.get(ProjectConstants.CONFIG_MODULES, [])
            for module in modules:
                module_name = module.get("name")
                if module_name:
                    module_pom_template = self.jinja_env.get_template("module-pom.xml.j2")
                    module_pom_content = module_pom_template.render(config=config, module=module)
                    write_file(str(project_path / module_name / "pom.xml"), module_pom_content)
    
    def _generate_java_sources(self, config: Dict[str, Any], project_path: Path) -> None:
        """
        生成Java源代码
        
        Args:
            config: 项目配置
            project_path: 项目路径
        """
        package_path = config.get(ProjectConstants.CONFIG_PACKAGE, "").replace(".", "/")
        
        # 生成主应用类
        if config.get(ProjectConstants.CONFIG_PROJECT_TYPE) == ProjectConstants.PROJECT_TYPE_SINGLE:
            self._generate_main_application(config, project_path, package_path)
        
        # 生成示例代码（如果启用）
        if config.get(ProjectConstants.CONFIG_GENERATE_SAMPLE_CODE, False):
            self._generate_sample_code(config, project_path, package_path)
        
        # 生成测试代码（如果启用）
        if config.get(ProjectConstants.CONFIG_GENERATE_TESTS, False):
            self._generate_test_code(config, project_path, package_path)
    
    def _generate_main_application(self, config: Dict[str, Any], project_path: Path, package_path: str) -> None:
        """
        生成主应用类
        
        Args:
            config: 项目配置
            project_path: 项目路径
            package_path: 包路径
        """
        app_template = self.jinja_env.get_template("Application.java.j2")
        app_content = app_template.render(config=config)
        
        app_file_path = project_path / "src/main/java" / package_path / "Application.java"
        ensure_dir(str(app_file_path.parent))
        write_file(str(app_file_path), app_content)
    
    def _generate_sample_code(self, config: Dict[str, Any], project_path: Path, package_path: str) -> None:
        """
        生成示例代码
        
        Args:
            config: 项目配置
            project_path: 项目路径
            package_path: 包路径
        """
        # 生成示例控制器
        controller_template = self.jinja_env.get_template("controller/HelloController.java.j2")
        controller_content = controller_template.render(config=config)
        
        controller_path = project_path / "src/main/java" / package_path / "controller"
        ensure_dir(str(controller_path))
        write_file(str(controller_path / "HelloController.java"), controller_content)
        
        # 根据技术栈生成相应的示例代码
        tech_stack = config.get(ProjectConstants.CONFIG_TECH_STACK, {})
        
        # 如果使用数据库，生成实体和服务示例
        if tech_stack.get(ProjectConstants.TECH_DATABASE) != "none":
            self._generate_database_examples(config, project_path, package_path)
    
    def _generate_database_examples(self, config: Dict[str, Any], project_path: Path, package_path: str) -> None:
        """
        生成数据库相关示例代码
        
        Args:
            config: 项目配置
            project_path: 项目路径
            package_path: 包路径
        """
        tech_stack = config.get(ProjectConstants.CONFIG_TECH_STACK, {})
        orm = tech_stack.get(ProjectConstants.TECH_ORM)
        
        if orm == "jpa":
            # 生成JPA实体示例
            entity_template = self.jinja_env.get_template("entity/User.java.j2")
            entity_content = entity_template.render(config=config, orm="jpa")
            
            entity_path = project_path / "src/main/java" / package_path / "entity"
            ensure_dir(str(entity_path))
            write_file(str(entity_path / "User.java"), entity_content)
            
            # 生成Repository示例
            repo_template = self.jinja_env.get_template("repository/UserRepository.java.j2")
            repo_content = repo_template.render(config=config, orm="jpa")
            
            repo_path = project_path / "src/main/java" / package_path / "repository"
            ensure_dir(str(repo_path))
            write_file(str(repo_path / "UserRepository.java"), repo_content)
        
        elif orm == "mybatis":
            # 生成MyBatis相关示例
            # 实体类
            entity_template = self.jinja_env.get_template("entity/User.java.j2")
            entity_content = entity_template.render(config=config, orm="mybatis")
            
            entity_path = project_path / "src/main/java" / package_path / "entity"
            ensure_dir(str(entity_path))
            write_file(str(entity_path / "User.java"), entity_content)
            
            # Mapper接口
            mapper_template = self.jinja_env.get_template("mapper/UserMapper.java.j2")
            mapper_content = mapper_template.render(config=config)
            
            mapper_path = project_path / "src/main/java" / package_path / "mapper"
            ensure_dir(str(mapper_path))
            write_file(str(mapper_path / "UserMapper.java"), mapper_content)
            
            # Mapper XML
            mapper_xml_template = self.jinja_env.get_template("mapper/UserMapper.xml.j2")
            mapper_xml_content = mapper_xml_template.render(config=config)
            
            mapper_xml_path = project_path / "src/main/resources/mapper"
            ensure_dir(str(mapper_xml_path))
            write_file(str(mapper_xml_path / "UserMapper.xml"), mapper_xml_content)
    
    def _generate_test_code(self, config: Dict[str, Any], project_path: Path, package_path: str) -> None:
        """
        生成测试代码
        
        Args:
            config: 项目配置
            project_path: 项目路径
            package_path: 包路径
        """
        # 生成应用测试类
        test_template = self.jinja_env.get_template("test/ApplicationTest.java.j2")
        test_content = test_template.render(config=config)
        
        test_path = project_path / "src/test/java" / package_path
        ensure_dir(str(test_path))
        write_file(str(test_path / "ApplicationTest.java"), test_content)
    
    def _generate_config_files(self, config: Dict[str, Any], project_path: Path) -> None:
        """
        生成配置文件
        
        Args:
            config: 项目配置
            project_path: 项目路径
        """
        # 生成application.yml
        app_config_template = self.jinja_env.get_template("application.yml.j2")
        app_config_content = app_config_template.render(config=config)
        write_file(str(project_path / "src/main/resources/application.yml"), app_config_content)
        
        # 生成logback-spring.xml
        logback_template = self.jinja_env.get_template("logback-spring.xml.j2")
        logback_content = logback_template.render(config=config)
        write_file(str(project_path / "src/main/resources/logback-spring.xml"), logback_content)
    
    def _generate_documentation(self, config: Dict[str, Any], project_path: Path) -> None:
        """
        生成文档文件
        
        Args:
            config: 项目配置
            project_path: 项目路径
        """
        # 生成README.md
        readme_template = self.jinja_env.get_template("README.md.j2")
        readme_content = readme_template.render(config=config)
        write_file(str(project_path / "README.md"), readme_content)
        
        # 生成.gitignore
        gitignore_template = self.jinja_env.get_template(".gitignore.j2")
        gitignore_content = gitignore_template.render(config=config)
        write_file(str(project_path / ".gitignore"), gitignore_content)
    
    def _generate_docker_files(self, config: Dict[str, Any], project_path: Path) -> None:
        """
        生成Docker配置文件
        
        Args:
            config: 项目配置
            project_path: 项目路径
        """
        # 生成Dockerfile
        dockerfile_template = self.jinja_env.get_template("Dockerfile.j2")
        dockerfile_content = dockerfile_template.render(config=config)
        write_file(str(project_path / "Dockerfile"), dockerfile_content)
        
        # 生成docker-compose.yml
        compose_template = self.jinja_env.get_template("docker-compose.yml.j2")
        compose_content = compose_template.render(config=config)
        write_file(str(project_path / "docker-compose.yml"), compose_content)
    
    def _setup_filters(self) -> None:
        """
        设置Jinja2自定义过滤器
        """
        def to_camel_case(text: str) -> str:
            """转换为驼峰命名法"""
            components = text.replace('-', '_').split('_')
            return components[0] + ''.join(word.capitalize() for word in components[1:])
        
        def to_pascal_case(text: str) -> str:
            """转换为帕斯卡命名法"""
            components = text.replace('-', '_').split('_')
            return ''.join(word.capitalize() for word in components)
        
        def to_snake_case(text: str) -> str:
            """转换为蛇形命名法"""
            import re
            s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
            return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
        
        def package_to_path(package: str) -> str:
            """将包名转换为路径"""
            return package.replace('.', '/')
        
        # 注册过滤器
        self.jinja_env.filters['camel_case'] = to_camel_case
        self.jinja_env.filters['pascal_case'] = to_pascal_case
        self.jinja_env.filters['snake_case'] = to_snake_case
        self.jinja_env.filters['package_to_path'] = package_to_path
    
    def _load_templates_from_manager(self) -> Dict[str, str]:
        """
        从模板管理器中加载模板内容
        
        Returns:
            Dict[str, str]: 模板名称到模板内容的映射
        """
        templates = {}
        
        # 尝试加载spring-boot-templates模板
        try:
            if self.template_manager.template_exists("spring-boot-templates"):
                content = self.template_manager.load_template("spring-boot-templates")
                templates = self.template_manager.extract_templates_from_markdown(content)
            else:
                # 如果模板文件不存在，使用默认模板
                print("警告: spring-boot-templates.md 模板文件不存在，使用默认模板")
                templates = self._get_default_templates()
        except Exception as e:
            print(f"警告: 加载模板文件失败 ({str(e)})，使用默认模板")
            templates = self._get_default_templates()
        
        return templates
    

    
    def _get_default_templates(self) -> Dict[str, str]:
        """
        获取默认模板内容（作为后备方案）
        
        Returns:
            Dict[str, str]: 默认模板映射
        """
        return {
            "Application.java.j2": """package {{ config.package }};

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * {{ config.description }}
 * 
 * @author AI Generator
 * @version {{ config.version }}
 */
@SpringBootApplication
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}""",
            "README.md.j2": """# {{ config.name }}

{{ config.description }}

## 项目信息

- **项目名称**: {{ config.name }}
- **版本**: {{ config.version }}
- **Java版本**: {{ config.java_version }}
- **Spring Boot版本**: {{ config.spring_boot_version }}
- **包名**: {{ config.package }}
""",
            ".gitignore.j2": """# Compiled class file
*.class

# Log file
*.log

# Package Files #
*.jar
*.war
*.nar
*.ear
*.zip
*.tar.gz
*.rar

# Maven
target/

# IntelliJ IDEA
.idea/
*.iws
*.iml
*.ipr

# Eclipse
.project
.classpath
.settings/

# VS Code
.vscode/
"""
        }