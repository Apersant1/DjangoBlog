from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):  # новое
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    fields = ['title', 'author', 'body']
    template_name = 'create post.html'


#

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'post_edit.html'


class BlogDeleteView(DeleteView):  # Создание нового класса
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
