from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request, slug=None):
    return render(request, 'blog/index.html')

def get_categories(request, slug):
    return  render(request, 'blog/categories.html')