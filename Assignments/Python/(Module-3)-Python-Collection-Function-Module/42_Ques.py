# Write a Python program to print all unique values in a dictionary. 

my_dict1 = {
    'a': 100, 
    'b': 200, 
    'c':300,
    'd': 300, 
    'e': 200, 
    'f':400
    }

emp_list = []
for key,value in my_dict1.items():
    if value not in emp_list:
        emp_list.append(value)
print("unique values are: ",emp_list)
