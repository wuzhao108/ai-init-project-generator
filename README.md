# AI Spring Boot 项目生成器

一个基于 Python 的智能化 Spring Boot 项目生成器，支持多种技术栈和项目结构的快速生成。该工具提供了丰富的技术栈选择、灵活的配置管理和友好的交互式界面。

## 📖 项目概述

### 🎯 设计目标
- **提高开发效率** - 减少项目初始化时间，让开发者专注于业务逻辑
- **标准化项目结构** - 确保团队项目结构的一致性
- **技术栈集成** - 预配置常用技术栈，减少配置工作
- **最佳实践** - 内置行业最佳实践和代码规范

## ✨ 核心特性

- 🚀 **快速生成** - 一键生成完整的 Spring Boot 项目结构
- 🎯 **技术栈丰富** - 支持主流数据库、缓存、消息队列等技术栈
- 📋 **配置管理** - 支持配置文件的保存、导入、导出和管理
- 🔧 **灵活定制** - 支持单模块和多模块项目架构
- 📚 **文档完整** - 自动生成项目文档和 API 文档
- 🐳 **Docker 支持** - 自动生成 Docker 配置文件
- 🎨 **交互友好** - 提供直观的命令行交互界面
- 🔄 **配置管理系统V2** - 分层配置管理，支持系统、模板、历史三层架构

## 📁 项目目录结构

```
ai-init-project-generator/
├── main.py                    # 主程序入口
├── requirements.txt           # Python 依赖
├── setup.py                  # 安装配置
├── README.md                 # 项目说明
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
├── configs/                # 配置管理系统V2
│   ├── README.md           # 配置系统详细说明
│   ├── system/             # 系统级配置
│   │   └── system.json    # 系统配置文件
│   ├── templates/          # 模板配置（Markdown格式）
│   │   ├── spring-boot-basic.md
│   │   ├── spring-boot-microservice.md
│   │   └── spring-boot-web.md
│   ├── history/            # 历史配置（Markdown格式）
│   │   └── *.md           # 项目历史配置
│   ├── backup/             # 备份目录
│   ├── config_manager_v2.py # 配置管理器V2
│   ├── config_cli.py       # 配置管理CLI工具
│   ├── config_migrator.py  # 配置迁移工具
│   └── default_template.json # 默认模板配置
├── docs/                    # 项目文档
│   ├── README.md           # 详细功能文档
│   ├── QUICK_START.md      # 快速开始指南
│   ├── API_REFERENCE.md    # API参考文档
│   ├── TROUBLESHOOTING.md  # 故障排除指南
│   └── INDEX.md            # 文档索引
├── scripts/                 # 测试和调试脚本
│   ├── README.md           # 脚本说明
│   ├── test_click.py       # 依赖测试脚本
│   ├── verify_structure.py # 结构验证脚本
│   └── debug_import.py     # 导入调试脚本
├── output/                  # 生成的项目输出目录
└── tests/                   # 测试文件
    ├── __init__.py
    └── test_*.py
```

## 🚀 快速开始

### 环境要求

- Python 3.6+
- pip 包管理器
- Java 8+ (用于运行生成的项目)
- Maven 3.6+ (用于构建生成的项目)

### 安装步骤

```bash
# 1. 克隆项目
git clone <repository-url>
cd ai-init-project-generator

# 2. 安装依赖
pip install -r requirements.txt

# 3. 验证安装
python main.py --help
```

### 创建第一个项目

```bash
# 启动交互式界面
python main.py

# 选择菜单选项：
# 1. 🆕 创建项目模板
# 2. 📁 从配置文件生成项目
# 3. 📋 查看已保存的配置
# 4. 📄 查看配置详情
# 5. 🗑️ 删除配置文件
# 6. 📤 导出配置文件
# 7. 📥 导入配置文件
# 8. 📚 查看可用模板
```

## 📋 主要功能

### 1. 🆕 创建项目模板
- **默认模板模式** - 使用预配置的模板快速创建
- **自定义配置模式** - 通过交互式界面自定义项目配置
- 支持单模块和多模块项目架构
- 自动配置技术栈依赖和代码结构

### 2. 📁 配置文件管理
- **保存配置** - 将项目配置保存为可重用的模板
- **导入/导出** - 支持配置文件的导入导出和团队共享
- **历史记录** - 自动记录每次项目创建的配置历史
- **配置迁移** - 支持从旧版本JSON格式迁移到新版本Markdown格式

### 3. 🔧 配置管理系统V2
- **分层架构** - 系统配置、模板配置、历史配置三层管理
- **Markdown格式** - 模板和历史配置使用Markdown格式，提供更好的可读性
- **CLI工具** - 完整的命令行工具支持配置管理操作
- **自动备份** - 配置变更时自动创建备份

### 4. 📚 模板和文档
- **丰富模板** - 内置多种项目模板和技术栈组合
- **自动文档** - 自动生成项目文档和API文档
- **Docker集成** - 自动生成Docker配置文件
- **测试支持** - 生成完整的测试框架和示例代码

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

# 使用默认配置创建项目
python main.py create --name my-project --package com.example.myproject

# 指定技术栈
python main.py create --name my-project --package com.example.myproject --database mysql --orm mybatis --cache redis

# 创建多模块项目
python main.py create --name my-project --package com.example.myproject --multi-module
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

# 配置管理CLI工具
python configs/config_cli.py template list
python configs/config_cli.py history cleanup --days 30
```

## 📖 详细文档

本项目提供了完整的文档体系，详细说明了各项功能的使用方法：

- **[📋 详细功能文档](docs/README.md)** - 完整的功能说明和操作演示
- **[🚀 快速开始指南](docs/QUICK_START.md)** - 新手入门和快速上手
- **[📚 API参考文档](docs/API_REFERENCE.md)** - 核心类和方法的详细说明
- **[🔧 故障排除指南](docs/TROUBLESHOOTING.md)** - 常见问题和解决方案
- **[📑 文档索引](docs/INDEX.md)** - 文档导航和搜索指南
- **[⚙️ 配置管理系统](configs/README.md)** - 配置管理系统V2详细说明
- **[🔨 脚本工具](scripts/README.md)** - 测试和调试脚本说明

### 命令行选项

```bash
# 查看所有可用命令
python main.py --help

# 查看创建命令的详细选项
python main.py create --help

# 查看配置管理CLI帮助
python configs/config_cli.py --help
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

## 📈 项目历史版本

### v2.0.0 (2025-01-06) - 配置管理系统重构
- ✨ **重大更新**: 配置管理系统V2
- 🔄 **分层架构**: 系统、模板、历史三层配置管理
- 📝 **Markdown格式**: 模板和历史配置改用Markdown格式
- 🛠️ **CLI工具**: 完整的配置管理命令行工具
- 🔄 **配置迁移**: 支持从JSON格式迁移到Markdown格式
- 📚 **文档完善**: 新增详细的功能文档和API参考
- 🔧 **脚本工具**: 新增测试、调试和验证脚本

### v1.5.0 (2024-12-01) - 功能增强
- 🆕 **多模块支持**: 完善多模块项目生成
- 🐳 **Docker集成**: 自动生成Docker配置
- 📋 **配置管理**: 增强配置文件管理功能
- 🎨 **UI优化**: 改进交互式界面体验

### v1.0.0 (2024-01-01) - 初始版本
- 🚀 **基础功能**: Spring Boot项目生成
- 📦 **技术栈支持**: 主流数据库、缓存、消息队列
- 🎯 **项目类型**: 单模块项目支持
- 💾 **配置管理**: JSON格式配置文件

## 🧪 开发和测试

### 运行测试

```bash
# 运行所有测试
python -m pytest tests/

# 运行特定测试文件
python -m pytest tests/test_generator.py

# 运行测试并显示覆盖率
python -m pytest tests/ --cov=spring_init

# 运行脚本测试
python scripts/test_click.py
python scripts/verify_structure.py
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
- 文档反馈：请通过 Issues 或 Pull Request 提供文档改进建议

## 🙏 致谢

感谢所有为这个项目做出贡献的开发者和用户！

特别感谢：
- Spring Boot 团队提供的优秀框架
- 开源社区提供的各种技术栈支持
- 所有提供反馈和建议的用户

---

⭐ 如果这个项目对你有帮助，请给我们一个 Star！

📖 **推荐阅读顺序**：
1. 先阅读本 README 了解项目概况
2. 查看 [快速开始指南](docs/QUICK_START.md) 快速上手
3. 参考 [详细功能文档](docs/README.md) 了解所有功能
4. 遇到问题时查看 [故障排除指南](docs/TROUBLESHOOTING.md)
5. 开发时参考 [API参考文档](docs/API_REFERENCE.md)