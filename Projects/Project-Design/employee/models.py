from django.db import models
from master.models import BaseModel
from django.core.mail import send_mail
import os

from master.utils.TA_UNIQE.random_password import generate_random_password

# Create your models here.

class Role(BaseModel):
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.role

class Employee(BaseModel):
    PRIFIX = "EMP"
    employee_id = models.CharField(primary_key=True,blank=True,max_length=255)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255,blank=False,null=False)
    last_name = models.CharField(max_length=255,blank=False,null=False)
    email = models.EmailField(max_length=255,blank=False,null=False,unique=True)
    mobile = models.CharField(max_length=255,blank=False,null=False,unique=True)
    password = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return f"{self.employee_id} {self.first_name} {self.last_name}"
    
    def save(self,*args,**kwargs):
        if not self.pk:
            last_employee = Employee.objects.order_by("-created_at").first()
            if last_employee:
                last_numeric_value = int(last_employee.employee_id[3:])
                new_numeric_value = last_numeric_value + 1
                # Format the new ID with the prefix and zero-padded numeric value
                new_id = f"{self.PRIFIX}{new_numeric_value:04}"
            else:
                new_id = f"{self.PRIFIX}0001"
            
            self.employee_id = new_id
            self.password = generate_random_password()

            subject = 'Your Login Credential for Tops Technology Pvt. Ltd.'
            message = f"""
                Dear {self.first_name} {self.last_name},

                Welcome to Tops Technology Pvt. Ltd.
                Your login credentials are as follows:

                Employee ID : {self.employee_id}
                password : {self.password}
                
                For security reasons, we recommend changing your password upon your first login. You can change your password by logging into your account and navigating to the settings or profile section.

                Please keep this information secure and do not share it with anyone. If you have any questions or need assistance, feel free to contact our support team.

                Best regards,
                Tops Technology Pvt. Ltd. Team
                """
            from_email = os.getenv("EMAIL_HOST_USER")
            recipient_list = [f"{self.email}"]

            send_mail(subject,message,from_email,recipient_list)
            #subject
            #message
            #from_email
            #recipient_list
            
        super(Employee,self).save(*args,**kwargs)
