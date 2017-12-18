from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps import Sitemap
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap

from news.sitemap import PostsSitemap, StaticSitemap
from posts.views import search, economic_calender, calender
from specificpages.views import specific_pages
from users.views import contact
from . import settings




sitemaps = {
    'post': PostsSitemap(),
    'static': StaticSitemap(),
}
urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'', include('posts.urls')),
    url(r'^user/', include('users.urls')),
    url(r'^search/', search, name='search'),
    url(r'^software/metatrader/$', TemplateView.as_view(template_name='specificpages/metatrader.html'),name='metatrader'),
    url(r'^rules/$', TemplateView.as_view(template_name='specificpages/rules.html'),name='rules'),
    url(r'^about-us/$', TemplateView.as_view(template_name='specificpages/about-us.html'),name='about-us'),
    url(r'^tariffs/$', TemplateView.as_view(template_name='specificpages/tariffs.html'),name='tariffs'),

    url(r'^mql5/$', TemplateView.as_view(template_name='specificpages/mql.html'),name='mql'),
    url(r'^pamm/$', TemplateView.as_view(template_name='specificpages/pamm.html'),name='pamm'),
    url(r'^chart/GOLD/$', TemplateView.as_view(template_name='specificpages/GOLD.html'),name='GOLD'),
    url(r'^chart/EURUSD/$', TemplateView.as_view(template_name='specificpages/EURUSD.html'),name='EURUSD'),
    url(r'^chart/USDJPY/$', TemplateView.as_view(template_name='specificpages/USDJPY.html'),name='USDJPY'),
    url(r'^chart/USDJPY/$', TemplateView.as_view(template_name='specificpages/GBPUSD.html'),name='GBPUSD'),

    url(r'^chart/USDCHF/$', TemplateView.as_view(template_name='specificpages/USDCHF.html'),name='USDCHF'),
    url(r'^chart/AUDUSD/$', TemplateView.as_view(template_name='specificpages/AUDUSD.html'),name='AUDUSD'),
    url(r'^chart/NZDUSD/$', TemplateView.as_view(template_name='specificpages/NZDUSD.html'),name='NZDUSD'),
    url(r'^chart/BTCUSD/$', TemplateView.as_view(template_name='specificpages/BTCUSD.html'),name='BTCUSD'),

    url(r'^economicCalender/$', economic_calender, name='economic_calendar'),
    url(r'^contact-us/$', contact, name='Contact'),

    url(r'^calender/$', calender, name='calender'),

    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'), ]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
