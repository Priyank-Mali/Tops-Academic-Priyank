# Write a Python program to calculate surface volume and area of a cylinder 

"""
cylinder volume: pi*r^2*h
surface area : 2*pi*r*h + 2*pi*r^2
"""
def cylinderVolume(radius,height):
    return 3.14*(radius**2)*height

def cylinderSurfaceArea(radius,height):
    return ((2*3.14*radius*height) + (2*3.14*radius**2))

radiusInput = int(input("Enter cylinder radius: "))
heightInput = int(input("Enter cylinder height: "))

print(f"Cylinder volume is: {cylinderVolume(radiusInput,heightInput)}")
print(f"Cylinder surface area is: {cylinderSurfaceArea(radiusInput,heightInput)}")