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

def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password != password2:
            messages.error(request, "passwords does not match.")

        if User.objects.filter(username=username).exists():
            messages.error(request, "username already exists.")
            return redirect("register")
        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, "email already exists.")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password, email=email)
                user.save()
                messages.success(request, "you are now registered and can login")
                return redirect("login")

        return render(request, "accounts/register.html")
    return render(request, "accounts/register.html")


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "you are logged out successfully.")
        return redirect("index")
