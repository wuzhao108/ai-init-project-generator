# 使用官方的OpenJDK运行时作为父镜像
FROM openjdk:{{ config.java_version }}-jre-slim

# 设置维护者信息
LABEL maintainer="{{ config.name }} <admin@example.com>"
LABEL description="{{ config.description }}"
LABEL version="{{ config.version }}"

# 设置工作目录
WORKDIR /app

# 创建应用用户（安全最佳实践）
RUN groupadd -r appuser && useradd -r -g appuser appuser

# 安装必要的工具和依赖
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# 设置时区
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 创建日志目录
RUN mkdir -p /var/log/{{ config.name }} && \
    chown -R appuser:appuser /var/log/{{ config.name }}

# 创建上传目录
RUN mkdir -p /var/uploads/{{ config.name }} && \
    chown -R appuser:appuser /var/uploads/{{ config.name }}

# 复制jar文件到容器中
COPY target/{{ config.name }}-{{ config.version }}.jar app.jar

# 修改文件权限
RUN chown appuser:appuser app.jar

# 切换到应用用户
USER appuser

# 设置JVM参数
ENV JAVA_OPTS="-Xms512m -Xmx1024m -XX:+UseG1GC -XX:G1HeapRegionSize=16m -XX:+UseG1OptionalCollectionSet -XX:+UseStringDeduplication -XX:+PrintGCDetails -XX:+PrintGCTimeStamps -Xloggc:/var/log/{{ config.name }}/gc.log"

# 设置Spring Boot配置
ENV SPRING_PROFILES_ACTIVE=prod
ENV SERVER_PORT=8080

# 暴露端口
EXPOSE 8080

# 健康检查
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:8080/actuator/health || exit 1

# 启动应用
ENTRYPOINT ["sh", "-c", "java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar app.jar"]