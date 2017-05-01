__author__ = 'Makubex'
#coding: utf8
from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from django.views.generic.base import TemplateView
from Home import views

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='Home/index.html')),
)