from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User)
    bio  = models.TextField('About me')
    # Where I left off
    picture = models.ImageField('Profile Image', upload_to='pictures/%Y/%m/%d', blank="True")
    following = models.ManyToManyField('self')

    def __unicode__(self):
        return self.user.username



class Post(models.Model):
    profile = models.ForeignKey(Profile)
    message  = models.CharField(max_length=140)
    pub_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.message

