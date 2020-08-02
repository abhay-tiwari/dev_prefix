from django.shortcuts import render
from django.http import HttpResponse

from blogs.models import Blog, Category

def index(request):
    
    blogs = Blog.objects.all()
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
    context = {
        "category": category_name
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