from django.db import models

from master.models import BaseModel
# Create your models here.

class Student(BaseModel):
    student_id = models.CharField(max_length=100,primary_key=True,blank=True)
    first_name = models.CharField(max_length=255,blank=False)
    last_name = models.CharField(max_length=255,blank=False)
    email = models.EmailField(max_length=255,unique=True,blank=False)
    mobile = models.CharField(max_length=50,unique=True,blank=False)
    password = models.CharField(max_length=100,blank=True)

    def save(self,*args,**kwargs):
        if not self.pk:
            month = 