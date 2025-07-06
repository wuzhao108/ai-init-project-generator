# -*- coding: utf-8 -*-
"""
项目常量定义模块
定义项目中使用的各种常量
"""

from typing import List, Dict


class ProjectConstants:
    """项目常量类"""
    
    # 项目类型
    PROJECT_TYPE_SINGLE = "single"
    PROJECT_TYPE_MULTI = "multi"
    
    # Java版本
    JAVA_VERSIONS: List[str] = ["8", "11", "17", "21"]
    
    # Spring Boot版本
    SPRING_BOOT_VERSIONS: List[str] = ["2.7.18", "3.0.13", "3.1.8", "3.2.2", "3.3.0"]
    
    # 数据库类型
    DATABASE_MYSQL = "mysql"
    DATABASE_POSTGRESQL = "postgresql"
    DATABASE_H2 = "h2"
    DATABASES: List[str] = [DATABASE_MYSQL, DATABASE_POSTGRESQL, DATABASE_H2]
    
    # ORM框架
    ORM_MYBATIS = "mybatis"
    ORM_JPA = "jpa"
    ORMS: List[str] = [ORM_MYBATIS, ORM_JPA]
    
    # 缓存类型
    CACHE_REDIS = "redis"
    CACHE_CAFFEINE = "caffeine"
    CACHES: List[str] = [CACHE_REDIS, CACHE_CAFFEINE]
    
    # 消息队列
    MQ_RABBITMQ = "rabbitmq"
    MQ_KAFKA = "kafka"
    MQS: List[str] = [MQ_RABBITMQ, MQ_KAFKA]
    
    # NoSQL数据库
    NOSQL_MONGODB = "mongodb"
    NOSQL_ELASTICSEARCH = "elasticsearch"
    NOSQLS: List[str] = [NOSQL_MONGODB, NOSQL_ELASTICSEARCH]
    
    # 文档工具
    DOC_SWAGGER = "swagger"
    DOCS: List[str] = [DOC_SWAGGER]
    
    # 安全框架
    SECURITY_SPRING_SECURITY = "spring-security"
    SECURITIES: List[str] = [SECURITY_SPRING_SECURITY]
    
    # 监控工具
    MONITOR_ACTUATOR = "actuator"
    MONITORS: List[str] = [MONITOR_ACTUATOR]
    
    # Web框架
    WEB_SPRING_WEB = "spring-web"
    WEB_SPRING_WEBFLUX = "spring-webflux"
    WEB_FRAMEWORKS: List[str] = [WEB_SPRING_WEB, WEB_SPRING_WEBFLUX]
    
    # 测试框架
    TEST_JUNIT5 = "junit5"
    TEST_MOCKITO = "mockito"
    TEST_TESTCONTAINERS = "testcontainers"
    TEST_FRAMEWORKS: List[str] = [TEST_JUNIT5, TEST_MOCKITO, TEST_TESTCONTAINERS]
    
    # 模块类型
    MODULE_COMMON = "common"
    MODULE_API = "api"
    MODULE_DAO = "dao"
    MODULE_SERVICE = "service"
    MODULE_WEB = "web"
    MODULES: List[str] = [MODULE_COMMON, MODULE_API, MODULE_DAO, MODULE_SERVICE, MODULE_WEB]
    
    # 默认配置
    DEFAULT_PROJECT_VERSION = "1.0.0"
    DEFAULT_JAVA_VERSION = "17"
    DEFAULT_SPRING_BOOT_VERSION = "3.2.2"
    DEFAULT_DATABASE = DATABASE_MYSQL
    DEFAULT_ORM = ORM_MYBATIS
    DEFAULT_CACHE = [CACHE_REDIS]
    DEFAULT_WEB_FRAMEWORK = WEB_SPRING_WEB
    DEFAULT_TEST_FRAMEWORKS = [TEST_JUNIT5, TEST_MOCKITO]
    
    # 文件扩展名
    EXTENSION_JAVA = ".java"
    EXTENSION_XML = ".xml"
    EXTENSION_YML = ".yml"
    EXTENSION_YAML = ".yaml"
    EXTENSION_PROPERTIES = ".properties"
    EXTENSION_JSON = ".json"
    EXTENSION_MD = ".md"
    EXTENSION_DOCKERFILE = ""
    EXTENSION_GITIGNORE = ""
    
    # 目录名称
    DIR_SRC = "src"
    DIR_MAIN = "main"
    DIR_TEST = "test"
    DIR_JAVA = "java"
    DIR_RESOURCES = "resources"
    DIR_WEBAPP = "webapp"
    DIR_TARGET = "target"
    DIR_LOGS = "logs"
    DIR_UPLOADS = "uploads"
    DIR_DOCKER = "docker"
    DIR_DOCS = "docs"
    
    # 包名称
    PACKAGE_CONTROLLER = "controller"
    PACKAGE_SERVICE = "service"
    PACKAGE_SERVICE_IMPL = "service.impl"
    PACKAGE_MAPPER = "mapper"
    PACKAGE_REPOSITORY = "repository"
    PACKAGE_ENTITY = "entity"
    PACKAGE_DTO = "dto"
    PACKAGE_VO = "vo"
    PACKAGE_CONFIG = "config"
    PACKAGE_COMMON = "common"
    PACKAGE_EXCEPTION = "common.exception"
    PACKAGE_UTIL = "util"
    
    # 文件名称
    FILE_POM_XML = "pom.xml"
    FILE_APPLICATION_JAVA = "Application.java"
    FILE_APPLICATION_YML = "application.yml"
    FILE_APPLICATION_DEV_YML = "application-dev.yml"
    FILE_APPLICATION_TEST_YML = "application-test.yml"
    FILE_APPLICATION_PROD_YML = "application-prod.yml"
    FILE_LOGBACK_SPRING_XML = "logback-spring.xml"
    FILE_DOCKERFILE = "Dockerfile"
    FILE_DOCKER_COMPOSE_YML = "docker-compose.yml"
    FILE_GITIGNORE = ".gitignore"
    FILE_README_MD = "README.md"
    
    # 配置文件键名
    CONFIG_NAME = "name"
    CONFIG_PACKAGE = "package"
    CONFIG_VERSION = "version"
    CONFIG_DESCRIPTION = "description"
    CONFIG_JAVA_VERSION = "java_version"
    CONFIG_SPRING_BOOT_VERSION = "spring_boot_version"
    CONFIG_PROJECT_TYPE = "project_type"
    CONFIG_TECH_STACK = "tech_stack"
    CONFIG_MODULES = "modules"
    CONFIG_OUTPUT_DIR = "output_dir"
    CONFIG_PREVIEW_MODE = "preview_mode"
    CONFIG_CREATED_AT = "created_at"
    CONFIG_UPDATED_AT = "updated_at"
    
    # 技术栈配置键名
    TECH_DATABASE = "database"
    TECH_ORM = "orm"
    TECH_CACHE = "cache"
    TECH_MQ = "mq"
    TECH_NOSQL = "nosql"
    TECH_DOC = "doc"
    TECH_SECURITY = "security"
    TECH_MONITOR = "monitor"
    TECH_WEB_FRAMEWORK = "web_framework"
    TECH_TEST_FRAMEWORKS = "test_frameworks"
    
    # 环境配置
    ENV_DEV = "dev"
    ENV_TEST = "test"
    ENV_PROD = "prod"
    ENVIRONMENTS: List[str] = [ENV_DEV, ENV_TEST, ENV_PROD]
    
    # 端口配置
    DEFAULT_SERVER_PORT = 8080
    DEFAULT_MYSQL_PORT = 3306
    DEFAULT_POSTGRESQL_PORT = 5432
    DEFAULT_REDIS_PORT = 6379
    DEFAULT_RABBITMQ_PORT = 5672
    DEFAULT_RABBITMQ_MANAGEMENT_PORT = 15672
    DEFAULT_KAFKA_PORT = 9092
    DEFAULT_MONGODB_PORT = 27017
    DEFAULT_ELASTICSEARCH_PORT = 9200
    DEFAULT_KIBANA_PORT = 5601
    
    # 错误消息
    ERROR_INVALID_PROJECT_NAME = "项目名称格式不正确"
    ERROR_INVALID_PACKAGE_NAME = "包名格式不正确"
    ERROR_INVALID_VERSION = "版本号格式不正确"
    ERROR_INVALID_JAVA_VERSION = "不支持的Java版本"
    ERROR_INVALID_SPRING_BOOT_VERSION = "不支持的Spring Boot版本"
    ERROR_INVALID_OUTPUT_DIR = "输出目录无效"
    ERROR_CONFIG_NOT_FOUND = "配置文件不存在"
    ERROR_CONFIG_INVALID = "配置文件格式无效"
    ERROR_TEMPLATE_NOT_FOUND = "模板文件不存在"
    ERROR_GENERATION_FAILED = "项目生成失败"
    
    # 成功消息
    SUCCESS_PROJECT_CREATED = "项目创建成功"
    SUCCESS_CONFIG_SAVED = "配置保存成功"
    SUCCESS_CONFIG_LOADED = "配置加载成功"
    
    # 日志级别
    LOG_LEVEL_DEBUG = "DEBUG"
    LOG_LEVEL_INFO = "INFO"
    LOG_LEVEL_WARN = "WARN"
    LOG_LEVEL_ERROR = "ERROR"
    
    # 编码格式
    ENCODING_UTF8 = "utf-8"
    ENCODING_GBK = "gbk"
    
    # 换行符
    LINE_SEPARATOR_UNIX = "\n"
    LINE_SEPARATOR_WINDOWS = "\r\n"
    
    # 路径分隔符
    PATH_SEPARATOR_UNIX = "/"
    PATH_SEPARATOR_WINDOWS = "\\"
    
    # 模板变量
    TEMPLATE_VAR_CONFIG = "config"
    TEMPLATE_VAR_PROJECT_NAME = "project_name"
    TEMPLATE_VAR_PACKAGE_NAME = "package_name"
    TEMPLATE_VAR_CLASS_NAME = "class_name"
    TEMPLATE_VAR_CURRENT_DATE = "current_date"
    TEMPLATE_VAR_CURRENT_DATETIME = "current_datetime"
    
    # 依赖版本
    DEPENDENCY_VERSIONS: Dict[str, str] = {
        "mysql-connector-java": "8.0.33",
        "postgresql": "42.6.0",
        "h2": "2.2.224",
        "mybatis-spring-boot-starter": "3.0.3",
        "spring-boot-starter-data-jpa": "auto",
        "spring-boot-starter-data-redis": "auto",
        "caffeine": "3.1.8",
        "spring-boot-starter-amqp": "auto",
        "spring-kafka": "auto",
        "spring-boot-starter-data-mongodb": "auto",
        "spring-boot-starter-data-elasticsearch": "auto",
        "springdoc-openapi-starter-webmvc-ui": "2.2.0",
        "spring-boot-starter-security": "auto",
        "jjwt-api": "0.11.5",
        "jjwt-impl": "0.11.5",
        "jjwt-jackson": "0.11.5",
        "spring-boot-starter-actuator": "auto",
        "spring-boot-starter-test": "auto",
        "testcontainers-junit-jupiter": "1.19.3",
        "testcontainers-mysql": "1.19.3",
        "testcontainers-postgresql": "1.19.3"
    }