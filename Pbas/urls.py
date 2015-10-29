from django.conf import settings
from Pbas import views
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^index$', views.login, name='pbas_index'),
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
 

    )