from django.utils.text import slugify
import random
import string

def generate_unique_slug(model, field):
    """    return unique slug if origin slug is exist. """
    origin_slug = slugify(field)
    unique_slug = origin_slug
    numb = 1
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = '%s-%d' % (origin_slug, numb)
        numb += 1
    return unique_slug


def create_random_string(N=7):
    """ Function create a random string and return """
    return ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=N))