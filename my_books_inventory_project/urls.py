"""my_books_inventory_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from my_books_inventory.views import (AddNewBook, BookDetail, BookList, DeleteBook, UpdateBook)
from my_books_blog.views import (index, ListPost, CreatePost, PostDetail, DeletePost, UpdatePost,
UserSignUp, UserLogin, UserLogout, UpdateAvatar, UpdateUser, MessageDetail, ListMessage, CreateMessage, DeleteMessage)
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('panel-books/add/', AddNewBook.as_view()),
    path('panel-books/<int:pk>/detail/', BookDetail.as_view()),
    path('panel-books/list/', BookList.as_view()),
    path('panel-books/<int:pk>/delete/', DeleteBook.as_view()),
    path('panel-books/<int:pk>/update/', UpdateBook.as_view()),
    path('my-books-blog/', index, name="my-books-blog-index"),
    path('my-books-blog/list/', ListPost.as_view(), name="my-books-blog-list"),
    path('my-books-blog/create/', staff_member_required(CreatePost.as_view()), name="my-books-blog-create"),
    path('my-books-blog/<int:pk>/detail/', PostDetail.as_view(), name="my-books-blog-detail"),
    path('my-books-blog/<int:pk>/delete/', staff_member_required(DeletePost.as_view()), name="my-books-blog-delete"),
    path('my-books-blog/<int:pk>/update/', staff_member_required(UpdatePost.as_view()), name="my-books-blog-update"),
    path('my-books-blog/signup/', UserSignUp.as_view(), name="my-books-blog-signup"),
    path('my-books-blog/login/', UserLogin.as_view(), name= "my-books-blog-login"),
    path('my-books-blog/logout/', UserLogout.as_view(), name="my-books-blog-logout"),
    path('my-books-blog/avatars/<int:pk>/update/', UpdateAvatar.as_view(), name="my-books-blog-update-avatar"),
    path('my-books-blog/users/<int:pk>/update/', UpdateUser.as_view(), name="my-books-blog-update-user"),
    path('my-books-blog/messages/<int:pk>/detail/', MessageDetail.as_view(), name="my-books-blog-message-detail"),
    path('my-books-blog/messages/list/', ListMessage.as_view(), name="my-books-blog-list-message"),
    path('my-books-blog/messages/create/', CreateMessage.as_view(), name="my-books-blog-create-message"),
    path('my-books-blog/messages/<int:pk>/delete/', DeleteMessage.as_view(), name="my-books-blog-delete-message"),
    path('my-books-blog/about', TemplateView.as_view(template_name='my_books_blog/about.html'), name="my-books-blog-about"),
    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)