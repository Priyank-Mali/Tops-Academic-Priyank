from django.db import models

# Create your models here.

class Snippets(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    linenos = models.BooleanField(default=False)
    language = models.CharField(max_length=50)
    style = models.CharField(max_length=100)

    def __str__(self):
        return self.title