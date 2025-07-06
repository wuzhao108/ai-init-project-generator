# Spring Boot 微服务模板配置

## 模板信息

- **模板名称**: Spring Boot 微服务模板
- **模板ID**: `spring-boot-microservice`
- **版本**: `1.0.0`
- **描述**: 适用于微服务架构的Spring Boot项目模板
- **创建时间**: 2024-01-01
- **更新时间**: 2024-01-01
- **作者**: AI Project Generator

## 项目基础配置

### 基本信息
```yaml
name: "microservice-demo"               # 项目名称
package: "com.example.microservice"     # 基础包名
version: "1.0.0"                        # 项目版本
description: "基于Spring Boot的微服务应用" # 项目描述
```

### 技术版本
```yaml
java_version: "17"                      # Java版本 (推荐17+)
spring_version: "3.1.5"                 # Spring Boot版本 (最新稳定版)
```

### 项目结构
```yaml
multi_module: true                      # 多模块项目
modules:                                # 模块配置
  - name: "common"
    description: "公共模块"
  - name: "api"
    description: "API接口模块"
  - name: "service"
    description: "业务服务模块"
  - name: "dao"
    description: "数据访问模块"
  - name: "web"
    description: "Web控制器模块"
```

## 技术栈配置

### 数据层
```yaml
database: "mysql"                       # 数据库类型
orm: "jpa"                             # ORM框架 (微服务推荐JPA)
```

### 缓存
```yaml
cache: ["redis"]                        # 分布式缓存
```

### 消息队列
```yaml
mq: ["rabbitmq", "kafka"]              # 消息队列组件
  # RabbitMQ: 服务间通信
  # Kafka: 事件流处理
```

### NoSQL数据库
```yaml
mongodb: true                           # 文档数据库
elasticsearch: true                     # 搜索引擎
```

### 服务发现与配置
```yaml
service_discovery: "eureka"             # 服务发现
  # 可选值: eureka, consul, nacos
  
config_center: "nacos"                  # 配置中心
  # 可选值: nacos, apollo, spring-cloud-config
```

### API网关
```yaml
api_gateway: "spring-cloud-gateway"     # API网关
  # 可选值: spring-cloud-gateway, zuul
```

### 链路追踪
```yaml
tracing: "zipkin"                       # 链路追踪
  # 可选值: zipkin, jaeger, skywalking
```

### 熔断器
```yaml
circuit_breaker: "hystrix"              # 熔断器
  # 可选值: hystrix, resilience4j
```

### 文档工具
```yaml
doc: true                               # API文档
```

### 安全框架
```yaml
security: true                          # Spring Security + OAuth2
```

### Web框架
```yaml
web_framework: "spring-web"             # Web框架
```

### 监控
```yaml
actuator: true                          # 应用监控
prometheus: true                        # 指标收集
grafana: true                           # 监控面板
```

### 测试框架
```yaml
test_framework: ["junit5", "mockito", "testcontainers"]
```

## 代码生成选项

```yaml
generate_sample_code: true              # 生成示例代码
generate_tests: true                    # 生成测试代码
generate_docker: true                  # 生成Docker配置
generate_k8s: true                     # 生成Kubernetes配置
generate_helm: true                    # 生成Helm Charts
```

## 微服务特有配置

### 服务配置
```yaml
service:
  port: 8080                            # 服务端口
  context_path: "/api/v1"               # 上下文路径
  timeout: 30000                        # 超时时间(ms)
  
load_balancer:
  strategy: "round_robin"               # 负载均衡策略
  # 可选值: round_robin, random, weighted
  
retry:
  max_attempts: 3                       # 最大重试次数
  backoff_delay: 1000                   # 退避延迟(ms)
```

### 数据库配置
```yaml
database:
  connection_pool:
    initial_size: 5
    max_active: 20
    max_wait: 60000
  sharding:
    enabled: false                      # 是否启用分库分表
    strategy: "hash"                    # 分片策略
```

## 依赖版本管理

### Spring Cloud依赖
- Spring Cloud: 2022.0.4
- Spring Cloud Alibaba: 2022.0.0.0
- Eureka: 3.1.x
- Gateway: 3.1.x
- OpenFeign: 3.1.x

### 消息队列
- Spring Cloud Stream: 3.2.x
- RabbitMQ: 3.11.x
- Kafka: 3.4.x

### 监控相关
- Micrometer: 1.11.x
- Prometheus: 1.11.x
- Zipkin: 2.24.x

### 数据库相关
- Spring Data JPA: 3.1.x
- HikariCP: 5.0.x
- Flyway: 9.x

## 多模块项目结构

```
{project_name}/
├── {project_name}-common/              # 公共模块
│   ├── src/main/java/{package}/common/
│   │   ├── constant/                   # 常量定义
│   │   ├── util/                       # 工具类
│   │   ├── exception/                  # 异常定义
│   │   └── dto/                        # 通用DTO
│   └── pom.xml
├── {project_name}-api/                 # API模块
│   ├── src/main/java/{package}/api/
│   │   ├── feign/                      # Feign客户端
│   │   ├── dto/                        # API DTO
│   │   └── vo/                         # 视图对象
│   └── pom.xml
├── {project_name}-dao/                 # 数据访问模块
│   ├── src/main/java/{package}/dao/
│   │   ├── entity/                     # 实体类
│   │   ├── repository/                 # 数据仓库
│   │   └── config/                     # 数据源配置
│   └── pom.xml
├── {project_name}-service/             # 服务模块
│   ├── src/main/java/{package}/service/
│   │   ├── impl/                       # 服务实现
│   │   ├── config/                     # 服务配置
│   │   └── event/                      # 事件处理
│   └── pom.xml
├── {project_name}-web/                 # Web模块
│   ├── src/main/java/{package}/web/
│   │   ├── controller/                 # 控制器
│   │   ├── config/                     # Web配置
│   │   ├── filter/                     # 过滤器
│   │   └── Application.java            # 启动类
│   ├── src/main/resources/
│   │   ├── application.yml
│   │   ├── bootstrap.yml               # 引导配置
│   │   └── logback-spring.xml
│   └── pom.xml
├── docker/                             # Docker配置
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── docker-compose-dev.yml
├── k8s/                                # Kubernetes配置
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── configmap.yaml
│   └── ingress.yaml
├── helm/                               # Helm Charts
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
├── scripts/                            # 部署脚本
│   ├── build.sh
│   ├── deploy.sh
│   └── health-check.sh
├── pom.xml                             # 父POM
├── .gitignore
└── README.md
```

## 使用说明

1. **适用场景**: 
   - 大型分布式系统
   - 微服务架构
   - 云原生应用
   - 高并发系统

2. **推荐用途**:
   - 企业级微服务平台
   - SaaS应用
   - 电商系统
   - 金融系统

3. **部署建议**:
   - 使用容器化部署
   - 配合Kubernetes使用
   - 建议使用Helm管理
   - 配置CI/CD流水线

## 注意事项

- 微服务架构复杂度较高，需要团队有相关经验
- 需要完善的监控和日志系统
- 建议先从单体应用开始，逐步拆分为微服务
- 注意服务间的数据一致性问题
- 需要考虑分布式事务处理
- 建议使用API版本管理策略