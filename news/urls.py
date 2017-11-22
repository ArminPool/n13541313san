from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from posts.views import contact, about_us, advertising, set_timezone, search
from news import settings

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'', include('posts.urls')),
    url(r'^user/', include('users.urls')),
    url(r'^search/', search,name='search'),

    url(r'^contact/$', contact, name='Contact'),
    url(r'^about-us/$', about_us, name='about-us'),
    url(r'^advertising/$', advertising, name='advertising'),
    url(r'^timezone/$', set_timezone, name='timezone'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
