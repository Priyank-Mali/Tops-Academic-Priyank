# Write python program that swap two number with temp variable and without temp variable.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

temp = num2
num2 = num1
num1 = temp
print("Using Temp Variable.")
print(f"the swapping numbers are num1 = {num1} and num2 = {num2}" )


num3 = int(input("Enter first number: "))
num4 = int(input("Enter second number: "))

# num3,num4 = num4,num3
# print(num3,num4)

num3 = num3 + num4
num4 = num3 - num4
num3 = num3 - num4
print("Without Temp Variable.")
print(f"swapping numbers are num3 = {num3} and num4 = {num4}")




