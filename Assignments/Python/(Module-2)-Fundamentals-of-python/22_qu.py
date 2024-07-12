# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
# If the string length is less than 2, return instead of the empty string.

input_str = input("Enter a string: ")

if len(input_str)<=2:
    print(input_str)
else:
    new_str = input_str[0:2] + input_str[-2:]
    print(new_str)

