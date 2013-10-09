# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages

from jobboard.models import Profile, Post, Subscriber
from jobboard.forms import JobPostForm, ProfileForm, SubscriberForm, UnsubscriberForm

def index(request):
    now = timezone.now()
    posts = Post.objects.filter(active=True).filter(expiration__gte=now).order_by('-pub_date')[:20]
    context = {
        'posts': posts,
    }
    return render(request, 'jobboard/index.html', context)

def post_detail(request, post_id):
    now = timezone.now()
    post = get_object_or_404(Post, pk=post_id, active=True, expiration__gte=now)

    context = {
        'post': post,
    }
    return render(request, 'jobboard/detail.html', context)

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
    # check to see if we have a profile yet. If not, direct the user to the form to edit their profile first.
    try:
        profile = Profile.objects.get(user = request.user)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('jobboard:edit-profile'))
    
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

@login_required
def edit_post(request, post_id):
    # check to see if we have a profile yet. If not, direct the user to the form to edit their profile first.
    try:
        profile = Profile.objects.get(user = request.user)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('jobboard:edit-profile'))

    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        job_form = JobPostForm(request.POST, instance=post)
        if job_form.is_valid():
            job_form.save()
            messages.success(request, "Your job post changes have been saved.")
            return HttpResponseRedirect(reverse('jobboard:profile-job-list'))
          
    else:
        job_form = JobPostForm(instance=post)

    context = {
        'post': post,
        'form': job_form,
    }

    return render(request, 'jobboard/edit_post.html', context)

def subscribe(request):

    if request.method == 'POST':
        subscriber_form = SubscriberForm(request.POST)
        if subscriber_form.is_valid():
            subscriber_form.save()
            messages.success(request, "You've successfully been signed up for new job post alerts.")
            return HttpResponseRedirect(reverse('jobboard:index')) 
    else:
        subscriber_form = SubscriberForm()

    context = {
        'form': subscriber_form,
    }

    return render(request, 'jobboard/subscribe.html', context)

def unsubscribe(request):
    if request.method == 'POST':
        unsubscriber_form = UnsubscriberForm(request.POST)
        if unsubscriber_form.is_valid():
            email_to_remove = unsubscriber_form.cleaned_data.get('email')
            try:
                subscriber = Subscriber.objects.get(email=email_to_remove)
                subscriber.delete()
            except ObjectDoesNotExist:
                messages.error(request, "ERROR: the email address you specified is not in the subscriber database.")
                return HttpResponseRedirect(reverse('jobboard:unsubscribe'))

            messages.success(request, "You've successfully been unsubscribed from new job post alerts.")
            return HttpResponseRedirect(reverse('jobboard:index')) 
    else:
        unsubscriber_form = UnsubscriberForm()

    context = {
        'form': unsubscriber_form,
    }

    return render(request, 'jobboard/unsubscribe.html', context)
    

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
