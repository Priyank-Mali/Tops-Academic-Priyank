# •	Write a Python program to add 'ing' at the end of a given string 
# (length should be at least 3). If the given string already ends with 'ing' then add 'ly' 
# instead if the string length of the given string is less than 3, leave it unchanged. 

input_str = input("Enter a string: ")
print("Your string is:",input_str)
if len(input_str)<3:
    print("please Enter a string whose length is greater than 3")

elif len(input_str)<3:
    print(input_str)
else:
    if input_str.endswith("ing"):
        input_str= input_str + "ly"
    else:
        input_str = input_str + "ing"
print(input_str)