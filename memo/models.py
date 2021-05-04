from django.db import models
from user.models import User
from book.models import Book, Book_Article
# Create your models here.


class Memo(models.Model):
    objects = models.Manager()
    memo_id = models.AutoField(primary_key=True)
    memo_title = models.CharField(max_length=250)
    memo_content = models.TextField()
    memo_date = models.DateTimeField(auto_now=True)
    memo_img = models.CharField(max_length=250, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Book_Article, on_delete=models.SET_DEFAULT, default='bookshelf')
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)


