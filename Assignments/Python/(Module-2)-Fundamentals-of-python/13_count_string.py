# •	Write a Python program to count the number of characters (character frequency) in a string 

str_input = input("Enter any string: ")
count = 0
for ch in str_input:
    print(ch,end=" ")
    count+=1
print()
print("No.of character in string is:",count)
