package com.example.project.service.impl;

import com.example.project.entity.User;
import com.example.project.service.UserService;
import com.example.project.repository.UserRepository;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.List;
import java.util.Optional;

/**
 * 用户服务实现类
 * 
 * @author my-spring-boot-project
 * @since 2024-01-01
 */
@Service
@Transactional(rollbackFor = Exception.class)
public class UserServiceImpl implements UserService {

    private static final Logger logger = LoggerFactory.getLogger(UserServiceImpl.class);

    @Autowired
    private UserRepository userRepository;

    @Override
    @Transactional(readOnly = true)
    public List<User> findAll() {
        logger.info("查询所有用户");
        return userRepository.findAll();
    }

    @Override
    @Transactional(readOnly = true)
    public User findById(Long id) {
        logger.info("根据ID查询用户: {}", id);
        Optional<User> userOptional = userRepository.findById(id);
        return userOptional.orElse(null);
    }

    @Override
    @Transactional(readOnly = true)
    public User findByUsername(String username) {
        logger.info("根据用户名查询用户: {}", username);
        return userRepository.findByUsername(username);
    }

    @Override
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
        
        return userRepository.save(user);
    }

    @Override
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
        
        return userRepository.save(user);
    }

    @Override
    public boolean deleteById(Long id) {
        logger.info("删除用户: {}", id);
        
        User user = findById(id);
        if (user == null) {
            return false;
        }
        
        userRepository.deleteById(id);
        return true;
    }

    @Override
    @Transactional(readOnly = true)
    public boolean existsByUsername(String username) {
        return userRepository.existsByUsername(username);
    }

    @Override
    @Transactional(readOnly = true)
    public boolean existsByEmail(String email) {
        return userRepository.existsByEmail(email);
    }

    @Override
    @Transactional(readOnly = true)
    public List<User> findByPage(int page, int size) {
        logger.info("分页查询用户: page={}, size={}", page, size);
        Pageable pageable = PageRequest.of(page, size);
        Page<User> userPage = userRepository.findAll(pageable);
        return userPage.getContent();
    }

    @Override
    @Transactional(readOnly = true)
    public long count() {
        return userRepository.count();
    }
}