from django.conf.urls import url
from django.conf import settings
from website import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^projects$', views.ongoing_projects, name='ongoing_projects'),
    #url(r'^website/projects$', views.ongoing_projects, name='ongoing_projects'),
            #Projects
    url(r'^ShaligramPrajapat/projects/ongoing_projects$', views.ongoing_projects, name='ongoing_projects'),
    url(r'^ShaligramPrajapat/projects/completed_projects$', views.completed_projects, name='completed_projects'),
    url(r'^ShaligramPrajapat/Myfriend$', views.myfriends, name='Myfriend'),
            #Teachings
    url(r'^ShaligramPrajapat/Lectures$', views.lecture, name='lecture'),
    url(r'^ShaligramPrajapat/InnovativeTeaching$', views.innovative_teaching, name='innovative_teaching'),
    url(r'^ShaligramPrajapat/AdditionalTeaching$', views.additional_teaching, name='additional_teaching'),
            #Publications
    url(r'^ShaligramPrajapat/Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^ShaligramPrajapat/Chapters_Published$', views.chapters_published, name='chapters_published'),
    url(r'^ShaligramPrajapat/Full_Papers$', views.full_papers, name='full_papers'),
    url(r'^ShaligramPrajapat/Books_Published$', views.books_published, name='books_published'),




    url(r'^ShaligramPrajapat/Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^ShaligramPrajapat/Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^ShaligramPrajapat/Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^ShaligramPrajapat/Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^ShaligramPrajapat/Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^ShaligramPrajapat/Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^ShaligramPrajapat/Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^ShaligramPrajapat/Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^ShaligramPrajapat/Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^ShaligramPrajapat/Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^ShaligramPrajapat/Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^ShaligramPrajapat/Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^ShaligramPrajapat/Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^ShaligramPrajapat/Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^ShaligramPrajapat/Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^ShaligramPrajapat/Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^ShaligramPrajapat/Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^ShaligramPrajapat/Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^ShaligramPrajapat/Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^ShaligramPrajapat/Published_Papers$', views.published_papers, name='published_papers'),  

                    ###########   pbas    ###########

    url(r'^Pbas/Index$', views.pbas_index, name='pbas_index'),
    url(r'^Pbas/Index$', views.published_papers, name='published_papers'),
    url(r'^Pbas/Index$', views.published_papers, name='published_papers'),
    url(r'^Pbas/Index$', views.published_papers, name='published_papers'),
    url(r'^Pbas/Index$', views.published_papers, name='published_papers'),
    url(r'^Pbas/Index$', views.published_papers, name='published_papers'),
    url(r'^Pbas/Index$', views.published_papers, name='published_papers'),
    url(r'^Pbas/Index$', views.published_papers, name='published_papers'),
    url(r'^Pbas/Index$', views.published_papers, name='published_papers'),
    url(r'^Pbas/Index$', views.published_papers, name='published_papers'),
    url(r'^Pbas/Index$', views.published_papers, name='published_papers'),
    url(r'^Pbas/Index$', views.published_papers, name='published_papers'),
    url(r'^Pbas/Index$', views.published_papers, name='published_papers'),
    url(r'^Pbas/Index$', views.published_papers, name='published_papers'),
    url(r'^Pbas/Index$', views.published_papers, name='published_papers'),
    url(r'^Pbas/Index$', views.published_papers, name='published_papers'),
    url(r'^Pbas/Index$', views.published_papers, name='published_papers'),
    url(r'^Pbas/Index$', views.published_papers, name='published_papers'),
    url(r'^ShaligramPrajapat/Published_Papers$', views.published_papers, name='published_papers'),
    url(r'^ShaligramPrajapat/Published_Papers$', views.published_papers, name='published_papers'),                                          

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
]