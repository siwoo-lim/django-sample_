from django.db import models

# Create your models here.
class CommentData(models.Model):
    nickname = models.CharField(max_length=20)
    comment = models.TextField()

class WHYWEDONTEXIST(models.Model):
    title = models.CharField(max_length=20)
    link = models.URLField()
