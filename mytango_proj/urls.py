from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mytango_proj.views.home', name='home'),
    # url(r'^mytango_proj/', include('mytango_proj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^Gumbo/', include('Gumbo.urls')), # SM IS ADDING THIS NEW TUPLE!
    url(r'^admin/', include(admin.site.urls)), # ADDED THIS LINE at DATABASE setup stage
)
