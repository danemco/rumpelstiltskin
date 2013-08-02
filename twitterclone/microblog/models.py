from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(Users)
    bio  = models.TextField('About me')
    # Where I left off
    # picture = models.


    def __unicode__(self):
        return self.user.username
