from django.db import models
from django.utils import timezone
from .utils.TA_UNIQUE.filename import generate_unique_filename

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        if self.pk:
            self.updated_at = timezone.now()
        self.updated_at = timezone.now()

        super(BaseModel,self).save(*args,**kwargs)


class Information(BaseModel):
    first_name = models.CharField(max_length=255,blank=False)
    last_name = models.CharField(max_length=255,blank=False)
    email = models.EmailField(max_length=255,unique=True)
    mobile = models.CharField(max_length=20,unique=True)
   

class ProductBrand(BaseModel):
    name= models.CharField(max_length=100)
   
    class Meta:
        unique_together = ['name']

    def __str__(self):
        return self.name
    
class ProductSubCategory(BaseModel):
    DIR_NAME = 'productImage'
    SUFFIX_WORD = 'IMG'
    company = models.ForeignKey(ProductBrand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=255,blank=False)
    image = models.ImageField(upload_to=generate_unique_filename,blank=True)
    ram = models.CharField(max_length=50,blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ['company','model_name']
   
    def __str__(self):
        return f"{self.company.name} {self.model_name}"
