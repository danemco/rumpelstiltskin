from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    status = models.CharField(max_length=25)

    def __unicode__(self):
        return self.status

class Idea(models.Model):
    user = models.ForienKey(User)
    title = models.CharField(max_length=100)
    body = models.TextField('suggestion')
    status = models.ForeignKey(Status)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return title

class Comment(models.Model):
    comment = models.TextField()
    idea = models.ForeignKey(Idea)

    def __unicode__(self):
        return comment
