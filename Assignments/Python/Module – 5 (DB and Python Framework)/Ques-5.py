# What is a QuerySet ? Write program to create a new Post object in database:

"""
In Django, QuerySet is a collection of databases queries that represent a set of objects from our databses

QuearySets allow to read the data from the databse , filter it , and manipulate it
"""


from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=255,primary_key=True)
    first_name = models.CharField(max_length=255,blank=False)
    last_name = models.CharField(max_length=255,blank=False)
    email = models.EmailField(max_length=255,unique=True)

    def __str__(self):
        return self.student_id
    
from myapp.models import Student

all_students = Student.ojects.all()

get_student = Student.objects.get(student_id = 'STU0001')


new_student = Student(
    student_id = 'STU002',
    first_name = 'priyank',
    last_name  = 'mali',
    email      = 'test@gmail.com'
)
new_student.save()
