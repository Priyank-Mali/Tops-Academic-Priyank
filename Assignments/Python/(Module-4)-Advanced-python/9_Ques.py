# Write a Python program to count the number of lines in a text file. 

file = open("9_ques.txt","r")
file_list = file.read().split("\n")
count = 0
for line in file_list:
    count += 1
print(count)
file.close()