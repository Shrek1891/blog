from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog'
        return context

def index(request, slug=None):
    return render(request, 'blog/index.html')

def get_categories(request, slug):
    return  render(request, 'blog/categories.html')

def get_post(request, slug):
    return render(request, 'blog/categories.html')