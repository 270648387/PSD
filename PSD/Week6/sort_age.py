employees = [
    {'name': "Alice", 'age': 30, 'salary': 80000},
    {'name': "Bob", 'age': 25, 'salary': 50000},
    {'name': "Charlie", 'age': 35, 'salary': 120000},
    {'name': "Michael", 'age': 35, 'salary': 220000},
    ]

#sort by age then by salary if age is same
sorted_age = sorted(employees, key = lambda x: (x['age'], -x['salary']))
print(sorted_age)


def sort_key(x):
    return (x['age'], -x['salary'])
sorted_age1 = sorted(employees, key = sort_key)

print(sorted_age1)