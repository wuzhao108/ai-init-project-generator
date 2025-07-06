# AI Spring Boot 项目生成器 - 详细文档

## 📖 项目概述

AI Spring Boot 项目生成器是一个基于 Python 的智能化工具，旨在帮助开发者快速生成标准化、生产就绪的 Spring Boot 项目。该工具提供了丰富的技术栈选择、灵活的配置管理和友好的交互式界面。

### 🎯 设计目标

- **提高开发效率** - 减少项目初始化时间，让开发者专注于业务逻辑
- **标准化项目结构** - 确保团队项目结构的一致性
- **技术栈集成** - 预配置常用技术栈，减少配置工作
- **最佳实践** - 内置行业最佳实践和代码规范

### 🌟 核心特性

1. **智能化配置** - 基于用户选择自动配置依赖和代码结构
2. **多技术栈支持** - 支持主流数据库、缓存、消息队列等技术栈
3. **项目类型灵活** - 支持单模块和多模块项目架构
4. **配置文件管理** - 完整的配置文件生命周期管理
5. **Docker 集成** - 自动生成 Docker 配置文件
6. **文档生成** - 自动生成项目文档和 API 文档

## 🚀 快速开始

### 环境要求

- Python 3.6+
- pip 包管理器
- Java 8+ (用于运行生成的项目)
- Maven 3.6+ (用于构建生成的项目)

### 安装步骤

1. **克隆项目**
   ```bash
   git clone <repository-url>
   cd ai-init-project-generator
   ```

2. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

3. **验证安装**
   ```bash
   python main.py --help
   ```

### 第一个项目

运行以下命令创建你的第一个 Spring Boot 项目：

```bash
python main.py
```

选择菜单选项 "1. 🆕 创建项目模板"，然后按照提示进行操作。

## 📋 功能详解

### 1. 创建项目模板 🆕

#### 功能说明
创建新的 Spring Boot 项目，支持两种模式：
- **默认模板模式** - 使用预配置的模板快速创建
- **自定义配置模式** - 通过交互式界面自定义项目配置

#### 使用场景
- 快速启动新项目
- 为团队创建标准化项目模板
- 学习 Spring Boot 项目结构

#### 操作步骤

**默认模板模式：**
1. 选择菜单选项 "1"
2. 选择 "1. 📋 使用默认模板创建"
3. 查看默认配置详情
4. 确认创建项目

**自定义配置模式：**
1. 选择菜单选项 "1"
2. 选择 "2. ⚙️ 自定义配置创建"
3. 按照提示输入项目信息：
   - 项目名称
   - 包名
   - 项目描述
   - Java 版本
   - Spring Boot 版本
   - 项目类型（单模块/多模块）
   - 技术栈选择
4. 确认配置并生成项目

#### 操作演示

```bash
# 启动程序
$ python main.py

# 选择创建项目
📋 请选择操作:
1. 🆕 创建项目模板
请选择操作: 1

# 选择创建方式
请选择创建方式:
1. 📋 使用默认模板创建
2. ⚙️ 自定义配置创建
请选择: 2

# 输入项目信息
请输入项目名称: my-awesome-project
请输入基础包名: com.example.awesome
请输入项目描述: 我的第一个Spring Boot项目
请选择Java版本: 17
请选择Spring Boot版本: 3.2.2
# ... 更多配置选项

# 确认并生成
确认以上配置并生成项目？ [Y/n]: Y
✅ 项目生成完成！路径: ./output/my-awesome-project
```

### 2. 从配置文件生成项目 📁

#### 功能说明
使用已保存的配置文件快速生成项目，支持配置文件的重复使用。

#### 使用场景
- 基于已有配置创建相似项目
- 团队共享项目配置
- 批量创建项目

#### 操作步骤
1. 选择菜单选项 "2"
2. 从列表中选择要使用的配置文件
3. 指定输出目录
4. 确认生成项目

#### 操作演示

```bash
# 选择从配置文件生成
📋 请选择操作:
2. 📁 从配置文件生成项目
请选择操作: 2

# 选择配置文件
📋 可用的配置文件:
1. my-web-project - Web应用项目 (Java 17)
2. my-api-project - API服务项目 (Java 11)
请选择配置文件: 1

# 指定输出目录
请输入输出目录 [./output]: ./output

✅ 项目生成成功: ./output/my-web-project
```

### 3. 查看已保存的配置 📋

#### 功能说明
列出所有已保存的配置文件，显示配置的基本信息。

#### 使用场景
- 查看可用的配置文件
- 管理配置文件
- 选择合适的配置模板

#### 操作步骤
1. 选择菜单选项 "3"
2. 查看配置文件列表

#### 操作演示

```bash
# 查看已保存的配置
📋 请选择操作:
3. 📋 查看已保存的配置
请选择操作: 3

📋 已保存的配置文件:
  • my-web-project - Web应用项目 (Java 17)
  • my-api-project - API服务项目 (Java 11)
  • microservice-template - 微服务模板 (Java 17)
```

### 4. 查看配置详情 📄

#### 功能说明
查看特定配置文件的详细信息，包括技术栈、模块配置等。

#### 使用场景
- 了解配置文件的具体内容
- 验证配置的正确性
- 学习项目配置

#### 操作步骤
1. 选择菜单选项 "4"
2. 从列表中选择要查看的配置文件
3. 查看详细配置信息

#### 操作演示

```bash
# 查看配置详情
📋 请选择操作:
4. 📄 查看配置详情
请选择操作: 4

# 选择配置文件
📋 可用的配置文件:
1. my-web-project
2. my-api-project
请选择要查看的配置文件: 1

# 显示详细信息
📄 配置文件: my-web-project
项目名称: my-web-project
包名: com.example.web
版本: 1.0.0
描述: Web应用项目
Java版本: 17
Spring Boot版本: 3.2.2
项目类型: 单模块

🔧 技术栈:
  database: mysql
  orm: mybatis
  cache: redis
  doc: true
  security: true
```

### 5. 删除配置文件 🗑️

#### 功能说明
删除不再需要的配置文件，支持确认机制防止误删。

#### 使用场景
- 清理过期的配置文件
- 管理配置文件存储空间
- 移除错误的配置

#### 操作步骤
1. 选择菜单选项 "5"
2. 从列表中选择要删除的配置文件
3. 确认删除操作

#### 操作演示

```bash
# 删除配置文件
📋 请选择操作:
5. 🗑️ 删除配置文件
请选择操作: 5

# 选择要删除的配置
📋 可用的配置文件:
1. old-project
2. test-config
请选择要删除的配置文件: 1

# 确认删除
确定要删除配置文件 'old-project' 吗？ [y/N]: y
✅ 配置文件已删除: old-project
```

### 6. 导出配置文件 📤

#### 功能说明
将配置文件导出到指定位置，便于备份和分享。

#### 使用场景
- 备份重要配置
- 团队间共享配置
- 版本控制配置文件

#### 操作步骤
1. 选择菜单选项 "6"
2. 选择要导出的配置文件
3. 指定导出路径
4. 完成导出

#### 操作演示

```bash
# 导出配置文件
📋 请选择操作:
6. 📤 导出配置文件
请选择操作: 6

# 选择配置文件
📋 可用的配置文件:
1. my-web-project
2. my-api-project
请选择要导出的配置文件: 1

# 指定导出路径
请输入导出路径 [./my-web-project.json]: ./backup/web-config.json

✅ 配置文件已导出: ./backup/web-config.json
```

### 7. 导入配置文件 📥

#### 功能说明
从外部文件导入配置，支持自定义配置名称。

#### 使用场景
- 导入团队共享的配置
- 恢复备份的配置
- 使用第三方配置模板

#### 操作步骤
1. 选择菜单选项 "7"
2. 输入要导入的配置文件路径
3. 指定配置名称（可选）
4. 完成导入

#### 操作演示

```bash
# 导入配置文件
📋 请选择操作:
7. 📥 导入配置文件
请选择操作: 7

# 输入文件路径
请输入要导入的配置文件路径: ./shared/team-config.json

# 指定配置名称
请输入配置名称（留空使用文件名）: team-standard

✅ 配置文件已导入: team-standard
```

### 8. 查看可用模板 📚

#### 功能说明
显示系统支持的所有项目模板和技术栈组合。

#### 使用场景
- 了解支持的技术栈
- 选择合适的项目模板
- 学习技术栈组合

#### 操作步骤
1. 选择菜单选项 "8"
2. 查看模板列表

#### 操作演示

```bash
# 查看可用模板
📋 请选择操作:
8. 📚 查看可用模板
请选择操作: 8

📚 可用模板列表
  📁 单模块项目模板
  📁 多模块项目模板
  🔧 MyBatis集成模板
  🔧 JPA集成模板
  🔧 Redis集成模板
  🔧 RabbitMQ集成模板
  🔧 Kafka集成模板
  📚 Swagger文档模板
  🔒 Spring Security模板
```

## 🛠️ 技术栈支持

### 数据库支持

| 数据库 | 描述 | 配置值 | 依赖包 |
|--------|------|--------|--------|
| MySQL | 最流行的开源关系型数据库 | `mysql` | mysql-connector-java |
| PostgreSQL | 功能强大的开源对象关系型数据库 | `postgresql` | postgresql |
| H2 | 内存数据库，适用于开发和测试 | `h2` | h2 |
| Oracle | 企业级关系型数据库 | `oracle` | ojdbc8 |
| SQL Server | 微软关系型数据库 | `sqlserver` | mssql-jdbc |

### ORM 框架支持

| 框架 | 描述 | 配置值 | 特点 |
|------|------|--------|------|
| MyBatis | 优秀的持久层框架 | `mybatis` | SQL 可控，性能优秀 |
| MyBatis-Plus | MyBatis 的增强工具 | `mybatis-plus` | 代码生成，CRUD 简化 |
| JPA/Hibernate | Java 持久化 API | `jpa` | 对象关系映射，标准化 |

### 缓存支持

| 缓存 | 描述 | 配置值 | 使用场景 |
|------|------|--------|----------|
| Redis | 高性能的内存数据结构存储 | `redis` | 分布式缓存，会话存储 |
| Caffeine | 高性能的本地缓存库 | `caffeine` | 本地缓存，高并发 |
| Ehcache | Java 分布式缓存 | `ehcache` | 本地和分布式缓存 |

### 消息队列支持

| 消息队列 | 描述 | 配置值 | 特点 |
|----------|------|--------|------|
| RabbitMQ | 可靠的消息代理 | `rabbitmq` | 可靠性高，功能丰富 |
| Apache Kafka | 分布式流处理平台 | `kafka` | 高吞吐量，持久化 |
| RocketMQ | 阿里巴巴开源的消息中间件 | `rocketmq` | 低延迟，高可用 |
| ActiveMQ | Apache 消息代理 | `activemq` | 标准化，易用 |

### NoSQL 数据库支持

| 数据库 | 描述 | 配置值 | 使用场景 |
|--------|------|--------|----------|
| MongoDB | 面向文档的数据库 | `mongodb` | 文档存储，灵活模式 |
| Elasticsearch | 分布式搜索和分析引擎 | `elasticsearch` | 全文搜索，日志分析 |

### 安全框架支持

| 框架 | 描述 | 配置值 | 功能 |
|------|------|--------|------|
| Spring Security | 强大的安全框架 | `spring-security` | 认证，授权，防护 |
| JWT | JSON Web Token 认证 | `jwt` | 无状态认证 |
| OAuth2 | 开放授权协议 | `oauth2` | 第三方登录 |

### 文档工具支持

| 工具 | 描述 | 配置值 | 特点 |
|------|------|--------|------|
| Swagger/OpenAPI 3 | API 文档生成 | `swagger` | 交互式文档 |
| Spring REST Docs | 测试驱动的文档 | `restdocs` | 测试保证准确性 |

### 监控工具支持

| 工具 | 描述 | 配置值 | 功能 |
|------|------|--------|------|
| Spring Boot Actuator | 生产就绪功能 | `actuator` | 健康检查，指标监控 |
| Micrometer | 应用监控门面 | `micrometer` | 指标收集 |
| Zipkin | 分布式追踪 | `zipkin` | 链路追踪 |

## 📁 生成的项目结构详解

### 单模块项目结构

```
my-spring-project/
├── src/
│   ├── main/
│   │   ├── java/com/example/myproject/
│   │   │   ├── MyProjectApplication.java    # 🚀 Spring Boot 启动类
│   │   │   ├── controller/                  # 🎮 控制器层
│   │   │   │   ├── BaseController.java     # 基础控制器
│   │   │   │   └── UserController.java     # 用户控制器示例
│   │   │   ├── service/                     # 🔧 服务层
│   │   │   │   ├── UserService.java        # 用户服务接口
│   │   │   │   └── impl/
│   │   │   │       └── UserServiceImpl.java # 用户服务实现
│   │   │   ├── repository/                  # 💾 数据访问层
│   │   │   │   └── UserRepository.java     # 用户数据访问
│   │   │   ├── entity/                      # 📊 实体类
│   │   │   │   └── User.java               # 用户实体
│   │   │   ├── dto/                         # 📦 数据传输对象
│   │   │   │   ├── UserDTO.java            # 用户DTO
│   │   │   │   └── request/                # 请求DTO
│   │   │   │   └── response/               # 响应DTO
│   │   │   ├── config/                      # ⚙️ 配置类
│   │   │   │   ├── DatabaseConfig.java     # 数据库配置
│   │   │   │   ├── RedisConfig.java        # Redis配置
│   │   │   │   └── SwaggerConfig.java      # Swagger配置
│   │   │   ├── exception/                   # ❌ 异常处理
│   │   │   │   ├── GlobalExceptionHandler.java # 全局异常处理
│   │   │   │   └── BusinessException.java  # 业务异常
│   │   │   ├── common/                      # 🔗 通用类
│   │   │   │   ├── Result.java             # 统一返回结果
│   │   │   │   ├── PageResult.java         # 分页结果
│   │   │   │   └── Constants.java          # 常量定义
│   │   │   └── util/                        # 🛠️ 工具类
│   │   │       ├── DateUtil.java          # 日期工具
│   │   │       └── StringUtil.java        # 字符串工具
│   │   └── resources/
│   │       ├── application.yml              # 🔧 主配置文件
│   │       ├── application-dev.yml          # 🔧 开发环境配置
│   │       ├── application-test.yml         # 🔧 测试环境配置
│   │       ├── application-prod.yml         # 🔧 生产环境配置
│   │       ├── logback-spring.xml          # 📝 日志配置
│   │       ├── mapper/                      # 📋 MyBatis映射文件
│   │       │   └── UserMapper.xml
│   │       └── static/                      # 📁 静态资源
│   │           └── templates/               # 📄 模板文件
│   └── test/                               # 🧪 测试代码
│       └── java/com/example/myproject/
│           ├── MyProjectApplicationTests.java # 启动测试
│           ├── controller/                  # 控制器测试
│           │   └── UserControllerTest.java
│           ├── service/                     # 服务测试
│           │   └── UserServiceTest.java
│           └── repository/                  # 数据访问测试
│               └── UserRepositoryTest.java
├── docker/
│   ├── Dockerfile                          # 🐳 Docker 镜像构建文件
│   ├── docker-compose.yml                 # 🐳 Docker Compose 配置
│   └── docker-compose-dev.yml             # 🐳 开发环境 Docker 配置
├── docs/                                   # 📚 项目文档
│   ├── README.md                          # 项目说明
│   ├── API.md                             # API 文档
│   └── DEPLOYMENT.md                      # 部署文档
├── scripts/                                # 📜 脚本文件
│   ├── build.sh                          # 构建脚本
│   ├── deploy.sh                         # 部署脚本
│   └── init-db.sql                       # 数据库初始化脚本
├── pom.xml                                 # 📦 Maven 配置文件
├── .gitignore                             # 🚫 Git 忽略文件
├── .editorconfig                          # 📝 编辑器配置
└── README.md                              # 📖 项目说明文档
```

### 多模块项目结构

```
my-spring-project/
├── my-spring-project-common/               # 📦 公共模块
│   ├── src/main/java/
│   │   └── com/example/myproject/common/
│   │       ├── entity/                     # 公共实体
│   │       ├── dto/                        # 公共DTO
│   │       ├── util/                       # 公共工具类
│   │       ├── exception/                  # 公共异常
│   │       └── constant/                   # 公共常量
│   └── pom.xml
├── my-spring-project-api/                  # 🌐 API 模块
│   ├── src/main/java/
│   │   └── com/example/myproject/api/
│   │       ├── controller/                 # REST 控制器
│   │       ├── dto/                        # API DTO
│   │       └── config/                     # API 配置
│   └── pom.xml
├── my-spring-project-service/              # 🔧 服务模块
│   ├── src/main/java/
│   │   └── com/example/myproject/service/
│   │       ├── service/                    # 业务服务
│   │       ├── repository/                 # 数据访问
│   │       └── config/                     # 服务配置
│   └── pom.xml
├── my-spring-project-web/                  # 🖥️ Web 模块
│   ├── src/main/java/
│   │   └── com/example/myproject/
│   │       ├── MyProjectApplication.java   # 启动类
│   │       └── config/                     # Web 配置
│   ├── src/main/resources/
│   │   ├── application.yml                 # 配置文件
│   │   └── static/                         # 静态资源
│   └── pom.xml
├── docker/
├── docs/
├── scripts/
├── pom.xml                                 # 📦 父 POM
├── .gitignore
└── README.md
```

## 🔧 配置文件详解

### 主配置文件格式

配置文件采用 JSON 格式，包含以下主要字段：

```json
{
  "name": "my-spring-project",              // 项目名称
  "package": "com.example.myproject",       // 基础包名
  "version": "1.0.0",                       // 项目版本
  "description": "A Spring Boot project",   // 项目描述
  "java_version": "17",                     // Java 版本
  "spring_boot_version": "3.2.2",          // Spring Boot 版本
  "project_type": "single-module",          // 项目类型
  "multi_module": false,                     // 是否多模块
  "modules": [],                             // 模块列表
  "tech_stack": {                            // 技术栈配置
    "database": "mysql",                    // 数据库
    "orm": "mybatis",                       // ORM 框架
    "cache": ["redis"],                     // 缓存组件
    "mq": ["rabbitmq"],                     // 消息队列
    "doc": true,                            // API 文档
    "security": true,                       // 安全框架
    "mongodb": false,                       // MongoDB
    "elasticsearch": false,                 // Elasticsearch
    "web_framework": "spring-web",          // Web 框架
    "actuator": true,                       // 监控组件
    "test_framework": ["junit5", "mockito"] // 测试框架
  },
  "output_dir": "./output",                 // 输出目录
  "generate_sample_code": true,             // 生成示例代码
  "generate_tests": true,                   // 生成测试代码
  "generate_docker": true,                  // 生成Docker配置
  "created_at": "2024-01-01T00:00:00",      // 创建时间
  "updated_at": "2024-01-01T00:00:00"       // 更新时间
}
```

### 技术栈配置详解

#### 数据库配置

```json
{
  "tech_stack": {
    "database": "mysql",  // 可选值: mysql, postgresql, h2, oracle, sqlserver
    "orm": "mybatis"      // 可选值: mybatis, mybatis-plus, jpa
  }
}
```

#### 缓存配置

```json
{
  "tech_stack": {
    "cache": ["redis", "caffeine"]  // 可选值: redis, caffeine, ehcache
  }
}
```

#### 消息队列配置

```json
{
  "tech_stack": {
    "mq": ["rabbitmq", "kafka"]  // 可选值: rabbitmq, kafka, rocketmq, activemq
  }
}
```

#### 安全配置

```json
{
  "tech_stack": {
    "security": true,     // 是否启用 Spring Security
    "jwt": true,          // 是否启用 JWT
    "oauth2": false       // 是否启用 OAuth2
  }
}
```

### 环境配置文件

生成的项目包含多环境配置文件：

#### application.yml (主配置)

```yaml
spring:
  profiles:
    active: dev  # 默认激活开发环境
  application:
    name: ${project.name}

server:
  port: 8080

management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics
```

#### application-dev.yml (开发环境)

```yaml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/${project.name}_dev
    username: root
    password: password
    driver-class-name: com.mysql.cj.jdbc.Driver
  
  redis:
    host: localhost
    port: 6379
    database: 0

logging:
  level:
    com.example: DEBUG
    org.springframework: INFO
```

#### application-test.yml (测试环境)

```yaml
spring:
  datasource:
    url: jdbc:h2:mem:testdb
    driver-class-name: org.h2.Driver
    username: sa
    password: 
  
  h2:
    console:
      enabled: true

logging:
  level:
    root: WARN
    com.example: INFO
```

#### application-prod.yml (生产环境)

```yaml
spring:
  datasource:
    url: ${DB_URL}
    username: ${DB_USERNAME}
    password: ${DB_PASSWORD}
    driver-class-name: com.mysql.cj.jdbc.Driver
  
  redis:
    host: ${REDIS_HOST}
    port: ${REDIS_PORT}
    password: ${REDIS_PASSWORD}

logging:
  level:
    root: INFO
    com.example: INFO
  file:
    name: /var/log/${project.name}.log
```

## 🐳 Docker 集成

### Dockerfile

生成的项目包含优化的多阶段构建 Dockerfile：

```dockerfile
# 构建阶段
FROM maven:3.8.4-openjdk-17 AS builder
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline -B
COPY src ./src
RUN mvn clean package -DskipTests

# 运行阶段
FROM openjdk:17-jre-slim
WORKDIR /app
COPY --from=builder /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

### docker-compose.yml

完整的开发环境编排：

```yaml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "8080:8080"
    environment:
      - SPRING_PROFILES_ACTIVE=docker
      - DB_HOST=mysql
      - REDIS_HOST=redis
    depends_on:
      - mysql
      - redis
  
  mysql:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: password
      MYSQL_DATABASE: ${project.name}
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql
  
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

volumes:
  mysql_data:
  redis_data:
```

## 🧪 测试支持

### 测试框架集成

生成的项目包含完整的测试支持：

- **JUnit 5** - 现代化的测试框架
- **Mockito** - Mock 框架
- **TestContainers** - 集成测试容器
- **Spring Boot Test** - Spring Boot 测试支持

### 测试示例

#### 单元测试示例

```java
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    
    @Mock
    private UserRepository userRepository;
    
    @InjectMocks
    private UserServiceImpl userService;
    
    @Test
    void shouldCreateUser() {
        // Given
        User user = new User("John", "john@example.com");
        when(userRepository.save(any(User.class))).thenReturn(user);
        
        // When
        User result = userService.createUser(user);
        
        // Then
        assertThat(result.getName()).isEqualTo("John");
        verify(userRepository).save(user);
    }
}
```

#### 集成测试示例

```java
@SpringBootTest
@Testcontainers
class UserControllerIntegrationTest {
    
    @Container
    static MySQLContainer<?> mysql = new MySQLContainer<>("mysql:8.0")
            .withDatabaseName("testdb")
            .withUsername("test")
            .withPassword("test");
    
    @Autowired
    private TestRestTemplate restTemplate;
    
    @Test
    void shouldCreateUser() {
        // Given
        User user = new User("John", "john@example.com");
        
        // When
        ResponseEntity<User> response = restTemplate.postForEntity(
                "/api/users", user, User.class);
        
        // Then
        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.CREATED);
        assertThat(response.getBody().getName()).isEqualTo("John");
    }
}
```

## 📚 最佳实践

### 代码规范

1. **包结构规范**
   - `controller` - 控制器层，处理HTTP请求
   - `service` - 服务层，业务逻辑处理
   - `repository` - 数据访问层，数据持久化
   - `entity` - 实体类，数据模型
   - `dto` - 数据传输对象，API接口数据
   - `config` - 配置类，Spring配置
   - `exception` - 异常处理，统一异常管理
   - `util` - 工具类，通用功能

2. **命名规范**
   - 类名使用 PascalCase
   - 方法名和变量名使用 camelCase
   - 常量使用 UPPER_SNAKE_CASE
   - 包名使用小写字母

3. **注释规范**
   - 类和方法必须有 Javadoc 注释
   - 复杂逻辑必须有行内注释
   - 使用有意义的变量名减少注释需求

### 安全最佳实践

1. **输入验证**
   - 使用 Bean Validation 进行参数校验
   - 对所有外部输入进行验证
   - 防止 SQL 注入和 XSS 攻击

2. **认证授权**
   - 使用 Spring Security 进行安全控制
   - 实现基于角色的访问控制 (RBAC)
   - 使用 JWT 进行无状态认证

3. **数据保护**
   - 敏感数据加密存储
   - 使用 HTTPS 传输数据
   - 实现审计日志

### 性能优化

1. **数据库优化**
   - 合理设计数据库索引
   - 使用连接池管理数据库连接
   - 实现读写分离

2. **缓存策略**
   - 使用 Redis 缓存热点数据
   - 实现多级缓存架构
   - 合理设置缓存过期时间

3. **异步处理**
   - 使用消息队列处理异步任务
   - 实现事件驱动架构
   - 使用线程池管理并发任务

### 监控和运维

1. **健康检查**
   - 使用 Actuator 提供健康检查端点
   - 监控应用关键指标
   - 实现自定义健康检查

2. **日志管理**
   - 使用结构化日志格式
   - 实现日志级别动态调整
   - 集成日志收集系统

3. **部署策略**
   - 使用 Docker 容器化部署
   - 实现蓝绿部署或滚动更新
   - 配置自动扩缩容

## 🔧 自定义和扩展

### 添加新的技术栈支持

1. **更新常量定义**
   
   在 `scripts/constants/project_constants.py` 中添加新的技术栈常量：
   
   ```python
   # 添加新的数据库支持
   DATABASES = {
       'mysql': 'MySQL',
       'postgresql': 'PostgreSQL',
       'mongodb': 'MongoDB',
       'cassandra': 'Apache Cassandra'  # 新增
   }
   ```

2. **添加验证逻辑**
   
   在 `scripts/validators/project_validator.py` 中添加验证：
   
   ```python
   def validate_database(database):
       """验证数据库选择"""
       valid_databases = ['mysql', 'postgresql', 'mongodb', 'cassandra']
       if database not in valid_databases:
           raise ValueError(f"不支持的数据库: {database}")
   ```

3. **创建模板文件**
   
   在 `spring_init/templates/` 目录下创建相应的模板文件：
   
   ```
   spring_init/templates/
   ├── cassandra/
   │   ├── config/
   │   │   └── CassandraConfig.java.j2
   │   ├── repository/
   │   │   └── CassandraRepository.java.j2
   │   └── entity/
   │       └── CassandraEntity.java.j2
   ```

4. **更新生成器逻辑**
   
   在 `spring_init/generator.py` 中添加生成逻辑：
   
   ```python
   def generate_cassandra_config(self):
       """生成 Cassandra 配置"""
       if self.config.tech_stack.database == 'cassandra':
           # 生成 Cassandra 相关文件
           self._generate_from_template(
               'cassandra/config/CassandraConfig.java.j2',
               f'{self.java_dir}/config/CassandraConfig.java'
           )
   ```

### 自定义模板文件

模板文件使用 Jinja2 语法，支持变量替换和逻辑控制：

```java
// UserController.java.j2
package {{ package }}.controller;

import org.springframework.web.bind.annotation.*;
import {{ package }}.service.UserService;
import {{ package }}.entity.User;

@RestController
@RequestMapping("/api/users")
public class UserController {
    
    private final UserService userService;
    
    public UserController(UserService userService) {
        this.userService = userService;
    }
    
    {% if tech_stack.security %}
    @PreAuthorize("hasRole('USER')")
    {% endif %}
    @GetMapping
    public List<User> getAllUsers() {
        return userService.findAll();
    }
    
    {% if tech_stack.doc %}
    @ApiOperation("创建用户")
    @ApiResponses({
        @ApiResponse(code = 201, message = "创建成功"),
        @ApiResponse(code = 400, message = "参数错误")
    })
    {% endif %}
    @PostMapping
    public User createUser(@RequestBody @Valid User user) {
        return userService.create(user);
    }
}
```

### 扩展配置选项

1. **扩展配置数据结构**
   
   在 `spring_init/config.py` 中添加新的配置字段：
   
   ```python
   @dataclass
   class TechStack:
       database: str = "h2"
       orm: str = "jpa"
       cache: List[str] = field(default_factory=list)
       mq: List[str] = field(default_factory=list)
       # 新增配置
       search_engine: str = ""  # elasticsearch, solr
       workflow_engine: str = ""  # activiti, flowable
   ```

2. **更新交互式配置收集**
   
   在 `spring_init/interactive.py` 中添加新的配置收集逻辑：
   
   ```python
   def collect_search_engine_config(self):
       """收集搜索引擎配置"""
       console.print("\n[green]🔍 搜索引擎配置[/green]")
       
       choices = {
           "1": "elasticsearch",
           "2": "solr",
           "3": "不使用"
       }
       
       console.print("请选择搜索引擎:")
       for key, value in choices.items():
           console.print(f"{key}. {value}")
       
       choice = Prompt.ask("请选择", choices=list(choices.keys()), default="3")
       return choices[choice] if choice != "3" else ""
   ```

## 🚀 部署指南

### 本地开发环境

1. **启动依赖服务**
   
   ```bash
   # 使用 Docker Compose 启动依赖服务
   cd generated-project
   docker-compose -f docker/docker-compose-dev.yml up -d
   ```

2. **启动应用**
   
   ```bash
   # 使用 Maven 启动
   mvn spring-boot:run
   
   # 或者使用 IDE 直接运行 Application 类
   ```

3. **验证部署**
   
   ```bash
   # 检查健康状态
   curl http://localhost:8080/actuator/health
   
   # 访问 API 文档
   open http://localhost:8080/swagger-ui.html
   ```

### 生产环境部署

1. **构建 Docker 镜像**
   
   ```bash
   # 构建镜像
   docker build -t my-spring-project:latest .
   
   # 推送到镜像仓库
   docker tag my-spring-project:latest registry.example.com/my-spring-project:latest
   docker push registry.example.com/my-spring-project:latest
   ```

2. **Kubernetes 部署**
   
   ```yaml
   # deployment.yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: my-spring-project
   spec:
     replicas: 3
     selector:
       matchLabels:
         app: my-spring-project
     template:
       metadata:
         labels:
           app: my-spring-project
       spec:
         containers:
         - name: app
           image: registry.example.com/my-spring-project:latest
           ports:
           - containerPort: 8080
           env:
           - name: SPRING_PROFILES_ACTIVE
             value: "prod"
           - name: DB_URL
             valueFrom:
               secretKeyRef:
                 name: db-secret
                 key: url
   ```

3. **监控和日志**
   
   ```bash
   # 查看应用日志
   kubectl logs -f deployment/my-spring-project
   
   # 查看应用指标
   kubectl port-forward service/my-spring-project 8080:8080
   curl http://localhost:8080/actuator/metrics
   ```

## 🤝 贡献指南

### 开发环境设置

1. **克隆项目**
   
   ```bash
   git clone https://github.com/your-username/ai-init-project-generator.git
   cd ai-init-project-generator
   ```

2. **创建虚拟环境**
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # 或
   venv\Scripts\activate  # Windows
   ```

3. **安装开发依赖**
   
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. **运行测试**
   
   ```bash
   python -m pytest tests/ -v
   ```

### 代码贡献流程

1. **创建功能分支**
   
   ```bash
   git checkout -b feature/new-feature
   ```

2. **编写代码和测试**
   
   - 遵循现有代码风格
   - 添加必要的测试用例
   - 更新相关文档

3. **提交代码**
   
   ```bash
   git add .
   git commit -m "feat: add new feature"
   ```

4. **推送分支**
   
   ```bash
   git push origin feature/new-feature
   ```

5. **创建 Pull Request**
   
   - 详细描述变更内容
   - 关联相关 Issue
   - 等待代码审查

### 代码规范

1. **Python 代码规范**
   
   ```bash
   # 使用 black 格式化代码
   black .
   
   # 使用 flake8 检查代码质量
   flake8 .
   
   # 使用 isort 排序导入
   isort .
   ```

2. **提交信息规范**
   
   ```
   feat: 新功能
   fix: 修复bug
   docs: 文档更新
   style: 代码格式调整
   refactor: 代码重构
   test: 测试相关
   chore: 构建过程或辅助工具的变动
   ```

## 📞 支持和反馈

### 获取帮助

1. **查看文档** - 首先查看本文档和项目 README
2. **搜索 Issues** - 在 GitHub Issues 中搜索相关问题
3. **提交 Issue** - 如果没有找到解决方案，请提交新的 Issue
4. **社区讨论** - 参与 GitHub Discussions

### 问题报告

提交 Bug 报告时，请包含以下信息：

- **环境信息** - 操作系统、Python 版本、依赖版本
- **重现步骤** - 详细的操作步骤
- **期望结果** - 期望的行为
- **实际结果** - 实际发生的情况
- **错误日志** - 相关的错误信息和堆栈跟踪

### 功能建议

提交功能建议时，请说明：

- **使用场景** - 什么情况下需要这个功能
- **解决问题** - 这个功能解决什么问题
- **实现思路** - 可能的实现方案
- **影响范围** - 对现有功能的影响

---

📝 **文档版本**: v1.0.0  
📅 **最后更新**: 2024-01-01  
👥 **维护团队**: AI Spring Boot Generator Team