from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime

from blogs.models import Blog, Category


@login_required()
def dashboard(request):
    return render(request, 'users/dashboard.html')

@login_required()
def add_blog(request):
    if request.method == "POST":
        title = request.POST['title']
        meta_title = request.POST['meta-title']
        slug = request.POST['slug']
        summary = request.POST['summary']
        author_name = request.POST['author']
        category_name = request.POST['category']
        tags = request.POST['tags']
        meta_tags = request.POST['meta-tags']
        meta_description = request.POST['meta-description']
        content = request.POST['content']
        likes_count = 0
        comments_count = 0
        share_count = 0
        read_duration = 0
        created_on = datetime.now()

        author = User.objects.filter(username=author_name).first()
        category = Category.objects.filter(name=category_name).first()

        blog = Blog(title=title, body=content,summary=summary, author=author, tags=tags, likes_count=likes_count, comments_count=comments_count, share_count=share_count, created_on= created_on, read_duration=read_duration, meta_title=meta_title, meta_description=meta_description, meta_tags=meta_tags, category=category)

        blog.save()

        return redirect('add_blog')
    
    return render(request, 'users/add-blog.html')

@login_required()
def get_all_blogs(request):
    blogs = Blog.objects.filter(is_deleted=False)

    context = {
        'blogs': blogs
    }

    return render(request, 'users/blogs.html', context)

@login_required()
def update_blog(request, blog_id):
    if request.method == "POST":
        author_id = request.POST["author"]
        category_id = request.POST["category"]

        author = User.objects.filter(id=author_id).first()
        category = Category.objects.filter(id=category_id).first()

        Blog.objects.update_or_create(id=blog_id, defaults = {
            "title": request.POST["title"],
            "meta_title": request.POST["meta-title"],
            "slug": request.POST["slug"],
            "summary": request.POST["summary"],
            "author": author,
            "category": category,
            "tags": request.POST["tags"],
            "meta-tags": request.POST["meta-tags"],
            "meta-description": request.POST["meta-description"],
            "body": request.POST["content"],
            "updated_on": datetime.now()
        })

        messages.success(request, "Blog updated successfully.")

        return redirect("all_blogs")

    blog = Blog.objects.filter(id=blog_id).first()

    authors = User.objects.all()
    categories = Category.objects.all()
    
    context = { 
        'blog': blog,
        'authors': authors,
        'categories': categories
    }

    return render(request, 'users/add-blog.html', context=context)

@login_required()
def delete_blog(request):
    if request.method == "POST":
        blog_id = int(request.POST["blog-id"])
        blog = Blog.objects.filter(id = blog_id).first()

        if blog.is_deleted == True:
            messages.error(request, "Blog is already deleted.")

        else:
            blog.is_deleted = True
            blog.deleted_on = datetime.now()
            blog.save()
            messages.success(request, "Blog deleted successfully.")

        return redirect("all_blogs")

@login_required()
def publish_blog(request):
    if request.method == "POST":
        blog_id = int(request.POST["blog-id"])
        blog = Blog.objects.filter(id = blog_id).first()

        if blog.is_published == True:
            messages.error(request, "Blog is already published")
        else:
            blog.is_published = True
            blog.publish_date = datetime.now()
            blog.save()

            messages.success(request, "Blog published successfully.")

        return redirect("all_blogs")