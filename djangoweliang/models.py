from django.db import models
from django.contrib.auth.models import User

class MyUser(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=16)
    permission = models.IntegerField(default=1)

    def __str__(self):
        return self.user.username

class House(models.Model):
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    price = models.CharField(max_length=128)
    area = models.CharField(max_length=128)
    numofman = models.CharField(max_length=128)
    bedsize = models.CharField(max_length=128)

    class META:
        ordering = ['name']

    def __str__(self):
        return self.name






# Create your models here.
