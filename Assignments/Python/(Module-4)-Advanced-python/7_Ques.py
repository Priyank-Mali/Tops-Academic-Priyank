# Write a Python program to read a file line by line store it into a variable. 

file = open("7_ques.txt",'r')
file_list = file.readlines()

for line in file_list:
    print(line)
file.close()
