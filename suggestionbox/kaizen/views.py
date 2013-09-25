# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from kaizen.models import Status, Idea, Comment, Category
from django.contrib.auth.models import User

from kaizen.forms import NewIdeaForm

@login_required
def index(request):
    """
    Display a list of suggestions (ideas).  Everyone can see everyone else's ideas.
    """
    ideas = Idea.objects.all().order_by(-pub_date)

    new_idea_form = NewIdeaForm()

    context = {
        'ideas': ideas,
        'new_idea_form': new_idea_form,
    }

    return render(request, 'kaizen/index.html', context)

@login_required
def detail(request, idea_id):
    pass

@login_required
def new_comment(request, idea_id):
    pass

@login_required
def change_status(request, idea_id):
    pass

@login_required
def new_idea(request):
    pass
