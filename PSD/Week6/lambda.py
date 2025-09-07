


students = [
    {'name': "John", 'grade': "A", 'age': 20}, 
    {'name': "Jane", 'grade': "B", 'age': 21}, 
    {'name': "Joss", 'grade': "A+", 'age': 19}, 
    {'name': "Jack", 'grade': "A-", 'age': 16}, 
    {'name': "Dave", 'grade': "C", 'age': 25}, 
    {'name': "Michael", 'grade': "A", 'age': 25}
]

sorted_age = sorted(students, key=lambda x: x['age'], reverse=True)
print(sorted_age)

sorted_grade = sorted(students, key= lambda x: x['grade'])
print(sorted_grade)

grade_order = {"A+": 1, "A": 2, "A-": 3, "B": 4, "C": 5}
sorted_grade1 = sorted(students, key = lambda x: grade_order[x['grade']])
print(sorted_grade1)