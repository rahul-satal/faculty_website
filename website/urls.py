from django.conf.urls import url
from django.conf import settings
from website import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^projects$', views.ongoing_projects, name='ongoing_projects'),
    url(r'^website/projects$', views.ongoing_projects, name='ongoing_projects'),
    url(r'^ShaligramPrajapat/projects/ongoing_projects$', views.ongoing_projects, name='ongoing_projects'),
    url(r'^ShaligramPrajapat/projects/completed_projects$', views.completed_projects, name='completed_projects'),
    url(r'^ShaligramPrajapat/Myfriend$', views.myfriends, name='Myfriend'),
    url(r'^ShaligramPrajapat/Lectures$', views.lecture, name='lecture'),
    url(r'^ShaligramPrajapat/InnovativeTeaching$', views.innovative_teaching, name='innovative_teaching'),
    url(r'^ShaligramPrajapat/AdditionalTeaching$', views.additional_teaching, name='additional_teaching'),
    url(r'^ShaligramPrajapat/projects/completed_projects$', views.completed_projects, name='completed_projects'),
    url(r'^ShaligramPrajapat/projects/completed_projects$', views.completed_projects, name='completed_projects'),


    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
]