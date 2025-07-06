package com.wshoto.entity;

import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;

import java.time.LocalDateTime;

/**
 * 用户实体类
 * 
 * @author AI Generator
 * @version 1.0.0
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
public class User {

    private Long id;

    private String username;

    private String email;

    private String password;

    private String fullName;

    private LocalDateTime createdAt;

    private LocalDateTime updatedAt;
}