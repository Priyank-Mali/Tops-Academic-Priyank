from django.contrib import admin
from .models import Student,StudentProfile,studentAddress

# Register your models here.

admin.site.register(Student)
admin.site.register(StudentProfile)
admin.site.register(studentAddress)