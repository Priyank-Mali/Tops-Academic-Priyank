# Write a Python program to convert degree to radian 

def degreeConverter(deg):
    radian = deg * (3.14 / 180)
    return radian

input_degree = float(input("Enter any Degree: "))
print(degreeConverter(input_degree))