from django.shortcuts import render
from django.http import HttpResponse

from .models import Blog, Comment

def index(request):
    return render(request, "blogs/index.html")

def add_blogs(request):
    return render(request, "blogs/add-blog.html")

def blog(request, slug):
    blogs = Blog.objects.filter(slug = slug)

    if blogs.exists():
        blog = blogs.first()
        
        tags = blog.tags
        tags = tags.split(",")
        blog.tags = tags

        related_blogs = Blog.objects.filter(category=blog.category)[:6]

        for related_blog in related_blogs:
            tags = related_blog.tags
            tags = tags.split(",")
            related_blog.tags = tags

        comments = Comment.objects.filter(blog=blog)

        context = {
            "blog": blog,
            "related_blogs": related_blogs,
            "comments": comments
        }

        return render(request, "blogs/blog.html", context)

    else: 
        return HttpResponse("<h1>Page not found</h1>")