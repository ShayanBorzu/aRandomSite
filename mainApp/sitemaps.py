from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1
    changefreq = 'never'

    def items(self):
        return ['main:index', 'main:about', 'main:contact']

    def location(self, item): # type: ignore
        return reverse(item)