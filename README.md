# Java项目上下文工程生成器

一个基于Python的交互式工具，用于生成Java项目初始化的上下文提示词。支持多种技术栈配置，生成系统提示词、用户提示词和Gemini斜杠命令文件，帮助AI快速生成高质量的Java Spring Boot项目。

## 📖 项目概述

### 🎯 设计目标
- **AI驱动开发** - 生成标准化的AI提示词，确保项目生成质量
- **上下文工程** - 提供完整的项目生成上下文，包含系统指令和用户需求
- **技术栈集成** - 支持主流Java技术栈的配置和选择
- **标准化输出** - 生成统一格式的上下文工程文件

## ✨ 核心特性

- 🚀 **交互式配置** - 通过友好的命令行界面收集Java项目配置
- 🤖 **AI提示词生成** - 自动生成系统提示词和用户提示词
- 💎 **Gemini CLI支持** - 生成Gemini斜杠命令文件，支持一键项目生成
- 📋 **多种技术栈** - 支持JDK版本、Spring Boot、数据库、缓存、消息队列等配置
- 🏗️ **项目结构** - 支持单模块和多模块项目架构
- 📁 **标准化输出** - 生成完整的上下文工程目录
- 💾 **配置保存** - 自动保存配置历史，支持重复使用
- 📚 **文档完整** - 包含项目结构说明和使用指南

## 📁 项目目录结构

```
ai-init-project-generator/
├── .gitignore                    # Git忽略文件配置
├── main.py                       # 主程序入口
├── requirements.txt              # Python依赖包列表
├── README.md                     # 项目说明文档
├── scripts/                      # 核心脚本目录
│   ├── core/                     # 核心功能模块
│   │   ├── __init__.py
│   │   ├── config_collector.py   # 配置收集器
│   │   └── context_generator.py  # 上下文生成器
│   └── templates/                # 项目模板文件
│       └── java_project_template.md
└── output/                       # 生成的上下文工程输出目录
    └── [项目名称_时间戳]/         # 每次生成的上下文工程
        ├── config.json           # 项目配置文件
        ├── system_prompt.md      # 系统提示词
        ├── user_prompt.md        # 用户提示词
        ├── project_generator.gemini # Gemini斜杠命令文件
        ├── project_structure.md  # 项目结构说明
        └── README.md             # 使用说明
```

## 🚀 快速开始

### 环境要求

- Python 3.6+
- pip 包管理器

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

### 创建第一个上下文工程

```bash
# 启动交互式界面
python main.py

# 按照提示进行配置：
# 1. 输入项目基本信息（名称、包名、版本、描述）
# 2. 选择技术版本（JDK、构建工具、Spring Boot版本）
# 3. 配置项目结构（单模块/多模块）
# 4. 选择技术栈（数据库、ORM、缓存、消息队列等）
# 5. 设置生成选项（示例代码、测试、Docker等）
# 6. 确认配置并生成上下文工程
```

## 📋 主要功能

### 1. 上下文工程生成

- **系统提示词**: 生成AI项目生成的规范和步骤说明
- **用户提示词**: 根据用户配置生成具体的项目需求描述
- **Gemini命令**: 生成支持Gemini CLI的斜杠命令文件
- **项目结构**: 生成详细的项目目录结构说明
- **配置保存**: 自动保存用户配置，支持历史查看

### 2. 技术栈支持

#### JDK版本
- Java 8
- Java 11
- Java 17 (推荐)
- Java 21

#### 构建工具
- Maven
- Gradle

#### Spring Boot版本
- 3.2.0 (最新)
- 3.1.6
- 3.0.13
- 2.7.18

#### 数据库支持
- MySQL
- PostgreSQL
- H2 (内存数据库)
- Oracle
- SQL Server

#### ORM框架
- MyBatis
- JPA/Hibernate
- MyBatis-Plus

#### 缓存组件
- Redis
- Caffeine
- Ehcache

#### 消息队列
- RabbitMQ
- Apache Kafka
- RocketMQ

#### 其他组件
- Swagger/OpenAPI 3.0 (API文档)
- Spring Security (安全框架)
- Spring Boot Actuator (监控)

### 3. 生成选项

- **示例代码**: 生成完整的业务逻辑示例
- **测试代码**: 生成单元测试和集成测试
- **Docker配置**: 生成容器化部署配置
- **README文档**: 生成详细的项目说明文档

## 🔧 使用生成的上下文工程

生成的上下文工程包含多种使用方式：

### 方法一：使用Gemini CLI

```bash
# 安装Gemini CLI工具
npm install -g @google/generative-ai-cli

# 使用生成的Gemini命令文件
gemini run output/[项目名称_时间戳]/project_generator.gemini
```

### 方法二：手动使用提示词

1. 复制 `system_prompt.md` 的内容作为系统提示词
2. 复制 `user_prompt.md` 的内容作为用户输入
3. 在支持的AI工具（ChatGPT、Claude等）中执行生成

### 方法三：API调用

```python
# 使用配置文件通过编程方式调用AI API
import json

with open('output/[项目名称_时间戳]/config.json', 'r') as f:
    config = json.load(f)
    # 使用config调用AI API生成项目
```

## 📚 详细文档链接

- [项目模板说明](scripts/templates/java_project_template.md) - Java项目模板详细说明
- [配置收集器文档](scripts/core/config_collector.py) - 配置收集逻辑说明
- [上下文生成器文档](scripts/core/context_generator.py) - 上下文生成逻辑说明
- [输出目录结构](output/) - 生成的上下文工程示例

## 🛠️ 命令行选项

```bash
# 基本使用
python main.py

# 显示帮助信息
python main.py --help

# 查看版本信息
python main.py --version
```

## 📁 生成的上下文工程结构

### 输出目录结构
```
output/
└── [项目名称_时间戳]/
    ├── config.json              # 项目配置文件
    ├── system_prompt.md         # 系统提示词
    ├── user_prompt.md           # 用户提示词
    ├── project_generator.gemini # Gemini斜杠命令文件
    ├── project_structure.md     # 项目结构说明
    └── README.md                # 使用说明
```

### 配置文件示例
```json
{
  "project_name": "my-java-app",
  "package_name": "com.example.myjavaapp",
  "version": "1.0.0",
  "description": "my-java-app - Java应用程序",
  "jdk_version": "17",
  "build_tool": "Maven",
  "spring_boot_version": "3.2.0",
  "is_multi_module": false,
  "modules": [],
  "database": "MySQL",
  "orm_framework": "MyBatis",
  "cache": "Redis",
  "message_queue": "无消息队列",
  "include_swagger": true,
  "include_security": false,
  "include_actuator": true,
  "generate_sample_code": true,
  "generate_tests": true,
  "generate_docker": true,
  "generate_readme": true,
  "created_at": "2025-01-07T10:30:00"
}
```

## 📄 生成的文件说明

### system_prompt.md
包含AI生成Java项目的系统级指令和规范，确保生成高质量的代码。

### user_prompt.md
根据用户配置生成的具体项目需求描述，包含所有技术栈和功能要求。

### project_generator.gemini
Gemini CLI斜杠命令文件，可直接在Gemini命令行工具中执行。

### project_structure.md
详细的项目目录结构说明，包含标准的Maven/Gradle项目布局。

### config.json
完整的项目配置信息，可用于编程方式调用AI API。

### README.md
上下文工程的使用说明，包含多种使用方式和注意事项。

## 📈 项目历史版本

### v3.0.0 (2025-01-07) - 上下文工程生成器重构
- **重大重构**:
  - 项目完全重构为Java项目上下文工程生成器
  - 专注于生成AI项目初始化的上下文提示词
  - 移除传统的项目生成功能，转为AI提示词生成
- **新增功能**:
  - 系统提示词自动生成，包含项目生成规范和步骤
  - 用户提示词生成，基于用户配置的具体需求描述
  - Gemini CLI斜杠命令文件生成，支持一键AI项目生成
  - 项目结构说明文档自动生成
  - 完整的上下文工程输出目录管理
- **技术特性**:
  - 支持JDK 8/11/17/21版本选择
  - 支持Maven/Gradle构建工具
  - 支持Spring Boot多版本配置
  - 丰富的技术栈选择（数据库、ORM、缓存、消息队列）
  - 灵活的生成选项配置
- **架构优化**:
  - 简化项目结构，移除无用目录（logs、docs、templates、tests）
  - 重新设计核心模块：ConfigCollector和ContextGenerator
  - 优化交互式界面，提升用户体验
  - 标准化输出格式，便于AI工具集成

### v2.1.0 (2025-07-06) - 日志管理系统规范化
- **新增功能**:
  - 新增 `logs` 目录，统一管理项目变更日志
  - 实现日志文件标准化命名格式
  - 建立详细的变更记录体系
- **改进优化**:
  - 完善测试覆盖
  - 更新项目文档
  - 优化项目结构

### v2.0.0 (2025-01-07) - 配置管理系统V2重构
- **重大更新**:
  - 全新的配置管理系统V2
  - 分层架构设计
  - Markdown格式支持
- **新增功能**:
  - 配置迁移工具
  - 自动备份机制
  - CLI工具支持

### v1.0.0 (2024-10-01) - 首个正式版本
- **核心功能**:
  - 交互式Spring Boot项目生成
  - 多种技术栈配置支持
  - 配置文件管理系统

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

📖 **推荐使用流程**：
1. 先阅读本 README 了解项目概况
2. 运行 `python main.py` 开始生成上下文工程
3. 使用生成的上下文工程在AI工具中生成Java项目
4. 根据需要调整配置并重新生成