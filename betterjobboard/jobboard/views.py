# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

from jobboard.models import Profile, Post, Subscriber
from jobboard.forms import JobPostForm, ProfileForm, SubscriberForm

def index(request):
    pass

def post_detail(request, post_id):
    pass


@login_required
def new_post(request):
    pass

def subscribe(request):
    pass

def subscribe_success(request):
    pass

def unsubscribe(request):
    pass

def unsubscribe_success(request):
    pass

@login_required
def edit_profile(request):
    pass
