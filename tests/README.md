# 测试配置文件

## 运行测试

### 运行所有测试
```bash
python -m pytest tests/ -v
```

### 运行特定测试文件
```bash
python -m pytest tests/test_config_validator.py -v
python -m pytest tests/test_config_collector.py -v
python -m pytest tests/test_context_generator.py -v
```

### 生成测试覆盖率报告
```bash
python -m pytest tests/ --cov=scripts --cov-report=html
```

## 测试结构

- `test_config_validator.py` - 配置验证器测试
- `test_config_collector.py` - 配置收集器测试  
- `test_context_generator.py` - 上下文生成器测试

## 测试数据

测试使用模拟数据和临时文件，不会影响实际项目文件。