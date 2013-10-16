from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.title

class Record(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return start_time
