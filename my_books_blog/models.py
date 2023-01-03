from django.db import models
from django.contrib.auth.admin import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    text = models.TextField(max_length=3000)
    date_published = models.DateField()
    image = models.ImageField(upload_to='posts', null=True, blank=True)

class Avatar(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='avatar')
    image = models.ImageField(upload_to='avatars', null=True, blank=True)

class Message(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=3000)
    sent_on = models.DateField(auto_now_add=True)