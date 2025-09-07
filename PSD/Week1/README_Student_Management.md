# YooBee学院学生信息管理系统

## 系统概述

这是一个为YooBee学院开发的Python学生信息管理系统，使用SQLite数据库存储学生数据。系统提供了完整的学生信息管理功能，包括添加、更新、删除和查询学生信息。

## 功能特性

### 1. 添加新学生
- 输入学生姓名、地址和年龄
- 自动生成唯一的学生ID
- 数据验证和错误处理

### 2. 更新学生信息
- 根据学生ID更新地址和年龄
- 检查学生是否存在
- 提供操作确认和反馈

### 3. 删除学生
- 根据学生ID删除学生记录
- 删除前确认操作
- 安全的数据删除

### 4. 查询学生信息
- 支持按姓名模糊查询
- 显示完整的学生信息
- 支持部分匹配搜索

### 5. 显示所有学生
- 按ID排序显示所有学生
- 统计学生总数
- 清晰的信息展示

## 系统要求

- Python 3.6+
- SQLite3 (Python内置)
- 无需额外安装依赖包

## 文件结构

```
PSD/
├── student_management_system.py    # 主系统文件
├── demo_student_system.py          # 演示脚本
├── README_Student_Management.md    # 说明文档
├── yb_college.db                  # 数据库文件
└── check_db.py                    # 数据库检查工具
```

## 使用方法

### 方法1: 运行完整系统
```bash
python student_management_system.py
```

这将启动交互式菜单系统，您可以：
- 选择1-6的操作选项
- 按照提示输入相关信息
- 查看操作结果和反馈

### 方法2: 运行演示脚本
```bash
python demo_student_system.py
```

这将自动演示系统的所有功能：
- 添加测试学生数据
- 展示查询和更新功能
- 演示删除操作
- 验证系统完整性

### 方法3: 作为模块使用
```python
from student_management_system import StudentManagementSystem

# 创建系统实例
system = StudentManagementSystem()

# 添加学生
system.add_student("张三", "北京市朝阳区", 20)

# 查询学生
students = system.query_student_by_name("张")

# 更新学生信息
system.update_student(1, "北京市海淀区", 21)

# 删除学生
system.delete_student(1)
```

## 数据库结构

系统使用SQLite数据库，包含以下表结构：

### student表
- `student_id`: 学生ID (主键，自增)
- `student_name`: 学生姓名 (必填)
- `address`: 学生地址
- `age`: 学生年龄

## 系统特点

### 安全性
- 使用参数化查询防止SQL注入
- 输入验证和类型检查
- 异常处理和错误恢复

### 用户友好
- 清晰的中文界面
- 直观的菜单系统
- 详细的操作反馈

### 可扩展性
- 模块化设计
- 易于添加新功能
- 支持自定义数据库路径

## 错误处理

系统包含完善的错误处理机制：
- 数据库连接错误
- 输入验证错误
- 数据操作失败
- 文件不存在错误

## 开发说明

### 添加新功能
1. 在`StudentManagementSystem`类中添加新方法
2. 在`display_menu()`中添加菜单选项
3. 在`run()`方法中添加处理逻辑
4. 创建相应的处理函数

### 修改数据库结构
1. 修改`init_database()`方法中的表结构
2. 更新相关的CRUD操作
3. 测试数据完整性

## 故障排除

### 常见问题

1. **数据库文件不存在**
   - 系统会自动创建新的数据库文件
   - 检查文件权限和路径

2. **Python版本不兼容**
   - 确保使用Python 3.6或更高版本
   - 检查类型注解语法

3. **数据库锁定错误**
   - 确保没有其他程序正在使用数据库
   - 重启应用程序

### 调试模式
在代码中添加调试信息：
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 版本历史

- v1.0: 初始版本，包含基本的CRUD操作
- 支持学生信息的增删改查
- 完整的用户界面和错误处理

## 联系方式

如有问题或建议，请联系系统管理员。

---

**注意**: 这是一个演示系统，生产环境使用前请进行充分测试和安全评估。



