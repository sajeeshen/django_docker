from __future__ import absolute_import, unicode_literals
import random
from celery import task
from core.models import Post


@task(name='sum_two_numbers')
def add(x, y):
    add_post_count(10)
    return x+y

@task(name='add_post_count')
def add_post_count(a, b):
    print("I am here in add post_count")
    res = Post.objects.all()
    print(len(res))
    # obj = Post.objects.create(post_count=a)
    return a+b