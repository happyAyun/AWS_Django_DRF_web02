from django.db import models
from user.models import Profile
from book.models import Book, Book_Article
# Create your models here.

class QnA(models.Model):
    objects = models.Manager()
    qna_id = models.AutoField(primary_key=True)
    qna_title = models.CharField(max_length=250)
    qna_content = models.TextField()
    qna_img = models.CharField(max_length=250, null=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)

class QnA_Reply(models.Model):
    objects = models.Manager()
    reply_id = models.AutoField(primary_key=True)
    reply_content = models.TextField()
    qna_id = models.ForeignKey(QnA, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
