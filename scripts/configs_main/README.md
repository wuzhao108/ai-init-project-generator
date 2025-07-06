# 配置管理系统 V2

本文档介绍了Spring Boot项目生成器的新配置管理系统，该系统将配置分为三个层次：系统配置、模板配置和历史配置。

## 目录结构

```
configs/
├── system/                 # 系统级配置
│   └── system.json        # 系统配置文件
├── templates/             # 模板配置（Markdown格式）
│   ├── spring-boot-basic.md
│   ├── spring-boot-microservice.md
│   └── spring-boot-web.md
├── history/               # 历史配置（Markdown格式）
│   ├── my-project-20240101-120000.md
│   └── another-project-20240102-130000.md
└── backup/                # 备份目录
    └── 20250706_100856/   # 迁移备份
        ├── migration_report.md
        └── *.json         # 原始JSON配置文件
```

## 配置类型说明

### 1. 系统配置 (system/system.json)

存储与系统运行相关的配置，包括：
- 应用基本信息（名称、版本、描述）
- 输出目录配置
- 模板路径配置
- 日志配置
- 生成器参数
- UI设置
- 验证规则

**示例：**
```json
{
  "version": "1.0.0",
  "app_name": "Spring Boot Project Generator",
  "description": "AI驱动的Spring Boot项目生成器",
  "output": {
    "default_dir": "./output",
    "backup_dir": "./backup",
    "temp_dir": "./temp"
  },
  "logging": {
    "level": "INFO",
    "file": "./logs/generator.log"
  }
}
```

### 2. 模板配置 (templates/*.md)

存储项目模板的默认配置，以Markdown格式提供更好的可读性：
- 模板元数据（名称、版本、作者、描述）
- 项目基础配置
- 技术栈配置
- 代码生成选项
- 使用说明

**示例：**
```markdown
# Spring Boot 基础模板配置

## 模板信息

- **模板名称**: Spring Boot 基础模板
- **模板ID**: `spring-boot-basic`
- **版本**: `1.0.0`
- **描述**: 适用于单体应用的基础Spring Boot项目模板

## 项目配置

```yaml
project:
  name: my-spring-boot-app
  package_name: com.example.app
  version: 1.0.0
  java_version: "17"
  spring_boot_version: "3.2.0"

tech_stack:
  database: h2
  orm: jpa
  cache: none
  security: false
```
```

### 3. 历史配置 (history/*.md)

存储用户每次创建项目时的配置记录，包括：
- 项目基本信息
- 完整的配置详情
- 业务需求描述
- 技术选型说明
- 配置变更记录

**命名规则：** `{项目名称}-{时间戳}.md`

## 使用方法

### 1. 使用配置管理器 (Python API)

```python
from configs.config_manager_v2 import ConfigManagerV2

# 创建配置管理器
manager = ConfigManagerV2()

# 系统配置操作
system_config = manager.load_system_config()
manager.save_system_config(system_config)

# 模板配置操作
templates = manager.list_templates()
template_config = manager.load_template_config('spring-boot-basic')

# 历史配置操作
histories = manager.list_history_configs()
history_config = manager.load_history_config('my-project-20240101-120000')

# 保存新的历史配置
config_id = manager.save_history_config(
    project_name='my-new-project',
    config=project_config,
    metadata={
        'creator': 'developer',
        'project_type': '单体应用',
        'template_id': 'spring-boot-basic'
    }
)
```

### 2. 使用命令行工具 (CLI)

```bash
# 查看系统配置
python common/config/config_cli.py system show

# 列出所有模板
python common/config/config_cli.py template list

# 查看模板详情
python common/config/config_cli.py template show spring-boot-basic

# 列出历史配置
python common/config/config_cli.py history list

# 搜索配置
python common/config/config_cli.py search "spring boot"

# 导出配置
python common/config/config_cli.py export spring-boot-basic template --output ./my-template.md

# 清理历史配置（删除30天前的配置）
python common/config/config_cli.py history cleanup --days 30
```

### 3. 配置迁移

如果你有旧的JSON格式配置文件，可以使用迁移工具：

```bash
# 执行配置迁移
python common/config/config_migrator.py

# 或使用CLI
python common/config/config_cli.py migrate run
```

迁移工具会：
1. 备份原有的JSON配置文件
2. 将模板配置转换为Markdown格式
3. 将项目配置转换为历史配置
4. 生成迁移报告

## 配置管理最佳实践

### 1. 模板配置管理

- **版本控制**: 模板配置应纳入版本控制系统
- **命名规范**: 使用清晰的模板ID，如 `spring-boot-{类型}`
- **文档完整**: 在Markdown中提供详细的使用说明
- **定期更新**: 根据技术栈更新及时更新模板配置

### 2. 历史配置管理

- **定期清理**: 使用CLI工具定期清理过期的历史配置
- **备份重要配置**: 对重要项目的配置进行额外备份
- **配置复用**: 可以基于历史配置创建新的模板

### 3. 系统配置管理

- **环境隔离**: 不同环境使用不同的系统配置
- **安全考虑**: 敏感配置信息应加密存储
- **监控告警**: 对配置变更进行监控和告警

## 配置架构优势

### 1. 可读性提升
- Markdown格式提供更好的可读性
- 支持富文本格式，可以包含说明文档
- 便于团队协作和知识传承

### 2. 管理便利性
- 分层管理，职责清晰
- 支持版本控制
- 提供完整的CLI工具

### 3. 扩展性
- 易于添加新的配置类型
- 支持自定义配置验证
- 可以集成到CI/CD流程

### 4. 维护性
- 配置变更可追溯
- 支持配置导入导出
- 提供迁移和回滚机制

## 故障排除

### 常见问题

1. **配置文件损坏**
   - 检查备份目录中的文件
   - 使用迁移工具重新生成配置

2. **模板加载失败**
   - 检查模板文件的YAML语法
   - 验证模板ID是否正确

3. **历史配置过多**
   - 使用清理命令删除过期配置
   - 考虑增加自动清理策略

### 日志查看

系统日志位置：`./logs/generator.log`

可以通过修改系统配置中的日志级别来获取更详细的调试信息。

## 开发指南

如果需要扩展配置管理系统，请参考：

1. **添加新的配置类型**：继承 `ConfigManagerV2` 类
2. **自定义验证规则**：实现配置验证接口
3. **集成外部系统**：使用配置管理器的API接口

## 更新日志

- **v2.0.0** (2025-01-06)
  - 重构配置架构，分为系统、模板、历史三层
  - 模板和历史配置改用Markdown格式
  - 提供完整的CLI工具
  - 支持配置迁移和回滚

- **v1.0.0** (2024-01-01)
  - 初始版本，使用JSON格式配置