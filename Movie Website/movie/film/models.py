from django.db import models


class Movies(models.Model):
    title = models.CharField(max_length=30)
    year = models.IntegerField()
    rating = models.IntegerField()
    desc = models.CharField(max_length=50)
    img=models.ImageField(upload_to='film/img',null=True,blank=True)
