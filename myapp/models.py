from django.db import models

# Create your models here.
class jon(models.Model):
    company=models.CharField(max_length=250,blank=True,null=True)
    descriptions = models.CharField(max_length=300,blank=True,null=True) 
    image = models.ImageField(upload_to="images/")
     