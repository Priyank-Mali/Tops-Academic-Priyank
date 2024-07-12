# Write a Python program to read a random line from a file. 

import random

def readLines(file):
    file_list = file.readlines()
    return random.choice(file_list)

file = open("58_ques.txt",'r')
print(readLines(file))


