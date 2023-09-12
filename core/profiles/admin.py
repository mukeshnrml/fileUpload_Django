from django.contrib import admin
from .models import *

@admin.register(profile)

class profileAdmin(admin.ModelAdmin):
    list_display = ['name', 'dob', 'gender', 'pin', 'phone', 'mail', 'state', 'skills', 'img' ]

# Register your models here.
