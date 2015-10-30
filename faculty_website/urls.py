from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'faculty_website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^ShaligramPrajapat/', include('website.urls',namespace="website")),
    url(r'^Pbas/', include('Pbas.urls',namespace="pbas")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('favicon.urls')),
)
