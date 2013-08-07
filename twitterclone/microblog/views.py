# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

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
    
    pass
