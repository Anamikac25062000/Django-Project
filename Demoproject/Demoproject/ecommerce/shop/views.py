from shop.models import Category
from shop.models import Product
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def home(request):
    c=Category.objects.all
    return render(request,'category.html',{'c':c})

@login_required
def allproducts(request,p):
    c=Category.objects.get(slug=p)
    product=Product.objects.filter(category__slug=p)
    return render(request,'allproduct.html',{'product':product,'c':c})

@login_required
def productdetails(request,p):
    p=Product.objects.get(slug=p)
    return render(request,'productdetails.html',{'p':p})


def register(request):
    if(request.method=="POST"):
        a=request.POST['a']
        b=request.POST['b']
        c=request.POST['c']
        d=request.POST['d']
        e=request.POST['e']
        f=request.POST['f']
        if(b==c):
            u=User.objects.create_user(username=a,password=b,email=d,first_name=e,last_name=f)
            u.save()
            return redirect('shop:home')
        else:
            messages.error(request,"Password are not same")
    return render(request,'register.html')

def user_login(request):
    if(request.method=="POST"):
        username=request.POST['x']
        password=request.POST['y']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('shop:home')
        else:
            messages.error(request,"Invalid User Credentials")
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('shop:home')
