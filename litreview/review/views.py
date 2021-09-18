from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        # pass
    return render(request, "review/base.html", {"connected": False, "content": "Feed page"})


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username, password)
        if user is not None:
            login(request, user)
            return redirect("/feed/")


def feed(request):
    return render(request, "litreview/base.html", {"connected": True, "content": "Feed page"})


def follow(request):
    pass


def ticket_creation(request):
    pass


def ticket_modification(request):
    pass


def review_creation(request):
    pass


def review_modification(request):
    pass