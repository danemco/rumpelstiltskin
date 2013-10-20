# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages

from timeclock.models import Profile, Post, Subscriber
#from timeclock.forms import #

from registration.backends.simple.views import RegistrationView 
from django.views.generic import ListView, DetailView


class ListEntries(ListView):
    template_name = 'record_list.html'
