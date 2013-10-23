# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from timeclock.models import Project, Record
#from timeclock.forms import #

from registration.backends.simple.views import RegistrationView 
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

class ListRecords(ListView):
    template_name = 'timeclock/record_list.html'
    model = Record
    context_object_name = 'records'
    
    def get_queryset(self):
        return Record.objects.filter(user = self.request.user).order_by('-end_time')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ListRecords, self).dispatch(*args, **kwargs)

class RecordDetail(DetailView):
    template_name = 'timeclock/record_detail.html'
    model = Record
    context_object_name = 'record'

    def get_object(self):
        record = get_object_or_404(Record, pk = self.kwargs.get('pk'), user = self.request.user)
        return record

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RecordDetail, self).dispatch(*args, **kwargs)

class RecordUpdate(UpdateView):
    model = Record

    def get_object(self):
        record = get_object_or_404(Record, pk = self.kwargs.get('pk'), user = self.request.user)
        return record

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RecordUpdate, self).dispatch(*args, **kwargs)

class RecordDelete(DeleteView):
    model = Record
    success_url = reverse_lazy('timeclock:list-index')

    def get_object(self):
        record = get_object_or_404(Record, pk = self.kwargs.get('pk'), user = self.request.user)
        return record

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RecordDelete, self).dispatch(*args, **kwargs)

class RecordAdd(CreateView):
    model = Record

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RecordAdd, self).dispatch(*args, **kwargs)
