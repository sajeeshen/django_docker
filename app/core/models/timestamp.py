from django.db import models


class TimeStamp(models.Model):
    """ Generic timestamp model for all models """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True