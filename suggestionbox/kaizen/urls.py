from django.conf.urls import patterns, url

from kaizen import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'), # list all kaizens for the user
    url(r'^detail/(?P<idea_id>\d+)$', views.detail, name='detail'), # details for an idea, including comments
    url(r'^detail/(?P<idea_id>\d+)/comment/new/$', views.new_comment, name='new-comment'), # post a new comment
    url(r'^detail/(?P<idea_id>\d+)/changestatus/$', views.change_status, name='change-status'), # Change the status for a deal
    url(r'^new-idea/$', views.new_idea, name='new-idea'), # form for posting a new idea
)

