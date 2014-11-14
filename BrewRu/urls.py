from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
import recipe
import create
import start

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BrewRu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Homepage
    url(r'^$', TemplateView.as_view(template_name="base.html")),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^recipe/', include('recipe.urls')),
    url(r'^create/', include('create.urls')),
    url(r'^start/', include('start.urls')),
)
