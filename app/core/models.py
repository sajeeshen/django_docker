from django.db import models

# Create your models here.


class Employee(models.Model):
    """ Models for Employee"""
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name