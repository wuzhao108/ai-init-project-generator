package com.example.project.controller;

import com.example.project.common.Result;
import com.example.project.entity.User;
import com.example.project.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.validation.annotation.Validated;

import javax.validation.Valid;
import javax.validation.constraints.NotNull;
import java.util.List;

/**
 * 用户控制器
 * 
 * @author my-spring-boot-project
 * @since 2024-01-01
 */
@RestController
@RequestMapping("/api/users")
@Validated
@Api(tags = "用户管理")
public class UserController {

    @Autowired
    private UserService userService;

    /**
     * 获取所有用户
     * 
     * @return 用户列表
     */
    @GetMapping
    @ApiOperation("获取所有用户")
    public Result<List<User>> getAllUsers() {
        List<User> users = userService.findAll();
        return Result.success(users);
    }

    /**
     * 根据ID获取用户
     * 
     * @param id 用户ID
     * @return 用户信息
     */
    @GetMapping("/{id}")
    @ApiOperation("根据ID获取用户")
    public Result<User> getUserById(
            @ApiParam("用户ID") 
            @PathVariable @NotNull Long id) {
        User user = userService.findById(id);
        if (user != null) {
            return Result.success(user);
        } else {
            return Result.error("用户不存在");
        }
    }

    /**
     * 创建用户
     * 
     * @param user 用户信息
     * @return 创建结果
     */
    @PostMapping
    @ApiOperation("创建用户")
    public Result<User> createUser(
            @ApiParam("用户信息") 
            @RequestBody @Valid User user) {
        User savedUser = userService.save(user);
        return Result.success(savedUser);
    }

    /**
     * 更新用户
     * 
     * @param id 用户ID
     * @param user 用户信息
     * @return 更新结果
     */
    @PutMapping("/{id}")
    @ApiOperation("更新用户")
    public Result<User> updateUser(
            @ApiParam("用户ID") 
            @PathVariable @NotNull Long id,
            @ApiParam("用户信息") 
            @RequestBody @Valid User user) {
        user.setId(id);
        User updatedUser = userService.update(user);
        if (updatedUser != null) {
            return Result.success(updatedUser);
        } else {
            return Result.error("用户不存在");
        }
    }

    /**
     * 删除用户
     * 
     * @param id 用户ID
     * @return 删除结果
     */
    @DeleteMapping("/{id}")
    @ApiOperation("删除用户")
    public Result<Void> deleteUser(
            @ApiParam("用户ID") 
            @PathVariable @NotNull Long id) {
        boolean deleted = userService.deleteById(id);
        if (deleted) {
            return Result.success();
        } else {
            return Result.error("用户不存在");
        }
    }

    /**
     * 根据用户名查询用户
     * 
     * @param username 用户名
     * @return 用户信息
     */
    @GetMapping("/search")
    @ApiOperation("根据用户名查询用户")
    public Result<User> getUserByUsername(
            @ApiParam("用户名") 
            @RequestParam String username) {
        User user = userService.findByUsername(username);
        if (user != null) {
            return Result.success(user);
        } else {
            return Result.error("用户不存在");
        }
    }
}