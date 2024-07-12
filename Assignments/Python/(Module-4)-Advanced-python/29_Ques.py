# •	What relationship is appropriate for Student and Person? 

'''
IS a relationship 
-> student is a person
-> student class can inherit from a person class 
'''


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self,name,age,id):
        super().__init__(name,age)
        self.id = id

per = Person('priyank',99)
stu = Student('kalam',99,1111)

print(per.name,per.age)
print(stu.name,stu.age,stu.id)