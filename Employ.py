class Employee:
    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary
        self.job_title = job_title

    def display_info(self):
        print(f"Name: {self.name}\nSalary: ${self.salary}\nJob Title: {self.job_title}\n")

    def give_raise(self, amount):
        self.salary += amount
        print(f"Give a raise of ${amount} to {self.name}. New salary: ${self.salary}\n")


def main():
    employee1 = Employee("Michael", 20000, "Software Engineer")
    employee2 = Employee("Tom", 18000, "Data Analyst")

    employee1.display_info()
    employee2.display_info()

    employee1.give_raise(5000)
    employee1.display_info()


if __name__ == "__main__":
    main()
