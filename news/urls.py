from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps import Sitemap
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap

from news.sitemap import PostsSitemap
from posts.views import search, economic_calender, calender
from specificpages.views import specific_pages
from users.views import contact
from . import settings


class StaticSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'

    # The below method returns all urls defined in urls.py file
    def items(self):
        mylist = []
        for url in mylist:
            mylist.append('home:' + url.name)
        return mylist

    def location(self, item):
        return reverse(item)


sitemaps = {
    'post': PostsSitemap(),
    'static': StaticSitemap(),
}
urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'', include('posts.urls')),
    url(r'^user/', include('users.urls')),
    url(r'^search/', search, name='search'),
    url(r'^software/metatrader/$', TemplateView.as_view(template_name='specificpages/metatrader.html')),
    url(r'^rules/$', TemplateView.as_view(template_name='specificpages/rules.html')),
    url(r'^about-us/$', TemplateView.as_view(template_name='specificpages/about-us.html')),
    url(r'^tariffs/$', TemplateView.as_view(template_name='specificpages/tariffs.html')),

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
    url(r'^contact-us/$', contact, name='Contact'),

    url(r'^calender/$', calender, name='calender'),

    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'), ]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
