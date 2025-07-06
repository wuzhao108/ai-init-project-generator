# my-spring-boot-project

基于默认模板的Spring Boot项目

## 项目信息

- **项目名称**: my-spring-boot-project
- **项目版本**: 1.0.0
- **Java版本**: 17
- **Spring Boot版本**: 
- **构建工具**: Maven
- **项目类型**: 多模块项目
## 技术栈

### 核心框架
- Spring Boot 
- Spring Framework
- Spring Web MVC

### 数据层
- Spring Data JPA - 数据访问层
- H2 - 关系型数据库

### 缓存

### 消息队列

### NoSQL数据库

### 文档工具
- Swagger/OpenAPI 3 - API文档生成

### 安全框架

### 监控
- Spring Boot Actuator - 应用监控

## 项目结构

```
my-spring-boot-project/
├── my-spring-boot-project-common/                        # 公共模块
│   ├── src/main/java//common/
│   └── pom.xml
├── my-spring-boot-project-api/                           # API模块
│   ├── src/main/java//api/
│   └── pom.xml
├── my-spring-boot-project-dao/                           # 数据访问模块
│   ├── src/main/java//dao/
│   └── pom.xml
├── my-spring-boot-project-service/                       # 服务模块
│   ├── src/main/java//service/
│   └── pom.xml
├── my-spring-boot-project-web/                           # Web模块
│   ├── src/main/java//web/
│   ├── src/main/resources/
│   └── pom.xml
├── logs/                                            # 日志目录
├── Dockerfile                                       # Docker镜像构建文件
├── docker-compose.yml                               # Docker编排文件
├── pom.xml                                          # 父POM文件
├── .gitignore                                       # Git忽略文件
└── README.md                                        # 项目说明文档
```

## 快速开始

### 环境要求

- JDK 17+
- Maven 3.6+

### 本地开发

1. **克隆项目**
   ```bash
   git clone <repository-url>
   cd my-spring-boot-project
   ```

2. **配置数据库**

3. **修改配置文件**
   
   编辑 `src/main/resources/application-dev.yml`，修改数据库连接信息：
   ```yaml
   spring:
     datasource:
       username: my-spring-boot-project_user
       password: your_password
   ```

4. **启动应用**
   ```bash
   # 使用Maven启动
   mvn spring-boot:run
   
   # 或者编译后启动
   mvn clean package
   java -jar target/my-spring-boot-project-1.0.0.jar
   ```

5. **访问应用**
   - 应用地址: http://localhost:8080
   - API文档: http://localhost:8080/swagger-ui/index.html
   - 健康检查: http://localhost:8080/actuator/health

### Docker部署

1. **构建镜像**
   ```bash
   docker build -t my-spring-boot-project:1.0.0 .
   ```

2. **使用Docker Compose启动**
   ```bash
   docker-compose up -d
   ```

3. **查看日志**
   ```bash
   docker-compose logs -f my-spring-boot-project
   ```

## 开发指南

### 代码规范

- 遵循阿里巴巴Java开发手册
- 使用统一的代码格式化配置
- 所有公共方法必须添加注释
- 单元测试覆盖率不低于80%

### 分层架构

```
Controller层 -> Service层 -> DAO层 -> 数据库
     ↓            ↓           ↓
   接收请求    业务逻辑处理   数据访问
```

### API设计规范

- 使用RESTful风格
- 统一的响应格式
- 合理的HTTP状态码
- 完善的错误处理

### 数据库设计

- 遵循数据库设计三范式
- 合理使用索引
- 统一的命名规范
- 必要的字段注释

## 部署说明

### 环境配置

- **开发环境**: `application-dev.yml`
- **测试环境**: `application-test.yml`
- **生产环境**: `application-prod.yml`

### 构建部署

```bash
# 打包应用
mvn clean package -P prod

# 运行应用
java -jar -Dspring.profiles.active=prod target/my-spring-boot-project-1.0.0.jar
```

## 监控运维


### 日志管理

- 日志文件位置: `logs/`
- 日志级别配置: `logback-spring.xml`
- 日志滚动策略: 按天滚动，保留30天

## 常见问题

### Q: 如何修改端口号？
A: 在配置文件中修改 `server.port` 属性。

### Q: 如何添加新的依赖？
A: 在 `pom.xml` 文件中添加相应的依赖配置。

### Q: 如何配置跨域？
A: 在配置类中添加 `@CrossOrigin` 注解或配置 `CorsConfigurationSource`。

## 贡献指南

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 联系方式

- 项目维护者: [Your Name]
- 邮箱: [your.email@example.com]
- 项目地址: [https://github.com/username/my-spring-boot-project]

## 更新日志

### v1.0.0 (2024-01-01)
- 初始版本发布
- 基础功能实现
- 项目架构搭建完成