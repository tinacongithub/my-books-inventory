from django.shortcuts import render
from my_books_inventory.models import Books
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView

class AddNewBook(CreateView):
  model = Books
  success_url = "/panel-books"
  fields = ["title", "author", "year_published"]

class BookDetail(DetailView):
  model = Books

class BookList(ListView):
  model = Books

class DeleteBook(DeleteView):
  model = Books
  success_url = "/panel-books"

class UpdateBook(UpdateView):
  model = Books
  success_url = "/panel-books"
  fields = ["title", "author", "year_published"]