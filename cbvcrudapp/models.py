from django.db import models
from django.urls import reverse 

# Create your models here.

class student(models.Model):
   # id = models.IntegerField()
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    testscore1 = models.FloatField(default=0)
    testscore2= models.FloatField(default=0)
    testscore3 = models.FloatField(default=0)
    testscore4 = models.FloatField(default=0)
    testscore5 = models.FloatField(default=0)
    testscore6 = models.FloatField(default=0)
    
    
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={"pk": self.pk})
    