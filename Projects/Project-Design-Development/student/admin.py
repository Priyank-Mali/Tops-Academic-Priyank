from django.contrib import admin
from .models import Student,StudentProfile,studentAddress,StudentCourse,StudentPayment,StudentPaymentEntry

# Register your models here.

admin.site.register(Student)
admin.site.register(StudentProfile)
admin.site.register(studentAddress)
admin.site.register(StudentCourse)
admin.site.register(StudentPayment)
admin.site.register(StudentPaymentEntry)