from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from pinboard.models import Comment, Board, Pin


class ListPins(ListView):
    template_name = 'pinboard/pin_list.html'
    model = Pin
    context_object_name = 'pins'
    paginate_by = 20
    
    def get_queryset(self):
        return Pin.objects.filter(is_public=True).order_by('-pub_date')

