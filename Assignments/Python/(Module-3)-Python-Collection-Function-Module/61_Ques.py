# Write a Python program to calculate the area of a parallelogram 

def area(base,height):
    return base*height

baseInput = int(input("Enter base of parallelogram: "))
heightInput = int(input("Enter height of parallelogram: "))
print("The area of parallellogram is: ",area(baseInput,heightInput))