# Create your views here.
from django.http import HttpResponse
from polls.models import Poll
from django.shortcuts import render, get_object_or_404
from django.http import Http404

def index(request):
    latest_poll_list = Poll.objects.filter(active=True).order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    poll = get_object_or_404(Poll, active=True, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
    return HttpResponse("This is where the results for the poll <b>%s</b> will go." % poll_id)

def vote(request, poll_id):
    return HttpResponse("Want to vote on poll <b>%s</b>?" % poll_id)
