from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)
    bio  = models.TextField('About me')
    picture = models.ImageField('Profile picture', upload_to='photos/%Y/%m/%d')

    def __unicode__(self):
        return self.user.username

class Post(models.Model):
    profile  = models.ForeignKey(Profile)
    pub_date = models.DateTimeField('Published date', auto_now=True)
    message  = models.CharField(max_length=140)

    def __unicode__(self):
        return self.message
