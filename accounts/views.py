from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are not logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")

        return render(request, "accounts/login.html")
        
    return render(request, "accounts/login.html")

def dashboard(request):
    return render(request, "accounts/dashboard.html")


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "you are logged out successfully.")
        return redirect("index")
