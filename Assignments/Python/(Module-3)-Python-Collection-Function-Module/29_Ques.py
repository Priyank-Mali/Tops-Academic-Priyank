# Write a Python program to unzip a list of tuples into individual lists. 

my_list = [("name","priyank"),("surname","mali"),("age",99)]

list1 = []
list2 = []

for i in my_list:
    list1.append(i[0])
    list2.append(i[1])
print("List 1: ",list1)
print("List 2: ",list2)