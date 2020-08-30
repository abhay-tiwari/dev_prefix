from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from datetime import datetime
import json

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

        related_blogs = Blog.objects.filter(category=blog.category and slug != blog.slug)[:6]

        for related_blog in related_blogs:
            tags = related_blog.tags
            tags = tags.split(",")
            related_blog.tags = tags

        comments = Comment.objects.filter(active=True, blog = blog)

        context = {
            "blog": blog,
            "related_blogs": related_blogs,
            "comments": comments
        }

        return render(request, "blogs/blog.html", context)

    else: 
        return HttpResponse("<h1>Page not found</h1>")

def add_comment(request):
    if request.method == "POST":
        author_name = request.POST["name"]
        author_email = request.POST["email"]
        comment = request.POST["comment"]
        blog_id = request.POST["blog_id"]

        blog = Blog.objects.filter(id=blog_id).first()

        comment = Comment(author_name=author_name, author_email=author_email, content=comment, blog=blog, active=False, created_on=datetime.now())
        comment.save()

        return redirect('/blogs/' + blog.slug)
        

def like_blog(request):
    if request.method == "POST":
        request_body = json.loads(request.body.decode('utf-8'))
        blog_id = request_body.get("blogId")
        is_liked = request_body.get("isLiked")
        blog = Blog.objects.filter(id=blog_id).first()
        likes_count = blog.likes_count

        if is_liked == True:
            likes_count += 1
        else:
            likes_count -= 1

        Blog.objects.filter(id=blog_id).update(likes_count=likes_count)

        return JsonResponse({"is_liked": is_liked}, status= 200)

    