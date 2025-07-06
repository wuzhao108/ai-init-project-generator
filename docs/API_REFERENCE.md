# 📚 API 参考文档

## 🔧 核心模块 API

### ConfigManager 类

配置文件管理的核心类，提供配置的增删改查功能。

#### 方法列表

##### `save_config(name: str, config: dict) -> bool`

保存配置文件到本地存储。

**参数:**
- `name` (str): 配置文件名称
- `config` (dict): 配置数据字典

**返回值:**
- `bool`: 保存成功返回 True，失败返回 False

**示例:**
```python
config_manager = ConfigManager()
config_data = {
    "name": "my-project",
    "package": "com.example.myproject",
    "tech_stack": {
        "database": "mysql",
        "orm": "mybatis"
    }
}
result = config_manager.save_config("my-config", config_data)
```

##### `load_config(name: str) -> dict`

加载指定名称的配置文件。

**参数:**
- `name` (str): 配置文件名称

**返回值:**
- `dict`: 配置数据字典，如果文件不存在返回空字典

**异常:**
- `FileNotFoundError`: 配置文件不存在
- `json.JSONDecodeError`: 配置文件格式错误

**示例:**
```python
config = config_manager.load_config("my-config")
print(config["name"])  # 输出: my-project
```

##### `list_configs() -> List[str]`

列出所有已保存的配置文件名称。

**返回值:**
- `List[str]`: 配置文件名称列表

**示例:**
```python
configs = config_manager.list_configs()
for config_name in configs:
    print(f"配置: {config_name}")
```

##### `delete_config(name: str) -> bool`

删除指定的配置文件。

**参数:**
- `name` (str): 要删除的配置文件名称

**返回值:**
- `bool`: 删除成功返回 True，失败返回 False

**示例:**
```python
result = config_manager.delete_config("old-config")
if result:
    print("配置删除成功")
```

##### `config_exists(name: str) -> bool`

检查指定名称的配置文件是否存在。

**参数:**
- `name` (str): 配置文件名称

**返回值:**
- `bool`: 存在返回 True，不存在返回 False

##### `export_config(name: str, export_path: str) -> bool`

导出配置文件到指定路径。

**参数:**
- `name` (str): 要导出的配置文件名称
- `export_path` (str): 导出文件路径

**返回值:**
- `bool`: 导出成功返回 True，失败返回 False

##### `import_config(file_path: str, config_name: str = None) -> bool`

从文件导入配置。

**参数:**
- `file_path` (str): 要导入的配置文件路径
- `config_name` (str, 可选): 导入后的配置名称，默认使用文件名

**返回值:**
- `bool`: 导入成功返回 True，失败返回 False

##### `get_config_info(name: str) -> dict`

获取配置文件的详细信息。

**参数:**
- `name` (str): 配置文件名称

**返回值:**
- `dict`: 包含配置详细信息的字典

**返回字典结构:**
```python
{
    "name": "配置名称",
    "description": "配置描述",
    "java_version": "Java版本",
    "spring_boot_version": "Spring Boot版本",
    "project_type": "项目类型",
    "tech_stack": "技术栈信息",
    "created_at": "创建时间",
    "file_size": "文件大小"
}
```

### ProjectGenerator 类

项目生成的核心类，负责根据配置生成 Spring Boot 项目。

#### 方法列表

##### `__init__(config: dict, output_dir: str = "./output")`

初始化项目生成器。

**参数:**
- `config` (dict): 项目配置字典
- `output_dir` (str): 输出目录路径，默认为 "./output"

##### `generate() -> bool`

生成完整的 Spring Boot 项目。

**返回值:**
- `bool`: 生成成功返回 True，失败返回 False

**生成流程:**
1. 创建项目目录结构
2. 生成 Maven 配置文件 (pom.xml)
3. 生成 Java 源代码
4. 生成配置文件
5. 生成测试代码
6. 生成 Docker 配置
7. 生成文档文件

**示例:**
```python
config = {
    "name": "my-project",
    "package": "com.example.myproject",
    "tech_stack": {
        "database": "mysql",
        "orm": "mybatis"
    }
}

generator = ProjectGenerator(config, "./output")
result = generator.generate()
if result:
    print("项目生成成功")
```

##### `generate_pom() -> None`

生成 Maven POM 文件。

**功能:**
- 根据技术栈配置添加相应依赖
- 设置项目基本信息
- 配置构建插件

##### `generate_application_class() -> None`

生成 Spring Boot 主启动类。

**生成内容:**
- @SpringBootApplication 注解
- main 方法
- 根据配置添加其他注解

##### `generate_config_files() -> None`

生成应用配置文件。

**生成文件:**
- `application.yml` - 主配置文件
- `application-dev.yml` - 开发环境配置
- `application-test.yml` - 测试环境配置
- `application-prod.yml` - 生产环境配置
- `logback-spring.xml` - 日志配置

##### `generate_sample_code() -> None`

生成示例代码。

**生成内容:**
- Controller 示例
- Service 示例
- Repository 示例
- Entity 示例
- DTO 示例

##### `generate_tests() -> None`

生成测试代码。

**生成内容:**
- 单元测试
- 集成测试
- 测试配置

##### `generate_docker_files() -> None`

生成 Docker 相关文件。

**生成文件:**
- `Dockerfile` - Docker 镜像构建文件
- `docker-compose.yml` - Docker Compose 配置
- `docker-compose-dev.yml` - 开发环境 Docker 配置
- `.dockerignore` - Docker 忽略文件

### InteractiveConfig 类

交互式配置收集类，提供用户友好的配置界面。

#### 方法列表

##### `collect_config() -> dict`

通过交互式界面收集项目配置。

**返回值:**
- `dict`: 完整的项目配置字典

**收集流程:**
1. 基本项目信息
2. Java 和 Spring Boot 版本
3. 项目类型选择
4. 数据库配置
5. ORM 框架选择
6. 缓存配置
7. 消息队列配置
8. 其他技术栈选择

##### `collect_basic_info() -> dict`

收集项目基本信息。

**收集内容:**
- 项目名称
- 基础包名
- 项目描述
- 项目版本

##### `collect_tech_stack() -> dict`

收集技术栈配置。

**收集内容:**
- 数据库类型
- ORM 框架
- 缓存组件
- 消息队列
- 文档工具
- 安全框架
- 监控工具

## 🔧 配置文件格式

### 完整配置文件结构

```json
{
  "name": "项目名称",
  "package": "基础包名",
  "version": "项目版本",
  "description": "项目描述",
  "java_version": "Java版本",
  "spring_boot_version": "Spring Boot版本",
  "project_type": "项目类型",
  "multi_module": false,
  "modules": [],
  "tech_stack": {
    "database": "数据库类型",
    "orm": "ORM框架",
    "cache": ["缓存组件列表"],
    "mq": ["消息队列列表"],
    "doc": true,
    "security": true,
    "mongodb": false,
    "elasticsearch": false,
    "web_framework": "Web框架",
    "actuator": true,
    "test_framework": ["测试框架列表"]
  },
  "output_dir": "输出目录",
  "generate_sample_code": true,
  "generate_tests": true,
  "generate_docker": true,
  "created_at": "创建时间",
  "updated_at": "更新时间"
}
```

### 技术栈配置选项

#### 数据库 (database)

| 值 | 描述 | 依赖 |
|---|---|---|
| `mysql` | MySQL 数据库 | mysql-connector-java |
| `postgresql` | PostgreSQL 数据库 | postgresql |
| `h2` | H2 内存数据库 | h2 |
| `oracle` | Oracle 数据库 | ojdbc8 |
| `sqlserver` | SQL Server 数据库 | mssql-jdbc |

#### ORM 框架 (orm)

| 值 | 描述 | 依赖 |
|---|---|---|
| `mybatis` | MyBatis 框架 | mybatis-spring-boot-starter |
| `mybatis-plus` | MyBatis-Plus 框架 | mybatis-plus-boot-starter |
| `jpa` | Spring Data JPA | spring-boot-starter-data-jpa |

#### 缓存 (cache)

| 值 | 描述 | 依赖 |
|---|---|---|
| `redis` | Redis 缓存 | spring-boot-starter-data-redis |
| `caffeine` | Caffeine 本地缓存 | caffeine |
| `ehcache` | Ehcache 缓存 | ehcache |

#### 消息队列 (mq)

| 值 | 描述 | 依赖 |
|---|---|---|
| `rabbitmq` | RabbitMQ | spring-boot-starter-amqp |
| `kafka` | Apache Kafka | spring-kafka |
| `rocketmq` | Apache RocketMQ | rocketmq-spring-boot-starter |
| `activemq` | Apache ActiveMQ | spring-boot-starter-activemq |

## 🛠️ 命令行接口

### 主程序参数

```bash
python main.py [OPTIONS]
```

#### 选项说明

| 参数 | 描述 | 默认值 |
|---|---|---|
| `--config` | 指定配置文件路径 | 无 |
| `--output` | 指定输出目录 | `./output` |
| `--template` | 使用指定模板 | `default` |
| `--interactive` | 启用交互模式 | `True` |
| `--help` | 显示帮助信息 | - |
| `--version` | 显示版本信息 | - |

#### 使用示例

```bash
# 交互式创建项目
python main.py

# 使用配置文件创建项目
python main.py --config my-config.json --output ./my-project

# 使用默认模板创建项目
python main.py --template default --output ./default-project

# 显示帮助信息
python main.py --help
```

## 🔌 扩展接口

### 自定义模板

#### 模板文件结构

```
templates/
├── custom-template/
│   ├── config.json              # 模板配置
│   ├── pom.xml.j2              # Maven POM 模板
│   ├── src/
│   │   └── main/
│   │       ├── java/
│   │       │   └── Application.java.j2
│   │       └── resources/
│   │           └── application.yml.j2
│   └── docker/
│       └── Dockerfile.j2
```

#### 模板配置文件

```json
{
  "name": "自定义模板",
  "description": "模板描述",
  "version": "1.0.0",
  "author": "作者",
  "tags": ["web", "api"],
  "requirements": {
    "java_version": ">=11",
    "spring_boot_version": ">=2.7.0"
  },
  "default_config": {
    "tech_stack": {
      "database": "mysql",
      "orm": "mybatis"
    }
  }
}
```

### 自定义生成器

#### 继承 ProjectGenerator

```python
from spring_init.generator import ProjectGenerator

class CustomProjectGenerator(ProjectGenerator):
    
    def __init__(self, config, output_dir):
        super().__init__(config, output_dir)
    
    def generate_custom_files(self):
        """生成自定义文件"""
        # 自定义生成逻辑
        pass
    
    def generate(self):
        """重写生成方法"""
        # 调用父类方法
        super().generate()
        
        # 添加自定义生成逻辑
        self.generate_custom_files()
        
        return True
```

### 插件系统

#### 插件接口

```python
from abc import ABC, abstractmethod

class GeneratorPlugin(ABC):
    
    @abstractmethod
    def get_name(self) -> str:
        """获取插件名称"""
        pass
    
    @abstractmethod
    def get_version(self) -> str:
        """获取插件版本"""
        pass
    
    @abstractmethod
    def generate(self, config: dict, output_dir: str) -> bool:
        """执行生成逻辑"""
        pass
    
    @abstractmethod
    def validate_config(self, config: dict) -> bool:
        """验证配置"""
        pass
```

#### 插件示例

```python
class SwaggerPlugin(GeneratorPlugin):
    
    def get_name(self) -> str:
        return "swagger-plugin"
    
    def get_version(self) -> str:
        return "1.0.0"
    
    def generate(self, config: dict, output_dir: str) -> bool:
        if config.get("tech_stack", {}).get("doc"):
            # 生成 Swagger 配置
            self._generate_swagger_config(config, output_dir)
            return True
        return False
    
    def validate_config(self, config: dict) -> bool:
        # 验证配置是否支持 Swagger
        return True
    
    def _generate_swagger_config(self, config, output_dir):
        # 具体的 Swagger 配置生成逻辑
        pass
```

## 🧪 测试接口

### 单元测试

```python
import unittest
from spring_init.config_manager import ConfigManager

class TestConfigManager(unittest.TestCase):
    
    def setUp(self):
        self.config_manager = ConfigManager()
        self.test_config = {
            "name": "test-project",
            "package": "com.example.test"
        }
    
    def test_save_config(self):
        result = self.config_manager.save_config("test", self.test_config)
        self.assertTrue(result)
    
    def test_load_config(self):
        self.config_manager.save_config("test", self.test_config)
        loaded_config = self.config_manager.load_config("test")
        self.assertEqual(loaded_config["name"], "test-project")
    
    def tearDown(self):
        # 清理测试数据
        if self.config_manager.config_exists("test"):
            self.config_manager.delete_config("test")
```

### 集成测试

```python
import tempfile
import shutil
from spring_init.generator import ProjectGenerator

class TestProjectGeneration(unittest.TestCase):
    
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.config = {
            "name": "test-project",
            "package": "com.example.test",
            "tech_stack": {
                "database": "h2",
                "orm": "jpa"
            }
        }
    
    def test_generate_project(self):
        generator = ProjectGenerator(self.config, self.temp_dir)
        result = generator.generate()
        self.assertTrue(result)
        
        # 验证生成的文件
        project_dir = os.path.join(self.temp_dir, "test-project")
        self.assertTrue(os.path.exists(project_dir))
        self.assertTrue(os.path.exists(os.path.join(project_dir, "pom.xml")))
    
    def tearDown(self):
        shutil.rmtree(self.temp_dir)
```

---

📝 **API 版本**: v1.0.0  
📅 **最后更新**: 2024-01-01  
🔧 **兼容性**: Python 3.6+