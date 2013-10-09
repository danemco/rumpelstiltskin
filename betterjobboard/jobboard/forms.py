from django.forms import ModelForm
from jobboard.models import Profile, Post, Subscriber

class JobPostForm(ModelForm):
    class Meta:
        fields = ['title', 'description', 'job_type', 'wage', 'expiration', 'active']
        model = Post

class ProfileForm(ModelForm):
    class Meta:
        fields = ['company_name', 'company_website', 'email', 'contact']
        model = Profile

class SubscriberForm(ModelForm):
    class Meta:
        model = Subscriber
