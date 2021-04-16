from django.db import models
from user.models import Profile

class Communication(models.Model):
    objects = models.Manager()
    communication_id = models.AutoField(primary_key=True)
    communication_title = models.CharField(max_length=250)
    communication_content = models.TextField()
    communication_img = models.CharField(max_length=250, null=True)
    communication_date = models.DateTimeField(auto_now=True)
    communication_views = models.IntegerField(default=0)
    communication_category = models.IntegerField()
    user_pk = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Communication_Comment(models.Model):
    objects = models.Manager()
    comment_id = models.AutoField(primary_key=True)
    comment_content = models.TextField()
    communication_id = models.ForeignKey(Communication, on_delete=models.CASCADE)