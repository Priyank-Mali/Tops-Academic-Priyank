# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. 
# Sample data: {'1': ['a','b'], '2': ['c','d']} Expected Output: ac ad bc bd 

my_dict = {
    '1':['a','b'],
    '2':['c','d']
}

emp_list = []

for item1 in my_dict['1']:
    for item2 in my_dict['2']:
        emp_list.append((item1+item2))

str = " ".join(emp_list)
print(str)


    
        