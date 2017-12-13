from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from posts.models import Post


class PostsSitemap(Sitemap):
    changefreq = "never"
    priority = 0.9

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class StaticSitemap(Sitemap):
    priority = 0.6
    changefreq = 'never'

    def items(self):
        mylist = ['pamm', 'mql', 'GOLD', 'EURUSD', 'USDJPY', 'GBPUSD', 'USDCHF', 'AUDUSD'
            , 'NZDUSD', 'BTCUSD', 'calender', 'Contact', 'search', 'metatrader', 'rules'
                  ]

        return mylist

    def location(self, item):
        return reverse(item)
