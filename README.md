# Spring Boot 项目生成器

一个基于 Python 的 CLI 工具，用于快速生成标准化的 Spring Boot 项目模板。支持配置文件管理、多种技术栈选择和项目结构定制。

## 🌟 功能特性

- 🚀 **快速生成** - 一键生成完整的 Spring Boot 项目结构
- 🎯 **技术栈丰富** - 支持多种数据库、缓存、消息队列等技术栈
- 📦 **项目类型** - 支持单模块和多模块项目
- 🎨 **交互式配置** - 友好的命令行交互界面
- 💾 **配置管理** - JSON 格式配置文件的保存、加载和管理
- 📝 **完整文档** - 自动生成项目文档和使用说明
- 🐳 **Docker 支持** - 包含完整的 Docker 配置
- ⚙️ **开发环境** - 预配置的开发、测试、生产环境

## 📁 项目目录结构

```
ai-init-project-generator/
├── spring_init/              # 核心生成器模块
│   ├── __init__.py
│   ├── cli.py               # CLI 命令行接口
│   ├── config.py            # 配置数据结构
│   ├── generator.py         # 项目生成器核心
│   ├── interactive.py       # 交互式配置收集
│   ├── template_manager.py  # 模板文件管理
│   └── utils.py            # 工具函数
├── common/                  # 通用代码目录
│   ├── utils/              # 通用工具函数
│   │   ├── string_utils.py # 字符串处理工具
│   │   └── file_utils.py   # 文件操作工具
│   ├── validators/         # 验证器
│   │   └── project_validator.py # 项目配置验证
│   ├── constants/          # 常量定义
│   │   └── project_constants.py # 项目常量
│   └── config_manager.py   # 配置文件管理器
├── templates/              # Jinja2 模板文件
├── output/                 # 生成的项目输出目录
├── configs/                # 用户配置文件存储目录
├── tests/                  # 测试文件
├── main.py                 # 主入口文件
├── requirements.txt        # Python 依赖
└── README.md
```

## 🚀 快速开始

### 安装依赖

```bash
# 克隆项目
git clone <repository-url>
cd ai-init-project-generator

# 安装依赖
pip install -r requirements.txt
```

### 基本使用

#### 1. 交互式创建项目

```bash
# 使用交互式界面创建项目
python main.py create --interactive
```

#### 2. 命令行创建项目

```bash
# 直接通过命令行参数创建项目
python main.py create \
  --name my-spring-project \
  --package com.example.myproject \
  --java-version 17 \
  --spring-boot-version 3.2.0 \
  --multi-module
```

#### 3. 配置文件管理

```bash
# 列出所有保存的配置
python main.py list-configs

# 查看特定配置详情
python main.py show-config my-config

# 从配置文件生成项目
python main.py generate my-config

# 导出配置文件
python main.py export-config my-config ./exported-config.json

# 导入配置文件
python main.py import-config ./config.json --config-name imported-config

# 删除配置文件
python main.py delete-config my-config
```

### 命令行选项

```bash
# 查看所有可用命令
python main.py --help

# 查看创建命令的详细选项
python main.py create --help
```

## 🛠️ 支持的技术栈

### 数据库
- **MySQL** - 最流行的开源关系型数据库
- **PostgreSQL** - 功能强大的开源对象关系型数据库
- **H2** - 内存数据库，适用于开发和测试

### ORM 框架
- **MyBatis** - 优秀的持久层框架
- **MyBatis-Plus** - MyBatis 的增强工具
- **JPA/Hibernate** - Java 持久化 API

### 缓存
- **Redis** - 高性能的内存数据结构存储
- **Caffeine** - 高性能的本地缓存库

### 消息队列
- **RabbitMQ** - 可靠的消息代理
- **Apache Kafka** - 分布式流处理平台
- **RocketMQ** - 阿里巴巴开源的消息中间件

### NoSQL 数据库
- **MongoDB** - 面向文档的数据库
- **Elasticsearch** - 分布式搜索和分析引擎

### 文档工具
- **Swagger/OpenAPI 3** - API 文档生成
- **Spring REST Docs** - 测试驱动的文档

### 安全框架
- **Spring Security** - 强大的安全框架
- **JWT** - JSON Web Token 认证

### 监控工具
- **Spring Boot Actuator** - 生产就绪功能
- **Micrometer** - 应用监控门面

## 📋 生成的项目结构

### 单模块项目

```
my-spring-project/
├── src/
│   ├── main/
│   │   ├── java/com/example/myproject/
│   │   │   ├── MyProjectApplication.java    # 启动类
│   │   │   ├── controller/                  # 控制器层
│   │   │   │   └── UserController.java
│   │   │   ├── service/                     # 服务层
│   │   │   │   ├── UserService.java
│   │   │   │   └── impl/
│   │   │   │       └── UserServiceImpl.java
│   │   │   ├── repository/                  # 数据访问层
│   │   │   │   └── UserRepository.java
│   │   │   ├── entity/                      # 实体类
│   │   │   │   └── User.java
│   │   │   ├── dto/                         # 数据传输对象
│   │   │   ├── config/                      # 配置类
│   │   │   ├── exception/                   # 异常处理
│   │   │   └── common/                      # 通用类
│   │   └── resources/
│   │       ├── application.yml              # 主配置文件
│   │       ├── application-dev.yml          # 开发环境配置
│   │       ├── application-test.yml         # 测试环境配置
│   │       ├── application-prod.yml         # 生产环境配置
│   │       └── logback-spring.xml          # 日志配置
│   └── test/                               # 测试代码
├── docker/
│   ├── Dockerfile                          # Docker 镜像构建文件
│   └── docker-compose.yml                 # Docker Compose 配置
├── docs/                                   # 项目文档
├── pom.xml                                 # Maven 配置文件
├── .gitignore                             # Git 忽略文件
└── README.md                              # 项目说明文档
```

### 多模块项目

```
my-spring-project/
├── my-spring-project-common/               # 公共模块
├── my-spring-project-api/                  # API 模块
├── my-spring-project-service/              # 服务模块
├── my-spring-project-web/                  # Web 模块
├── docker/
├── docs/
├── pom.xml                                 # 父 POM
└── README.md
```

## 🔧 配置文件格式

配置文件采用 JSON 格式，包含以下主要字段：

```json
{
  "name": "my-spring-project",
  "package": "com.example.myproject",
  "version": "1.0.0",
  "description": "A Spring Boot project",
  "java_version": "17",
  "spring_boot_version": "3.2.0",
  "project_type": "single-module",
  "tech_stack": {
    "database": "mysql",
    "orm": "mybatis",
    "cache": ["redis"],
    "message_queue": ["rabbitmq"],
    "nosql": ["mongodb"],
    "documentation": ["swagger"],
    "security": ["spring-security"],
    "monitoring": ["actuator"]
  },
  "modules": [],
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-01T00:00:00"
}
```

## 🧪 开发和测试

### 运行测试

```bash
# 运行所有测试
python -m pytest tests/

# 运行特定测试文件
python -m pytest tests/test_generator.py

# 运行测试并显示覆盖率
python -m pytest tests/ --cov=spring_init
```

### 添加新功能

1. **添加新的技术栈支持**
   - 在 `common/constants/project_constants.py` 中添加新的常量
   - 在 `common/validators/project_validator.py` 中添加验证逻辑
   - 在 `templates/` 目录下添加相应的模板文件

2. **添加新的模板文件**
   - 在 `templates/` 目录下创建新的 Jinja2 模板
   - 在 `spring_init/template_manager.py` 中注册新模板
   - 在 `spring_init/generator.py` 中添加生成逻辑

3. **扩展配置选项**
   - 在 `spring_init/config.py` 中扩展配置数据结构
   - 在 `spring_init/interactive.py` 中添加交互式收集逻辑
   - 在 `spring_init/cli.py` 中添加命令行选项

## 🤝 贡献指南

我们欢迎所有形式的贡献！

### 提交 Issue

- 🐛 **Bug 报告** - 详细描述问题和复现步骤
- 💡 **功能建议** - 描述新功能的用途和实现思路
- 📚 **文档改进** - 指出文档中的错误或不清楚的地方

### 提交 Pull Request

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 开启 Pull Request

### 代码规范

- 遵循 PEP 8 Python 代码规范
- 添加适当的注释和文档字符串
- 为新功能编写测试用例
- 确保所有测试通过

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 📞 联系方式

- 项目主页：[GitHub Repository](https://github.com/your-username/ai-init-project-generator)
- 问题反馈：[GitHub Issues](https://github.com/your-username/ai-init-project-generator/issues)
- 邮箱：ai@example.com

---

⭐ 如果这个项目对你有帮助，请给我们一个 Star！