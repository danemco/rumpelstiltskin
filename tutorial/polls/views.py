# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from polls.models import Poll

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        return Poll.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'
    model = Poll

class ResultsView(generic.DetailView):
    template_name = 'polls/results.html'
    model = Poll

def vote(request, poll_id):
    p = get_object_or_404(Poll, active=True, pk=poll_id)
    try:
        choiceObj = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message' : "You didn't select a valid choice. Try again.",
        })
    else:
        choiceObj.votes += 1
        choiceObj.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
