from django.db import models
from master.models import BaseModel
from .constants.paymentchoice import PAYMENT_STATUS
from .constants.coursestatus import COURSE_STATUS
from django.core.exceptions import ValidationError

from master.utils.TA_UNIQE.date_time import CURRENT_DATETIME
from master.utils.TA_UNIQE.uniques_filename import generate_unique_filename
from master.models import Technology
from master.utils.TA_UNIQE.unique_id import generate_unique_id

from employee.constants.gender import CHOICE_GENDER

from django.utils import timezone

from decimal import Decimal

# Create your models here.
class Student(BaseModel):
    student_id = models.CharField(max_length=100,primary_key=True,blank=True)
    first_name = models.CharField(max_length=255,blank=False)
    last_name = models.CharField(max_length=255,blank=False)
    email = models.EmailField(max_length=255,unique=True,blank=False)
    mobile = models.CharField(max_length=50,unique=True,blank=False)
    password = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.student_id

    def save(self,*args,**kwargs):
        month = CURRENT_DATETIME.month
        year = CURRENT_DATETIME.year
        PREFIX = 'STU'+month+year+'T'
        if not self.pk:
            last_student = Student.objects.order_by('-created_at').first()
            if last_student:
                last_numeric_value = int(last_student.student_id[len(PREFIX):])
                new_value = last_numeric_value + 1
                new_id = f"{PREFIX}{new_value:04}"
            else:
                new_id = f"{PREFIX}0001"
            
            self.student_id = new_id
            self.password = self.mobile
        super(Student,self).save(*args,**kwargs)


class StudentProfile(BaseModel):
    DIR_NAME = 'student_profiles'
    SUFFIX_WORD = 'studentprofileimage'
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=generate_unique_filename)
    gender = models.CharField(choices= CHOICE_GENDER ,max_length=20, blank=False)
    date_of_birth = models.DateField(blank=False)

    def __str__(self):
        return self.student_id_id

class StudentAddress(BaseModel):
    student_id= models.ForeignKey(Student,on_delete=models.CASCADE)
    address= models.CharField(max_length=255,blank=False)
    country=models.CharField(max_length=50,blank=False)
    state= models.CharField(max_length=50,blank=False)
    city = models.CharField(max_length=50,blank=False)
    pincode =models.CharField(max_length=20,blank=False)

    def __str__(self):
        return self.student_id_id
    
class StudentCourse(BaseModel):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    technology_id = models.ForeignKey(Technology, on_delete=models.CASCADE)
    batch_start_date = models.DateField()
    batch_end_date = models.DateField()
    batch_status = models.CharField(choices=COURSE_STATUS,blank=False,max_length=20)

    def __str__(self):
        return f'{self.student_id}  {self.technology_id}'

class StudentPayment(BaseModel):
    student_id= models.ForeignKey(Student,on_delete=models.CASCADE)
    technology_id = models.ForeignKey(Technology,on_delete=models.CASCADE)
    total_fees = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    remaining_fees = models.DecimalField(max_digits=10,default=0.00,decimal_places=2)
    paid_fees = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    status = models.CharField(choices=PAYMENT_STATUS, default='I',max_length=20)

    def __str__(self):
        return str(self.student_id)
    
    class Meta:
        unique_together = ['student_id','technology_id']

    def save(self,*args,**kwargs):
        if not self.pk:
            if StudentPayment.objects.filter(student_id=self.student_id,technology_id=self.technology_id).exists():
                raise ValidationError("This Record is already Exixts")
            else:
                self.total_fees = self.technology_id.fees
                self.remaining_fees = self.total_fees - self.paid_fees
        
        super(StudentPayment,self).save(*args,**kwargs)


class StudentPaymentEntry(BaseModel):
    DIR_NAME = 'student_fees'
    SUFFIX_WORD = 'studentfees'
    payment_id = models.CharField(primary_key=True,blank=True,max_length=50)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    proof = models.ImageField(upload_to=generate_unique_filename)
    paid_date = models.DateField(default=timezone.now)
    installment = models.FloatField(default=0.00)

    def __str__(self):
        return f'{self.student_id} {self.payment_id}'
    
    def save(self,*args,**kwargs):
        if not self.pk:
            self.payment_id = generate_unique_id(self)

            student_fees_account = StudentPayment.objects.get(student_id_id = self.student_id)
            self.installment = Decimal(self.installment)
            if self.installment != 0:
                if self.installment <= student_fees_account.remaining_fees:
                    student_fees_account.remaining_fees -=  self.installment
                    student_fees_account.paid_fees += self.installment

                    if student_fees_account.remaining_fees != 0:
                        student_fees_account.status = 'P'
                    else:
                        student_fees_account.status = 'C'
                    student_fees_account.save()
                else:
                    raise ValidationError("Your Payment Installment should be less than or equal to remaining fees")
            else:
               raise ValidationError("Your Payment Installment should be greater than Zero")
        
        super().save(*args,**kwargs) 