class Student:
    def __init__(self, name, age):
        self.name = name # public​

        self._age = age # protected​

        self.__grade = 'A' # private​


    def get_grade(self):

        return self.__grade
    
    def set_grade(self, grade):
        
        self.__grade = grade




s = Student('Ali', 20)

print(s.name) # accessible​

print(s._age) # discouraged​

print(s.get_grade()) # correct way​

s.set_grade("B")

print(f"New Grade: {s.get_grade()}")



class Teacher:
    def __init__(self, name, subject):
          self.name = name
          self._subject = subject
          self.__salary = 2000
    
    def get_salary(self):
        return self.__salary 
    
    def set_salary(self, salary):
        self.__salary = salary

t = Teacher('Bob', 'Python')

print(t.name)
print(t._subject)
print(t.get_salary())

t.set_salary(4000)

print(f"New Salary: {t.get_salary()}")