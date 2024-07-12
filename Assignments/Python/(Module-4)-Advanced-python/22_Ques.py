# •	How to Define a Class in Python? What Is Self? Give An Example Of A Python Class 

"""
syntax: 

class class_name:
    # class variables
    # class method

obj = class_name()
"""

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def per_info(self):
        return f"Hello {self.name} your age is {self.age}"

per1 = person("priyank",99)
print(per1.per_info())


"""
-> When you define a method in a class, you typically use self as the first parameter of the method definition. 
-> However, when you call the method on an object, you don't need to explicitly pass self as an argument. 
-> Python automatically passes the instance itself to the method when it is called.
"""