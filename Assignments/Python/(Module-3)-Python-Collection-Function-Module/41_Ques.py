# Write a Python program to combine two dictionary adding values for common keys. 
# d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400} 
# Sample output: Counter ({'a': 400, 'b': 400,'c': 300 ,'d':400}). 

my_dict1 = {'a': 100, 'b': 200, 'c':300}
my_dict2 = {'a': 300, 'b': 200, 'd':400}

final_dict = my_dict1.copy()

for key,value in my_dict2.items():
    if key in final_dict:
        final_dict[key] = final_dict[key] + value
    else:
        final_dict[key] = value

print(final_dict)