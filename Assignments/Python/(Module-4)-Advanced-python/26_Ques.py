# •	What is Instantiation in terms of OOP terminology? 

"""
In Object-Oriented Programming , Instantiation is a process of creating an instance of class


"""
class Car:
    def __init__(self,model):
        self.model = model
    
car1 = Car('Honda')
print(car1.model)
car2 = Car('BMW')
print(car2.model)