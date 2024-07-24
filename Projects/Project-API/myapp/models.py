from django.db import models
from django.utils import timezone
# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self,*args,**Kwargs):
        if self.pk:
            self.updated_at = timezone.now()
        self.created_at = timezone.now()

        super(BaseModel,self).save(*args,**Kwargs)

class globalNote(BaseModel):
    student_id = models.CharField(max_length=255,blank=False)
    comment = models.TextField()