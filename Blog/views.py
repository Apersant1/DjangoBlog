from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from django.urls import reverse_lazy
from .models import Post

from .forms import (
    BlogCreateForm,
    BlogUpdateForm,
)


class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):  # новое
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    queryset = Post.objects.all()
    form_class = BlogCreateForm
    template_name = 'create post.html'
    success_url = reverse_lazy('home')


#

class BlogUpdateView(UpdateView):
    queryset = Post.objects.all()
    form_class = BlogUpdateForm
    template_name = 'post_edit.html'


class BlogDeleteView(DeleteView):  # Создание нового класса
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
