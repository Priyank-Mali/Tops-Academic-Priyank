# Write a Python program to get unique values from a list 

my_list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

unique_list = []

for i in my_list:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)