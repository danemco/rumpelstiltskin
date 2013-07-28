from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body  = models.TextField()
    pub_date = models.DateTimeField("date published")
    active = models.BooleanField(default=True)
    author = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.title;

    def is_publshied(self):
        return self.pub_date <= timezone.now() and self.active

class Category(models.Model):
    category_name = models.CharField(max_length=64)
    description   = models.CharField(max_length=256)
    post          = models.ManyToManyField(Post)
