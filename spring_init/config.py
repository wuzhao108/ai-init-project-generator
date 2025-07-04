#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
项目配置模块
定义项目配置的数据结构和相关方法
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any
import os


@dataclass
class TechStack:
    """技术栈配置"""
    # 数据层
    database: str = "mysql"  # mysql, postgresql, h2
    orm: str = "mybatis"  # mybatis, jpa
    
    # 缓存
    cache: List[str] = field(default_factory=lambda: ["redis"])  # redis, caffeine
    
    # 消息队列
    mq: List[str] = field(default_factory=list)  # rabbitmq, kafka
    
    # 文档
    doc: bool = True  # swagger/openapi
    
    # 安全
    security: bool = False  # spring security
    
    # 其他组件
    mongodb: bool = False
    elasticsearch: bool = False
    
    # Web相关
    web_framework: str = "spring-web"  # spring-web, spring-webflux
    
    # 监控
    actuator: bool = True
    
    # 测试
    test_framework: List[str] = field(default_factory=lambda: ["junit5", "mockito"])


@dataclass
class ModuleConfig:
    """模块配置"""
    name: str
    description: str
    dependencies: List[str] = field(default_factory=list)


@dataclass
class ProjectConfig:
    """项目配置"""
    # 基本信息
    name: str
    package: str
    version: str = "1.0.0"
    description: str = ""
    
    # 技术版本
    java_version: str = "11"
    spring_version: str = "2.7.18"
    
    # 项目结构
    multi_module: bool = False
    modules: List[ModuleConfig] = field(default_factory=list)
    
    # 技术栈
    tech_stack: TechStack = field(default_factory=TechStack)
    
    # 输出配置
    output_dir: str = "."
    
    # 代码生成选项
    generate_sample_code: bool = True
    generate_tests: bool = True
    generate_docker: bool = True
    
    def __post_init__(self):
        """初始化后处理"""
        if self.multi_module and not self.modules:
            # 默认多模块结构
            self.modules = [
                ModuleConfig("common", "公共模块"),
                ModuleConfig("api", "API接口模块"),
                ModuleConfig("service", "业务服务模块"),
                ModuleConfig("dao", "数据访问模块"),
                ModuleConfig("web", "Web控制器模块"),
            ]
    
    @property
    def project_path(self) -> str:
        """项目路径"""
        return os.path.join(self.output_dir, self.name)
    
    @property
    def package_path(self) -> str:
        """包路径"""
        return self.package.replace('.', '/')
    
    @property
    def main_class_name(self) -> str:
        """主类名"""
        # 将项目名转换为驼峰命名
        words = self.name.replace('-', '_').split('_')
        return ''.join(word.capitalize() for word in words) + 'Application'
    
    def get_spring_boot_dependencies(self) -> List[Dict[str, Any]]:
        """获取SpringBoot依赖列表"""
        dependencies = [
            {
                'groupId': 'org.springframework.boot',
                'artifactId': 'spring-boot-starter-web',
                'scope': None
            },
            {
                'groupId': 'org.springframework.boot',
                'artifactId': 'spring-boot-starter-test',
                'scope': 'test'
            }
        ]
        
        # 根据技术栈添加依赖
        if self.tech_stack.orm == 'mybatis':
            dependencies.append({
                'groupId': 'org.mybatis.spring.boot',
                'artifactId': 'mybatis-spring-boot-starter',
                'scope': None
            })
        elif self.tech_stack.orm == 'jpa':
            dependencies.append({
                'groupId': 'org.springframework.boot',
                'artifactId': 'spring-boot-starter-data-jpa',
                'scope': None
            })
        
        # 数据库驱动
        if self.tech_stack.database == 'mysql':
            dependencies.append({
                'groupId': 'mysql',
                'artifactId': 'mysql-connector-java',
                'scope': 'runtime'
            })
        elif self.tech_stack.database == 'postgresql':
            dependencies.append({
                'groupId': 'org.postgresql',
                'artifactId': 'postgresql',
                'scope': 'runtime'
            })
        elif self.tech_stack.database == 'h2':
            dependencies.append({
                'groupId': 'com.h2database',
                'artifactId': 'h2',
                'scope': 'runtime'
            })
        
        # Redis
        if 'redis' in self.tech_stack.cache:
            dependencies.append({
                'groupId': 'org.springframework.boot',
                'artifactId': 'spring-boot-starter-data-redis',
                'scope': None
            })
        
        # RabbitMQ
        if 'rabbitmq' in self.tech_stack.mq:
            dependencies.append({
                'groupId': 'org.springframework.boot',
                'artifactId': 'spring-boot-starter-amqp',
                'scope': None
            })
        
        # Kafka
        if 'kafka' in self.tech_stack.mq:
            dependencies.append({
                'groupId': 'org.springframework.kafka',
                'artifactId': 'spring-kafka',
                'scope': None
            })
        
        # Swagger
        if self.tech_stack.doc:
            dependencies.extend([
                {
                    'groupId': 'io.springfox',
                    'artifactId': 'springfox-swagger2',
                    'scope': None
                },
                {
                    'groupId': 'io.springfox',
                    'artifactId': 'springfox-swagger-ui',
                    'scope': None
                }
            ])
        
        # Spring Security
        if self.tech_stack.security:
            dependencies.append({
                'groupId': 'org.springframework.boot',
                'artifactId': 'spring-boot-starter-security',
                'scope': None
            })
        
        # MongoDB
        if self.tech_stack.mongodb:
            dependencies.append({
                'groupId': 'org.springframework.boot',
                'artifactId': 'spring-boot-starter-data-mongodb',
                'scope': None
            })
        
        # Elasticsearch
        if self.tech_stack.elasticsearch:
            dependencies.append({
                'groupId': 'org.springframework.boot',
                'artifactId': 'spring-boot-starter-data-elasticsearch',
                'scope': None
            })
        
        # Actuator
        if self.tech_stack.actuator:
            dependencies.append({
                'groupId': 'org.springframework.boot',
                'artifactId': 'spring-boot-starter-actuator',
                'scope': None
            })
        
        return dependencies
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        return {
            'name': self.name,
            'package': self.package,
            'version': self.version,
            'description': self.description,
            'java_version': self.java_version,
            'spring_version': self.spring_version,
            'multi_module': self.multi_module,
            'modules': [{'name': m.name, 'description': m.description} for m in self.modules],
            'tech_stack': {
                'database': self.tech_stack.database,
                'orm': self.tech_stack.orm,
                'cache': self.tech_stack.cache,
                'mq': self.tech_stack.mq,
                'doc': self.tech_stack.doc,
                'security': self.tech_stack.security,
                'mongodb': self.tech_stack.mongodb,
                'elasticsearch': self.tech_stack.elasticsearch,
            },
            'dependencies': self.get_spring_boot_dependencies()
        }