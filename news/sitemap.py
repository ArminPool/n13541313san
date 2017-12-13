from django.contrib.sitemaps import Sitemap
from posts.models import Post

import news.urls as homeurls


class PostsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Post.objects.all()


from django.core.urlresolvers import reverse


class StaticSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'

    # The below method returns all urls defined in urls.py file
    def items(self):
        mylist = []
        for url in homeurls.urlpatterns:
            mylist.append('home:' + url.name)
        return mylist

    def location(self, item):
        return reverse(item)
