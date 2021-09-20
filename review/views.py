from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserFollows, Ticket, Review
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import FollowForm, NewTicketForm, NewReviewForm, NewTicketAndReviewForm
from django.core.exceptions import ObjectDoesNotExist
from itertools import chain


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
    if request.user.is_authenticated:
        return redirect("/feed/")
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
    users = [link.followed_user for link in UserFollows.objects.filter(user=request.user)]
    users.append(request.user)
    tickets = Ticket.objects.filter(user__in=users)
    reviews = Review.objects.filter(user__in=users)
    tickets_and_reviews = sorted(chain(tickets, reviews), key=lambda i: i.time_created, reverse=True)
    return render(request, "review/feed.html", {"tickets_and_reviews": tickets_and_reviews})


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
    form = NewTicketForm()
    if request.method == "POST":
        form = NewTicketForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            image = form.cleaned_data["image"]
            ticket = Ticket(title=title, description=description, user=request.user, image=image)
            ticket.save()
            return redirect("/feed/")
    return render(request, "review/ticket_creation.html", {"form": form})


@login_required(redirect_field_name=None)
def ticket_modification(request, ticket_id):
    return render(request, "review/base.html", {})


@login_required(redirect_field_name=None)
def ticket_deletion(request, ticket_id):
    try:
        ticket = Ticket.objects.get(id=ticket_id)
    except ObjectDoesNotExist:
        return redirect("/posts/")
    if request.method == "POST":
        if ticket.user == request.user:
            ticket.delete()
        return redirect("/posts/")
    return render(request, "review/ticket_deletion.html", {"ticket": ticket})


@login_required(redirect_field_name=None)
def review_creation(request, ticket_id):
    try:
        ticket = Ticket.objects.get(id=ticket_id)
    except ObjectDoesNotExist:
        return redirect("/feed/")
    form = NewReviewForm()
    if request.method == "POST":
        form = NewReviewForm(request.POST)
        if form.is_valid():
            headline = form.cleaned_data["headline"]
            rating = form.cleaned_data["rating"]
            body = form.cleaned_data["body"]
            review = Review(user=request.user, ticket=ticket, headline=headline, rating=rating, body=body)
            review.save()
            return redirect("/feed/")
    return render(request, "review/review_creation.html", {"form": form, "ticket": ticket})


@login_required(redirect_field_name=None)
def ticket_and_review_creation(request):
    form = NewTicketAndReviewForm()
    if request.method == "POST":
        form = NewTicketAndReviewForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            image = form.cleaned_data["image"]
            ticket = Ticket(user=request.user, title=title, description=description, image=image)
            ticket.save()
            headline = form.cleaned_data["headline"]
            rating = form.cleaned_data["rating"]
            body = form.cleaned_data["body"]
            review = Review(user=request.user, ticket=ticket, headline=headline, rating=rating, body=body)
            review.save()
            return redirect("/feed/")
    return render(request, "review/ticket_and_review_creation.html", {"form": form})


@login_required(redirect_field_name=None)
def review_modification(request, review_id):
    return render(request, "review/base.html", {})


@login_required(redirect_field_name=None)
def review_deletion(request, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except ObjectDoesNotExist:
        return redirect("/posts/")
    if request.method == "POST":
        if review.user == request.user:
            review.delete()
        return redirect("/posts/")
    return render(request, "review/review_deletion.html", {"review": review})


@login_required(redirect_field_name=None)
def posts(request):
    tickets = Ticket.objects.filter(user=request.user)
    reviews = Review.objects.filter(user=request.user)
    posts = sorted(chain(tickets, reviews), key=lambda i: i.time_created, reverse=True)
    return render(request, "review/posts.html", {"posts": posts})


@login_required(redirect_field_name=None)
def log_out(request):
    logout(request)
    return redirect("/")
