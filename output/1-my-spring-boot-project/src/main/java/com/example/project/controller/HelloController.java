package com.example.project.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Hello World 控制器
 * 
 * @author AI Generator
 * @version 1.0.0
 */
@RestController
public class HelloController {

    @GetMapping("/hello")
    public String hello() {
        return "Hello, World! Welcome to my-spring-boot-project!";
    }

    @GetMapping("/")
    public String index() {
        return "基于默认模板的Spring Boot项目";
    }
}