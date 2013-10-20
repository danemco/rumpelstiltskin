from django.conf.urls import patterns, url

from timeclock import views

urlpatterns = patterns('',
    url(r'^$', views.ListEntries.as_view(), name="index"), # Index page to show a list of latest entries
    url(r'^detail/(?P<pk>\d+)/$', views.detail, name="detail"), # Detail of a time card entry
    url(r'^edit/(?P<pk>\d+)/$', views.edit, name="detail"), # Detail of a time card entry
    url(r'^clock-in/', ),
    url(r'^clock-out/', ),
)


