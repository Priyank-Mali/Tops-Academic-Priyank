# Write a Python program to find the repeated items of a tuple. 

my_tuple = (1,2,3,4,5,3,1,1,3,4,5,9,3,0,1,3,4,5)

emp_dict = {}

for i in my_tuple:
    if i in emp_dict.keys():
        emp_dict[i] = emp_dict[i] + 1
    else:
        emp_dict[i] = 1
print(emp_dict)
