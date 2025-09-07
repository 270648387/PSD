import sqlite3
import os
from typing import Optional, List, Tuple

class StudentManagementSystem:
    def __init__(self, db_path: str = 'yb_college.db'):
        """初始化学生管理系统"""
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """初始化数据库，如果student表不存在则创建，如果存在则添加缺失的字段"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # 检查student表是否存在
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='student'")
            table_exists = cursor.fetchone()
            
            if not table_exists:
                # 创建新的student表
                cursor.execute("""
                    CREATE TABLE student (
                        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_name TEXT NOT NULL,
                        address TEXT,
                        age INTEGER
                    )
                """)
                print("创建了新的student表")
            else:
                # 检查是否需要添加age字段
                cursor.execute("PRAGMA table_info(student)")
                columns = [col[1] for col in cursor.fetchall()]
                
                if 'age' not in columns:
                    # 添加age字段
                    cursor.execute("ALTER TABLE student ADD COLUMN age INTEGER")
                    print("为现有student表添加了age字段")
                else:
                    print("student表结构完整")
            
            conn.commit()
            conn.close()
            print("数据库初始化完成！")
            
        except Exception as e:
            print(f"数据库初始化错误: {e}")
    
    def add_student(self, name: str, address: str, age: int) -> bool:
        """添加新学生
        
        Args:
            name: 学生姓名
            address: 学生地址
            age: 学生年龄
            
        Returns:
            bool: 添加是否成功
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute("""
                INSERT INTO student (student_name, address, age)
                VALUES (?, ?, ?)
            """, (name, address, age))
            
            conn.commit()
            conn.close()
            
            print(f"成功添加学生: {name}")
            return True
            
        except Exception as e:
            print(f"添加学生失败: {e}")
            return False
    
    def update_student(self, student_id: int, address: str, age: int) -> bool:
        """更新学生信息
        
        Args:
            student_id: 学生ID
            address: 新地址
            age: 新年龄
            
        Returns:
            bool: 更新是否成功
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # 检查学生是否存在
            cursor.execute("SELECT student_name FROM student WHERE student_id = ?", (student_id,))
            student = cursor.fetchone()
            
            if not student:
                print(f"未找到ID为 {student_id} 的学生")
                conn.close()
                return False
            
            cursor.execute("""
                UPDATE student 
                SET address = ?, age = ?
                WHERE student_id = ?
            """, (address, age, student_id))
            
            conn.commit()
            conn.close()
            
            print(f"成功更新学生 {student[0]} 的信息")
            return True
            
        except Exception as e:
            print(f"更新学生信息失败: {e}")
            return False
    
    def delete_student(self, student_id: int) -> bool:
        """删除学生
        
        Args:
            student_id: 学生ID
            
        Returns:
            bool: 删除是否成功
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # 检查学生是否存在
            cursor.execute("SELECT student_name FROM student WHERE student_id = ?", (student_id,))
            student = cursor.fetchone()
            
            if not student:
                print(f"未找到ID为 {student_id} 的学生")
                conn.close()
                return False
            
            cursor.execute("DELETE FROM student WHERE student_id = ?", (student_id,))
            
            conn.commit()
            conn.close()
            
            print(f"成功删除学生: {student[0]}")
            return True
            
        except Exception as e:
            print(f"删除学生失败: {e}")
            return False
    
    def query_student_by_name(self, name: str) -> List[Tuple]:
        """根据姓名查询学生信息
        
        Args:
            name: 学生姓名
            
        Returns:
            List[Tuple]: 学生信息列表
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT student_id, student_name, address, age
                FROM student 
                WHERE student_name LIKE ?
            """, (f'%{name}%',))
            
            students = cursor.fetchall()
            conn.close()
            
            if students:
                print(f"找到 {len(students)} 个匹配的学生:")
                for student in students:
                    age_display = student[3] if student[3] is not None else "未设置"
                    print(f"ID: {student[0]}, 姓名: {student[1]}, 地址: {student[2]}, 年龄: {age_display}")
            else:
                print(f"未找到姓名包含 '{name}' 的学生")
            
            return students
            
        except Exception as e:
            print(f"查询学生信息失败: {e}")
            return []
    
    def get_all_students(self) -> List[Tuple]:
        """获取所有学生信息
        
        Returns:
            List[Tuple]: 所有学生信息列表
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT student_id, student_name, address, age
                FROM student 
                ORDER BY student_id
            """)
            
            students = cursor.fetchall()
            conn.close()
            
            if students:
                print(f"数据库中共有 {len(students)} 个学生:")
                for student in students:
                    age_display = student[3] if student[3] is not None else "未设置"
                    print(f"ID: {student[0]}, 姓名: {student[1]}, 地址: {student[2]}, 年龄: {age_display}")
            else:
                print("数据库中暂无学生信息")
            
            return students
            
        except Exception as e:
            print(f"获取所有学生信息失败: {e}")
            return []
    
    def display_menu(self):
        """显示主菜单"""
        print("\n" + "="*50)
        print("        YooBee学院学生信息管理系统")
        print("="*50)
        print("1. 添加新学生")
        print("2. 更新学生信息")
        print("3. 删除学生")
        print("4. 查询学生信息")
        print("5. 显示所有学生")
        print("6. 退出系统")
        print("="*50)
    
    def run(self):
        """运行学生管理系统"""
        while True:
            self.display_menu()
            choice = input("请选择操作 (1-6): ").strip()
            
            if choice == '1':
                self.handle_add_student()
            elif choice == '2':
                self.handle_update_student()
            elif choice == '3':
                self.handle_delete_student()
            elif choice == '4':
                self.handle_query_student()
            elif choice == '5':
                self.get_all_students()
            elif choice == '6':
                print("感谢使用YooBee学院学生信息管理系统！")
                break
            else:
                print("无效选择，请重新输入！")
            
            input("\n按回车键继续...")
    
    def handle_add_student(self):
        """处理添加学生操作"""
        print("\n--- 添加新学生 ---")
        name = input("请输入学生姓名: ").strip()
        if not name:
            print("学生姓名不能为空！")
            return
        
        address = input("请输入学生地址: ").strip()
        age_str = input("请输入学生年龄: ").strip()
        
        try:
            age = int(age_str) if age_str else 0
            if age < 0 or age > 150:
                print("年龄必须在0-150之间！")
                return
        except ValueError:
            print("年龄必须是数字！")
            return
        
        self.add_student(name, address, age)
    
    def handle_update_student(self):
        """处理更新学生信息操作"""
        print("\n--- 更新学生信息 ---")
        student_id_str = input("请输入学生ID: ").strip()
        
        try:
            student_id = int(student_id_str)
        except ValueError:
            print("学生ID必须是数字！")
            return
        
        address = input("请输入新地址: ").strip()
        age_str = input("请输入新年龄: ").strip()
        
        try:
            age = int(age_str) if age_str else 0
            if age < 0 or age > 150:
                print("年龄必须在0-150之间！")
                return
        except ValueError:
            print("年龄必须是数字！")
            return
        
        self.update_student(student_id, address, age)
    
    def handle_delete_student(self):
        """处理删除学生操作"""
        print("\n--- 删除学生 ---")
        student_id_str = input("请输入要删除的学生ID: ").strip()
        
        try:
            student_id = int(student_id_str)
        except ValueError:
            print("学生ID必须是数字！")
            return
        
        confirm = input(f"确定要删除ID为 {student_id} 的学生吗？(y/N): ").strip().lower()
        if confirm in ['y', 'yes']:
            self.delete_student(student_id)
        else:
            print("取消删除操作")
    
    def handle_query_student(self):
        """处理查询学生信息操作"""
        print("\n--- 查询学生信息 ---")
        name = input("请输入学生姓名(支持模糊查询): ").strip()
        if not name:
            print("学生姓名不能为空！")
            return
        
        self.query_student_by_name(name)

def main():
    """主函数"""
    print("欢迎使用YooBee学院学生信息管理系统！")
    
    # 检查数据库文件是否存在
    if not os.path.exists('yb_college.db'):
        print("正在创建新的数据库文件...")
    
    # 创建并运行系统
    system = StudentManagementSystem()
    system.run()

if __name__ == "__main__":
    main()
