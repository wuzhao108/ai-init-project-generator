# 🔧 故障排除指南

## 🚨 常见问题解决方案

### 安装和环境问题

#### 问题 1: Python 版本不兼容

**错误信息:**
```
SyntaxError: invalid syntax
```
或
```
ModuleNotFoundError: No module named 'dataclasses'
```

**原因:** Python 版本过低，需要 Python 3.6 或更高版本。

**解决方案:**
```bash
# 检查 Python 版本
python --version
# 或
python3 --version

# 如果版本低于 3.6，请升级 Python
# Windows: 从 python.org 下载最新版本
# macOS: brew install python3
# Ubuntu: sudo apt update && sudo apt install python3.8
```

#### 问题 2: 依赖包安装失败

**错误信息:**
```
ERROR: Could not install packages due to an EnvironmentError
```

**解决方案:**
```bash
# 升级 pip
pip install --upgrade pip

# 使用国内镜像源
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

# 如果权限问题，使用用户安装
pip install --user -r requirements.txt

# 使用虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

#### 问题 3: 模块导入错误

**错误信息:**
```
ModuleNotFoundError: No module named 'spring_init'
```

**原因:** 没有正确设置 Python 路径或没有在项目根目录运行。

**解决方案:**
```bash
# 确保在项目根目录
cd ai-init-project-generator

# 设置 PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$(pwd)  # Linux/Mac
set PYTHONPATH=%PYTHONPATH%;%cd%      # Windows

# 或者安装为开发包
pip install -e .
```

### 配置文件问题

#### 问题 4: 配置文件格式错误

**错误信息:**
```
json.decoder.JSONDecodeError: Expecting ',' delimiter
```

**原因:** JSON 格式不正确。

**解决方案:**
1. 使用 JSON 验证工具检查格式
2. 确保所有字符串使用双引号
3. 确保最后一个元素后没有逗号
4. 检查括号匹配

**正确的 JSON 格式:**
```json
{
  "name": "my-project",
  "package": "com.example.myproject",
  "tech_stack": {
    "database": "mysql",
    "orm": "mybatis"
  }
}
```

#### 问题 5: 配置文件权限问题

**错误信息:**
```
PermissionError: [Errno 13] Permission denied
```

**解决方案:**
```bash
# 检查文件权限
ls -la configs/

# 修改权限
chmod 644 configs/*.json

# 检查目录权限
chmod 755 configs/

# Windows 下检查文件属性，取消只读属性
```

### 项目生成问题

#### 问题 6: 输出目录创建失败

**错误信息:**
```
OSError: [Errno 2] No such file or directory
```

**原因:** 输出路径不存在或权限不足。

**解决方案:**
```bash
# 创建输出目录
mkdir -p output

# 检查权限
ls -la output/

# 修改权限
chmod 755 output/

# 使用绝对路径
python main.py --output /absolute/path/to/output
```

#### 问题 7: 模板文件缺失

**错误信息:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'templates/...'
```

**原因:** 模板文件不完整或路径错误。

**解决方案:**
```bash
# 检查模板文件是否存在
ls -la spring_init/templates/

# 重新克隆项目
git clone <repository-url>

# 检查 Git 状态
git status
git pull origin main
```

#### 问题 8: 生成的项目无法编译

**错误信息:**
```
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-compiler-plugin
```

**原因:** Java 版本不匹配或依赖冲突。

**解决方案:**
```bash
# 检查 Java 版本
java -version
javac -version

# 检查 Maven 版本
mvn -version

# 清理并重新编译
cd generated-project
mvn clean compile

# 如果依赖问题，更新依赖
mvn dependency:resolve
mvn dependency:tree
```

### 运行时问题

#### 问题 9: 数据库连接失败

**错误信息:**
```
com.mysql.cj.jdbc.exceptions.CommunicationsException: Communications link failure
```

**原因:** 数据库服务未启动或连接配置错误。

**解决方案:**
```bash
# 检查数据库服务状态
# MySQL
sudo systemctl status mysql
# 或
brew services list | grep mysql

# 启动数据库服务
sudo systemctl start mysql
# 或
brew services start mysql

# 检查连接配置
cat src/main/resources/application-dev.yml

# 测试数据库连接
mysql -h localhost -u root -p
```

#### 问题 10: Redis 连接失败

**错误信息:**
```
io.lettuce.core.RedisConnectionException: Unable to connect to Redis
```

**解决方案:**
```bash
# 检查 Redis 服务
redis-cli ping

# 启动 Redis
redis-server
# 或
sudo systemctl start redis
# 或
brew services start redis

# 检查 Redis 配置
cat src/main/resources/application-dev.yml | grep redis
```

#### 问题 11: 端口被占用

**错误信息:**
```
Web server failed to start. Port 8080 was already in use.
```

**解决方案:**
```bash
# 查找占用端口的进程
lsof -i :8080
# 或 Windows
netstat -ano | findstr :8080

# 杀死进程
kill -9 <PID>
# 或 Windows
taskkill /PID <PID> /F

# 或者修改端口
echo "server.port=8081" >> src/main/resources/application.yml
```

### Docker 相关问题

#### 问题 12: Docker 构建失败

**错误信息:**
```
ERROR: failed to solve: process "/bin/sh -c mvn clean package" did not complete successfully
```

**解决方案:**
```bash
# 检查 Dockerfile
cat Dockerfile

# 本地测试 Maven 构建
mvn clean package

# 检查 Docker 版本
docker --version

# 清理 Docker 缓存
docker system prune -a

# 重新构建
docker build --no-cache -t my-project .
```

#### 问题 13: Docker Compose 启动失败

**错误信息:**
```
ERROR: Version in "./docker-compose.yml" is unsupported
```

**解决方案:**
```bash
# 检查 Docker Compose 版本
docker-compose --version

# 更新 Docker Compose
pip install --upgrade docker-compose

# 或者修改 docker-compose.yml 中的版本号
sed -i 's/version: "3.8"/version: "3.3"/' docker-compose.yml
```

## 🔍 调试技巧

### 启用详细日志

```bash
# 设置日志级别
export LOG_LEVEL=DEBUG
python main.py

# 或者修改代码中的日志级别
import logging
logging.basicConfig(level=logging.DEBUG)
```

### 使用调试模式

```python
# 在代码中添加调试点
import pdb
pdb.set_trace()

# 或者使用 IPython
import IPython
IPython.embed()
```

### 检查生成的文件

```bash
# 查看生成的项目结构
tree output/my-project/

# 检查关键文件
cat output/my-project/pom.xml
cat output/my-project/src/main/resources/application.yml
```

## 📋 常见问题 FAQ

### Q1: 支持哪些 Spring Boot 版本？

**A:** 目前支持 Spring Boot 2.7.x 和 3.x 系列。推荐使用最新的稳定版本。

### Q2: 可以生成 Gradle 项目吗？

**A:** 当前版本只支持 Maven 项目。Gradle 支持在后续版本中会添加。

### Q3: 如何添加自定义依赖？

**A:** 可以在生成项目后手动编辑 `pom.xml` 文件，或者创建自定义模板。

### Q4: 生成的项目可以直接部署到生产环境吗？

**A:** 生成的项目包含了生产环境的基础配置，但建议根据实际需求进行调整和安全加固。

### Q5: 如何贡献新的技术栈支持？

**A:** 请参考 [贡献指南](README.md#贡献指南) 和 [API 参考文档](API_REFERENCE.md#扩展接口)。

### Q6: 配置文件可以版本控制吗？

**A:** 可以。配置文件是标准的 JSON 格式，可以纳入 Git 版本控制。

### Q7: 如何批量生成多个项目？

**A:** 可以编写脚本调用 API，或者使用命令行参数：

```bash
# 批量生成脚本示例
for config in configs/*.json; do
    python main.py --config "$config" --output "./output/$(basename "$config" .json)"
done
```

### Q8: 生成的测试代码覆盖率如何？

**A:** 生成的测试代码包含基础的单元测试和集成测试，覆盖主要功能。建议根据业务需求补充测试用例。

### Q9: 如何自定义代码模板？

**A:** 可以修改 `spring_init/templates/` 目录下的 Jinja2 模板文件，或者创建新的模板目录。

### Q10: 支持微服务架构吗？

**A:** 支持多模块项目生成，可以作为微服务的基础。Spring Cloud 支持在后续版本中会添加。

## 🆘 获取帮助

### 社区支持

- **GitHub Issues**: [提交 Bug 报告或功能请求](https://github.com/your-repo/issues)
- **GitHub Discussions**: [参与社区讨论](https://github.com/your-repo/discussions)
- **Stack Overflow**: 使用标签 `spring-boot-generator`

### 联系方式

- **邮箱**: support@example.com
- **微信群**: 扫描二维码加入技术交流群
- **QQ 群**: 123456789

### 报告问题时请提供

1. **环境信息**
   ```bash
   python --version
   pip list | grep -E "(jinja2|rich|click)"
   uname -a  # Linux/Mac
   systeminfo  # Windows
   ```

2. **错误日志**
   - 完整的错误堆栈信息
   - 相关的配置文件内容
   - 操作步骤

3. **重现步骤**
   - 详细的操作步骤
   - 使用的配置文件
   - 期望的结果

### 紧急问题处理

对于影响生产环境的紧急问题：

1. 立即回滚到上一个稳定版本
2. 收集详细的错误信息和环境数据
3. 通过邮箱联系技术支持
4. 在 GitHub Issues 中标记为 `urgent`

---

🔧 **故障排除版本**: v1.0.0  
📅 **最后更新**: 2024-01-01  
🆘 **支持渠道**: GitHub Issues, Email, 社区论坛