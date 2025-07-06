package {{ config.package }}.service.impl;

import {{ config.package }}.entity.User;
import {{ config.package }}.service.UserService;
{% if config.tech_stack.orm == 'mybatis' %}
import {{ config.package }}.mapper.UserMapper;
{% elif config.tech_stack.orm == 'jpa' %}
import {{ config.package }}.repository.UserRepository;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
{% endif %}
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
{% if 'redis' in config.tech_stack.cache %}
import org.springframework.cache.annotation.Cacheable;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.CachePut;
{% endif %}
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.List;
{% if config.tech_stack.orm == 'jpa' %}
import java.util.Optional;
{% endif %}

/**
 * 用户服务实现类
 * 
 * @author {{ config.name }}
 * @since 2024-01-01
 */
@Service
@Transactional(rollbackFor = Exception.class)
public class UserServiceImpl implements UserService {

    private static final Logger logger = LoggerFactory.getLogger(UserServiceImpl.class);

    {% if config.tech_stack.orm == 'mybatis' %}
    @Autowired
    private UserMapper userMapper;
    {% elif config.tech_stack.orm == 'jpa' %}
    @Autowired
    private UserRepository userRepository;
    {% endif %}

    @Override
    @Transactional(readOnly = true)
    {% if 'redis' in config.tech_stack.cache %}
    @Cacheable(value = "users", key = "'all'")
    {% endif %}
    public List<User> findAll() {
        logger.info("查询所有用户");
        {% if config.tech_stack.orm == 'mybatis' %}
        return userMapper.findAll();
        {% elif config.tech_stack.orm == 'jpa' %}
        return userRepository.findAll();
        {% endif %}
    }

    @Override
    @Transactional(readOnly = true)
    {% if 'redis' in config.tech_stack.cache %}
    @Cacheable(value = "users", key = "#id")
    {% endif %}
    public User findById(Long id) {
        logger.info("根据ID查询用户: {}", id);
        {% if config.tech_stack.orm == 'mybatis' %}
        return userMapper.findById(id);
        {% elif config.tech_stack.orm == 'jpa' %}
        Optional<User> userOptional = userRepository.findById(id);
        return userOptional.orElse(null);
        {% endif %}
    }

    @Override
    @Transactional(readOnly = true)
    {% if 'redis' in config.tech_stack.cache %}
    @Cacheable(value = "users", key = "'username:' + #username")
    {% endif %}
    public User findByUsername(String username) {
        logger.info("根据用户名查询用户: {}", username);
        {% if config.tech_stack.orm == 'mybatis' %}
        return userMapper.findByUsername(username);
        {% elif config.tech_stack.orm == 'jpa' %}
        return userRepository.findByUsername(username);
        {% endif %}
    }

    @Override
    {% if 'redis' in config.tech_stack.cache %}
    @CachePut(value = "users", key = "#result.id")
    {% endif %}
    public User save(User user) {
        logger.info("保存用户: {}", user.getUsername());
        
        // 检查用户名是否已存在
        if (existsByUsername(user.getUsername())) {
            throw new RuntimeException("用户名已存在: " + user.getUsername());
        }
        
        // 检查邮箱是否已存在
        if (user.getEmail() != null && existsByEmail(user.getEmail())) {
            throw new RuntimeException("邮箱已存在: " + user.getEmail());
        }
        
        {% if config.tech_stack.orm == 'mybatis' %}
        userMapper.insert(user);
        return user;
        {% elif config.tech_stack.orm == 'jpa' %}
        return userRepository.save(user);
        {% endif %}
    }

    @Override
    {% if 'redis' in config.tech_stack.cache %}
    @CachePut(value = "users", key = "#user.id")
    {% endif %}
    public User update(User user) {
        logger.info("更新用户: {}", user.getId());
        
        // 检查用户是否存在
        User existingUser = findById(user.getId());
        if (existingUser == null) {
            return null;
        }
        
        // 检查用户名是否被其他用户使用
        User userWithSameUsername = findByUsername(user.getUsername());
        if (userWithSameUsername != null && !userWithSameUsername.getId().equals(user.getId())) {
            throw new RuntimeException("用户名已存在: " + user.getUsername());
        }
        
        {% if config.tech_stack.orm == 'mybatis' %}
        userMapper.update(user);
        return user;
        {% elif config.tech_stack.orm == 'jpa' %}
        return userRepository.save(user);
        {% endif %}
    }

    @Override
    {% if 'redis' in config.tech_stack.cache %}
    @CacheEvict(value = "users", key = "#id")
    {% endif %}
    public boolean deleteById(Long id) {
        logger.info("删除用户: {}", id);
        
        User user = findById(id);
        if (user == null) {
            return false;
        }
        
        {% if config.tech_stack.orm == 'mybatis' %}
        int result = userMapper.deleteById(id);
        return result > 0;
        {% elif config.tech_stack.orm == 'jpa' %}
        userRepository.deleteById(id);
        return true;
        {% endif %}
    }

    @Override
    @Transactional(readOnly = true)
    public boolean existsByUsername(String username) {
        {% if config.tech_stack.orm == 'mybatis' %}
        return userMapper.countByUsername(username) > 0;
        {% elif config.tech_stack.orm == 'jpa' %}
        return userRepository.existsByUsername(username);
        {% endif %}
    }

    @Override
    @Transactional(readOnly = true)
    public boolean existsByEmail(String email) {
        {% if config.tech_stack.orm == 'mybatis' %}
        return userMapper.countByEmail(email) > 0;
        {% elif config.tech_stack.orm == 'jpa' %}
        return userRepository.existsByEmail(email);
        {% endif %}
    }

    @Override
    @Transactional(readOnly = true)
    public List<User> findByPage(int page, int size) {
        logger.info("分页查询用户: page={}, size={}", page, size);
        {% if config.tech_stack.orm == 'mybatis' %}
        int offset = page * size;
        return userMapper.findByPage(offset, size);
        {% elif config.tech_stack.orm == 'jpa' %}
        Pageable pageable = PageRequest.of(page, size);
        Page<User> userPage = userRepository.findAll(pageable);
        return userPage.getContent();
        {% endif %}
    }

    @Override
    @Transactional(readOnly = true)
    public long count() {
        {% if config.tech_stack.orm == 'mybatis' %}
        return userMapper.count();
        {% elif config.tech_stack.orm == 'jpa' %}
        return userRepository.count();
        {% endif %}
    }
}