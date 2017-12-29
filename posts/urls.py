# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.views.generic import TemplateView

from posts import views
from .views import homepage, articles, news
from .views import detail, tags,author

# namespace
app_name = 'posts'

urlpatterns = [

    url(r'^$', homepage, name='home'),
    url(r'^post/(?P<header>.+)/$', detail, name='detail'),
    url(r'^tag/(?P<tag>.+)/$', tags, name='tag'),
    url(r'^author/(?P<author_username>.+)/$', author, name='author-view'),
    url(r'^articles/(?P<find>.+)/$', articles, name='articles'),
    url(r'^news/$', news, name='news'),
    url(r'^basic-upload/$', views.upload_photo_affiliate, name='upload-photo-affiliate'),

]
