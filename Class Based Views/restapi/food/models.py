from statistics import mode
from django.db import models

# Create your models here.


class Food(models.Model):
    name=models.CharField(max_length=200)
    isFresh=models.BooleanField()
    
    def __str__(self):
        return self.name