# •	Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))
num3 = int(input("Enter Third number: "))

if (num1==num2) or (num1==num3) or (num2==num3 ):
    print("Sum is Zero\nBcoz You entered same number\nDo you want sum then enter different numbers. ")
else:
    sum = num1+num2+num3
    print("Sum of Three Number is: ",sum)
