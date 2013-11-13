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

from binpaste.models import Bin
from binpaste.forms import NewBinForm

class NewBin(CreateView):
    form = NewBinForm
    model = Bin
    template = 'binpaste/new_bin.html'


class BinDetail(DetailView):
    model = Bin
    template_name = 'binpaste/bin_detail.html'
    context_object_name = 'bin'

class 
