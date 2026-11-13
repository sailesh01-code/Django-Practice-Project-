from django.db import models
# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=25)
    desg = models.CharField(max_length=25)
    age = models.IntegerField()
    sal = models.FloatField()
    address = models.CharField(max_length=25)
