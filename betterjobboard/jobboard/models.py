from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User)
    company_name = models.CharField(max_length=100)
    company_website = models.URLField()
    email = models.EmailField()
    contact = models.CharField(max_length=100)

    def __unicode__(self):
        return self.company_name

class Post(models.Model):
    INTERN = 'intern'
    FULL_TIME = 'full'
    PART_TIME = 'part'
    TYPES_OF_JOB_POSTINGS = (
        (INTERN, 'Internship'),
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part Time'),
    )
    profile = models.ForiegnKey(Profile)
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=6, choices=TYPES_OF_JOB_POSTINGS, default=PART_TIME)
    wage = models.IntegerField(null=True, blank=True)
    expiration = models.DateField()
    pub_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

class Subscriber(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subscribe_date = models.DateTimeField(auto_now_add=True)
