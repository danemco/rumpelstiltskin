from django.forms import ModelForm
from jobboard.models import Profile, Post, Subscriber

class JobPostForm(ModelForm):
    class Meta:
        model = Post

class ProfileForm(ModelForm):
    class Meta:
        model = Profile

class SubscriberForm(ModelForm):
    class Meta:
        model = Subscriber
