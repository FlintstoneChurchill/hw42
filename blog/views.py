from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post, User


class PostListView(ListView):
    model = Post
    template_name = 'index.html'


class PostDetailsView(DetailView):
    model = Post
    template_name = 'post.html'


class UserListView(ListView):
    model = User
    template_name = 'users.html'


class UserDetailsView(DetailView):
    model = User
    template_name = 'user_details.html'


class CommentsListView(ListView):
    pass

