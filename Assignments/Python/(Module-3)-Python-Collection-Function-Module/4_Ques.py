"""
Write a Python function to get the largest number, smallest num and sum of all from a list
"""

def maximum(list):   
    max = float("-inf")
    for i in range(0,len(list)):
        if list[i]>max:
            max = list[i]
    print("Maximum Number:",max)
    
def minimun(list):
    min = float("inf")
    for i in range(0,len(list)):
        if list[i]<min:
            min = list[i]
    print("Minimum Number:",min)

def sum(list):
    sum = 0
    for i in list:
        sum = sum + i
    print("Total is:",sum)


my_list = [11,32,45,-45,67,-1,0,34,45]

maximum(my_list)
minimun(my_list)
sum(my_list)



