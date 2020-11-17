from django.forms import forms,ModelForm
from .models import Post

class BlogCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'body']

    def valid_form(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)


class BlogUpdateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

    def valid_form(self,form):
        return super().form_valid(form)