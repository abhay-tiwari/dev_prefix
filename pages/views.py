from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')

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
