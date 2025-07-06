package com.example.project.repository;

import com.example.project.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

/**
 * 用户数据访问层
 * 
 * @author my-spring-boot-project
 * @since 2024-01-01
 */
@Repository
public interface UserRepository extends JpaRepository<User, Long>, JpaSpecificationExecutor<User> {

    /**
     * 根据用户名查询用户
     * 
     * @param username 用户名
     * @return 用户信息
     */
    Optional<User> findByUsername(String username);

    /**
     * 根据用户名查询用户（返回User对象）
     * 
     * @param username 用户名
     * @return 用户信息
     */
    User findByUsername(String username);

    /**
     * 根据邮箱查询用户
     * 
     * @param email 邮箱
     * @return 用户信息
     */
    Optional<User> findByEmail(String email);

    /**
     * 根据手机号查询用户
     * 
     * @param phone 手机号
     * @return 用户信息
     */
    Optional<User> findByPhone(String phone);

    /**
     * 检查用户名是否存在
     * 
     * @param username 用户名
     * @return 是否存在
     */
    boolean existsByUsername(String username);

    /**
     * 检查邮箱是否存在
     * 
     * @param email 邮箱
     * @return 是否存在
     */
    boolean existsByEmail(String email);

    /**
     * 检查手机号是否存在
     * 
     * @param phone 手机号
     * @return 是否存在
     */
    boolean existsByPhone(String phone);

    /**
     * 根据状态查询用户
     * 
     * @param status 状态
     * @return 用户列表
     */
    List<User> findByStatus(Integer status);

    /**
     * 根据状态查询用户（按创建时间倒序）
     * 
     * @param status 状态
     * @return 用户列表
     */
    List<User> findByStatusOrderByCreateTimeDesc(Integer status);

    /**
     * 根据性别查询用户
     * 
     * @param gender 性别
     * @return 用户列表
     */
    List<User> findByGender(Integer gender);

    /**
     * 根据年龄范围查询用户
     * 
     * @param minAge 最小年龄
     * @param maxAge 最大年龄
     * @return 用户列表
     */
    List<User> findByAgeBetween(Integer minAge, Integer maxAge);

    /**
     * 根据创建时间范围查询用户
     * 
     * @param startTime 开始时间
     * @param endTime 结束时间
     * @return 用户列表
     */
    List<User> findByCreateTimeBetween(LocalDateTime startTime, LocalDateTime endTime);

    /**
     * 根据用户名模糊查询
     * 
     * @param username 用户名关键字
     * @return 用户列表
     */
    List<User> findByUsernameContaining(String username);

    /**
     * 根据真实姓名模糊查询
     * 
     * @param realName 真实姓名关键字
     * @return 用户列表
     */
    List<User> findByRealNameContaining(String realName);

    /**
     * 查询启用状态的用户数量
     * 
     * @return 用户数量
     */
    @Query("SELECT COUNT(u) FROM User u WHERE u.status = 1")
    long countActiveUsers();

    /**
     * 查询禁用状态的用户数量
     * 
     * @return 用户数量
     */
    @Query("SELECT COUNT(u) FROM User u WHERE u.status = 0")
    long countInactiveUsers();

    /**
     * 根据状态统计用户数量
     * 
     * @param status 状态
     * @return 用户数量
     */
    long countByStatus(Integer status);

    /**
     * 查询最近注册的用户
     * 
     * @param days 天数
     * @return 用户列表
     */
    @Query("SELECT u FROM User u WHERE u.createTime >= :startTime ORDER BY u.createTime DESC")
    List<User> findRecentUsers(@Param("startTime") LocalDateTime startTime);

    /**
     * 根据多个条件查询用户
     * 
     * @param username 用户名（可选）
     * @param email 邮箱（可选）
     * @param status 状态（可选）
     * @return 用户列表
     */
    @Query("SELECT u FROM User u WHERE " +
           "(:username IS NULL OR u.username LIKE %:username%) AND " +
           "(:email IS NULL OR u.email LIKE %:email%) AND " +
           "(:status IS NULL OR u.status = :status) " +
           "ORDER BY u.createTime DESC")
    List<User> findByConditions(@Param("username") String username,
                               @Param("email") String email,
                               @Param("status") Integer status);

    /**
     * 更新用户状态
     * 
     * @param id 用户ID
     * @param status 新状态
     * @return 影响行数
     */
    @Query("UPDATE User u SET u.status = :status, u.updateTime = CURRENT_TIMESTAMP WHERE u.id = :id")
    int updateStatus(@Param("id") Long id, @Param("status") Integer status);

    /**
     * 批量更新用户状态
     * 
     * @param ids 用户ID列表
     * @param status 新状态
     * @return 影响行数
     */
    @Query("UPDATE User u SET u.status = :status, u.updateTime = CURRENT_TIMESTAMP WHERE u.id IN :ids")
    int batchUpdateStatus(@Param("ids") List<Long> ids, @Param("status") Integer status);

    /**
     * 删除指定状态的用户
     * 
     * @param status 状态
     * @return 删除数量
     */
    long deleteByStatus(Integer status);

    /**
     * 删除指定时间之前创建的用户
     * 
     * @param createTime 创建时间
     * @return 删除数量
     */
    long deleteByCreateTimeBefore(LocalDateTime createTime);

    /**
     * 查询用户统计信息
     * 
     * @return 统计结果
     */
    @Query("SELECT new map(" +
           "COUNT(u) as total, " +
           "SUM(CASE WHEN u.status = 1 THEN 1 ELSE 0 END) as active, " +
           "SUM(CASE WHEN u.status = 0 THEN 1 ELSE 0 END) as inactive, " +
           "SUM(CASE WHEN u.gender = 1 THEN 1 ELSE 0 END) as male, " +
           "SUM(CASE WHEN u.gender = 2 THEN 1 ELSE 0 END) as female" +
           ") FROM User u")
    List<Object> getUserStatistics();

    /**
     * 查询所有用户（按创建时间倒序）
     * 
     * @return 用户列表
     */
    List<User> findAllByOrderByCreateTimeDesc();

    /**
     * 查询所有用户（按更新时间倒序）
     * 
     * @return 用户列表
     */
    List<User> findAllByOrderByUpdateTimeDesc();
}