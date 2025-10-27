from django.template import Library
from blogApp.models import Tag, Category, Post
from django.utils import timezone

register = Library()


@register.inclusion_tag(filename="templatetags/blogApp/tags.html")
def tags():
    posts = Post.objects.filter(is_published=True, published_at__lte=timezone.now())
    posts_tags = posts.values_list('tags__id', flat=True).distinct()
    tags = Tag.objects.filter(id__in=posts_tags)
    return {"tags": tags}


@register.inclusion_tag(filename="templatetags/blogApp/categories.html")
def categories():
    posts = Post.objects.filter(is_published=True, published_at__lte=timezone.now())
    categories = Category.objects.all()
    available_categories = {}
    for category in categories:
        if posts.filter(categories=category).count() != 0:
            available_categories[category] = posts.filter(categories=category).count()
    return {"categories": available_categories}


@register.inclusion_tag(filename="templatetags/blogApp/recent_posts.html")
def recent_posts():
    posts = Post.objects.filter(is_published=True, published_at__lte=timezone.now()).order_by('-created_at')[:3]
    return {"posts": posts}

@register.inclusion_tag(filename="templatetags/blogApp/search.html")
def search():
    return {}