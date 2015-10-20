from django.conf.urls import url
from django.conf import settings
from website import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^projects$', views.ongoing_projects, name='ongoing_projects'),
    #url(r'^website/projects$', views.ongoing_projects, name='ongoing_projects'),
            #Projects
    url(r'^projects/ongoing_projects$', views.ongoing_projects, name='ongoing_projects'),
    url(r'^projects/completed_projects$', views.completed_projects, name='completed_projects'),
    url(r'^Myfriend$', views.myfriends, name='Myfriend'),
            #Teachings
    url(r'^Lectures$', views.lecture, name='lecture'),
    url(r'^InnovativeTeaching$', views.innovative_teaching, name='innovative_teaching'),
    url(r'^AdditionalTeaching$', views.additional_teaching, name='additional_teaching'),
            #Publications
    url(r'^Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^Chapters_Published$', views.chapters_published, name='chapters_published'),
    url(r'^Full_Papers$', views.full_papers, name='full_papers'),
    url(r'^Books_Published$', views.books_published, name='books_published'),




    url(r'^Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^Published_Papers$', views.published_papers, name='published_papers'),                                         

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
]