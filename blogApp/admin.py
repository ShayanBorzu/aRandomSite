from django.contrib import admin
from .models import Tag, Category, Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'is_published', 'published_at', 'created_at', 'views')
    list_filter = ('is_published', 'published_at', 'tags', 'categories')
    search_fields = ('title', 'content', 'author__username')
    filter_horizontal = ('tags', 'categories') 
    readonly_fields = ('views', 'created_at', 'updated_at')
    date_hierarchy = 'published_at'
    ordering = ('-created_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display= ('full_name', 'email')
    list_filter = ('is_approved',)
    