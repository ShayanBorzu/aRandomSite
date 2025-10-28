from django.db import models
from django.utils import timezone
from django.urls import reverse


class Tag(models.Model):
    """Tag model for posts"""

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    """Category model for posts"""

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    """Blog post model"""

    thumbnail = models.ImageField(
        upload_to=r"thumbnail/%Y/%m/%d/", default="blog_thumbnails/default.webp"
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(
        "Tag",
        related_name="posts",
    )
    categories = models.ManyToManyField(
        "Category",
        related_name="posts",
    )
    def read_time(self):
        time = round(len(self.content.split()) / 200)
        if time == 0:
            return '~ 1'
        return '~ ' + str(time)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Return the URL for this post"""
        return reverse('blog:details', kwargs={'pk': self.pk})
    class Meta:
        ordering = ["-created_at"]
        

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email Address",blank=True, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)
    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ["-created_at"]
        
class NewsLetter(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email