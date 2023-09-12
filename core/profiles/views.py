from django.shortcuts import render
from profiles.models import profile
from .forms import *
# Create your views here.
def pview(request):
    fm = profileForm(request.POST, request.FILES)
    if fm.is_valid():
        fm.save()
    else:pass
    return render(request, 'index.html', {'form':fm})
