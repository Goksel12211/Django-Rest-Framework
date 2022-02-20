from pyexpat import model
from django.db import models
from matplotlib.pyplot import cla

# Create your models here.


class Director(models.Model):   
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name}{self.surname}' 

class Movie(models.Model):
    director=models.ForeignKey(Director, on_delete=models.CASCADE,related_name='makaleler')
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.name