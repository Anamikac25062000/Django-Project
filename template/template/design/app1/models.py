from django.db import models

class Place(models.Model):
    img=models.ImageField(upload_to='travel/img',null=True,blank=True)
    name=models.CharField(max_length=30)
    desc=models.CharField(max_length=30)

class Team(models.Model):
    img=models.ImageField(upload_to='travel/img',null=True,blank=True)
    name=models.CharField(max_length=30)
    desc=models.CharField(max_length=30)

# Create your models here.
