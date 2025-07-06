package com.wshoto.mapper;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Update;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Param;
import com.wshoto.entity.User;

import java.util.List;

/**
 * 用户数据访问层
 * 
 * @author AI Generator
 * @version 1.0.0
 */
@Mapper
public interface UserMapper {

    /**
     * 查询所有用户
     * 
     * @return 用户列表
     */
    @Select("SELECT * FROM users")
    List<User> findAll();

    /**
     * 根据ID查询用户
     * 
     * @param id 用户ID
     * @return 用户信息
     */
    @Select("SELECT * FROM users WHERE id = #{id}")
    User findById(@Param("id") Long id);

    /**
     * 根据用户名查询用户
     * 
     * @param username 用户名
     * @return 用户信息
     */
    @Select("SELECT * FROM users WHERE username = #{username}")
    User findByUsername(@Param("username") String username);

    /**
     * 插入用户
     * 
     * @param user 用户信息
     * @return 影响行数
     */
    @Insert("INSERT INTO users(username, email, password, full_name, created_at, updated_at) VALUES(#{username}, #{email}, #{password}, #{fullName}, #{createdAt}, #{updatedAt})")
    int insert(User user);

    /**
     * 更新用户
     * 
     * @param user 用户信息
     * @return 影响行数
     */
    @Update("UPDATE users SET username=#{username}, email=#{email}, password=#{password}, full_name=#{fullName}, updated_at=#{updatedAt} WHERE id=#{id}")
    int update(User user);

    /**
     * 删除用户
     * 
     * @param id 用户ID
     * @return 影响行数
     */
    @Delete("DELETE FROM users WHERE id = #{id}")
    int deleteById(@Param("id") Long id);
}