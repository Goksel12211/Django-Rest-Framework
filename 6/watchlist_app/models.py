from pyexpat import model
from django.db import models
from matplotlib.pyplot import cla

# Create your models here.

class StreamPlatform(models.Model):
    name=models.CharField(max_length=50)
    about=models.CharField(max_length=200)
    website=models.URLField(max_length=200)
    def __str__(self):
        return self.name    


class WatchList(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name