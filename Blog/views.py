from django.views.generic import ListView,DetailView,CreateView
from .models import Post
class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView): # новое
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    fields = ['title','author','body']
    template_name = 'create post.html'
# TODO: need create deletePost view!