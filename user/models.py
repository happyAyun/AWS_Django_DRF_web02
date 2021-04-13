from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(models.Model):
    objects = models.Manager()
    user_id = models.CharField(max_length=50)
    pw = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)


class User_Profile(models.Model):
    objects = models.Manager()
    profile_id = models.AutoField(primary_key=True)
    profile_info = models.TextField()
    profile_img = models.CharField(max_length=250)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_User(sender, instance, created, **kwargs):
    if created:
        User.objects.create(user=instance, user_pk=instance.id)


@receiver(post_save, sender=User)
def save_user_User(sender, instance, **kwargs):
    instance.User.save()
