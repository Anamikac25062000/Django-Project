from django.shortcuts import render
from app1.models import Place
from app1.models import Team

def home(request):
    p=Place.objects.all()
    t=Team.objects.all()
    return render(request,'base.html',{'p':p,'t':t})


# Create your views here.
