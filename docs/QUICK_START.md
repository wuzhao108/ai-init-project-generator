# 🚀 快速开始指南

## 5分钟上手 AI Spring Boot 项目生成器

### 📋 前置要求

- Python 3.6+
- pip 包管理器

### 🎯 第一步：安装和运行

```bash
# 1. 克隆项目
git clone <repository-url>
cd ai-init-project-generator

# 2. 安装依赖
pip install -r requirements.txt

# 3. 启动程序
python main.py
```

### 🆕 第二步：创建你的第一个项目

1. **选择创建项目**
   ```
   📋 请选择操作:
   1. 🆕 创建项目模板  ← 选择这个
   ```

2. **选择创建方式**
   ```
   请选择创建方式:
   1. 📋 使用默认模板创建  ← 推荐新手选择
   2. ⚙️ 自定义配置创建
   ```

3. **查看并确认配置**
   - 系统会显示默认配置详情
   - 确认后开始生成项目

4. **项目生成完成**
   ```
   ✅ 项目生成完成！
   📁 项目路径: ./output/my-spring-project
   ```

### 🏃‍♂️ 第三步：运行生成的项目

```bash
# 1. 进入项目目录
cd output/my-spring-project

# 2. 启动项目
mvn spring-boot:run

# 3. 验证项目运行
curl http://localhost:8080/actuator/health
# 或在浏览器访问: http://localhost:8080/swagger-ui.html
```

### 🎉 恭喜！

你已经成功创建并运行了第一个 Spring Boot 项目！

## 🔄 下一步操作

### 保存配置模板

如果你对生成的项目满意，可以保存配置以便重复使用：

1. 在主菜单选择 "6. 📤 导出配置文件"
2. 选择要导出的配置
3. 指定保存路径

### 自定义项目配置

尝试创建自定义配置的项目：

1. 选择 "1. 🆕 创建项目模板"
2. 选择 "2. ⚙️ 自定义配置创建"
3. 按提示输入项目信息和技术栈选择

### 管理配置文件

- **查看配置**: 选择 "3. 📋 查看已保存的配置"
- **查看详情**: 选择 "4. 📄 查看配置详情"
- **删除配置**: 选择 "5. 🗑️ 删除配置文件"
- **导入配置**: 选择 "7. 📥 导入配置文件"

## 🛠️ 常用技术栈组合

### Web API 项目
```
数据库: MySQL
ORM: MyBatis
缓存: Redis
文档: Swagger
安全: Spring Security
```

### 微服务项目
```
数据库: PostgreSQL
ORM: JPA
缓存: Redis
消息队列: RabbitMQ
监控: Actuator
```

### 数据处理项目
```
数据库: MongoDB
搜索: Elasticsearch
缓存: Redis
消息队列: Kafka
```

## 🆘 遇到问题？

### 常见问题

1. **Python 版本问题**
   ```bash
   python --version  # 确保是 3.6+
   ```

2. **依赖安装失败**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **项目启动失败**
   - 检查 Java 版本 (需要 Java 8+)
   - 检查 Maven 版本 (需要 Maven 3.6+)

### 获取帮助

- 📖 查看完整文档: `docs/README.md`
- 🐛 报告问题: GitHub Issues
- 💬 社区讨论: GitHub Discussions

---

🎯 **目标**: 5分钟内创建并运行你的第一个 Spring Boot 项目！