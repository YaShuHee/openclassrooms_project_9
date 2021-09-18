from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
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
    return render(request, "review/base.html", {"connected": True, "content": "Feed page"})


def follow(request):
    return render(request, "review/base.html", {"connected": False, "content": "Follow page"})


def ticket_creation(request):
    return render(request, "review/base.html", {"connected": False, "content": "Ticket creation page"})


def ticket_modification(request, ticket_id):
    return render(request, "review/base.html", {"connected": False, "content": f"Ticket {ticket_id} modification page"})


def review_creation(request):
    return render(request, "review/base.html", {"connected": False, "content": "Review creation page"})


def review_modification(request, review_id):
    return render(request, "review/base.html", {"connected": False, "content": f"Review {review_id} modification page"})


def posts(request):
    return render(request, "review/base.html", {"connected": False, "content": "Posts page"})