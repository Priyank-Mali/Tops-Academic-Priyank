# •	Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python? 

"""
-> Inheritance allows us to define a class that inherits all the methods and properties from another class.
--> __init__ in python is used to initialize objects of a class
--> it is also called a constructor.
--> constructor is to assign value to the data member of class when an object of class is created.
"""

# class Animal:
#     def eat(self):
#         return 'I can eat'
# class Dog(Animal):
#     def speak(self):
#         return "bhow bhow"
# class Cat(Animal):
#     def speak(self):
#         return "Meow moew"
# dog = Dog()
# print(dog.eat())
# print(dog.speak())


"""
1.) Single level inheritance:
"""
# class Person():
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
#     def display(self):
#         print("Name: ",self.name,"ID: ",self.id)

# class Employee(Person):
#     pass

# obj = Employee('priyank',11)
# obj.display()


"""
2.) Multilevel inheritance:
"""

# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def eat(self):
#         return f'{self.name} is eating'
# class Dog(Animal):
#     def __init__(self,name,type):
#         super().__init__(name)
#         self.type = type
#     def speak(self):
#         return "Bho bho"
# class Pet(Dog):
#     def __init__(self,name,type,masti):
#         super().__init__(name,type)
#         self.masti = masti

# obj = Pet('Tommy','Pomerian','Runfast')
# print(obj.name)
# print(obj.speak())
# print(obj.masti)


"""
3.) Multiple inheritance:
"""

# class A:
#   def a(self):
#     return "I am form class A"

# class B:
#   def b(self):
#     return "I am form class B"

# class C(A,B):
#   def c(self):
#     return "I am form class C"

# obj = C()
# print(obj.a())
# print(obj.b())
# print(obj.c())


"""
4.) Hierarchical Inheritance:
"""
# class animal():
#   def __init__(self,name):
#     self.name = name
#   def eat(self):
#     return "i can eat"

# class dog(animal):
#   def __init__(self,name,type):
#     super().__init__(name)
#     self.type = type
#   def speak(self):
#     return "bho bho"

# class cat(animal):
#   def __init__(self,name,color):
#     super().__init__(name)
#     self.color = color
#   def speak(self):
#     return "meow meow"
  
# obj_dog = dog('Tommy','Pomerian')
# print(obj_dog.name)
# print(obj_dog.speak())
# print(obj_dog.eat())


"""
5.) Hybrid Inheritance:
"""

# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# class D(B,C):
#     pass

