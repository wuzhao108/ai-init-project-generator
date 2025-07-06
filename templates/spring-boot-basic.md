# Spring Boot 基础模板配置

## 模板信息

- **模板名称**: Spring Boot 基础模板
- **模板ID**: `spring-boot-basic`
- **版本**: `1.0.0`
- **描述**: 适用于单体应用的基础Spring Boot项目模板
- **创建时间**: 2025-07-06
- **更新时间**: 2025-07-06
- **作者**: AI Project Generator

## 项目配置

```yaml
generation:
  generate_docker: true
  generate_examples: true
  generate_tests: true
  output_dir: ./output
modules: []
project:
  description: 基于默认模板的Spring Boot项目
  java_version: '11'
  multi_module: false
  name: ''
  package_name: ''
  spring_boot_version: 3.2.0
  version: 1.0.0
tech_stack:
  cache:
  - redis
  database: mysql
  documentation: true
  monitoring:
    actuator: true
  mq: []
  nosql:
    elasticsearch: false
    mongodb: false
  orm: mybatis
  security: false
  testing: junit5
  web_framework: spring-web

```

## 使用说明

请根据实际需求调整配置参数。
