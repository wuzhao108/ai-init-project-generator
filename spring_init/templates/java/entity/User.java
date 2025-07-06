package {{ config.package }}.entity;

{% if config.tech_stack.orm == 'jpa' %}
import javax.persistence.*;
import javax.validation.constraints.*;
{% elif config.tech_stack.orm == 'mybatis' %}
import com.baomidou.mybatisplus.annotation.*;
{% endif %}
{% if config.tech_stack.doc %}
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
{% endif %}
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonIgnore;

import java.io.Serializable;
import java.time.LocalDateTime;
import java.util.Objects;

/**
 * 用户实体类
 * 
 * @author {{ config.name }}
 * @since 2024-01-01
 */
{% if config.tech_stack.orm == 'jpa' %}
@Entity
@Table(name = "t_user")
{% elif config.tech_stack.orm == 'mybatis' %}
@TableName("t_user")
{% endif %}
{% if config.tech_stack.doc %}
@ApiModel(description = "用户实体")
{% endif %}
public class User implements Serializable {

    private static final long serialVersionUID = 1L;

    /**
     * 用户ID
     */
    {% if config.tech_stack.orm == 'jpa' %}
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    {% elif config.tech_stack.orm == 'mybatis' %}
    @TableId(value = "id", type = IdType.AUTO)
    {% endif %}
    {% if config.tech_stack.doc %}
    @ApiModelProperty(value = "用户ID", example = "1")
    {% endif %}
    private Long id;

    /**
     * 用户名
     */
    {% if config.tech_stack.orm == 'jpa' %}
    @Column(name = "username", nullable = false, unique = true, length = 50)
    @NotBlank(message = "用户名不能为空")
    @Size(min = 3, max = 50, message = "用户名长度必须在3-50个字符之间")
    {% elif config.tech_stack.orm == 'mybatis' %}
    @TableField("username")
    {% endif %}
    {% if 'swagger' in config.tech_stack.docs %}
    @ApiModelProperty(value = "用户名", required = true, example = "admin")
    {% endif %}
    private String username;

    /**
     * 密码
     */
    {% if config.tech_stack.orm == 'jpa' %}
    @Column(name = "password", nullable = false)
    @NotBlank(message = "密码不能为空")
    @Size(min = 6, message = "密码长度不能少于6位")
    {% elif config.tech_stack.orm == 'mybatis' %}
    @TableField("password")
    {% endif %}
    {% if 'swagger' in config.tech_stack.docs %}
    @ApiModelProperty(value = "密码", required = true, example = "123456")
    {% endif %}
    @JsonIgnore
    private String password;

    /**
     * 邮箱
     */
    {% if config.tech_stack.orm == 'jpa' %}
    @Column(name = "email", unique = true, length = 100)
    @Email(message = "邮箱格式不正确")
    {% elif config.tech_stack.orm == 'mybatis' %}
    @TableField("email")
    {% endif %}
    {% if config.tech_stack.doc %}
    @ApiModelProperty(value = "邮箱", example = "admin@example.com")
    {% endif %}
    private String email;

    /**
     * 手机号
     */
    {% if config.tech_stack.orm == 'jpa' %}
    @Column(name = "phone", length = 20)
    @Pattern(regexp = "^1[3-9]\\d{9}$", message = "手机号格式不正确")
    {% elif config.tech_stack.orm == 'mybatis' %}
    @TableField("phone")
    {% endif %}
    {% if 'swagger' in config.tech_stack.docs %}
    @ApiModelProperty(value = "手机号", example = "13800138000")
    {% endif %}
    private String phone;

    /**
     * 真实姓名
     */
    {% if config.tech_stack.orm == 'jpa' %}
    @Column(name = "real_name", length = 50)
    {% elif config.tech_stack.orm == 'mybatis' %}
    @TableField("real_name")
    {% endif %}
    {% if 'swagger' in config.tech_stack.docs %}
    @ApiModelProperty(value = "真实姓名", example = "张三")
    {% endif %}
    private String realName;

    /**
     * 性别：0-未知，1-男，2-女
     */
    {% if config.tech_stack.orm == 'jpa' %}
    @Column(name = "gender")
    {% elif config.tech_stack.orm == 'mybatis' %}
    @TableField("gender")
    {% endif %}
    {% if 'swagger' in config.tech_stack.docs %}
    @ApiModelProperty(value = "性别：0-未知，1-男，2-女", example = "1")
    {% endif %}
    private Integer gender;

    /**
     * 年龄
     */
    {% if config.tech_stack.orm == 'jpa' %}
    @Column(name = "age")
    @Min(value = 0, message = "年龄不能小于0")
    @Max(value = 150, message = "年龄不能大于150")
    {% elif config.tech_stack.orm == 'mybatis' %}
    @TableField("age")
    {% endif %}
    {% if config.tech_stack.doc %}
    @ApiModelProperty(value = "用户名", example = "admin")
    {% endif %}
    private Integer age;

    /**
     * 头像URL
     */
    {% if config.tech_stack.orm == 'jpa' %}
    @Column(name = "avatar")
    {% elif config.tech_stack.orm == 'mybatis' %}
    @TableField("avatar")
    {% endif %}
    {% if 'swagger' in config.tech_stack.docs %}
    @ApiModelProperty(value = "头像URL", example = "https://example.com/avatar.jpg")
    {% endif %}
    private String avatar;

    /**
     * 状态：0-禁用，1-启用
     */
    {% if config.tech_stack.orm == 'jpa' %}
    @Column(name = "status")
    {% elif config.tech_stack.orm == 'mybatis' %}
    @TableField("status")
    {% endif %}
    {% if 'swagger' in config.tech_stack.docs %}
    @ApiModelProperty(value = "状态：0-禁用，1-启用", example = "1")
    {% endif %}
    private Integer status;

    /**
     * 备注
     */
    {% if config.tech_stack.orm == 'jpa' %}
    @Column(name = "remark")
    {% elif config.tech_stack.orm == 'mybatis' %}
    @TableField("remark")
    {% endif %}
    {% if 'swagger' in config.tech_stack.docs %}
    @ApiModelProperty(value = "备注", example = "系统管理员")
    {% endif %}
    private String remark;

    /**
     * 创建时间
     */
    {% if config.tech_stack.orm == 'jpa' %}
    @Column(name = "create_time", updatable = false)
    {% elif config.tech_stack.orm == 'mybatis' %}
    @TableField(value = "create_time", fill = FieldFill.INSERT)
    {% endif %}
    {% if config.tech_stack.doc %}
    @ApiModelProperty(value = "创建时间", example = "2023-01-01 12:00:00")
    {% endif %}
    @JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss")
    private LocalDateTime createTime;

    /**
     * 更新时间
     */
    {% if config.tech_stack.orm == 'jpa' %}
    @Column(name = "update_time")
    {% elif config.tech_stack.orm == 'mybatis' %}
    @TableField(value = "update_time", fill = FieldFill.INSERT_UPDATE)
    {% endif %}
    {% if config.tech_stack.doc %}
    @ApiModelProperty(value = "更新时间", example = "2023-01-01 12:00:00")
    {% endif %}
    @JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss")
    private LocalDateTime updateTime;

    // 构造函数
    public User() {
    }

    public User(String username, String password) {
        this.username = username;
        this.password = password;
        this.status = 1; // 默认启用
        this.createTime = LocalDateTime.now();
        this.updateTime = LocalDateTime.now();
    }

    // Getter和Setter方法
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getRealName() {
        return realName;
    }

    public void setRealName(String realName) {
        this.realName = realName;
    }

    public Integer getGender() {
        return gender;
    }

    public void setGender(Integer gender) {
        this.gender = gender;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    public String getAvatar() {
        return avatar;
    }

    public void setAvatar(String avatar) {
        this.avatar = avatar;
    }

    public Integer getStatus() {
        return status;
    }

    public void setStatus(Integer status) {
        this.status = status;
    }

    public String getRemark() {
        return remark;
    }

    public void setRemark(String remark) {
        this.remark = remark;
    }

    public LocalDateTime getCreateTime() {
        return createTime;
    }

    public void setCreateTime(LocalDateTime createTime) {
        this.createTime = createTime;
    }

    public LocalDateTime getUpdateTime() {
        return updateTime;
    }

    public void setUpdateTime(LocalDateTime updateTime) {
        this.updateTime = updateTime;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        User user = (User) o;
        return Objects.equals(id, user.id) &&
                Objects.equals(username, user.username);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, username);
    }

    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", username='" + username + '\'' +
                ", email='" + email + '\'' +
                ", phone='" + phone + '\'' +
                ", realName='" + realName + '\'' +
                ", gender=" + gender +
                ", age=" + age +
                ", status=" + status +
                ", createTime=" + createTime +
                ", updateTime=" + updateTime +
                '}';
    }
}