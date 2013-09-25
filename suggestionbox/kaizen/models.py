from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    status = models.CharField(max_length=25)

    def __unicode__(self):
        return self.status

    class Meta:
        verbose_name_plural = 'statuses'

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

class Idea(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    body = models.TextField('suggestion')
    status = models.ForeignKey(Status, null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, null=True, blank=True)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    idea = models.ForeignKey(Idea)
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.comment


