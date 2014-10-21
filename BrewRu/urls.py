from django.conf.urls import patterns, include, url
from django.contrib import admin
import recipe

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BrewRu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^recipe/', include('recipe.urls')),
)
