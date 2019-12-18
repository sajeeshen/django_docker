from django.db import models
from django.contrib.auth import get_user_model
from .timestamp import TimeStamp

User = get_user_model()

def user_profile_pic(instance, filename):
    """ Return the filename with user details """
    return 'user_{0}/{1}'.format(instance.user.slug, filename)


class Profile(TimeStamp, models.Model):
    """ Profile models for users """

    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile_user')
    address1 = models.CharField('Address 1', max_length=250,
                                blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField('Please enter city', max_length=250,
                            blank=True)
    state = models.CharField('State', max_length=200,
                            blank=True)
    country = models.CharField('Country', max_length=200,
                            blank=True)
    slug = models.SlugField(unique=True, max_length=200)
    profile_pic = models.FileField(blank=True,
                                   upload_to=user_profile_pic)

    
    def __str__(self):
        return '{0} {1}'.format(self.user.first_name, self.user.last_name)

