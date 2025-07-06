# my-spring-boot-project

基于默认模板的Spring Boot项目

## 项目信息

- **项目名称**: my-spring-boot-project
- **版本**: 1.0.0
- **Java版本**: 17
- **Spring Boot版本**: 3.2.2
- **包名**: com.example.project

## 技术栈

- **数据库**: MYSQL
- **ORM框架**: MYBATIS
- **Spring Boot Actuator**: 已启用

## 快速开始

### 环境要求

- JDK 17+
- Maven 3.6+
- MySQL 8.0+

### 运行步骤

1. **克隆项目**
   ```bash
   git clone <repository-url>
   cd my-spring-boot-project
   ```

2. **配置数据库**
   - 创建数据库: `CREATE DATABASE my_spring_boot_project;`
   - 修改 `src/main/resources/application.yml` 中的数据库连接信息

3. **编译项目**
   ```bash
   mvn clean compile
   ```

4. **运行应用**
   ```bash
   mvn spring-boot:run
   ```

5. **访问应用**
   - 应用地址: http://localhost:8080
   - API测试: http://localhost:8080/api/hello
   - 健康检查: http://localhost:8080/actuator/health

## 项目结构

```
my-spring-boot-project/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/example/project/
│   │   │       ├── Application.java
│   │   │       ├── controller/
│   │   │       ├── entity/
│   │   │       │   │   │       └── mapper/
│   │   │       │   │   └── resources/
│   │       ├── application.yml
│   │       ├── logback-spring.xml
│   │       │   │       └── mapper/
│   │       │   └── test/
│       └── java/
├── pom.xml
└── README.md
```

## API接口

### Hello Controller

- `GET /api/hello` - 返回问候信息
- `GET /api/health` - 健康检查

### User相关接口

- 使用MyBatis进行数据访问
- 实体类: `User`
- Mapper: `UserMapper`

## 开发指南

### 代码规范

- 遵循Java编码规范
- 使用驼峰命名法
- 添加适当的注释和文档

### 测试

```bash
# 运行所有测试
mvn test

# 运行特定测试类
mvn test -Dtest=ApplicationTest
```

### 打包部署

```bash
# 打包应用
mvn clean package

# 运行打包后的jar
java -jar target/my-spring-boot-project-1.0.0.jar
```

### Docker部署

```bash
# 构建镜像
docker build -t my-spring-boot-project:1.0.0 .

# 运行容器
docker run -p 8080:8080 my-spring-boot-project:1.0.0

# 使用docker-compose
docker-compose up -d
```

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 贡献

欢迎提交 Issue 和 Pull Request！

## 联系方式

如有问题，请联系项目维护者。