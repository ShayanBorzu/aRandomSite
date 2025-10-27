from django.urls import path
from blogApp.views import blog_index_view, blog_details_view, blog_search_view

app_name = "blog"

urlpatterns = [
    path("index/", blog_index_view, name="index"),
    path("details/<int:pk>", blog_details_view, name="details"),
    path("tag/<str:tag>/", blog_index_view, name="tag"),
    path("category/<str:category>/", blog_index_view, name="category"),
    path("author/<str:author>/", blog_index_view, name="author"),
    path("search/", blog_search_view, name="search"),
    
]
