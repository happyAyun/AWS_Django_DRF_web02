from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Memo(models.Model):
    objects = models.Manager()
    memo_id = models.AutoField(primary_key=True)
    memo_title = models.CharField(max_length=250)
    memo_content = models.TextField()
    memo_date = models.DateTimeField(auto_now=True)
    memo_img = models.CharField(max_length=250)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    article_id = models.ForeignKey(Book_Article, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)

class QnA(models.Model):
    objects = models.Manager()
    qna_id = models.AutoField(primary_key=True)
    qna_title = models.CharField(max_length=250)
    qna_content = models.TextField()
    qna_img = models.CharField(max_length=250)
    book_num = models.ForeignKey(Book, on_delete=models.CASCADE)


class QnA_Reply(models.Model):
    objects = models.Manager()
    reply_id = models.AutoField(primary_key=True)
    reply_content = models.TextField()
    qna_id = models.ForeignKey(QnA, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_user_Member(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(user=instance, user_pk=instance.id)

@receiver(post_save, sender=User)
def save_user_Member(sender, instance, **kwargs):
    instance.Member.save()