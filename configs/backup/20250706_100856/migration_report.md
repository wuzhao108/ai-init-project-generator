# 配置迁移报告

## 迁移概览

- **迁移时间**: 2025-07-06 10:08:56
- **迁移状态**: 成功
- **备份路径**: `configs\backup\20250706_100856`

## 模板配置迁移

| 源文件 | 模板ID | 状态 | 错误信息 |
|--------|--------|------|----------|
| default_template.json | spring-boot-basic | success |  |
| template.json | spring-boot-web | success |  |

## 历史配置迁移

| 源文件 | 配置ID | 状态 | 错误信息 |
|--------|--------|------|----------|
| my-spring-boot-project.json | my-spring-boot-project-20250706-100856 | success |  |
| sdafld;kj.json | sdafld;kj-20250706-100856 | success |  |

## 迁移后目录结构

```
configs/
├── system/
│   └── system.json
├── templates/
│   ├── spring-boot-basic.md
│   ├── spring-boot-microservice.md
│   └── spring-boot-web.md
└── history/
    ├── project1-20240101-120000.md
    └── project2-20240102-130000.md
```

## 使用新配置管理器

```python
from common.config.config_manager_v2 import ConfigManagerV2

# 创建配置管理器
manager = ConfigManagerV2()

# 加载系统配置
system_config = manager.load_system_config()

# 列出模板
templates = manager.list_templates()

# 列出历史配置
histories = manager.list_history_configs()
```
