from django.db import models
from django.urls import reverse #used to generate URLS by reversing the patterns
# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=200)
    publisher= models.ForeignKey('Publisher',on_delete=models.SET_NULL,null=True)
    summary= models.TextField(max_length=1000,help_text='Enter a brief description of the book')
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('game-detail',args=[str(self.id)])

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    address= models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('publisher-detail',args=[str(self.id)])
    
