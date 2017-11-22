from django.conf.urls import url, include

from .views import homepage, set_timezone, articles, news, calender, economic_calender
from .views import detail, tags,author

# namespace
app_name = 'posts'

urlpatterns = [

    url(r'^$', homepage, name='home'),
    url(r'^post/(?P<header>.+)/$', detail, name='detail'),

    url(r'^tag/(?P<tag>.+)/$', tags, name='tag'),
    url(r'^EconomicCalendar/$', economic_calender, name='economic_calendar'),

    url(r'^calender/$', calender, name='calender'),

    url(r'^author/(?P<author>.+)/$', author, name='author'),
    url(r'^articles/(?P<type>.+)/$', articles, name='articles'),
    url(r'^news/$', news, name='news'),

]
