from django.contrib.sitemaps import Sitemap
from posts.models import Post

from .urls import urlpatterns as homeUrls

class PostsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Post.objects.all()

