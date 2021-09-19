"""litreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.log_in, name="log_in"),
    path('signup/', views.sign_up, name="sign_up"),
    path('feed/', views.feed, name="feed"),
    path('follow/', views.follow, name="follow"),
    path('ticket/new/', views.ticket_creation, name="ticket_creation"),
    path('ticket/update/<int:ticket_id>/', views.ticket_modification, name="ticket_modification"),
    path('ticket/delete/<int:ticket_id>/', views.ticket_deletion, name="ticket_deletion"),
    path('review/new/', views.review_creation, name="review_creation"),
    path('review/new/<int:ticket_id>', views.review_creation, name="review_creation"),
    path('ticket_and_review/new/', views.ticket_and_review_creation, name="ticket_and_review_creation"),
    path('review/update/<int:review_id>/', views.review_modification, name="review_modification"),
    path('review/delete/<int:review_id>/', views.review_deletion, name="review_deletion"),
    path('posts/', views.posts, name="posts"),
    path('logout/', views.log_out, name="log_out"),
]
