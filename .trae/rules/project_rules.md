# 项目核心
1. 项目脚本统一写在scripts 目录下
2. 项目配置统一写出configs目录下
3. 项目输出统一在output下
4. 项目有结构更新时，及时更新REDME.md文件

# 有测试脚本时的操作
1. 在每次生成测试脚本时， 都只能放在tests目录下,
2. 测试脚本的名称必须以test_开头,
3. 每次新增脚本时，都需要先在tests目录下， 查询是否存在类似的脚本， 如果存在，则需要校验验证功能是否一致，并迭代优化当前脚本

# 项目功能更新时操作
4. 每次项目功能更新时， 都需要更新测试脚本，确保测试脚本的功能与项目功能保持一致
5. 每次项目功能更新时， 需要对测试脚本进行回归测试，确保测试脚本的功能与项目功能保持一致
6. 每次项目功能更新时， 需要功能说明文档，进行功能说明文档的更新
7. 每次项目功能更新时， 需要代码注释，进行代码注释的更新
8. 每次项目功能更新时， 需要代码变更记录，进行代码变更记录的更新

# 项目变更记录
1. 每次生成的修改日志说明文档，应该记录在根目录下的logs 文件目录下
1. 每次生成变更日志时，创建的日志文件，适应归纳总结后的中文
2. 文件日志，需要按  序号-变更内容-变更时间 进行记录
3. 变更内容，需要详细描述变更的内容，变更的原因，变更的影响，变更的解决方案