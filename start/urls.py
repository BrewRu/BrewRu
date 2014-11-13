from django.conf.urls import patterns, include, url
from start import views

urlpatterns = patterns('',
    url(r'^$', views.start, name='start'),
    url(r'^equipment$', views.equipment, name='equipment'),
)
