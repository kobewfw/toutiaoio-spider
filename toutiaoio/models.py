from django.db import models

# Create your models here.


class ToutiaoItem(models.Model):
    title = models.CharField(max_length=200, default="", null=True)
    url = models.CharField(max_length=200, default="", null=True)
    source = models.CharField(max_length=200, default="", null=True)
    comment = models.CharField(max_length=20, default="", null=True)
    username = models.CharField(max_length=200, default="", null=True)
    userurl = models.CharField(max_length=200, default="", null=True)
    subjectname = models.CharField(max_length=200, default="", null=True)
    subjecturl = models.CharField(max_length=200, default="", null=True)
    upvote = models.CharField(max_length=20, default="", null=True)
    date = models.CharField(max_length=50, default="", null=True)

    def __str__(self):
        return self.title
    pass
