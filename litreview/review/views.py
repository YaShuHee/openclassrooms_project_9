from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserFollows, Ticket, Review
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import FollowForm
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "review/sign_up.html", {"form": form})


def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
            return redirect("/feed/")
    else:
        form = AuthenticationForm(request)
    return render(request, "review/log_in.html", {"form": form})


@login_required(redirect_field_name=None)
def feed(request):
    return render(request, "review/base.html", {})


@login_required(redirect_field_name=None)
def follow(request):
    form = FollowForm()
    user = request.user
    if "unfollow" in request.GET:
        try:
            link = UserFollows.objects.get(id=request.GET.get("unfollow"))
            link.delete()
        except ObjectDoesNotExist:
            pass
    if "query" in request.GET:
        username = request.GET.get("query")
        try:
            to_follow = User.objects.get(username__iexact=username)
            if to_follow.id != user.id:
                follow_link = UserFollows(user=user, followed_user=to_follow)
                follow_link.save()
        except ObjectDoesNotExist:
            pass
    followers = UserFollows.objects.filter(followed_user=user)
    followed = UserFollows.objects.filter(user=user)
    return render(request, "review/follow.html", {"form": form, "followers": followers, "followed": followed})


@login_required(redirect_field_name=None)
def ticket_creation(request):
    return render(request, "review/base.html", {})


@login_required(redirect_field_name=None)
def ticket_modification(request, ticket_id):
    return render(request, "review/base.html", {})


@login_required(redirect_field_name=None)
def review_creation(request):
    return render(request, "review/base.html", {})


@login_required(redirect_field_name=None)
def review_modification(request, review_id):
    return render(request, "review/base.html", {})


@login_required(redirect_field_name=None)
def posts(request):
    return render(request, "review/base.html", {})


@login_required(redirect_field_name=None)
def log_out(request):
    logout(request)
    return redirect("/")
