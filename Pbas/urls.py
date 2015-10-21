from django.conf.urls import url
from django.conf import settings
from Pbas import views

urlpatterns = [
    url(r'^Index$', views.login, name='pbas_index'),
    url(r'^Home$', views.home_page, name='home_page'),
    '''
    url(r'^Index$', views.pbas_index, name='pbas_index'),
    url(r'^Index$', views.pbas_index, name='pbas_index'),
    url(r'^Index$', views.pbas_index, name='pbas_index'),
    url(r'^Index$', views.pbas_index, name='pbas_index'),
    url(r'^Index$', views.pbas_index, name='pbas_index'),
    url(r'^Index$', views.pbas_index, name='pbas_index'),
    url(r'^Index$', views.pbas_index, name='pbas_index'),
    url(r'^Index$', views.pbas_index, name='pbas_index'),
    url(r'^Index$', views.pbas_index, name='pbas_index'),
    url(r'^Index$', views.pbas_index, name='pbas_index'),
    url(r'^Index$', views.pbas_index, name='pbas_index'),
    url(r'^Index$', views.pbas_index, name='pbas_index'),
    url(r'^Index$', views.pbas_index, name='pbas_index'),
    url(r'^Index$', views.pbas_index, name='pbas_index'),
    url(r'^Index$', views.pbas_index, name='pbas_index'),
    url(r'^Index$', views.pbas_index, name='pbas_index'),'''
 

    ]