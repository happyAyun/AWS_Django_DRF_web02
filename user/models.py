from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Member(models.Model):
    objects = models.Manager()
    user_id = models.CharField(max_length=50, primary_key=True)
    pw = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    profile_info = models.TextField(null=True)
    profile_img = models.CharField(null=True, max_length=250)


@receiver(post_save, sender=User)
def create_user_Member(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(user=instance, user_pk=instance.id)


@receiver(post_save, sender=User)
def save_user_Member(sender, instance, **kwargs):
    instance.Member.save()
