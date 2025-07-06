package com.example.project.mapper;

import com.example.project.entity.User;
import org.apache.ibatis.annotations.*;

import java.util.List;

/**
 * User Mapper
 * 
 * @author AI Generator
 */
@Mapper
public interface UserMapper {

    /**
     * Insert user
     * 
     * @param user the user
     * @return affected rows
     */
    @Insert("INSERT INTO users(username, email, password) VALUES(#{username}, #{email}, #{password})")
    @Options(useGeneratedKeys = true, keyProperty = "id")
    int insert(User user);

    /**
     * Update user
     * 
     * @param user the user
     * @return affected rows
     */
    @Update("UPDATE users SET username=#{username}, email=#{email}, password=#{password} WHERE id=#{id}")
    int update(User user);

    /**
     * Delete user by id
     * 
     * @param id the user id
     * @return affected rows
     */
    @Delete("DELETE FROM users WHERE id=#{id}")
    int deleteById(Long id);

    /**
     * Find user by id
     * 
     * @param id the user id
     * @return User
     */
    @Select("SELECT * FROM users WHERE id=#{id}")
    User findById(Long id);

    /**
     * Find user by username
     * 
     * @param username the username
     * @return User
     */
    @Select("SELECT * FROM users WHERE username=#{username}")
    User findByUsername(String username);

    /**
     * Find user by email
     * 
     * @param email the email
     * @return User
     */
    @Select("SELECT * FROM users WHERE email=#{email}")
    User findByEmail(String email);

    /**
     * Find all users
     * 
     * @return List<User>
     */
    @Select("SELECT * FROM users")
    List<User> findAll();

    /**
     * Check if username exists
     * 
     * @param username the username
     * @return count
     */
    @Select("SELECT COUNT(*) FROM users WHERE username=#{username}")
    int countByUsername(String username);

    /**
     * Check if email exists
     * 
     * @param email the email
     * @return count
     */
    @Select("SELECT COUNT(*) FROM users WHERE email=#{email}")
    int countByEmail(String email);
}