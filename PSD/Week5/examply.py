# Week 5 Activity 6: Demonstrating Encapsulation in Python

# It uses access specifiers: public (no underscore), protected (_), and private (__).
# This helps to prevent misuse and provides controlled access using methods.

class Student:
    def __init__(self, name, age):
        self.name = name             # Public attribute – freely accessible
        self._age = age              # Protected attribute – internal use, subclasses allowed
        self.__grade = 'A'           # Private attribute – only accessible within the class

    def get_grade(self):
        """Getter method to safely access the private attribute __grade."""
        return self.__grade

    def promote_if_excellent(self):
        """
        New method that uses the private attribute.
        Business logic: Promote the student if grade is A.
        """
        if self.__grade == 'A':
            return f"{self.name} is promoted to the next academic year!"
        else:
            return f"{self.name} needs improvement before promotion."

# A separate class to demonstrate public and protected attribute usage
class StudentMentor:
    def __init__(self, student: Student):
        self.student = student

    def show_student_profile(self):
        print("--- Student Profile (Mentor View) ---")
        # Accessing public attribute
        print(f"Name: {self.student.name}")         # ✅ Allowed

        # Accessing protected attribute (allowed but discouraged outside subclass)
        print(f"Age: {self.student._age}")          # ⚠️ Technically allowed, use with care

        # Can't access private attribute directly
        # print(self.student.__grade)              ❌ Will raise AttributeError

        # Use the getter method instead
        print(f"Grade: {self.student.get_grade()}") # ✅ Best practice

# --- Example Usage ---
if __name__ == "__main__":
    student = Student("MJ", 23)

    # Direct access demonstration
    print("--- Direct Access ---")
    print(student.name)           # ✅ Public: allowed
    print(student._age)           # ⚠️ Protected: discouraged
    print(student.get_grade())    # ✅ Private: accessed via getter
    print(student.promote_if_excellent())  # ✅ Uses private attribute internally

    print()

    # Use of another class to access attributes
    mentor = StudentMentor(student)
    mentor.show_student_profile()