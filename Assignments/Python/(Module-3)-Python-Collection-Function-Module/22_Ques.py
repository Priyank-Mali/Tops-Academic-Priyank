# Write a Python program to check whether an element exists within a tuple. 


my_tuple = (1,2,3,4,5,6,7,8,9,10)

check_element = int(input("Enter element: "))
if check_element in my_tuple:
    print(f"{check_element} is present in my tuple")
else:
    print(f"{check_element} is not present in my tuple")