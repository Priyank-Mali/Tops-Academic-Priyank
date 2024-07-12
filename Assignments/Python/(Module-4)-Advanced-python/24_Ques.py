# •	Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle 

class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def area_circle(self):
        return f"The area of circle is: {3.14*self.radius**2}"
    
    def perimeter(self):
        return f"The perimeter of circle is: {2*3.14*self.radius}"

obj = Circle(4)
print(obj.area_circle())
print(obj.perimeter())