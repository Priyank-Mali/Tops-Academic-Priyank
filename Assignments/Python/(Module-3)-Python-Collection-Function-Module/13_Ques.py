# Write a Python program to select an item randomly from a list. 

import random

my_list = ['p','r','i','y','a','n','k']

randomNum = random.randint(0,len(my_list))
randomChar = my_list[randomNum]
print(randomChar)