# Write a Python program to find the highest 3 values in a dictionary 

my_dict = {
    'a':10,
    'b':20,
    'c':30,
    'd':40,
    'e':50
}

new_list = sorted(my_dict.items(),key= lambda x:x[1])
highest = dict(new_list[::-1][:3])
print("The highest value in dictionary are: ",highest)