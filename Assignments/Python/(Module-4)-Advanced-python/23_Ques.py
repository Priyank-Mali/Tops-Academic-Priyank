# •	Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle 

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area_rectangle(self):
        return f"The area of rectangle is: {self.length*self.width}"

rec = Rectangle(11,12)
print(rec.area_rectangle())