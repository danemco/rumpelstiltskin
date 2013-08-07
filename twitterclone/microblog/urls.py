from django.conf.urls import patterns, url

from microblog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<username>\w+)/$', views.detail, name='detail'),
)

