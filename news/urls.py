from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from posts.views import search, economic_calender, calender
from specificpages.views import specific_pages
from users.views import contact
from . import settings

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'', include('posts.urls')),
    url(r'^user/', include('users.urls')),
    url(r'^search/', search, name='search'),
    url(r'^mql5/$', TemplateView.as_view(template_name='specificpages/mql.html')),
    url(r'^pamm/$', TemplateView.as_view(template_name='specificpages/pamm.html')),
    url(r'^chart/GOLD/$', TemplateView.as_view(template_name='specificpages/GOLD.html')),
    url(r'^chart/EURUSD/$', TemplateView.as_view(template_name='specificpages/EURUSD.html')),
    url(r'^chart/USDJPY/$', TemplateView.as_view(template_name='specificpages/USDJPY.html')),
    url(r'^chart/USDJPY/$', TemplateView.as_view(template_name='specificpages/GBPUSD.html')),

    url(r'^chart/USDCHF/$', TemplateView.as_view(template_name='specificpages/USDCHF.html')),
    url(r'^chart/AUDUSD/$', TemplateView.as_view(template_name='specificpages/AUDUSD.html')),
    url(r'^chart/NZDUSD/$', TemplateView.as_view(template_name='specificpages/NZDUSD.html')),
    url(r'^chart/BTCUSD/$', TemplateView.as_view(template_name='specificpages/BTCUSD.html')),

    url(r'^economicCalendar/$', economic_calender, name='economic_calendar'),
    url(r'^contact/$', contact, name='Contact'),

    url(r'^calender/$', calender, name='calender'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
