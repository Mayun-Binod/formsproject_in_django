from django.db import models

# Create your models here.

class Employee(models.Model):
    ename = models.CharField(max_length=200)
    eaddr = models.CharField(max_length=100)
    eno = models.IntegerField()
    esal = models.FloatField()

    def __str__(self):
        return (f'{self.ename}')
    
