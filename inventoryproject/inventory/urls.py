from django.conf.urls import patterns, url

from inventory import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<category_id>\d+)/$', views.category_detail, name='detail'),
    url(r'^category/add/$', views.category_add, name='category_add'),
    url(r'^item/(?P<item_id>\d+)/edit/$', views.item_update, name='adjust_qty'),
    url(r'^item/(?P<item_id>\d+)/get/$', views.item_qty_get, name='get_qty'),
)
