from django.db import models

from master.models import BaseModel,AttributesModel
from master.utils.TA_UNIQUE.password import generate_password
from master.utils.TA_UNIQUE.filename import generate_unique_filename

from django.utils import timezone
from django.core.mail import send_mail
import os

# Create your models here.
class Role(BaseModel):
    role = models.CharField(max_length=255,blank=False,null=False)

    def __str__(self):
        return self.role
    
class Chairmans(AttributesModel):
    PRIFIX = 'CH'
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    chairman_id = models.CharField(max_length=255,primary_key=True,blank=True,null=False)
    password = models.CharField(max_length=255,blank=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name + " " + self.chairman_id  

    def save(self,*args,**kwargs):
        if not self.pk:
            last_chaiman = Chairmans.objects.order_by('-created_at').first()
            if last_chaiman:
                last_number = int(last_chaiman.chairman_id[len(self.PRIFIX):])
                new_numner = last_number + 1
                new_id = f'{self.PRIFIX}{new_numner:04}'
            else:
                new_id = f'{self.PRIFIX}0001'
            
            self.chairman_id = new_id
            self.password = generate_password()

        super(Chairmans,self).save(*args,**kwargs)

class Members(AttributesModel):
    PRIFIX = 'MEMB'
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    member_id = models.CharField(max_length=255,blank=True,primary_key=True)
    password = models.CharField(max_length=10,blank=True,null=False)

    def save(self,*args,**kwargs):
        if not self.pk:
            last_member = Members.objects.order_by('-created_at').first()
            if last_member:
                last_number = int(last_member.member_id[len(self.PRIFIX):])
                new_numner = last_number + 1
                new_id = f'{self.PRIFIX}{new_numner:04}'
            else:
                new_id = f'{self.PRIFIX}0001'
            
            self.member_id = new_id
            self.password = generate_password()

            subject =  'Your Login Creditial'
            message = f"""
            Hello, {self.first_name} {self.last_name}
            Your Login credential for society registration is:
            MEMBER ID : {self.member_id}
            PASSWORD : {self.password}

            Thank You !!
            """
            from_email =  'priyankmali297@gmail.com'
            recipient_list =  [self.email]
            send_mail(subject,message,from_email,recipient_list)

        super(Members,self).save(*args,**kwargs)

    def __str__(self) -> str:
            return self.first_name + " " + self.last_name + " " + self.member_id
        

class Watchmans(AttributesModel):
    PRIFIX = 'WATC'
    watchman_id = models.CharField(max_length=255,blank=True,primary_key=True)

    def save(self,*args,**kwargs):
        if not self.pk:
            last_watchman = Watchmans.objects.order_by('-created_at').first()
            if last_watchman:
                last_number = int(last_watchman.watchman_id[len(self.PRIFIX):])
                new_numner = last_number + 1
                new_id = f'{self.PRIFIX}{new_numner:04}'
            else:
                new_id = f'{self.PRIFIX}0001'
            
            self.watchman_id = new_id

        super(Watchmans,self).save(*args,**kwargs)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name + " " + self.watchman_id
    

class Notice(BaseModel):
    DIR_NAME = 'notice_image'
    SUFFIX_WORD = 'notice_img'
    notice_title = models.CharField(max_length=255,blank=False,null=False)
    notice_descriptions = models.TextField()
    image = models.FileField(upload_to=generate_unique_filename)

    def __str__(self):
        return self.notice_title
    

class Event(BaseModel):
    DIR_NAME = 'event_image'
    SUFFIX_WORD = 'event_img'
    event_topic = models.CharField(max_length=255,blank=False,null=False)
    event_description = models.TextField()
    image = models.FileField(upload_to=generate_unique_filename)

    def __str__(self):
        return self.event_topic
    
class Visitors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=20,primary_key=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    entry_time = models.DateTimeField(default=timezone.now)
    exit_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'