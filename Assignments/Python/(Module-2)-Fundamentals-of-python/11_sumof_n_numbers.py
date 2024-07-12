# •	Write a python program to sum of the first n positive integers

num = int(input("Enter range of number: "))
sum = 0
for numbers in range(1,num+1):
    sum = sum + numbers
print(sum,end=" ")
    