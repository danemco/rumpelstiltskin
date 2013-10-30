from django.conf.urls import patterns, url

from pinboard import views

urlpatterns = patterns('',
    url(r'^$', views.ListPins.as_view(), name="list-index"), # Index page to show a list of latest entries
)
