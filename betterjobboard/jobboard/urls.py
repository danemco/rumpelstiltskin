from django.conf.urls import patterns, url

from jobboard import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^job/(?P<post_id>\d+)/$', views.post_detail, name="detail"),
    url(r'^job/new/$', views.new_post, name='new-post'),
    url(r'^job/(?P<post_id>\d+)/edit/$', views.edit_post, name="edit-post"),
    url(r'^job/list/$', views.profile_job_list, name='profile-job-list'),
    url(r'^profile/edit/$', views.edit_profile, name='edit-profile'),
    url(r'^subscribe/$', views.subscribe, name='subscribe'),
    url(r'^unsubscribe/$', views.unsubscribe, name='unsubscribe'),
)
