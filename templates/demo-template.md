# 演示模板配置

## 模板信息

- **模板名称**: 演示模板
- **模板ID**: `demo-template`
- **版本**: `1.0.0`
- **描述**: 用于演示的Spring Boot项目模板
- **创建时间**: 2025-07-06
- **更新时间**: 2025-07-06
- **作者**: Demo User

## 项目配置

```yaml
generation:
  generate_docker: true
  generate_examples: true
  generate_tests: true
  output_dir: ./output
project:
  description: 演示应用
  java_version: '17'
  name: demo-app
  package_name: com.example.demo
  spring_boot_version: 3.2.0
  version: 1.0.0
tech_stack:
  cache: redis
  database: mysql
  documentation: true
  mq: rabbitmq
  orm: jpa
  security: true
  testing: junit5
  web_framework: spring-mvc

```

## 使用说明

请根据实际需求调整配置参数。
