from django.conf.urls import patterns, url
from Gumbo import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),

        url(r'^my_graph$', views.graph, name='graph'),
        )

