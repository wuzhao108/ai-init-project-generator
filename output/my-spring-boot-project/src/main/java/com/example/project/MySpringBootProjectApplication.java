package com.example.project;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

/**
 * SpringBoot应用启动类
 * 
 * @author my-spring-boot-project
 * @since 2024-01-01
 */
@SpringBootApplication
@EnableSwagger2
public class MySpringBootProjectApplication {

    public static void main(String[] args) {
        SpringApplication.run(MySpringBootProjectApplication.class, args);
        System.out.println("\n" +
            "  ____  _             _               ____              _   \n" +
            " / ___|| |_ __ _ _ __| |_ ___ _ __   / ___| _   _  ___  ___| |_ \n" +
            " \___ \| __/ _` | '__| __/ _ \ '__| \___ \| | | |/ __|/ __| __|\n" +
            "  ___) | || (_| | |  | ||  __/ |     ___) | |_| | (__| (__| |_ \n" +
            " |____/ \__\__,_|_|   \__\___|_|    |____/ \__,_|\___|\___|\__|\n" +
            "\n" +
            "my-spring-boot-project 启动成功！\n" +
            "访问地址: http://localhost:8080\n" +
            "API文档: http://localhost:8080/swagger-ui.html\n" +
            "健康检查: http://localhost:8080/actuator/health\n" +
            "\n");
    }
}