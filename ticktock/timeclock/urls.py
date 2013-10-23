from django.conf.urls import patterns, url

from timeclock import views

urlpatterns = patterns('',
    url(r'^$', views.ListRecords.as_view(), name="index"), # Index page to show a list of latest entries
    url(r'^record/(?P<pk>\d+)/$', views.RecordDetail.as_view(), name="record-detail"), # Detail of a time card entry
    # url(r'^record/(?P<pk>\d+)/edit/$', views.edit, name="record-edit"), # Detail of a time card entry
    # url(r'^record/(?P<pk>\d+)/delete/$', views.edit, name="record-delete"), # Detail of a time card entry
    # url(r'^record/(?P<pk>\d+)/add/$', views.edit, name="record-add"), # Detail of a time card entry
    # url(r'^project/(?P<pk>\d+)/$', views.EntryDetail.as_view(), name="project-detail"), # Detail of a time card entry
    # url(r'^project/(?P<pk>\d+)/edit/$', views.edit, name="project-edit"), # Detail of a time card entry
    # url(r'^project/(?P<pk>\d+)/delete/$', views.edit, name="project-delete"), # Detail of a time card entry
    # url(r'^project/(?P<pk>\d+)/add/$', views.edit, name="project-add"), # Detail of a time card entry
    #url(r'^clock-in/', ),
    #url(r'^clock-out/', ),
)


