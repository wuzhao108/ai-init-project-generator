package {{ config.package }}.service;

import {{ config.package }}.entity.User;
import java.util.List;

/**
 * 用户服务接口
 * 
 * @author {{ config.name }}
 * @since 2024-01-01
 */
public interface UserService {

    /**
     * 查询所有用户
     * 
     * @return 用户列表
     */
    List<User> findAll();

    /**
     * 根据ID查询用户
     * 
     * @param id 用户ID
     * @return 用户信息
     */
    User findById(Long id);

    /**
     * 根据用户名查询用户
     * 
     * @param username 用户名
     * @return 用户信息
     */
    User findByUsername(String username);

    /**
     * 保存用户
     * 
     * @param user 用户信息
     * @return 保存后的用户信息
     */
    User save(User user);

    /**
     * 更新用户
     * 
     * @param user 用户信息
     * @return 更新后的用户信息
     */
    User update(User user);

    /**
     * 根据ID删除用户
     * 
     * @param id 用户ID
     * @return 是否删除成功
     */
    boolean deleteById(Long id);

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
     * 分页查询用户
     * 
     * @param page 页码（从0开始）
     * @param size 每页大小
     * @return 用户列表
     */
    List<User> findByPage(int page, int size);

    /**
     * 获取用户总数
     * 
     * @return 用户总数
     */
    long count();
}