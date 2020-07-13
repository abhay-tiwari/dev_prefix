from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("index page.")

def about(request):
    return HttpResponse("about page")

def privacy_policy(request):
    return HttpResponse("privacy policy page.")

def cookie_policy(request):
    return HttpResponse("cookie policy page.")

def terms_conditions(request):
    return HttpResponse("terms and conditions page.")
