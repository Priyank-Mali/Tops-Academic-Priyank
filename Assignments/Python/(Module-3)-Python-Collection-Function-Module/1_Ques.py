"""
What is List? How will you reverse a list? 
"""

# In Python, a list is built-in data structure used to store a collection of items. 
# It's ordered and mutable, meaning you can change, add, and remove elements after it's created. 
# Lists can contain elements of different types, including integers, floats, strings, or even other lists. 

#---(method 1)---------------------
my_list = ["priyank","mali"]
rev_list = my_list[::-1]
print(rev_list) #['mali', 'priyank']


#-----(method 2)-------------------------------
my_list = ["priyank","mali"]
rev_list = []
i = len(my_list)-1
while i>=0:
    rev_list.append(my_list[i])
    i = i - 1   
print(rev_list)