from django.conf.urls import patterns, url

from binpaste import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^(?P<pk>\d+)$', views.BinDetail.as_view(), name="detail"),
)
