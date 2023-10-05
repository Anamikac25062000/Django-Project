from django.shortcuts import render,redirect
from shop.models import Product
from cart.models import Cart,Account,Order
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def add_cart(request,p):
    product=Product.objects.get(id=p)
    user=request.user
    try:
        cart=Cart.objects.get(products=product,user=user)
        if cart.quantity<cart.products.stock:
            cart.quantity+=1
        cart.save()
    except Cart.DoesNotExist:
        cart=Cart.objects.create(user=user,products=product,quantity=1)
        cart.save()
    return redirect('cart:cartview')

@login_required
def cartview(request):
    total=0
    user=request.user
    try:
        cart=Cart.objects.filter(user=user)
        for i in cart:
            #total+=i.quantity*i.products.price
            total+=i.subtotal()
    except Cart.DoesNotExist:
        pass
    return render(request,'cart.html',{'cart':cart,'total':total})

@login_required
def less_cart(request,p):
    product=Product.objects.get(id=p)
    user=request.user
    try:
        cart=Cart.objects.get(products=product,user=user)
        if cart.quantity>1:
            cart.quantity-=1
            cart.save()
        else:
            cart.delete()
    except Cart.DoesNotExist:
        pass
    return redirect('cart:cartview')

@login_required
def trash_cart(request,p):
    product=Product.objects.get(id=p)
    user=request.user
    try:
        cart = Cart.objects.get(products=product, user=user)
        cart.delete()
    except Cart.DoesNotExist:
        pass
    return redirect('cart:cartview')

@login_required
def orderform(request):
    total=0
    if(request.method=="POST"):
        a=request.POST['a']
        b=request.POST['b']
        c=request.POST['c']
        u=request.user
        cart=Cart.objects.filter(user=u)
        for i in cart:
            total+=i.quantity*i.products.price
        ac=Account.objects.get(accntnumber=c)
        if(ac.amount>=total):
            ac.amount=ac.amount-total
            ac.save()
            for i in cart:
                o=Order.objects.create(user=u,products=i.products,address=a,phone=b,order_status="paid",noofitems=i.quantity)
                i.products.stock=i.products.stock-i.quantity
                i.products.save()
                o.save()
            cart.delete()
            msg="Ordered Successfully"
            return render(request,'orderdetail.html',{'msg':msg,'total':total})
        else:
            msg="Insufficient Amount. You can't place an order."
            return render(request, 'orderform.html',{'msg':msg})
    return render(request,'orderform.html')

@login_required
def orderview(request):
    u=request.user
    o=Order.objects.filter(user=u,order_status="paid")
    return render(request,'orderview.html',{'o':o,'name':u.username})
