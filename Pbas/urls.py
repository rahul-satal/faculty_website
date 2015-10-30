from django.conf import settings
from Pbas import views
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^index$', views.login, name='pbas_index'),
    url(r'^Home$', views.home_page, name='home_page'),
    url(r'^signup_action/$', views.signup_action, name='signup_action'),
    )