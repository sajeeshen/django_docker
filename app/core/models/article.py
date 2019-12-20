from django.contrib.auth import get_user_model
from django.db import models
from .timestamp import TimeStamp


class Article(TimeStamp, models.Model):
    """ Article model """

    title  =  models.CharField(max_length=200)
    body   =  models.TextField()
    author =  models.ForeignKey(get_user_model(),
                                on_delete=models.CASCADE)
    pub_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']