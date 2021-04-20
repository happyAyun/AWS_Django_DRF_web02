from django.db import models
from user.models import Profile


class Book(models.Model):
    objects = models.Manager()
    book_id = models.AutoField(primary_key=True)
    book_title = models.CharField(max_length=250)
    book_writter = models.CharField(max_length=50, null=True)
    book_intro = models.TextField(null=True)
    book_like = models.IntegerField(default=0)
    book_publisher = models.CharField(max_length=50, null=True)
    book_img = models.CharField(max_length=250, null=True)
    book_subscribe = models.IntegerField(default=0)
    user_id = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, default='bookshelf')


class Book_Article(models.Model):
    objects = models.Manager()
    article_id = models.AutoField(primary_key=True)
    article_title = models.CharField(max_length=250)
    article_content = models.TextField()
    article_img = models.CharField(max_length=250, null=True)
    article_date = models.DateTimeField(auto_now=True)
    article_views = models.IntegerField(default=0)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)


class Bookmark(models.Model):
    objects = models.Manager()
    bookmark_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Book_Article, on_delete=models.CASCADE)


class SignBook(models.Model):
    objects = models.Manager()
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
