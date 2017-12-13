from django.contrib.sitemaps import Sitemap
from posts.models import Post


class PostsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Post.objects.all()

