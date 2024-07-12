# •	What is used to check whether an object o is an instance of class A? 

class Car:
    def __init__(self,model):
        self.model = model

class Bike:
    def __init__(self,model):
        self.model = model
    
car1 = Car('Honda')
print(car1.model)
print(isinstance(car1,Car))
# if type(car1) == Car:
#     print('Car1 is an instance of Car')
# else:
#     print('Car1 is not an instance of Car')



bike1 = Bike('Yamaha')
print(bike1.model)
print(isinstance(bike1,Car))
