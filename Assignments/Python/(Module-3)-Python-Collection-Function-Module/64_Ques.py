# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers. 

def maximum(list):
    max = float("-inf")
    for i in list:
        if i>max:
            max = i
    return max

def minimum(list):
    min = float("inf")
    for i in list:
        if i<min:
            min = i
    return min

my_list = [1.3,2.5,0.4,5.6,-1.6,-2.3]

print("Maximum number among the list is: ",maximum(my_list))
print("Minimum number among the list is: ",minimum(my_list))
