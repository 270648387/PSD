data = ['a5', 'a2', 'b1', 'b3', 'c2', 'c10']
print(sorted(data))

['a2', 'a5', 'b1', 'b3', 'c10', 'c2']


data = ['a5', 'a2', 'b1', 'b3', 'c2', 'c10']
sorted_data = sorted(data,key=lambda x: (x[0], int(x[1:])))
print(sorted_data)

['a2', 'a5', 'b1', 'b3', 'c2', 'c10']

sorted by the first character, in this case the first letter
x[0] represnts the first letter,
int(x[1:]) represents for everything after the first character as an integer, if its not integer an error will occur
lambda serves as a function that transforms attribute like a5 to a list [a,5]
then its sorted by the first letter