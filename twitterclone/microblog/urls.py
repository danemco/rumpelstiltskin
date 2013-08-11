from django.conf.urls import patterns, url

from microblog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<username>\w+)/$', views.detail, name='detail'),
    url(r'^(?P<username>\w+)/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^(?P<username>\w+)/add/$', views.add_post, name='add_post'),
)

