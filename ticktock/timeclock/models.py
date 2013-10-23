from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from time import strftime

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(sefl):
        return reverse('jobboard:project-detail', args=(self.pk,))

class Record(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def elapsed_time(self):
        if self.end_time is not None:
            difftime = self.end_time - self.start_time
            hours, remainder = divmod(difftime.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            return "%02d:%02d:%02d" % (hours, minutes, seconds)
        else:
            return None

    def __unicode__(self):
        return "Started " + self.start_time.strftime("%Y-%m-%d %I:%M:%S %p")

    def get_absolute_url(sefl):
        return reverse('jobboard:recordt-detail', args=(self.pk,))
