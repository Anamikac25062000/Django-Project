from django.contrib.auth.models import User
from django.db import models
from shop.models import Product

class Cart(models.Model):
    products=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    date_added=models.DateField(auto_now_add=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.products.name

    def subtotal(self):
        return self.quantity*self.products.price

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    products=models.ForeignKey(Product,on_delete=models.CASCADE)
    address=models.TextField(max_length=100)
    phone=models.CharField(max_length=10)
    order_status=models.CharField(max_length=30,default="Pending")
    delivery=models.CharField(max_length=30, default="Pending")
    noofitems=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

    def subtotal(self):
        return self.noofitems*self.products.price

class Account(models.Model):
    accntnumber=models.CharField(max_length=20)
    acctype=models.CharField(max_length=20)
    amount=models.IntegerField()
    def __str__(self):
        return self.accntnumber


# Create your models here.
