from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from posts.views import search, economic_calender, calender
from specificpages.views import specific_pages
from users.views import contact
from . import settings

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'', include('posts.urls')),
    url(r'^user/', include('users.urls')),
    url(r'^search/', search, name='search'),
    url(r'^specificpages/(?P<page>.+)/$',specific_pages,name="specific-pages"),
    url(r'^economicCalendar/$', economic_calender, name='economic_calendar'),
    url(r'^contact/$', contact, name='Contact'),

    url(r'^calender/$', calender, name='calender'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
