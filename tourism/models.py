from django.db import models

# Create your models here.

class Place(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='photos')
    date = models.DateField()
    desc  = models.TextField(default='Add something')
    posts = models.BooleanField(default=False)