# Write a Python program to get the Fibonacci series of given range.

a = 0
b = 1
num = int(input("range of fibonacci series: "))
print(a,b,end=" ")
for i in range(1,(num+1)-2):
    sum = a+b
    a = b
    b = sum
    print(sum,end=" ")

