from django.shortcuts import render
from .models import Category, Post

def index(request):
    """Функция представления для главной страницы"""
    posts = Post.objects.all() # QuerySet
    context = {
            "title": "Главная страница",
            "posts": posts
            }
    return render(request, "cooking/index.html", context)


