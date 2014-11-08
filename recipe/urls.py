from django.conf.urls import patterns, include, url
from recipe import views

urlpatterns = patterns('',
    url(r'^(?P<recipe_id>\d+)$', views.view_recipe, name='view_recipe'),
    url(r'^(?P<recipe_id>\d+)/brew$', views.brewmaster, name='brewmaster'),
    url(r'^$', views.view_all_recipes, name='view_all_recipes'),
)