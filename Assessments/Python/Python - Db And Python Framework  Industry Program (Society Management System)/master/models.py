from django.db import models
from django.utils import timezone

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    
    def save(self,*args,**kwargs):
        if self.pk:
            self.updated_at = timezone.now()
        self.created_at = timezone.now()

        super(BaseModel,self).save(*args,**kwargs)


class AttributesModel(BaseModel):
    first_name = models.CharField(max_length=255,blank=False,null=False)
    last_name = models.CharField(max_length=255,blank=False,null=False)
    email = models.EmailField(unique=True,max_length=255,blank=False)
    mobile = models.CharField(max_length=20,blank=True,unique=True,null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # If mobile is an empty string, set it to None
        if self.mobile == '':
            self.mobile = None
        super(AttributesModel, self).save(*args, **kwargs)