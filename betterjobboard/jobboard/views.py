# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages

from jobboard.models import Profile, Post, Subscriber
from jobboard.forms import JobPostForm, ProfileForm, SubscriberForm

def index(request):
    now = timezone.now()
    posts = Post.objects.filter(active=True).filter(expiration__lte=now).order_by('-pub_date')[:20]
    context = {
        'posts': posts,
    }
    return render(request, 'jobboard/index.html', context)

def post_detail(request, post_id):
    pass

@login_required
def profile_job_list(request):
    try:
        profile = Profile.objects.get(user = request.user)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('jobboard:edit-profile'))
    
    posts = Post.objects.filter(profile=profile).order_by('-pub_date')

    context = {
        'posts': posts,
        'profile': profile,
    }
    return render(request, 'jobboard/profile_job_list.html', context)


@login_required
def new_post(request):
    try:
        profile = Profile.objects.get(user = request.user)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('jobboard:edit-profile'))
    
    # check to see if we have a profile yet. If not, direct the user to the form to edit their profile first.
    if request.method == 'POST':
        job_form = JobPostForm(request.POST)
        if job_form.is_valid():
            job_form.instance.profile = profile
            job_form.save()
            messages.success(request, "Your job post has been saved.")
            return HttpResponseRedirect(reverse('jobboard:profile-job-list'))
          
    else:
        job_form = JobPostForm()

    context = {
        'form': job_form,
    }

    return render(request, 'jobboard/new_post.html', context)

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

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            # Check to see if we already have a profile for this guy.
            profile = Profile.objects.get(user = request.user)
            if profile:
                profile.company_name = profile_form.cleaned_data.get('company_name')
                profile.company_website = profile_form.cleaned_data.get('company_website')
                profile.email = profile_form.cleaned_data.get('email')
                profile.contact = profile_form.cleaned_data.get('contact')
                profile.save()
            else:
                profile_form.instance.user = request.user
                profile_form.save()

            messages.success(request, 'Your profile was saved successfully.')
            return HttpResponseRedirect(reverse('jobboard:edit-profile'))
    else:
        try:
            profile = Profile.objects.get(user = request.user)
        except ObjectDoesNotExist:
            profile = Profile(user = request.user)

    profile_form = ProfileForm(instance=profile)

    context = {
        'form': profile_form,
    }

    return render(request, 'jobboard/edit_profile.html', context)
