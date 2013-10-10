from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from jobboard.views import MyRegistrationBackend

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'betterjobboard.views.home', name='home'),
    # url(r'^betterjobboard/', include('betterjobboard.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^jobboard/', include('jobboard.urls', namespace='jobboard')),
    url(r'^accounts/register/', MyRegistrationBackend.as_view(), name="registration_register"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
