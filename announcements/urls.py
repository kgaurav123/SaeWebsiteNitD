from django.urls import path,include
from django.views.generic import ListView,DetailView
from announcements.models import Post
from .views import PostDetailView
from . import views

urlpatterns = [
    path('',views.announcements_list,name='announcements'),
    path('<int:pk>/',PostDetailView.as_view())
    ]
