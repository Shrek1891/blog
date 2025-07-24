from django.urls import path
from .views import Home, get_post, PostsByCategory, GetPost, PostByTag, Search

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('categories/<str:slug>/', PostsByCategory.as_view(), name='categories'),
    path('post/<str:slug>', GetPost.as_view(), name='post'),
    path('tag/<str:slug>/', PostByTag.as_view(), name='tag'),
    path('search/', Search.as_view(), name='search'),
]
