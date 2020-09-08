from django.shortcuts import render
from django.http import HttpResponse

from blogs.models import Blog, Category

def index(request):
    blogs = Blog.objects.filter(is_deleted=False, is_published=True).order_by('-publish_date')[:5]
    categories = Category.objects.all()

    for blog in blogs:
        tags_str = blog.tags
        tags_arr = tags_str.split(",")
        blog.tags = tags_arr 
        blog.summary += "..."

    context = { 
        "blogs": blogs,
        "categories": categories
    }

    return render(request, 'pages/index.html', context)

def category(request, category_name):

    category = Category.objects.filter(name=category_name).first()

    blogs = Blog.objects.filter(category=category, is_published=True, is_deleted=False)[:5]

    for blog in blogs:
        tags_str = blog.tags
        tags_arr = tags_str.split(",")
        blog.tags = tags_arr 
        blog.summary += "..."

    context = {
        "blogs": blogs,
        "category_name": category_name
    }

    return render(request, 'pages/category.html', context)

def about(request):
    return render(request, 'pages/about.html')

def privacy_policy(request):
    return render(request, 'pages/privacy-policy.html')

def cookie_policy(request):
    return render(request, 'pages/cookie-policy.html')

def terms_conditions(request):
    return render(request, 'pages/terms-conditions.html')

def blog(request):
    return render(request, 'pages/blog.html')