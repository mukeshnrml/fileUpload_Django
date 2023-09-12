from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group


admin.site.register(registration)
admin.site.register(author)



admin.site.unregister(Group)
admin.site.site_header='studen_Registration'
admin.site.site_title='ADIT_REGISTRATION'
admin.site.site_title='ADIT NSTI'


class registration(admin.ModelAdmin):
    list_display = ('id', 'name', 'docu')
# Register your models here.
