# from django.db import models
# # from ../user/models import User ????
# # Create your models here.
#
# class Book(models.Model):
#     book_id = models.AutoField(primary_key=True)
#     book_title = models.CharField(max_length=250)
#     book_content = models.TextField()
#     book_writter = models.CharField(max_length=50)
#     book_intro = models.TextField()
#     book_like = models.IntegerField(default=0)
#     book_publisher = models.CharField(max_length=50)
#     book_img = models.CharField(max_length=250)
#     user_id = models.ForeignKey(User,on_delete=models.CASCADE)
#
#
# class Book_Article(models.Model):
#     article_id = models.AutoField(primary_key=True)
#     article_title = models.CharField(max_length=250)
#     article_content = models.TextField()
#     article_img = models.CharField(max_length=250)
#     article_date = models.DateTimeField(auto_now=True)
#     article_views = models.IntegerField(default=0)
#     article_subscribe = models.IntegerField(default=0)
#     book_id = models.ForeignKey(Book,on_delete=models.CASCADE)
#
#
# class Bookmark(models.Model):
#     bookmark_id = models.AutoField(primary_key=True)
#     user_id = models.ForeignKey(User,on_delete=models.CASCADE)
#     book_id = models.ForeignKey(Book,on_delete=models.CASCADE)
#     article_id = models.ForeignKey(Book_Article,on_delete=models.CASCADE)