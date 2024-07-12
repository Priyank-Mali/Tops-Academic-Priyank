# Write a Python program to check whether a list contains a sub list 

my_list = [1,2,34,[23,45,7],0]

flag = False
for i in my_list:
    if isinstance(i,list):
        flag = True
        break
if flag:
     print("The list contain sublist")
else:
    print("the list does not contain sublist")