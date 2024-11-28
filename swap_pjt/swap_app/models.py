from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Brand(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to='upload_photos',null=False,blank=False)
    description=models.TextField(max_length=250,null=False,blank=False)
    def __str__(self):
        return self.name

class BrandModel(models.Model):
    model_name=models.ForeignKey(Brand,on_delete=models.CASCADE)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to='upload_photos',null=False,blank=False)
    year=models.FloatField(null=False,blank=False)
    kilometer=models.FloatField(null=False,blank=False)
    engine=models.CharField(max_length=150,null=False,blank=False)
    actual_price=models.FloatField(null=False,blank=False)
    booking_price=models.FloatField(null=False,blank=False)
    location=models.CharField(max_length=150,null=False,blank=False)
    description=models.TextField(max_length=200,null=False,blank=False)
    def __str__(self):
        return self.name
    
