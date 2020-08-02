from django.shortcuts import render

def index(request):
    return render(request, "blogs/index.html")

def add_blogs(request):
    return render(request, "blogs/add-blog.html")

def blog(request, slug):
    return render(request, "blogs/blog.html")