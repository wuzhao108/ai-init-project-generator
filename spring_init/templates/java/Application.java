package {{ config.package }};

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
{% if config.tech_stack.orm == 'mybatis' %}
import org.mybatis.spring.annotation.MapperScan;
{% endif %}
{% if config.tech_stack.cache and 'caffeine' in config.tech_stack.cache %}
import org.springframework.cache.annotation.EnableCaching;
{% endif %}
{% if config.tech_stack.doc %}
import springfox.documentation.swagger2.annotations.EnableSwagger2;
{% endif %}

/**
 * SpringBoot应用启动类
 * 
 * @author {{ config.name }}
 * @since 2024-01-01
 */
@SpringBootApplication
{% if config.tech_stack.orm == 'mybatis' %}
@MapperScan("{{ config.package }}.mapper")
{% endif %}
{% if config.tech_stack.cache and 'caffeine' in config.tech_stack.cache %}
@EnableCaching
{% endif %}
{% if config.tech_stack.doc %}
@EnableSwagger2
{% endif %}
public class {{ config.main_class_name }} {

    public static void main(String[] args) {
        SpringApplication.run({{ config.main_class_name }}.class, args);
        System.out.println("\n" +
            "  ____  _             _               ____              _   \n" +
            " / ___|| |_ __ _ _ __| |_ ___ _ __   / ___| _   _  ___  ___| |_ \n" +
            " \___ \| __/ _` | '__| __/ _ \ '__| \___ \| | | |/ __|/ __| __|\n" +
            "  ___) | || (_| | |  | ||  __/ |     ___) | |_| | (__| (__| |_ \n" +
            " |____/ \__\__,_|_|   \__\___|_|    |____/ \__,_|\___|\___|\__|\n" +
            "\n" +
            "{{ config.name }} 启动成功！\n" +
            "访问地址: http://localhost:8080\n" +
            {% if config.tech_stack.doc %}
            "API文档: http://localhost:8080/swagger-ui.html\n" +
            {% endif %}
            {% if config.tech_stack.actuator %}
            "健康检查: http://localhost:8080/actuator/health\n" +
            {% endif %}
            "\n");
    }
}