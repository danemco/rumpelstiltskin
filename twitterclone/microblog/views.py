# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from microblog.forms import EditProfileForm
from microblog.models import Profile, Post

def index(request):
    latest_posts = Post.objects.all().order_by('-pub_date')[:15]
    context = {'latest_posts' : latest_posts}
    return render(request, 'microblog/index.html', context)

def detail(request, username):
    latest_posts = Post.objects.filter(profile__user__username=username).order_by('-pub_date')[:15]
    profile      = Profile.objects.get(user__username=username)
    context = {
       'latest_posts' : latest_posts,
       'profile'      : profile,
    }
    return render(request, 'microblog/detail.html', context)

@login_required
def edit_profile(request, username):
    profile = Profile.objects.get(user__username=username)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            profile.bio = cd['bio']
            # handle the profile picture gracefully
            if cd.get('picture') is not None:
                profile.picture = cd['picture']
            profile.save()
            return HttpResponseRedirect(reverse('microblog:detail', args=(username,)))
        pass
    else:
        form = EditProfileForm(
            initial = {
                'bio' : profile.bio,
                'picture' : profile.picture,
            }
        )
    return render(request, 'microblog/edit_profile.html', {
        'form' : form, 
        'profile' : profile,
    })
