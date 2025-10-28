from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blogApp.models import Post, Comment
from django.utils import timezone
from blogApp.forms import CommentForm, NewsLetterForm
from django.contrib import messages
# Create your views here.

def blog_index_view(request, tag=None, category=None, author=None):
    posts = Post.objects.filter(is_published=True, published_at__lte=timezone.now())
    if request.method == "POST":
        newslettform =  NewsLetterForm(request.POST)
        if newslettform.is_valid():
            newslettform.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Thank you for signing up in our Newsletter.",
            )
        else:
            messages.add_message(
                request, messages.ERROR, "Error encountered. empty cache and try again."
            )
    if tag:
        posts = posts.filter(tags__name=tag)
    elif category:
        posts = posts.filter(categories__name=category)
    elif category:
        posts = posts.filter(author__username=author)
    posts = Paginator(posts, 4)
    try:  
        page = int(request.GET.get('p', 1))
        posts = posts.page(page)
    except (EmptyPage, ValueError, PageNotAnInteger):
        raise 

    return render(request, 'blogApp/blog_index.html', {'posts': posts})

def blog_search_view(request):
    query = request.GET.get('search')
    posts = Post.objects.filter(is_published=True, published_at__lte=timezone.now())
    if query:
        posts = (posts.filter(content__icontains=query) | posts.filter(title__icontains=query)).distinct()
    return render(request, 'blogApp/blog_index.html', {'posts': posts})

    
def blog_details_view(request, pk):
    post = get_object_or_404(Post, is_published=True, published_at__lte=timezone.now(), id=pk)
    comments = Comment.objects.filter(post=post, is_approved=True)
    if request.method == "POST":
        newslettform =  NewsLetterForm(request.POST)
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.post = post
            comment.save()
            
            messages.add_message(
                request,
                messages.SUCCESS,
                "Thank you for commenting. Your comment is awaiting approval.",
            )
            return redirect('blog:details', pk=post.pk)
            
        elif newslettform.is_valid():
            newslettform.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Thank you for signing up in our Newsletter.",
            )
            return redirect('blog:index')
        else:
            messages.add_message(
                request, messages.ERROR, "Error encountered. empty cache and try again."
            )
    post.views += 1
    post.save(update_fields=['views'])
    return render(request, 'blogApp/blog_details.html', {'post': post, 'comments': comments})