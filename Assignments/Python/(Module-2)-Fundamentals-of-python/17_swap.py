# Write a Python program to get a single string from two given strings, 
# separated by a space and swap the first two characters of each string.

str_1 = input("Enter First string: ")
str_2 = input("Enter Second string: ")

full_str = str_1 +" "+ str_2
print("Before swaping:",full_str)

temp = str_1[0:1]
str_1 = str_2[0:1] + str_1[1:]
str_2 = temp + str_2[1:] 
    
full_str = str_1 + " " + str_2

print("After swapping:",full_str)
