package {{ config.package }}.controller;

import {{ config.package }}.common.Result;
import {{ config.package }}.entity.User;
import {{ config.package }}.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
{% if config.tech_stack.doc %}
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
{% endif %}
import org.springframework.validation.annotation.Validated;

import javax.validation.Valid;
import javax.validation.constraints.NotNull;
import java.util.List;

/**
 * 用户控制器
 * 
 * @author {{ config.name }}
 * @since {{ "now" | strftime("%Y-%m-%d") }}
 */
@RestController
@RequestMapping("/api/users")
@Validated
{% if config.tech_stack.doc %}
@Api(tags = "用户管理")
{% endif %}
public class UserController {

    @Autowired
    private UserService userService;

    /**
     * 获取所有用户
     * 
     * @return 用户列表
     */
    @GetMapping
    {% if config.tech_stack.doc %}
    @ApiOperation("获取所有用户")
    {% endif %}
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
    {% if config.tech_stack.doc %}
    @ApiOperation("根据ID获取用户")
    {% endif %}
    public Result<User> getUserById(
            {% if config.tech_stack.doc %}
            @ApiParam("用户ID") 
            {% endif %}
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
    {% if config.tech_stack.doc %}
    @ApiOperation("创建用户")
    {% endif %}
    public Result<User> createUser(
            {% if config.tech_stack.doc %}
            @ApiParam("用户信息") 
            {% endif %}
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
    {% if config.tech_stack.doc %}
    @ApiOperation("更新用户")
    {% endif %}
    public Result<User> updateUser(
            {% if config.tech_stack.doc %}
            @ApiParam("用户ID") 
            {% endif %}
            @PathVariable @NotNull Long id,
            {% if config.tech_stack.doc %}
            @ApiParam("用户信息") 
            {% endif %}
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
    {% if config.tech_stack.doc %}
    @ApiOperation("删除用户")
    {% endif %}
    public Result<Void> deleteUser(
            {% if config.tech_stack.doc %}
            @ApiParam("用户ID") 
            {% endif %}
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
    {% if config.tech_stack.doc %}
    @ApiOperation("根据用户名查询用户")
    {% endif %}
    public Result<User> getUserByUsername(
            {% if config.tech_stack.doc %}
            @ApiParam("用户名") 
            {% endif %}
            @RequestParam String username) {
        User user = userService.findByUsername(username);
        if (user != null) {
            return Result.success(user);
        } else {
            return Result.error("用户不存在");
        }
    }
}