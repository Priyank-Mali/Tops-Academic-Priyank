# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30

my_list = range(1,31)
square = [i**2 for i in range(1,31)]

print(square[:5] + square[-5:])
