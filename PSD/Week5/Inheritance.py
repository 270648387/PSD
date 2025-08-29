class Person:
    def __init__(self, name, address, age, person_id):
        self.person_id = person_id
        self.name = name
        self.address = address
        self.age = age
    
    def display_info(self):
        return f"Name:{self.name}, Address:{self.address}, Age:{self.age}, ID:{self.person_id}, "

class Student(Person):
    def __init__(self, name, address, age, student_id):
        super().__init__(name, address, age, student_id)
        self.student_id = student_id
    
    def display_info(self):
        #overriding display_info from Person
        return f"|Student|  {super().display_info()}"

class Staff(Person):
    def __init__(self, name, address, age,staff_id):
        super().__init__(name, address, age, staff_id)
        self.staff_id = staff_id
    
    def display_info(self):
        #overriding display_info from Person
        return f"|Staff|  {super().display_info()}"

if __name__ == "__main__":
    student1 = Student("Michael", "3 City Road", 25, 1001)
    staff1 = Staff("Arun", "3 City Road", 30, 10001)
    
    print(student1.display_info())
    print(staff1.display_info())