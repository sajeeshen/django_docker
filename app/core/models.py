from django.db import models

# Create your models here.


class Employee(models.Model):
    """ Models for Employee"""
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    """ Sample model for Posts"""
    post_count = models.IntegerField()

    def __str__(self):
        return self.post_count