from django.db import models
from django.utils.safestring import mark_safe

class registration(models.Model):
    name = models.CharField('name', max_length=50)
    docu = models.FileField(upload_to = 'images/', max_length=255)

class author(models.Model):
    author_pic = models.ImageField(upload_to='images/')
    def image_tag(self):
        return mark_safe("<img src= '/media/images/%s'>" %(self.author_pic))

# Create your models here. 
