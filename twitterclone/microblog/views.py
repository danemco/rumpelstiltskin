# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from microblog.forms import EditProfileForm, NewPostForm
from microblog.models import Profile, Post

def index(request):
    latest_posts = Post.objects.all().order_by('-pub_date')[:15]
    context = {'latest_posts' : latest_posts}
    return render(request, 'microblog/index.html', context)

def detail(request, username):
    following = False
    try:
        profile      = Profile.objects.get(user__username=username)
    except ObjectDoesNotExist:
        u = User.objects.get(username=username)
        # user exists but no profile
        if u:
            profile = Profile(user=u)
            profile.save()

    if request.user.username == username:
        latest_posts = Post.objects.filter(profile__in=profile.following.all()).order_by('-pub_date')[:15]
    else:
        latest_posts = Post.objects.filter(profile__user__username=username).order_by('-pub_date')[:15]
    for user_profile in request.user.profile_set.all():
        if user_profile in profile.following.all():
            following = True
            break

    context = {
       'latest_posts': latest_posts,
       'profile': profile,
       'following': following,
    }
    return render(request, 'microblog/detail.html', context)

@login_required
def edit_profile(request, username):
    if request.user.username != username:
        return render(request, 'microblog/not_your_microblog.html')
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


@login_required
def add_post(request, username):
    if request.user.username != username:
        return render(request, 'microblog/not_your_microblog.html')


    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            # get the user's profile object
            profile = Profile.objects.get(user__username=username)

            # get the form data, create new Post object
            cd = form.cleaned_data
            p = Post(message=cd.get('message'), profile=profile)
            p.save()

            # take them back to the detail page
            return HttpResponseRedirect(reverse('microblog:detail', args=(username,)))
    else:
        form = NewPostForm()
        return render(request, 'microblog/add_post.html', {
            'form' : form
        })


@login_required
def follow(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    user_profile = get_object_or_404(Profile, user=request.user)
    user_profile.following.add(profile)
    user_profile.save()
    return HttpResponseRedirect(reverse('microblog:detail', args=(profile,)))

@login_required
def unfollow(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    user_profile = get_object_or_404(Profile, user=request.user)
    user_profile.following.remove(profile)
    user_profile.save()
    return HttpResponseRedirect(reverse('microblog:detail', args=(profile,)))


