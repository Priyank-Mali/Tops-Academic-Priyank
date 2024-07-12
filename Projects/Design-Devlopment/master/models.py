from django.db import models
from django.utils import timezone

from .utils.TA_UNIQE.uniques_filename import generate_unique_filename

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self,*args,**kwargs):
        if not self.pk:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super(BaseModel,self).save(*args,**kwargs)


class Technology(BaseModel): 
    DIR_NAME = 'technology_logos'
    PREFIX = '_TechLogo'
    SUFFIX_WORD = 'TechLogo_'
    technology_id = models.CharField(primary_key=True, blank=True, max_length=255)
    name = models.CharField(max_length=255, blank=False, null=False)
    logo = models.ImageField(upload_to=generate_unique_filename, blank=True, null=True)
    fees = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    
    def save(self, *args, **kwargs):
        if not self.technology_id: 
            last_technology = Technology.objects.order_by('-created_at').first()
            if last_technology :
                last_numeric_part = int(last_technology.technology_id[len(self.PREFIX):])
                new_numeric_part = last_numeric_part + 1
                new_id = f"{self.PREFIX}{new_numeric_part:04}"
            else:
                new_id = f"{self.PREFIX}001"
            self.technology_id = new_id

        super().save(*args, **kwargs)
        print(f"Technology ID: {self.technology_id}, Fees: {self.fees}")

    def __str__(self):
        return f"{self.name}-{self.technology_id}"

