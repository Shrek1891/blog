from django.urls import path
from blog.views import index, get_categories
from .views import Home, get_post, PostsByCategory

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('categories/<str:slug>/', PostsByCategory.as_view(), name='categories'),
    path('post/<str:slug>/', get_post, name='post'),
]
