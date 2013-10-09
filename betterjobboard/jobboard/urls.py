from django.conf.urls import patterns, url

from jobboard import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^job/(?P<post_id>\d+)/$', views.post_detail, name="detail"),
    url(r'^job/new/$', views.new_post, name='new-post'),
    url(r'^job/list/$', views.profile_job_list, name='profile-job-list'),
    url(r'^subscribe/$', views.subscribe, name='subscribe'),
    url(r'^subscribe/success/$', views.subscribe_success, name='subscribe-success'),
    url(r'^unsubscribe/$', views.unsubscribe, name='unsubscribe'),
    url(r'^unsubscribe/success/$', views.unsubscribe_success, name='unsubscribe-success'),
    url(r'^profile/edit/$', views.edit_profile, name='edit-profile'),
)
