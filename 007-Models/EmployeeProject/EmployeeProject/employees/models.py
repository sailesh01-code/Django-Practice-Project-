from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, default='Development')
    salary = models.IntegerField(default=0)
    email = models.EmailField(default='example@gmail.com')

    def __str__(self):
        return self.name
    