# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from timeclock.models import Profile, Post, Subscriber
#from timeclock.forms import #

from registration.backends.simple.views import RegistrationView 
from django.views.generic import ListView, DetailView

class ListRecords(ListView):
    template_name = 'ticktock/record_list.html'
    model = Record
    context_object_name = 'records'
    
    def get_queryset(self):
        return Record.objects.filter(user = self.request.user).order_by('-end_time')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ListRecords, self).dispatch(*args, **kwargs)

class RecordDetail(DetailView):
    template_name = 'ticktock/record_detail.html'
    model = Record
    context_object_name = 'record'

    def get_object(self):
        record = get_object_or_404(Record, pk = self.kwargs.get('pk'), user = self.request.user)
        return record

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ListRecords, self).dispatch(*args, **kwargs)

