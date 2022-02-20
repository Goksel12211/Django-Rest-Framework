from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.


class Book(models.Model):
    name=models.CharField(max_length=255)
    writer=models.CharField(max_length=255)
    description=models.TextField(blank=True,null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    stream_date=models.DateTimeField()
    def __str__(self):
        return f'{self.name} -- {self.writer}'
    
class  Comment(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='comments')
    owner=models.CharField(max_length=255)
    comment=models.TextField(blank=True,null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True) 
    rating=models.PositiveIntegerField( validators=[MinValueValidator(1),MaxValueValidator(5)] )
    def __str__(self):
        return f'{self.rating}'
    
    