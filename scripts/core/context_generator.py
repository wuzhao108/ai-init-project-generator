#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
上下文生成器 - 生成Java项目初始化的上下文提示词

负责根据用户配置生成：
- 系统提示词（项目生成步骤和规范）
- 用户提示词（用户的具体配置需求）
- Gemini斜杠命令文件
- 配置文件保存
"""

import json
import os
from pathlib import Path
from datetime import datetime
from rich.console import Console

console = Console()


class ContextGenerator:
    """上下文生成器类"""
    
    def __init__(self):
        self.output_base_dir = Path("./output")
        self.templates_dir = Path("./scripts/templates")
        
        # 确保目录存在
        self.output_base_dir.mkdir(parents=True, exist_ok=True)
        self.templates_dir.mkdir(parents=True, exist_ok=True)
    
    def generate(self, config):
        """生成完整的上下文工程"""
        try:
            # 创建项目特定的输出目录
            project_name = config['project_name']
            output_dir = self.output_base_dir / project_name
            output_dir.mkdir(parents=True, exist_ok=True)
            
            console.print(f"[blue]📁 创建输出目录: {output_dir}[/blue]")
            
            # 保存配置文件
            self._save_config(config, output_dir)
            
            # 生成系统提示词
            self._generate_system_prompt(config, output_dir)
            
            # 生成用户提示词
            self._generate_user_prompt(config, output_dir)
            
            # 生成Gemini斜杠命令文件
            self._generate_gemini_commands(config, output_dir)
            
            # 生成Claude Code斜杠命令文件
            self._generate_claude_commands(config, output_dir)
            
            # 生成执行计划文件
            self._generate_execution_plan(config, output_dir)
            
            # 生成项目结构说明
            self._generate_project_structure(config, output_dir)
            
            # 生成README文件
            self._generate_readme(config, output_dir)
            
            console.print(f"[green]✅ 上下文工程生成完成[/green]")
            return str(output_dir)
            
        except Exception as e:
            console.print(f"[red]❌ 生成上下文工程失败: {str(e)}[/red]")
            raise
    
    def _save_config(self, config, output_dir):
        """保存配置文件"""
        config_file = output_dir / "config.json"
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
        console.print(f"[green]✅ 配置文件已保存: {config_file.name}[/green]")
    
    def _generate_system_prompt(self, config, output_dir):
        """生成系统提示词"""
        system_prompt = self._build_system_prompt(config)
        
        system_file = output_dir / "system_prompt.md"
        with open(system_file, 'w', encoding='utf-8') as f:
            f.write(system_prompt)
        
        console.print(f"[green]✅ 系统提示词已生成: {system_file.name}[/green]")
    
    def _generate_user_prompt(self, config, output_dir):
        """生成用户提示词"""
        user_prompt = self._build_user_prompt(config)
        
        user_file = output_dir / "user_prompt.md"
        with open(user_file, 'w', encoding='utf-8') as f:
            f.write(user_prompt)
        
        console.print(f"[green]✅ 用户提示词已生成: {user_file.name}[/green]")
    
    def _generate_gemini_commands(self, config, output_dir):
        """生成Gemini斜杠命令文件"""
        commands = self._build_gemini_commands(config)
        
        # 生成.gemini文件
        gemini_file = output_dir / "project_generator.gemini"
        with open(gemini_file, 'w', encoding='utf-8') as f:
            f.write(commands)
        
        console.print(f"[green]✅ Gemini命令文件已生成: {gemini_file.name}[/green]")
    
    def _generate_claude_commands(self, config, output_dir):
        """生成Claude Code斜杠命令文件"""
        commands = self._build_claude_commands(config)
        
        # 生成.claude文件
        claude_file = output_dir / "project_generator.claude"
        with open(claude_file, 'w', encoding='utf-8') as f:
            f.write(commands)
        
        console.print(f"[green]✅ Claude Code命令文件已生成: {claude_file.name}[/green]")
    
    def _generate_execution_plan(self, config, output_dir):
        """生成执行计划文件"""
        execution_plan = self._build_execution_plan(config)
        
        plan_file = output_dir / "execution_plan.md"
        with open(plan_file, 'w', encoding='utf-8') as f:
            f.write(execution_plan)
        
        console.print(f"[green]✅ 执行计划已生成: {plan_file.name}[/green]")
    
    def _generate_project_structure(self, config, output_dir):
        """生成项目结构说明"""
        structure = self._build_project_structure(config)
        
        structure_file = output_dir / "project_structure.md"
        with open(structure_file, 'w', encoding='utf-8') as f:
            f.write(structure)
        
        console.print(f"[green]✅ 项目结构说明已生成: {structure_file.name}[/green]")
    
    def _generate_readme(self, config, output_dir):
        """生成README文件"""
        readme_content = self._build_readme(config)
        
        readme_file = output_dir / "README.md"
        with open(readme_file, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        console.print(f"[green]✅ README文件已生成: {readme_file.name}[/green]")
    
    def _build_system_prompt(self, config):
        """构建系统提示词"""
        return f"""# Java项目生成系统提示词

你是一个专业的Java项目架构师和开发专家，擅长创建高质量的Spring Boot项目。

请根据config.json配置文件中的要求，生成一个完整的Java项目。

## 核心原则

**重要**: 所有项目配置必须从config.json文件中动态读取，不得使用硬编码值。

## 项目生成规范

### 1. 项目结构规范
- 使用标准的Maven/Gradle项目结构（根据config.json中的build_tool）
- 遵循Java包命名规范（使用config.json中的package_name）
- 实现清晰的分层架构（Controller、Service、Repository/DAO、Entity）
- 配置合理的目录结构和文件组织

### 2. 代码质量要求
- 遵循Java编码规范和最佳实践
- 使用适当的设计模式
- 添加必要的注释和文档
- 实现异常处理和日志记录
- 根据config.json中的generate_tests配置编写测试代码

### 3. 技术栈集成
- 正确配置Spring Boot和相关依赖（版本来自config.json）
- 根据config.json中的database和orm_framework配置数据库连接
- 根据config.json中的cache和message_queue配置集成中间件
- 根据config.json中的include_*配置API文档和监控组件
- 根据config.json中的include_security配置安全认证

### 4. 配置文件管理
- 使用application.yml/properties进行配置
- 支持多环境配置（dev、test、prod）
- 实现外部化配置和敏感信息保护
- 根据config.json中的generate_docker配置提供Docker容器化

### 5. 文档和部署
- 根据config.json中的generate_readme配置生成README文档
- 根据config.json中的include_swagger配置提供API接口文档
- 包含部署和运行说明
- 添加项目依赖和环境要求说明

## 生成步骤

1. **读取配置文件**
   - 解析config.json中的所有配置项
   - 验证配置的完整性和有效性

2. **创建项目基础结构**
   - 根据build_tool生成Maven/Gradle构建文件
   - 根据package_name创建标准的Java包结构
   - 根据project_name配置Spring Boot主类

3. **配置依赖管理**
   - 添加Spring Boot Starter依赖（版本来自spring_boot_version）
   - 根据技术栈配置集成数据库和ORM框架
   - 根据配置添加缓存和消息队列依赖
   - 根据生成选项配置测试和文档依赖

4. **实现核心功能**
   - 根据generate_sample_code配置创建示例代码
   - 实现数据访问层、业务逻辑层、控制器层
   - 根据配置集成相应的技术组件

5. **配置集成组件**
   - 根据config.json动态配置数据库连接
   - 根据配置设置缓存组件
   - 根据配置集成消息队列
   - 根据include_security配置安全组件

6. **生成测试代码**
   - 根据generate_tests配置生成测试代码
   - 包含单元测试、集成测试、API测试

7. **完善文档和部署**
   - 根据generate_readme配置生成README文档
   - 根据include_swagger配置生成API文档
   - 根据generate_docker配置生成Docker配置
   - 提供部署和运行说明

## 注意事项

- 确保所有生成的代码都能正常编译和运行
- 遵循Spring Boot的约定优于配置原则
- 严格按照config.json中的版本配置使用相应的技术栈版本
- 考虑性能、安全性和可维护性
- 提供清晰的错误处理和日志记录
- 所有配置项都必须从config.json文件中读取，不得硬编码

请严格按照以上规范和config.json中的具体配置要求来生成项目。
"""
    
    def _build_user_prompt(self, config):
        """构建用户提示词"""
        return f"""# Java项目生成用户需求

请根据config.json配置文件生成一个完整的Java Spring Boot项目。

## 🚨 重要说明

### 项目创建位置
**必须在新的文件夹中创建项目，文件夹名称使用config.json中的project_name字段值。**

**禁止在当前目录直接生成项目文件，必须创建新的项目目录。**

### 配置文件引用
**所有项目配置信息请从config.json文件中动态读取**，包括但不限于：

#### 项目基本信息
- 项目名称 (project_name)
- 基础包名 (package_name)
- 项目版本 (version)
- 项目描述 (description)

#### 技术版本配置
- JDK版本 (jdk_version)
- 构建工具 (build_tool)
- Spring Boot版本 (spring_boot_version)

#### 项目架构
- 项目类型 (is_multi_module)
- 模块配置 (modules)

#### 技术栈配置
- 数据库 (database)
- ORM框架 (orm_framework)
- 缓存 (cache)
- 消息队列 (message_queue)

#### 附加组件
- API文档 (include_swagger)
- 安全框架 (include_security)
- 监控组件 (include_actuator)

#### 生成选项
- 示例代码 (generate_sample_code)
- 测试代码 (generate_tests)
- Docker配置 (generate_docker)
- README文档 (generate_readme)

## 📁 项目结构要求

### ⚠️ 重要：项目创建位置
**必须首先创建一个新的项目文件夹，文件夹名称为config.json中的project_name值，然后在该文件夹内创建所有项目文件。**

**绝对不允许在当前工作目录直接创建src、pom.xml等项目文件！**

### 基础项目结构
请按以下步骤创建标准的Spring Boot项目结构：

1. **第一步：创建项目根目录**
   ```
   mkdir {{project_name}}
   cd {{project_name}}
   ```

2. **第二步：在项目根目录内创建完整结构**
   ```
   {{project_name}}/                    ← 这是新创建的项目根目录
   ├── src/                          ← 在项目根目录内创建src
   │   ├── main/
   │   │   ├── java/
   │   │   │   └── {{package_name_path}}/
   │   │   │       ├── {{MainClassName}}Application.java
   │   │   │       ├── controller/
   │   │   │       ├── service/
   │   │   │       │   └── impl/
   │   │   │       ├── repository/
   │   │   │       ├── entity/
   │   │   │       ├── dto/
   │   │   │       ├── config/
   │   │   │       └── exception/
   │   │   └── resources/
   │   │       ├── application.yml
   │   │       ├── application-dev.yml
   │   │       ├── application-test.yml
   │   │       └── application-prod.yml
   │   └── test/
   │       └── java/
   │           └── {{package_name_path}}/
   ├── {{build_file}}                  ← 在项目根目录内创建构建文件
   ├── Dockerfile (如果generate_docker=true)
   ├── docker-compose.yml (如果generate_docker=true)
   └── README.md (如果generate_readme=true)
   ```

**再次强调：所有文件都必须在新创建的{{project_name}}文件夹内，不得在当前目录直接创建项目文件！**

## 💻 示例代码生成要求

**当config.json中generate_sample_code=true时，请生成以下示例代码：**

### 1. 示例实体类 (Entity)
```java
// 示例：用户实体
@Entity
@Table(name = "users")
public class User {{
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(nullable = false, unique = true)
    private String username;
    
    @Column(nullable = false)
    private String email;
    
    @CreationTimestamp
    private LocalDateTime createdAt;
    
    @UpdateTimestamp
    private LocalDateTime updatedAt;
    
    // 构造函数、getter、setter
}}
```

### 2. 示例Repository接口
```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {{
    Optional<User> findByUsername(String username);
    Optional<User> findByEmail(String email);
    boolean existsByUsername(String username);
    boolean existsByEmail(String email);
}}
```

### 3. 示例Service层
```java
@Service
@Transactional
public class UserService {{
    
    private final UserRepository userRepository;
    
    public UserService(UserRepository userRepository) {{
        this.userRepository = userRepository;
    }}
    
    public List<User> findAll() {{
        return userRepository.findAll();
    }}
    
    public Optional<User> findById(Long id) {{
        return userRepository.findById(id);
    }}
    
    public User save(User user) {{
        return userRepository.save(user);
    }}
    
    public void deleteById(Long id) {{
        userRepository.deleteById(id);
    }}
}}
```

### 4. 示例Controller层
```java
@RestController
@RequestMapping("/api/users")
@Validated
public class UserController {{
    
    private final UserService userService;
    
    public UserController(UserService userService) {{
        this.userService = userService;
    }}
    
    @GetMapping
    public ResponseEntity<List<User>> getAllUsers() {{
        List<User> users = userService.findAll();
        return ResponseEntity.ok(users);
    }}
    
    @GetMapping("/{{id}}")
    public ResponseEntity<User> getUserById(@PathVariable Long id) {{
        return userService.findById(id)
                .map(user -> ResponseEntity.ok(user))
                .orElse(ResponseEntity.notFound().build());
    }}
    
    @PostMapping
    public ResponseEntity<User> createUser(@Valid @RequestBody User user) {{
        User savedUser = userService.save(user);
        return ResponseEntity.status(HttpStatus.CREATED).body(savedUser);
    }}
    
    @PutMapping("/{{id}}")
    public ResponseEntity<User> updateUser(@PathVariable Long id, @Valid @RequestBody User user) {{
        return userService.findById(id)
                .map(existingUser -> {{
                    user.setId(id);
                    User updatedUser = userService.save(user);
                    return ResponseEntity.ok(updatedUser);
                }})
                .orElse(ResponseEntity.notFound().build());
    }}
    
    @DeleteMapping("/{{id}}")
    public ResponseEntity<Void> deleteUser(@PathVariable Long id) {{
        if (userService.findById(id).isPresent()) {{
            userService.deleteById(id);
            return ResponseEntity.noContent().build();
        }}
        return ResponseEntity.notFound().build();
    }}
}}
```

### 5. 示例DTO类
```java
public class UserDTO {{
    @NotBlank(message = "用户名不能为空")
    private String username;
    
    @Email(message = "邮箱格式不正确")
    @NotBlank(message = "邮箱不能为空")
    private String email;
    
    // 构造函数、getter、setter
}}
```

### 6. 全局异常处理
```java
@RestControllerAdvice
public class GlobalExceptionHandler {{
    
    @ExceptionHandler(ValidationException.class)
    public ResponseEntity<ErrorResponse> handleValidationException(ValidationException ex) {{
        ErrorResponse error = new ErrorResponse("VALIDATION_ERROR", ex.getMessage());
        return ResponseEntity.badRequest().body(error);
    }}
    
    @ExceptionHandler(EntityNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleEntityNotFoundException(EntityNotFoundException ex) {{
        ErrorResponse error = new ErrorResponse("NOT_FOUND", ex.getMessage());
        return ResponseEntity.notFound().build();
    }}
    
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleGenericException(Exception ex) {{
        ErrorResponse error = new ErrorResponse("INTERNAL_ERROR", "服务器内部错误");
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(error);
    }}
}}
```

## 🔧 生成要求

请根据config.json中的配置动态生成项目内容，确保：

1. **项目目录**: 创建以project_name命名的新文件夹
2. **项目结构**: 使用清晰的分层架构和标准的Maven/Gradle项目结构
3. **代码质量**: 遵循Java最佳实践和Spring Boot规范
4. **配置管理**: 提供多环境配置支持（dev、test、prod）
5. **技术栈集成**: 根据配置集成相应的数据库、缓存、消息队列等组件
6. **示例代码**: 当generate_sample_code=true时，生成上述示例代码
7. **错误处理**: 实现全局异常处理和适当的错误响应
8. **日志记录**: 配置合理的日志级别和输出格式
9. **API设计**: 遵循RESTful API设计规范
10. **数据验证**: 实现输入数据验证和业务规则检查
11. **安全考虑**: 实现基本的安全配置和最佳实践

## 🚀 项目启动要求

生成的项目应该能够：
- 直接编译和运行
- 通过Maven/Gradle命令启动
- 访问基本的健康检查端点
- 连接配置的数据库（如有）
- 正常处理API请求
- 示例API能够正常工作（如果生成了示例代码）

请确保生成的项目是一个完整、可运行的Spring Boot应用程序，严格按照config.json中的配置要求进行生成。
"""
    
    def _build_gemini_commands(self, config):
        """构建Gemini斜杠命令"""
        return f"""# Gemini CLI 项目生成命令

# 使用方法:
# 1. 将此文件保存为 project_generator.gemini
# 2. 在Gemini CLI中执行: gemini run project_generator.gemini

/system
你是一个专业的Java项目架构师和开发专家，擅长创建高质量的Spring Boot项目。

请严格按照当前目录下的执行计划文件(execution_plan.md)中定义的三个步骤执行项目生成。

同时请遵循system_prompt.md中定义的项目生成规范和代码质量要求。

/user
请根据当前目录下的配置文件生成Java Spring Boot项目：

**🚨 重要项目创建位置要求：**
1. **必须首先创建一个新的项目文件夹，文件夹名称为config.json中的project_name值**
2. **然后在该文件夹内创建所有项目文件（src、pom.xml等）**
3. **绝对不允许在当前工作目录直接创建src、pom.xml等项目文件**
4. **项目结构应为：{config['project_name']}/src/main/java/... 而不是 src/main/java/...**

**配置文件引用：**
- 系统提示词：system_prompt.md
- 用户需求：user_prompt.md  
- 项目配置：config.json
- 执行计划：execution_plan.md

**配置信息读取：**
所有项目配置信息请从config.json文件中动态读取，包括但不限于：
- 项目名称、包名、版本号
- JDK版本、Spring Boot版本、构建工具
- 数据库、ORM框架、缓存、消息队列配置
- 各种生成选项和附加组件配置
- 示例代码生成选项 (generate_sample_code)

请按照execution_plan.md中的三步执行计划开始生成项目。

/generate_project
# 启动Java项目生成器
echo "🚀 启动Java Spring Boot项目生成器"
echo "📁 读取配置文件: config.json"
echo "📝 应用系统提示词: system_prompt.md"
echo "👤 应用用户需求: user_prompt.md"
echo "⚡ 执行计划: execution_plan.md"
echo "🔧 开始三步执行流程..."
"""
    
    def _build_project_structure(self, config):
        """构建项目结构说明"""
        base_structure = f"""
# {config['project_name']} 项目结构说明

## 标准项目结构

```
{config['project_name']}/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── {config['package_name'].replace('.', '/')}/
│   │   │       ├── {config['project_name'].replace('-', '').title()}Application.java
│   │   │       ├── controller/
│   │   │       │   └── *.java
│   │   │       ├── service/
│   │   │       │   ├── impl/
│   │   │       │   └── *.java
│   │   │       ├── repository/
│   │   │       │   └── *.java
│   │   │       ├── entity/
│   │   │       │   └── *.java
│   │   │       ├── dto/
│   │   │       │   └── *.java
│   │   │       ├── config/
│   │   │       │   └── *.java
│   │   │       └── exception/
│   │   │           └── *.java
│   │   └── resources/
│   │       ├── application.yml
│   │       ├── application-dev.yml
│   │       ├── application-test.yml
│   │       ├── application-prod.yml
│   │       └── static/
│   └── test/
│       └── java/
│           └── {config['package_name'].replace('.', '/')}/
│               └── *Test.java
├── target/ (Maven) 或 build/ (Gradle)
├── pom.xml (Maven) 或 build.gradle (Gradle)
├── Dockerfile
├── docker-compose.yml
└── README.md
```
"""
        
        if config['is_multi_module'] and config['modules']:
            base_structure += "\n## 多模块结构\n\n"
            base_structure += "项目采用多模块架构，各模块职责如下：\n\n"
            for module in config['modules']:
                base_structure += f"### {module['name']} 模块\n"
                base_structure += f"- **描述**: {module['description']}\n"
                base_structure += f"- **包路径**: {config['package_name']}.{module['name'].replace('-', '')}\n\n"
        
        return base_structure
    
    def _build_execution_plan(self, config):
        """构建执行计划"""
        return f"""# Java项目生成执行计划

> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

本文档定义了Java Spring Boot项目生成的详细执行步骤，确保生成的项目符合配置要求且能正常运行。

## 执行概览

本执行计划包含三个核心步骤：
1. **配置校验与版本兼容性检查** - 确保技术栈版本兼容
2. **项目模板生成** - 基于规范和需求生成项目代码
3. **配置应用与验证** - 应用配置并验证项目可用性

---

## 第一步：配置校验与版本兼容性检查

### 1.1 配置文件解析

**目标**: 读取并验证config.json配置文件的完整性

**执行步骤**:
1. 读取当前目录下的`config.json`文件
2. 验证必要字段是否存在：
   - project_name, package_name, version, description
   - jdk_version, build_tool, spring_boot_version
   - database, orm_framework, cache, message_queue
   - 各种布尔配置项
3. 检查字段值的有效性（非空、格式正确等）

### 1.2 版本兼容性检查

**目标**: 确保所选技术栈版本之间兼容，避免运行时冲突

**关键兼容性规则**:
- Spring Boot 3.x 要求 JDK 17+
- Spring Boot 2.7.x 支持 JDK 8/11/17
- Spring Boot 2.6.x 及以下支持 JDK 8/11
- Maven: 3.6.3+ (推荐 3.8.x)
- Gradle: 7.x+ (推荐 8.x)

**检查项目**:
1. JDK与Spring Boot版本兼容性
2. 数据库与ORM框架兼容性
3. 构建工具版本要求
4. 中间件版本兼容性

### 1.3 版本冲突解决

**执行逻辑**:
1. 如发现版本冲突，输出详细的冲突说明
2. 自动选择兼容的版本组合
3. 记录版本调整的原因和影响
4. 更新配置并继续执行

---

## 第二步：项目模板生成

### 2.1 应用系统提示词规范

**目标**: 根据system_prompt.md中定义的规范生成项目结构

**执行步骤**:
1. 读取`system_prompt.md`文件内容
2. 应用项目生成规范（详见system_prompt.md）

### 2.2 应用用户需求描述

**目标**: 根据user_prompt.md中的具体需求定制项目

**执行步骤**:
1. 读取`user_prompt.md`文件内容
2. 解析用户的具体需求（详见user_prompt.md）

### 2.3 生成项目基础结构

**目标**: 创建符合规范的项目目录结构和基础文件

**生成内容**:
- 构建文件：pom.xml (Maven) 或 build.gradle (Gradle)
- 标准Java包结构（基于config.json中的package_name）
- Spring Boot主类（基于config.json中的project_name）
- 多环境配置文件
- 测试代码结构

### 2.4 集成技术栈组件

**根据config.json配置动态集成**:
- 数据库集成（如果database != '无数据库'）
- ORM框架集成（如果orm_framework != '无ORM'）
- 缓存集成（如果cache != '无缓存'）
- 消息队列集成（如果message_queue != '无消息队列'）
- 附加组件（Swagger、Security、Actuator等）

---

## 第三步：配置应用与验证

### 3.1 配置参数应用

**目标**: 将config.json中的所有配置应用到生成的项目中

**应用范围**:
- 项目基本信息（名称、包名、版本、描述）
- 技术版本配置（JDK、Spring Boot、构建工具）
- 技术栈配置（数据库、ORM、缓存、消息队列）
- 生成选项（示例代码、测试代码、Docker、README等）

### 3.2 项目结构验证

**验证项目**:
1. 目录结构是否正确
2. 包名是否与配置一致
3. 主类名是否正确
4. 配置文件是否完整
5. 依赖是否正确添加

### 3.3 编译和运行验证

**验证步骤**:
1. 检查构建文件语法正确性
2. 验证依赖版本兼容性
3. 确保配置文件格式正确
4. 验证主类能够正常启动
5. 检查测试代码能够正常运行

### 3.4 最终输出

**成功标准**:
- ✅ 项目结构完整且符合规范
- ✅ 所有配置正确应用
- ✅ 项目能够正常编译
- ✅ 应用能够正常启动
- ✅ 测试代码能够正常执行

---

## 执行注意事项

### 错误处理
- 如遇到版本冲突，自动调整并说明原因
- 如配置文件格式错误，提供详细错误信息
- 如依赖下载失败，提供替代方案

### 质量保证
- 生成的代码必须符合Java编码规范
- 所有配置文件必须格式正确
- 项目必须能够直接编译和运行
- 测试覆盖率达到基本要求

### 性能优化
- 使用合理的依赖版本
- 配置适当的连接池大小
- 启用必要的缓存机制
- 优化启动时间

---

## 执行完成标志

当以下所有条件满足时，认为执行计划完成：

1. ✅ 配置校验通过，无版本冲突
2. ✅ 项目结构生成完整
3. ✅ 所有配置正确应用
4. ✅ 项目编译成功
5. ✅ 应用启动正常
6. ✅ 测试执行通过

**最终输出**: 一个完整、可运行的Java Spring Boot项目，符合config.json中的配置要求。
```
src/test/java/{config['package_name'].replace('.', '/')}/
├── {config['project_name'].replace('-', '').title()}ApplicationTests.java
├── controller/
├── service/
└── repository/
```

### 2.4 集成技术栈组件

**数据库集成** (如果 database != '无数据库'):
- 数据库连接配置
- 数据源配置
- 连接池配置

**ORM框架集成** (如果 orm_framework != '无ORM'):
- MyBatis: 配置文件、Mapper接口、XML映射文件
- JPA: Entity注解、Repository接口、配置

**缓存集成** (如果 cache != '无缓存'):
- Redis: 连接配置、序列化配置
- Caffeine: 本地缓存配置

**消息队列集成** (如果 message_queue != '无消息队列'):
- RabbitMQ: 连接配置、队列定义
- Kafka: 生产者和消费者配置

**附加组件**:
- Swagger: API文档配置 (如果 include_swagger = true)
- Security: 安全配置 (如果 include_security = true)
- Actuator: 监控配置 (如果 include_actuator = true)

---

## 第三步：配置应用与验证

### 3.1 配置参数应用

**目标**: 将config.json中的所有配置应用到生成的项目中

**应用项目**:

#### 项目基本信息
- 项目名称: `{config['project_name']}`
- 基础包名: `{config['package_name']}`
- 项目版本: `{config['version']}`
- 项目描述: `{config['description']}`

#### 技术版本配置
- JDK版本: Java {config['jdk_version']}
- 构建工具: {config['build_tool']}
- Spring Boot版本: {config['spring_boot_version']}

#### 技术栈配置
- 数据库: {config['database']}
- ORM框架: {config['orm_framework']}
- 缓存: {config['cache']}
- 消息队列: {config['message_queue']}

#### 生成选项
- 示例代码: {'是' if config['generate_sample_code'] else '否'}
- 测试代码: {'是' if config['generate_tests'] else '否'}
- Docker配置: {'是' if config['generate_docker'] else '否'}
- README文档: {'是' if config['generate_readme'] else '否'}

### 3.2 项目结构验证

**目标**: 确保生成的项目结构符合配置要求

**验证项目**:
1. 目录结构是否正确
2. 包名是否与配置一致
3. 主类名是否正确
4. 配置文件是否完整
5. 依赖是否正确添加

### 3.3 编译和运行验证

**目标**: 验证生成的项目能够正常编译和启动

**验证步骤**:
1. 检查构建文件语法正确性
2. 验证依赖版本兼容性
3. 确保配置文件格式正确
4. 验证主类能够正常启动
5. 检查测试代码能够正常运行

### 3.4 最终输出

**成功标准**:
- ✅ 项目结构完整且符合规范
- ✅ 所有配置正确应用
- ✅ 项目能够正常编译
- ✅ 应用能够正常启动
- ✅ 测试代码能够正常执行

**输出内容**:
1. 完整的项目源代码
2. 构建和配置文件
3. 测试代码
4. Docker配置 (如果启用)
5. README文档 (如果启用)
6. 项目运行说明

---

## 执行注意事项

### 错误处理
- 如遇到版本冲突，自动调整并说明原因
- 如配置文件格式错误，提供详细错误信息
- 如依赖下载失败，提供替代方案

### 质量保证
- 生成的代码必须符合Java编码规范
- 所有配置文件必须格式正确
- 项目必须能够直接编译和运行
- 测试覆盖率达到基本要求

### 性能优化
- 使用合理的依赖版本
- 配置适当的连接池大小
- 启用必要的缓存机制
- 优化启动时间

---

## 执行完成标志

当以下所有条件满足时，认为执行计划完成：

1. ✅ 配置校验通过，无版本冲突
2. ✅ 项目结构生成完整
3. ✅ 所有配置正确应用
4. ✅ 项目编译成功
5. ✅ 应用启动正常
6. ✅ 测试执行通过

**最终输出**: 一个完整、可运行的Java Spring Boot项目，符合用户配置要求。
"""
    
    def _build_readme(self, config):
        """构建README文件内容"""
        return f"""# {config['project_name']} 上下文工程

> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

这是一个用于生成 **{config['project_name']}** Java Spring Boot项目的上下文工程。

## 项目配置概览

### 基本信息
- **项目名称**: {config['project_name']}
- **基础包名**: {config['package_name']}
- **项目版本**: {config['version']}
- **项目描述**: {config['description']}

### 技术栈
- **JDK版本**: Java {config['jdk_version']}
- **构建工具**: {config['build_tool']}
- **Spring Boot版本**: {config['spring_boot_version']}
- **数据库**: {config['database']}
- **ORM框架**: {config['orm_framework']}
- **缓存**: {config['cache']}
- **消息队列**: {config['message_queue']}

### 附加组件
- **API文档**: {'✅ Swagger' if config['include_swagger'] else '❌'}
- **安全框架**: {'✅ Spring Security' if config['include_security'] else '❌'}
- **监控组件**: {'✅ Spring Boot Actuator' if config['include_actuator'] else '❌'}

## 文件说明

### 核心文件
- `config.json` - 项目配置文件
- `system_prompt.md` - 系统提示词（AI生成规范）
- `user_prompt.md` - 用户提示词（具体需求描述）
- `project_structure.md` - 项目结构说明

### Gemini CLI 支持
- `project_generator.gemini` - Gemini斜杠命令文件

## 使用方法

### 方法一：使用Gemini CLI

1. 安装Gemini CLI工具
2. 执行命令：
   ```bash
   gemini run project_generator.gemini
   ```

### 方法二：手动使用提示词

1. 复制 `system_prompt.md` 的内容作为系统提示词
2. 复制 `user_prompt.md` 的内容作为用户输入
3. 在支持的AI工具中执行生成

### 方法三：API调用

使用配置文件 `config.json` 通过编程方式调用AI API生成项目。

## 生成的项目特性

- ✅ 标准的Spring Boot项目结构
- ✅ 完整的分层架构设计
- ✅ 多环境配置支持
- ✅ 数据库集成和ORM配置
- ✅ 缓存和消息队列集成
- ✅ API文档和监控配置
- ✅ 安全认证和授权
- ✅ 完整的测试代码
- ✅ Docker容器化支持
- ✅ 详细的项目文档

## 注意事项

1. 确保目标环境已安装对应版本的JDK
2. 根据选择的数据库准备相应的数据库环境
3. 如使用Redis、消息队列等中间件，请提前准备环境
4. 生成的项目可直接编译和运行

## 技术支持

如有问题，请检查：
1. 配置文件格式是否正确
2. 技术版本兼容性
3. 环境依赖是否满足

---

*此上下文工程由AI项目生成器自动创建*
"""
    
    def _build_claude_commands(self, config):
        """构建Claude Code斜杠命令"""
        return f"""# Claude Code 项目生成器斜杠命令

## 系统提示词设置
/system
请查看 system_prompt.md 文件获取完整的系统提示词。你是一个专业的Java项目架构师和开发专家，擅长创建高质量的Spring Boot项目。请根据config.json配置文件中的要求，生成一个完整的Java项目。

## 用户需求设置
/user
请查看 user_prompt.md 文件获取完整的用户提示词。请根据config.json配置文件生成一个完整的Java Spring Boot项目。

🚨 重要项目创建位置要求：
1. **必须首先创建一个新的项目文件夹，文件夹名称为config.json中的project_name值**
2. **然后在该文件夹内创建所有项目文件（src、pom.xml等）**
3. **绝对不允许在当前工作目录直接创建src、pom.xml等项目文件**
4. **项目结构应为：{project_name}/src/main/java/... 而不是 src/main/java/...**
5. 所有项目配置信息请从config.json文件中动态读取
6. 当generate_sample_code=true时，请生成完整的示例代码

## 执行计划查看
/plan
请查看 execution_plan.md 文件获取详细的项目生成执行计划，包含配置校验、项目模板生成、配置应用与验证三个核心步骤。

## 项目结构说明
/structure
请查看 project_structure.md 文件了解标准的Java Spring Boot项目结构和最佳实践。

## 配置文件查看
/config
请查看 config.json 文件了解项目的具体配置要求，包括技术栈版本、组件选择、生成选项等。

## 项目生成命令
/generate
根据 config.json 文件中的配置生成完整的Java Spring Boot项目。

执行步骤：
1. 读取并解析 config.json 配置文件
2. 根据配置创建标准的项目结构
3. 生成所有必要的源代码文件
4. 配置构建文件和依赖管理
5. 创建配置文件和环境设置
6. 生成测试代码和文档
7. 提供Docker配置和部署说明

## 快速开始
/start
一键生成项目的快速命令：
1. 首先执行 /config 查看配置
2. 然后执行 /generate 生成项目
3. 最后检查生成的项目结构和文件

## 帮助信息
/help
显示所有可用的斜杠命令和使用说明：

- `/system` - 设置系统提示词
- `/user` - 设置用户需求
- `/plan` - 查看执行计划
- `/structure` - 查看项目结构说明
- `/config` - 查看配置文件
- `/generate` - 生成完整项目
- `/start` - 快速开始生成
- `/help` - 显示帮助信息

## 使用说明

### 在Claude Code中使用
1. 打开Claude Code编辑器
2. 加载此 .claude 文件
3. 确保同目录下有以下文件：
   - config.json (项目配置)
   - system_prompt.md (系统提示词)
   - user_prompt.md (用户提示词)
   - execution_plan.md (执行计划)
   - project_structure.md (项目结构说明)
4. 使用上述斜杠命令进行项目生成

### 推荐工作流
1. `/config` - 确认项目配置
2. `/system` - 加载系统提示词
3. `/user` - 加载用户需求
4. `/generate` - 生成完整项目

### 注意事项
- 所有配置信息都从 config.json 文件中动态读取
- 生成的项目将严格按照配置要求创建
- 确保配置文件格式正确且完整
- 生成的项目可直接编译和运行

---

*Claude Code 斜杠命令文件 - 支持在Claude Code中直接使用命令生成Java Spring Boot项目*
"""