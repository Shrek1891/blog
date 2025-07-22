from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Category


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog'
        return context

class PostsByCategory(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 3
    allows_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context

def index(request, slug=None):
    return render(request, 'blog/index.html')

def get_categories(request, slug):
    return  render(request, 'blog/categories.html')

def get_post(request, slug):
    return render(request, 'blog/categories.html')