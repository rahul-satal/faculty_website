from django.conf.urls import url
from django.conf import settings
from website import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^projects$', views.ongoing_projects, name='ongoing_projects'),
    url(r'^website/projects$', views.ongoing_projects, name='ongoing_projects'),

    url(r'^ShaligramPrajapat/projects/completed_projects^$', views.completed_projects, name='completed_projects'),


    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
]