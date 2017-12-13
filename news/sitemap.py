from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from posts.models import Post


class PostsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Post.objects.all()


class StaticSitemap(Sitemap):
    priority = 0.6
    changefreq = 'daily'

    # The below method returns all urls defined in urls.py file
    def items(self):
        mylist = ['pamm', 'mql', 'Gold', 'EURUSD', 'USDJPY', 'GBPUSD', 'USDCHF', 'AUDUSD'
            , 'NZDUSD', 'BTCUSD', 'calender', 'Contact', 'search', 'metatrader', 'rules'
                  ]
        for url_name in mylist:
            mylist.append(url_name)
        return mylist

    def location(self, item):
        return reverse(item)
