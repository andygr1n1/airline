from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        # return render(request, "users/login.html", {
        #     "message": "You are not logged in"
        # })
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid username and/or password"
            })
    return render(request, "users/login.html")


def logout_view(request):
    return render(request, "users/logout.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        # register user
        user = User.objects.create_user(username=username, email=email, password=password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/register.html", {
                "message": "Invalid username and/or password"
            })
    return render(request, "users/register.html")
