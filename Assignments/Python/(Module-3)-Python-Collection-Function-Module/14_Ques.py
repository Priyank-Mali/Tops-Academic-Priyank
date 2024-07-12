# Write a Python program to find the second smallest number in a list. 


my_list = [10,20,40,-10,0,-1,-9,44,-19,44,21]

min = float("inf")
smin = float("inf")

for i in my_list:
    if i<min:
        min = i
for i in my_list:
    if i<smin and i!=min:
        smin = i

print("First minimum number is:",min)
print("Second minimum number is:",smin)