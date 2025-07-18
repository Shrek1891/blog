from django.urls import path

from blog.views import index, get_categories

urlpatterns = [
    path('', index, name='home'),
    path('categories/<str:slug>/', get_categories, name='categories'),
]
