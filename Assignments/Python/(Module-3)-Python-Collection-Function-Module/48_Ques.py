# Write a Python function to calculate the factorial of a number (a nonnegative integer) 

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    return fact


input_num = int(input("Enter any number: "))

print(f"The factorial of {input_num} is:",factorial(input_num))