# Write a Python program to remove an empty tuple(s) from a list of tuples. 

my_list = [(), (1, 2), ('a', 'b'), (), (3, 4, 5), ()]


for i in my_list:
    if i == ():
        my_list.remove(i)
print(my_list)

