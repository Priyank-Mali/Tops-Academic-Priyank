from django.db import models
from master.models import Information
from master.utils.TA_UNIQUE.password import generate_password

# Create your models here.
class Manager(Information):
    PRIFIX = 'ADM'
    manager_id = models.CharField(max_length=255,blank=True)
    password = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.manager_id

    def save(self,*args,**kwargs):
        if not self.pk:
            last_manager = Manager.objects.order_by('-created_at').first()
            if last_manager:
                numeric_value = int(last_manager.manager_id[len(self.PRIFIX):])
                new_value = numeric_value + 1
                new_id = f"{self.PRIFIX}{new_value:04}"
            else:
                new_id = f"{self.PRIFIX}0001"
            
            self.manager_id = new_id
            self.password = generate_password()

            super(Manager,self).save(*args,**kwargs)