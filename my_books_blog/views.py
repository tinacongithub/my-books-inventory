from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from my_books_blog.models import Post, Avatar, Message
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from my_books_blog.forms import UserForm
from django.contrib.auth.admin import User
from django.contrib.messages.views import SuccessMessageMixin

def index(request):
    posts = Post.objects.order_by('-date_published').all()
    return render(request,"my_books_blog/index.html", {"posts": posts})

class ListPost(ListView):
    model = Post

class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("my-books-blog-list")
    fields = '__all__'

class PostDetail(DetailView):
    model = Post

class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("my-books-blog-list")

class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("my-books-blog-list")
    fields = "__all__"

class UserSignUp(CreateView):
    form_class = UserForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy("my-books-blog-list")

class UserLogin(LoginView):
    next_page = reverse_lazy("my-books-blog-list")

class UserLogout(LogoutView):
    next_page = reverse_lazy("my-books-blog-list")

class UpdateAvatar(UpdateView):
    model = Avatar
    fields = ['image']
    success_url = reverse_lazy("my-books-blog-list")

class UpdateUser(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy("my-books-blog-list")

class MessageDetail(LoginRequiredMixin, DetailView):
    model = Message

class ListMessage(LoginRequiredMixin, ListView):
    model = Message 

class CreateMessage(SuccessMessageMixin, CreateView):
    model = Message
    success_url = reverse_lazy("my-books-blog-create-message")
    fields = ['name', 'email', 'text']
    success_message = "Your message has been sent!"

class DeleteMessage(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy("my-books-blog-list-message")