package {{ config.package }}.mapper;

import {{ config.package }}.entity.User;
import org.apache.ibatis.annotations.*;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * 用户数据访问层
 * 
 * @author {{ config.name }}
 * @since 2024-01-01
 */
@Mapper
@Repository
public interface UserMapper {

    /**
     * 查询所有用户
     * 
     * @return 用户列表
     */
    @Select("SELECT * FROM t_user ORDER BY create_time DESC")
    @Results({
            @Result(property = "id", column = "id"),
            @Result(property = "username", column = "username"),
            @Result(property = "password", column = "password"),
            @Result(property = "email", column = "email"),
            @Result(property = "phone", column = "phone"),
            @Result(property = "realName", column = "real_name"),
            @Result(property = "gender", column = "gender"),
            @Result(property = "age", column = "age"),
            @Result(property = "avatar", column = "avatar"),
            @Result(property = "status", column = "status"),
            @Result(property = "remark", column = "remark"),
            @Result(property = "createTime", column = "create_time"),
            @Result(property = "updateTime", column = "update_time")
    })
    List<User> findAll();

    /**
     * 根据ID查询用户
     * 
     * @param id 用户ID
     * @return 用户信息
     */
    @Select("SELECT * FROM t_user WHERE id = #{id}")
    @Results({
            @Result(property = "id", column = "id"),
            @Result(property = "username", column = "username"),
            @Result(property = "password", column = "password"),
            @Result(property = "email", column = "email"),
            @Result(property = "phone", column = "phone"),
            @Result(property = "realName", column = "real_name"),
            @Result(property = "gender", column = "gender"),
            @Result(property = "age", column = "age"),
            @Result(property = "avatar", column = "avatar"),
            @Result(property = "status", column = "status"),
            @Result(property = "remark", column = "remark"),
            @Result(property = "createTime", column = "create_time"),
            @Result(property = "updateTime", column = "update_time")
    })
    User findById(@Param("id") Long id);

    /**
     * 根据用户名查询用户
     * 
     * @param username 用户名
     * @return 用户信息
     */
    @Select("SELECT * FROM t_user WHERE username = #{username}")
    @Results({
            @Result(property = "id", column = "id"),
            @Result(property = "username", column = "username"),
            @Result(property = "password", column = "password"),
            @Result(property = "email", column = "email"),
            @Result(property = "phone", column = "phone"),
            @Result(property = "realName", column = "real_name"),
            @Result(property = "gender", column = "gender"),
            @Result(property = "age", column = "age"),
            @Result(property = "avatar", column = "avatar"),
            @Result(property = "status", column = "status"),
            @Result(property = "remark", column = "remark"),
            @Result(property = "createTime", column = "create_time"),
            @Result(property = "updateTime", column = "update_time")
    })
    User findByUsername(@Param("username") String username);

    /**
     * 插入用户
     * 
     * @param user 用户信息
     * @return 影响行数
     */
    @Insert("INSERT INTO t_user (username, password, email, phone, real_name, gender, age, avatar, status, remark, create_time, update_time) " +
            "VALUES (#{username}, #{password}, #{email}, #{phone}, #{realName}, #{gender}, #{age}, #{avatar}, #{status}, #{remark}, #{createTime}, #{updateTime})")
    @Options(useGeneratedKeys = true, keyProperty = "id")
    int insert(User user);

    /**
     * 更新用户
     * 
     * @param user 用户信息
     * @return 影响行数
     */
    @Update("UPDATE t_user SET username = #{username}, password = #{password}, email = #{email}, phone = #{phone}, " +
            "real_name = #{realName}, gender = #{gender}, age = #{age}, avatar = #{avatar}, status = #{status}, " +
            "remark = #{remark}, update_time = #{updateTime} WHERE id = #{id}")
    int update(User user);

    /**
     * 根据ID删除用户
     * 
     * @param id 用户ID
     * @return 影响行数
     */
    @Delete("DELETE FROM t_user WHERE id = #{id}")
    int deleteById(@Param("id") Long id);

    /**
     * 根据用户名统计用户数量
     * 
     * @param username 用户名
     * @return 用户数量
     */
    @Select("SELECT COUNT(*) FROM t_user WHERE username = #{username}")
    int countByUsername(@Param("username") String username);

    /**
     * 根据邮箱统计用户数量
     * 
     * @param email 邮箱
     * @return 用户数量
     */
    @Select("SELECT COUNT(*) FROM t_user WHERE email = #{email}")
    int countByEmail(@Param("email") String email);

    /**
     * 分页查询用户
     * 
     * @param offset 偏移量
     * @param limit 限制数量
     * @return 用户列表
     */
    @Select("SELECT * FROM t_user ORDER BY create_time DESC LIMIT #{offset}, #{limit}")
    @Results({
            @Result(property = "id", column = "id"),
            @Result(property = "username", column = "username"),
            @Result(property = "password", column = "password"),
            @Result(property = "email", column = "email"),
            @Result(property = "phone", column = "phone"),
            @Result(property = "realName", column = "real_name"),
            @Result(property = "gender", column = "gender"),
            @Result(property = "age", column = "age"),
            @Result(property = "avatar", column = "avatar"),
            @Result(property = "status", column = "status"),
            @Result(property = "remark", column = "remark"),
            @Result(property = "createTime", column = "create_time"),
            @Result(property = "updateTime", column = "update_time")
    })
    List<User> findByPage(@Param("offset") int offset, @Param("limit") int limit);

    /**
     * 统计用户总数
     * 
     * @return 用户总数
     */
    @Select("SELECT COUNT(*) FROM t_user")
    long count();

    /**
     * 根据状态查询用户
     * 
     * @param status 状态
     * @return 用户列表
     */
    @Select("SELECT * FROM t_user WHERE status = #{status} ORDER BY create_time DESC")
    @Results({
            @Result(property = "id", column = "id"),
            @Result(property = "username", column = "username"),
            @Result(property = "password", column = "password"),
            @Result(property = "email", column = "email"),
            @Result(property = "phone", column = "phone"),
            @Result(property = "realName", column = "real_name"),
            @Result(property = "gender", column = "gender"),
            @Result(property = "age", column = "age"),
            @Result(property = "avatar", column = "avatar"),
            @Result(property = "status", column = "status"),
            @Result(property = "remark", column = "remark"),
            @Result(property = "createTime", column = "create_time"),
            @Result(property = "updateTime", column = "update_time")
    })
    List<User> findByStatus(@Param("status") Integer status);

    /**
     * 批量插入用户
     * 
     * @param users 用户列表
     * @return 影响行数
     */
    @Insert("<script>" +
            "INSERT INTO t_user (username, password, email, phone, real_name, gender, age, avatar, status, remark, create_time, update_time) VALUES " +
            "<foreach collection='users' item='user' separator=','>" +
            "(#{user.username}, #{user.password}, #{user.email}, #{user.phone}, #{user.realName}, #{user.gender}, #{user.age}, #{user.avatar}, #{user.status}, #{user.remark}, #{user.createTime}, #{user.updateTime})" +
            "</foreach>" +
            "</script>")
    int batchInsert(@Param("users") List<User> users);
}