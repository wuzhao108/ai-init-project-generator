# Spring Boot 项目模板配置

## 模板信息

- **模板名称**: Spring Boot 完整模板集合
- **模板ID**: `spring-boot-templates`
- **版本**: `1.0.0`
- **描述**: 包含所有Spring Boot项目生成所需的模板文件
- **创建时间**: 2025-07-06
- **更新时间**: 2025-07-06
- **作者**: AI Project Generator

## 模板内容

### Application.java.j2
```jinja2
package {{ config.package }};

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
}
```

### README.md.j2
```jinja2
# {{ config.name }}

{{ config.description }}

## 项目信息

- **项目名称**: {{ config.name }}
- **版本**: {{ config.version }}
- **Java版本**: {{ config.java_version }}
- **Spring Boot版本**: {{ config.spring_boot_version }}
- **包名**: {{ config.package }}

## 技术栈

{% if config.tech_stack -%}
{% if config.tech_stack.database and config.tech_stack.database != 'none' -%}
- **数据库**: {{ config.tech_stack.database | title }}
{% endif -%}
{% if config.tech_stack.orm -%}
- **ORM框架**: {{ config.tech_stack.orm | title }}
{% endif -%}
{% if config.tech_stack.cache -%}
- **缓存**: {{ config.tech_stack.cache | join(', ') | title }}
{% endif -%}
{% if config.tech_stack.mq -%}
- **消息队列**: {{ config.tech_stack.mq | join(', ') | title }}
{% endif -%}
{% if config.tech_stack.nosql -%}
{% if config.tech_stack.nosql.elasticsearch -%}
- **NoSQL**: Elasticsearch
{% endif -%}
{% if config.tech_stack.nosql.mongodb -%}
- **NoSQL**: MongoDB
{% endif -%}
{% endif -%}
{% if config.tech_stack.documentation -%}
- **文档工具**: Swagger/OpenAPI
{% endif -%}
{% if config.tech_stack.security -%}
- **安全框架**: Spring Security
{% endif -%}
{% if config.tech_stack.monitoring and config.tech_stack.monitoring.actuator -%}
- **监控组件**: Spring Boot Actuator
{% endif -%}
{% endif -%}

## 快速开始

### 环境要求

- Java {{ config.java_version }}+
- Maven 3.6+

### 运行步骤

1. 克隆项目
```bash
git clone <repository-url>
cd {{ config.name }}
```

2. 编译项目
```bash
mvn clean compile
```

3. 运行应用
```bash
mvn spring-boot:run
```

4. 访问应用
```
http://localhost:8080
```

## 项目结构

```
{{ config.name }}/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── {{ config.package | package_to_path }}/
│   │   │       ├── Application.java
│   │   │       ├── controller/
│   │   │       ├── entity/
│   │   │       ├── service/
│   │   │       └── repository/
│   │   └── resources/
│   │       ├── application.yml
│   │       ├── logback-spring.xml
│   │       ├── static/
│   │       └── templates/
│   └── test/
│       └── java/
├── target/
├── pom.xml
├── README.md
└── .gitignore
```

## API接口

### 健康检查
- **GET** `/actuator/health` - 应用健康状态

### 示例接口
- **GET** `/hello` - Hello World示例

## 开发指南

### 代码规范
- 遵循阿里巴巴Java开发手册
- 使用统一的代码格式化配置
- 编写单元测试，保证代码覆盖率

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

# 运行jar包
java -jar target/{{ config.name }}-{{ config.version }}.jar
```

### Docker部署
```bash
# 构建镜像
docker build -t {{ config.name }}:{{ config.version }} .

# 运行容器
docker run -p 8080:8080 {{ config.name }}:{{ config.version }}
```

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request！

## 联系方式

- 邮箱: developer@example.com
- 项目地址: https://github.com/example/{{ config.name }}
```

### .gitignore.j2
```jinja2
# Compiled class file
*.class

# Log file
*.log

# BlueJ files
*.ctxt

# Mobile Tools for Java (J2ME)
.mtj.tmp/

# Package Files #
*.jar
*.war
*.nar
*.ear
*.zip
*.tar.gz
*.rar

# virtual machine crash logs
hs_err_pid*
replay_pid*

# Maven
target/
pom.xml.tag
pom.xml.releaseBackup
pom.xml.versionsBackup
pom.xml.next
release.properties
dependency-reduced-pom.xml
buildNumber.properties
.mvn/timing.properties
.mvn/wrapper/maven-wrapper.jar

# Gradle
.gradle
build/
!gradle/wrapper/gradle-wrapper.jar
!**/src/main/**/build/
!**/src/test/**/build/

# IntelliJ IDEA
.idea/
*.iws
*.iml
*.ipr
out/
!**/src/main/**/out/
!**/src/test/**/out/

# Eclipse
.apt_generated
.classpath
.factorypath
.project
.settings
.springBeans
.sts4-cache
bin/
!**/src/main/**/bin/
!**/src/test/**/bin/

# NetBeans
/nbproject/private/
/nbbuild/
/dist/
/nbdist/
/.nb-gradle/

# VS Code
.vscode/

# Mac
.DS_Store

# Windows
Thumbs.db
ehthumbs.db
Desktop.ini

# Application specific
application-local.yml
application-dev.yml
application-prod.yml
logs/
*.pid

# Database
*.db
*.sqlite
*.sqlite3

# Docker
.dockerignore

# Node.js (if using frontend)
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
```

### application.yml.j2
```jinja2
server:
  port: 8080
  servlet:
    context-path: /

spring:
  application:
    name: {{ config.name }}
  profiles:
    active: dev
{% if config.tech_stack and config.tech_stack.database and config.tech_stack.database != 'none' %}
  datasource:
{% if config.tech_stack.database == 'mysql' %}
    url: jdbc:mysql://localhost:3306/{{ config.name | replace('-', '_') }}?useUnicode=true&characterEncoding=utf8&useSSL=false&serverTimezone=Asia/Shanghai
    username: root
    password: password
    driver-class-name: com.mysql.cj.jdbc.Driver
{% elif config.tech_stack.database == 'postgresql' %}
    url: jdbc:postgresql://localhost:5432/{{ config.name | replace('-', '_') }}
    username: postgres
    password: password
    driver-class-name: org.postgresql.Driver
{% elif config.tech_stack.database == 'h2' %}
    url: jdbc:h2:mem:testdb
    username: sa
    password: password
    driver-class-name: org.h2.Driver
  h2:
    console:
      enabled: true
{% endif %}
{% if config.tech_stack.orm == 'mybatis' %}
mybatis:
  mapper-locations: classpath:mapper/*.xml
  type-aliases-package: {{ config.package }}.entity
  configuration:
    map-underscore-to-camel-case: true
    log-impl: org.apache.ibatis.logging.stdout.StdOutImpl
{% elif config.tech_stack.orm == 'jpa' %}
  jpa:
    hibernate:
      ddl-auto: update
    show-sql: true
    properties:
      hibernate:
        dialect: {% if config.tech_stack.database == 'mysql' %}org.hibernate.dialect.MySQL8Dialect{% elif config.tech_stack.database == 'postgresql' %}org.hibernate.dialect.PostgreSQLDialect{% elif config.tech_stack.database == 'h2' %}org.hibernate.dialect.H2Dialect{% endif %}
        format_sql: true
{% endif %}
{% endif %}
{% if config.tech_stack and config.tech_stack.cache and 'redis' in config.tech_stack.cache %}
  redis:
    host: localhost
    port: 6379
    password:
    database: 0
    timeout: 3000ms
    lettuce:
      pool:
        max-active: 8
        max-wait: -1ms
        max-idle: 8
        min-idle: 0
{% endif %}
{% if config.tech_stack and config.tech_stack.monitoring and config.tech_stack.monitoring.actuator %}
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,prometheus
  endpoint:
    health:
      show-details: always
{% endif %}

logging:
  config: classpath:logback-spring.xml
  level:
    {{ config.package }}: DEBUG
    org.springframework: INFO
    org.mybatis: DEBUG
```

### logback-spring.xml.j2
```jinja2
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <include resource="org/springframework/boot/logging/logback/defaults.xml"/>
    
    <!-- 控制台输出 -->
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
            <charset>UTF-8</charset>
        </encoder>
    </appender>
    
    <!-- 文件输出 -->
    <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>logs/{{ config.name }}.log</file>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>logs/{{ config.name }}.%d{yyyy-MM-dd}.%i.log</fileNamePattern>
            <timeBasedFileNamingAndTriggeringPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedFNATP">
                <maxFileSize>100MB</maxFileSize>
            </timeBasedFileNamingAndTriggeringPolicy>
            <maxHistory>30</maxHistory>
        </rollingPolicy>
        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
            <charset>UTF-8</charset>
        </encoder>
    </appender>
    
    <!-- 根日志级别 -->
    <root level="INFO">
        <appender-ref ref="CONSOLE"/>
        <appender-ref ref="FILE"/>
    </root>
    
    <!-- 应用日志级别 -->
    <logger name="{{ config.package }}" level="DEBUG" additivity="false">
        <appender-ref ref="CONSOLE"/>
        <appender-ref ref="FILE"/>
    </logger>
</configuration>
```

### pom.xml.j2
```jinja2
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>{{ config.spring_boot_version }}</version>
        <relativePath/>
    </parent>

    <groupId>{{ config.group_id }}</groupId>
    <artifactId>{{ config.artifact_id }}</artifactId>
    <version>{{ config.version }}</version>
    <name>{{ config.name }}</name>
    <description>{{ config.description }}</description>
    <packaging>jar</packaging>

    <properties>
        <java.version>{{ config.java_version }}</java.version>
        <maven.compiler.source>{{ config.java_version }}</maven.compiler.source>
        <maven.compiler.target>{{ config.java_version }}</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
    </properties>

    <dependencies>
        <!-- Spring Boot Starter Web -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <!-- Spring Boot Starter Test -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>

{% if config.tech_stack and config.tech_stack.monitoring and config.tech_stack.monitoring.actuator %}
        <!-- Spring Boot Actuator -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>
{% endif %}

{% if config.tech_stack and config.tech_stack.database and config.tech_stack.database != 'none' %}
{% if config.tech_stack.database == 'mysql' %}
        <!-- MySQL Driver -->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <scope>runtime</scope>
        </dependency>
{% elif config.tech_stack.database == 'postgresql' %}
        <!-- PostgreSQL Driver -->
        <dependency>
            <groupId>org.postgresql</groupId>
            <artifactId>postgresql</artifactId>
            <scope>runtime</scope>
        </dependency>
{% elif config.tech_stack.database == 'h2' %}
        <!-- H2 Database -->
        <dependency>
            <groupId>com.h2database</groupId>
            <artifactId>h2</artifactId>
            <scope>runtime</scope>
        </dependency>
{% endif %}

{% if config.tech_stack.orm == 'mybatis' %}
        <!-- MyBatis -->
        <dependency>
            <groupId>org.mybatis.spring.boot</groupId>
            <artifactId>mybatis-spring-boot-starter</artifactId>
            <version>2.3.1</version>
        </dependency>
{% elif config.tech_stack.orm == 'jpa' %}
        <!-- Spring Data JPA -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
{% endif %}
{% endif %}

{% if config.tech_stack and config.tech_stack.cache and 'redis' in config.tech_stack.cache %}
        <!-- Redis -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-redis</artifactId>
        </dependency>
{% endif %}

{% if config.tech_stack and config.tech_stack.documentation %}
        <!-- Swagger -->
        <dependency>
            <groupId>org.springdoc</groupId>
            <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
            <version>2.1.0</version>
        </dependency>
{% endif %}

{% if config.tech_stack and config.tech_stack.security %}
        <!-- Spring Security -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-security</artifactId>
        </dependency>
{% endif %}

        <!-- Lombok -->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <optional>true</optional>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <excludes>
                        <exclude>
                            <groupId>org.projectlombok</groupId>
                            <artifactId>lombok</artifactId>
                        </exclude>
                    </excludes>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

### controller/HelloController.java.j2
```jinja2
package {{ config.package }}.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Hello World 控制器
 * 
 * @author AI Generator
 * @version {{ config.version }}
 */
@RestController
public class HelloController {

    @GetMapping("/hello")
    public String hello() {
        return "Hello, World! Welcome to {{ config.name }}!";
    }

    @GetMapping("/")
    public String index() {
        return "{{ config.description }}";
    }
}
```

### entity/User.java.j2
```jinja2
package {{ config.package }}.entity;

{% if config.tech_stack and config.tech_stack.orm == 'jpa' %}
import javax.persistence.*;
{% endif %}
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;

import java.time.LocalDateTime;

/**
 * 用户实体类
 * 
 * @author AI Generator
 * @version {{ config.version }}
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
{% if config.tech_stack and config.tech_stack.orm == 'jpa' %}
@Entity
@Table(name = "users")
{% endif %}
public class User {

{% if config.tech_stack and config.tech_stack.orm == 'jpa' %}
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
{% endif %}
    private Long id;

{% if config.tech_stack and config.tech_stack.orm == 'jpa' %}
    @Column(nullable = false, unique = true, length = 50)
{% endif %}
    private String username;

{% if config.tech_stack and config.tech_stack.orm == 'jpa' %}
    @Column(nullable = false, unique = true, length = 100)
{% endif %}
    private String email;

{% if config.tech_stack and config.tech_stack.orm == 'jpa' %}
    @Column(nullable = false, length = 100)
{% endif %}
    private String password;

{% if config.tech_stack and config.tech_stack.orm == 'jpa' %}
    @Column(name = "full_name", length = 100)
{% endif %}
    private String fullName;

{% if config.tech_stack and config.tech_stack.orm == 'jpa' %}
    @Column(name = "created_at")
{% endif %}
    private LocalDateTime createdAt;

{% if config.tech_stack and config.tech_stack.orm == 'jpa' %}
    @Column(name = "updated_at")
{% endif %}
    private LocalDateTime updatedAt;
}
```

### mapper/UserMapper.java.j2
```jinja2
package {{ config.package }}.mapper;

{% if config.tech_stack and config.tech_stack.orm == 'mybatis' %}
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Update;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Param;
{% endif %}
import {{ config.package }}.entity.User;

import java.util.List;

/**
 * 用户数据访问层
 * 
 * @author AI Generator
 * @version {{ config.version }}
 */
{% if config.tech_stack and config.tech_stack.orm == 'mybatis' %}
@Mapper
{% endif %}
public interface UserMapper {

    /**
     * 查询所有用户
     * 
     * @return 用户列表
     */
{% if config.tech_stack and config.tech_stack.orm == 'mybatis' %}
    @Select("SELECT * FROM users")
{% endif %}
    List<User> findAll();

    /**
     * 根据ID查询用户
     * 
     * @param id 用户ID
     * @return 用户信息
     */
{% if config.tech_stack and config.tech_stack.orm == 'mybatis' %}
    @Select("SELECT * FROM users WHERE id = #{id}")
{% endif %}
    User findById(@Param("id") Long id);

    /**
     * 根据用户名查询用户
     * 
     * @param username 用户名
     * @return 用户信息
     */
{% if config.tech_stack and config.tech_stack.orm == 'mybatis' %}
    @Select("SELECT * FROM users WHERE username = #{username}")
{% endif %}
    User findByUsername(@Param("username") String username);

    /**
     * 插入用户
     * 
     * @param user 用户信息
     * @return 影响行数
     */
{% if config.tech_stack and config.tech_stack.orm == 'mybatis' %}
    @Insert("INSERT INTO users(username, email, password, full_name, created_at, updated_at) VALUES(#{username}, #{email}, #{password}, #{fullName}, #{createdAt}, #{updatedAt})")
{% endif %}
    int insert(User user);

    /**
     * 更新用户
     * 
     * @param user 用户信息
     * @return 影响行数
     */
{% if config.tech_stack and config.tech_stack.orm == 'mybatis' %}
    @Update("UPDATE users SET username=#{username}, email=#{email}, password=#{password}, full_name=#{fullName}, updated_at=#{updatedAt} WHERE id=#{id}")
{% endif %}
    int update(User user);

    /**
     * 删除用户
     * 
     * @param id 用户ID
     * @return 影响行数
     */
{% if config.tech_stack and config.tech_stack.orm == 'mybatis' %}
    @Delete("DELETE FROM users WHERE id = #{id}")
{% endif %}
    int deleteById(@Param("id") Long id);
}
```

### mapper/UserMapper.xml.j2
```jinja2
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="{{ config.package }}.mapper.UserMapper">

    <!-- 结果映射 -->
    <resultMap id="UserResultMap" type="{{ config.package }}.entity.User">
        <id column="id" property="id"/>
        <result column="username" property="username"/>
        <result column="email" property="email"/>
        <result column="password" property="password"/>
        <result column="full_name" property="fullName"/>
        <result column="created_at" property="createdAt"/>
        <result column="updated_at" property="updatedAt"/>
    </resultMap>

    <!-- 查询所有用户 -->
    <select id="findAll" resultMap="UserResultMap">
        SELECT id, username, email, password, full_name, created_at, updated_at
        FROM users
        ORDER BY created_at DESC
    </select>

    <!-- 根据ID查询用户 -->
    <select id="findById" parameterType="long" resultMap="UserResultMap">
        SELECT id, username, email, password, full_name, created_at, updated_at
        FROM users
        WHERE id = #{id}
    </select>

    <!-- 根据用户名查询用户 -->
    <select id="findByUsername" parameterType="string" resultMap="UserResultMap">
        SELECT id, username, email, password, full_name, created_at, updated_at
        FROM users
        WHERE username = #{username}
    </select>

    <!-- 插入用户 -->
    <insert id="insert" parameterType="{{ config.package }}.entity.User" useGeneratedKeys="true" keyProperty="id">
        INSERT INTO users (username, email, password, full_name, created_at, updated_at)
        VALUES (#{username}, #{email}, #{password}, #{fullName}, #{createdAt}, #{updatedAt})
    </insert>

    <!-- 更新用户 -->
    <update id="update" parameterType="{{ config.package }}.entity.User">
        UPDATE users
        SET username = #{username},
            email = #{email},
            password = #{password},
            full_name = #{fullName},
            updated_at = #{updatedAt}
        WHERE id = #{id}
    </update>

    <!-- 删除用户 -->
    <delete id="deleteById" parameterType="long">
        DELETE FROM users WHERE id = #{id}
    </delete>

</mapper>
```

### repository/UserRepository.java.j2
```jinja2
package {{ config.package }}.repository;

{% if config.tech_stack and config.tech_stack.orm == 'jpa' %}
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
{% endif %}
import {{ config.package }}.entity.User;

import java.util.Optional;

/**
 * 用户仓储接口
 * 
 * @author AI Generator
 * @version {{ config.version }}
 */
{% if config.tech_stack and config.tech_stack.orm == 'jpa' %}
@Repository
public interface UserRepository extends JpaRepository<User, Long> {

    /**
     * 根据用户名查询用户
     * 
     * @param username 用户名
     * @return 用户信息
     */
    Optional<User> findByUsername(String username);

    /**
     * 根据邮箱查询用户
     * 
     * @param email 邮箱
     * @return 用户信息
     */
    Optional<User> findByEmail(String email);

    /**
     * 检查用户名是否存在
     * 
     * @param username 用户名
     * @return 是否存在
     */
    boolean existsByUsername(String username);

    /**
     * 检查邮箱是否存在
     * 
     * @param email 邮箱
     * @return 是否存在
     */
    boolean existsByEmail(String email);
}
{% else %}
public interface UserRepository {
    // JPA repository interface placeholder
    // This interface would be implemented when JPA is enabled
}
{% endif %}
```

### test/ApplicationTest.java.j2
```jinja2
package {{ config.package }};

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.ActiveProfiles;

/**
 * 应用程序测试类
 * 
 * @author AI Generator
 * @version {{ config.version }}
 */
@SpringBootTest
@ActiveProfiles("test")
class ApplicationTest {

    @Test
    void contextLoads() {
        // 测试Spring上下文是否能正常加载
    }

    @Test
    void applicationStarts() {
        // 测试应用程序是否能正常启动
    }
}
```

### Dockerfile.j2
```jinja2
# 使用官方OpenJDK运行时作为基础镜像
FROM openjdk:{{ config.java_version }}-jre-slim

# 设置工作目录
WORKDIR /app

# 复制jar文件到容器中
COPY target/{{ config.artifact_id }}-{{ config.version }}.jar app.jar

# 暴露端口
EXPOSE 8080

# 设置JVM参数
ENV JAVA_OPTS="-Xmx512m -Xms256m"

# 运行应用程序
ENTRYPOINT ["sh", "-c", "java $JAVA_OPTS -jar app.jar"]

# 健康检查
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/actuator/health || exit 1
```

### docker-compose.yml.j2
```jinja2
version: '3.8'

services:
  {{ config.name }}:
    build: .
    ports:
      - "8080:8080"
    environment:
      - SPRING_PROFILES_ACTIVE=docker
{% if config.tech_stack and config.tech_stack.database and config.tech_stack.database == 'mysql' %}
      - SPRING_DATASOURCE_URL=jdbc:mysql://mysql:3306/{{ config.name | replace('-', '_') }}?useUnicode=true&characterEncoding=utf8&useSSL=false&serverTimezone=Asia/Shanghai
      - SPRING_DATASOURCE_USERNAME=root
      - SPRING_DATASOURCE_PASSWORD=password
{% elif config.tech_stack and config.tech_stack.database and config.tech_stack.database == 'postgresql' %}
      - SPRING_DATASOURCE_URL=jdbc:postgresql://postgres:5432/{{ config.name | replace('-', '_') }}
      - SPRING_DATASOURCE_USERNAME=postgres
      - SPRING_DATASOURCE_PASSWORD=password
{% endif %}
{% if config.tech_stack and config.tech_stack.cache and 'redis' in config.tech_stack.cache %}
      - SPRING_REDIS_HOST=redis
      - SPRING_REDIS_PORT=6379
{% endif %}
    depends_on:
{% if config.tech_stack and config.tech_stack.database and config.tech_stack.database == 'mysql' %}
      - mysql
{% elif config.tech_stack and config.tech_stack.database and config.tech_stack.database == 'postgresql' %}
      - postgres
{% endif %}
{% if config.tech_stack and config.tech_stack.cache and 'redis' in config.tech_stack.cache %}
      - redis
{% endif %}
    networks:
      - app-network

{% if config.tech_stack and config.tech_stack.database and config.tech_stack.database == 'mysql' %}
  mysql:
    image: mysql:8.0
    environment:
      - MYSQL_ROOT_PASSWORD=password
      - MYSQL_DATABASE={{ config.name | replace('-', '_') }}
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql
    networks:
      - app-network
{% elif config.tech_stack and config.tech_stack.database and config.tech_stack.database == 'postgresql' %}
  postgres:
    image: postgres:15
    environment:
      - POSTGRES_DB={{ config.name | replace('-', '_') }}
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - app-network
{% endif %}

{% if config.tech_stack and config.tech_stack.cache and 'redis' in config.tech_stack.cache %}
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    networks:
      - app-network
{% endif %}

volumes:
{% if config.tech_stack and config.tech_stack.database and config.tech_stack.database == 'mysql' %}
  mysql_data:
{% elif config.tech_stack and config.tech_stack.database and config.tech_stack.database == 'postgresql' %}
  postgres_data:
{% endif %}
{% if config.tech_stack and config.tech_stack.cache and 'redis' in config.tech_stack.cache %}
  redis_data:
{% endif %}

networks:
  app-network:
    driver: bridge
```

### module-pom.xml.j2
```jinja2
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>{{ config.group_id }}</groupId>
        <artifactId>{{ config.artifact_id }}-parent</artifactId>
        <version>{{ config.version }}</version>
    </parent>

    <artifactId>{{ config.artifact_id }}-{{ module.name }}</artifactId>
    <name>{{ config.name }} - {{ module.name | title }}</name>
    <description>{{ module.description }}</description>
    <packaging>jar</packaging>

    <dependencies>
        <!-- 模块特定依赖 -->
{% for dependency in module.dependencies %}
        <dependency>
            <groupId>{{ dependency.group_id }}</groupId>
            <artifactId>{{ dependency.artifact_id }}</artifactId>
{% if dependency.version %}
            <version>{{ dependency.version }}</version>
{% endif %}
{% if dependency.scope %}
            <scope>{{ dependency.scope }}</scope>
{% endif %}
        </dependency>
{% endfor %}
    </dependencies>

    <build>
        <plugins>
            <!-- 模块特定插件 -->
{% for plugin in module.plugins %}
            <plugin>
                <groupId>{{ plugin.group_id }}</groupId>
                <artifactId>{{ plugin.artifact_id }}</artifactId>
{% if plugin.version %}
                <version>{{ plugin.version }}</version>
{% endif %}
{% if plugin.configuration %}
                <configuration>
{{ plugin.configuration | indent(20, true) }}
                </configuration>
{% endif %}
            </plugin>
{% endfor %}
        </plugins>
    </build>
</project>
```

## 使用说明

此配置文件包含了生成Spring Boot项目所需的所有模板内容。模板使用Jinja2语法，支持动态变量替换和条件渲染。

### 模板特性

1. **动态配置**: 根据项目配置动态生成内容
2. **技术栈适配**: 支持多种数据库、ORM框架、缓存等
3. **条件渲染**: 根据选择的技术栈生成相应的配置
4. **完整覆盖**: 包含项目所需的所有文件模板
5. **最佳实践**: 遵循Spring Boot和Java开发最佳实践