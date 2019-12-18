from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.utility.slug import generate_unique_slug
from core.models import Profile


User = get_user_model()
@receiver(post_save, sender=User)
def create_user_slug(sender, instance, created, **kwargs):
    """ 
        When user is created then create user slug and profile
        object
    """
    if created:
        fields = instance.first_name+"-"+instance.last_name
        slug = generate_unique_slug(User, fields)
        instance.slug = slug
        instance.save()
        # Created User profile and slug
        profile = Profile.objects.create(user=instance)
        profile.slug = slug
        profile.save()
