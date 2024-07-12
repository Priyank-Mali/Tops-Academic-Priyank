# How can you pick a random item from a list or tuple? 

# by using random library

import random

my_tuple = (1,2,3,4,5,6,7)
my_list = ["priyank","rahul","kalam","ramesh"]

randomNum = random.randrange(0,len(my_tuple))
randomNum1 = random.randrange(0,len(my_list))

print(my_tuple[randomNum])
print(my_list[randomNum1])