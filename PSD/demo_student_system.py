#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YooBee学院学生信息管理系统演示脚本
演示系统的核心功能：添加、更新、删除和查询学生信息
"""

from student_management_system import StudentManagementSystem

def demo_system():
    """演示学生管理系统的功能"""
    print("="*60)
    print("        YooBee学院学生信息管理系统演示")
    print("="*60)
    
    # 创建系统实例
    system = StudentManagementSystem()
    
    # 演示1: 添加学生
    print("\n1. 演示添加学生功能:")
    print("-" * 40)
    
    # 添加几个测试学生
    test_students = [
        ("张三", "北京市朝阳区", 20),
        ("李四", "上海市浦东新区", 19),
        ("王五", "广州市天河区", 21),
        ("赵六", "深圳市南山区", 22)
    ]
    
    for name, address, age in test_students:
        success = system.add_student(name, address, age)
        if success:
            print(f"✓ 成功添加学生: {name}")
        else:
            print(f"✗ 添加学生失败: {name}")
    
    # 演示2: 显示所有学生
    print("\n2. 演示显示所有学生功能:")
    print("-" * 40)
    system.get_all_students()
    
    # 演示3: 查询学生信息
    print("\n3. 演示查询学生信息功能:")
    print("-" * 40)
    
    # 查询特定学生
    search_names = ["张", "李", "王"]
    for search_name in search_names:
        print(f"\n搜索包含 '{search_name}' 的学生:")
        system.query_student_by_name(search_name)
    
    # 演示4: 更新学生信息
    print("\n4. 演示更新学生信息功能:")
    print("-" * 40)
    
    # 更新第一个学生的信息
    print("更新张三的地址和年龄:")
    success = system.update_student(1, "北京市海淀区", 21)
    if success:
        print("✓ 更新成功！")
    else:
        print("✗ 更新失败！")
    
    # 再次显示所有学生以查看更新结果
    print("\n更新后的学生信息:")
    system.get_all_students()
    
    # 演示5: 删除学生
    print("\n5. 演示删除学生功能:")
    print("-" * 40)
    
    # 删除最后一个学生
    print("删除赵六:")
    success = system.delete_student(4)
    if success:
        print("✓ 删除成功！")
    else:
        print("✗ 删除失败！")
    
    # 显示删除后的学生列表
    print("\n删除后的学生信息:")
    system.get_all_students()
    
    print("\n" + "="*60)
    print("演示完成！系统功能正常。")
    print("您可以运行 'python student_management_system.py' 来使用完整的交互式系统。")
    print("="*60)

if __name__ == "__main__":
    demo_system()

