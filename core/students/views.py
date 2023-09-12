from django.shortcuts import render
from .models import *
from .form import * 
# Create your views here.

def create(request):
    fm = registrationForm(request.POST, request.FILES)
    data = registration.objects.all()
    if fm.is_valid():
        fm.save()
    else:pass
    return render(request, 'index.html', {'form':fm, 'data':data})


def read(request):
    fm = registrationForm(request.POST, request.FILES)
    data = registration.objects.all().values()

    return render(request, 'read.html', {'form':fm, 'data':data})


    
    