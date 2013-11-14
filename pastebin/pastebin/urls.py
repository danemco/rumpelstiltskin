from django.conf.urls import patterns, include, url
from rest_framework import routers
from binpaste import views

router = routers.DefaultRouter()
router.register(r'bins', views.BinViewset)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pastebin.views.home', name='home'),
    # url(r'^pastebin/', include('pastebin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('binpaste.urls', namespace='binpaste')),
    url(r'^router/', include(router.urls)),
    url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework')),
)
