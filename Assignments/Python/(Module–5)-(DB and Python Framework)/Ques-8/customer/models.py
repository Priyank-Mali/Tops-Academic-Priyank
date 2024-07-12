from django.db import models
from master.models import Information
# from master.utils.TA_UNIQUE.password import generate_password

# Create your models here.
class Customer(Information):
    PRIFIX = 'CUST'
    customer_id = models.CharField(primary_key=True,max_length=255,blank=True)
    password = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.customer_id

    def save(self,*args,**kwargs):
        if not self.pk:
            last_customer = Customer.objects.order_by('-created_at').first()
            if last_customer:
                numeric_value = int(last_customer.customer_id[len(self.PRIFIX):])
                new_value = numeric_value + 1
                new_id = f"{self.PRIFIX}{new_value:04}"
            else:
                new_id = f"{self.PRIFIX}0001"
            
            self.customer_id = new_id
            self.password = self.mobile
        else:
            self.password = self.mobile
            super(Customer,self).save(*args,**kwargs)
        super(Customer,self).save(*args,**kwargs)