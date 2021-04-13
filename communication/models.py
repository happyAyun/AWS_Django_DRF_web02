from django.db import models

# from ?????? import User

# Create your models here.
# class Communication(models.Model):
#     objects = models.Manager()
#     communication_id = models.AutoField(primary_key=True)
#     communication_title = models.CharField(max_length=250)
#     communication_content = models.TextField()
#     communication_img = models.CharField(max_length=250)
#     communication_date = models.DateTimeField(auto_now=True)
#     communication_views = models.IntegerField(max_length=1000)
#     communication_category = models.IntegerField(max_lenth=10)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#
# class Communication_Comment(models.Model):
#     objects = models.Manager()
#     comment_id = models.AutoField(primary_key=True)
#     comment_title = models.CharField(max_length=250)
#     comment_content = models.TextField()
#     communication_id = models.ForeignKey(Communication, on_delete=models.CASCADE)