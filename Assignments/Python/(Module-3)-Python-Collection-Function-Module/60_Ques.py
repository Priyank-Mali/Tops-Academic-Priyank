# Write a Python program to calculate the area of a trapezoid 

def areaTrapezoid(a,b,h):
    area = ((a+b)/2)*h
    return area

base1 = int(input("Enter first base of trapezoid: "))
base2 = int(input("Enter second base of trapezoid: "))
height = int(input("Enter height of trapezoid: "))

print("The area of Trapezoid is: ",areaTrapezoid(base1,base2,height))