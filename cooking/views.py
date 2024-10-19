from django.shortcuts import render
from .models import Category, Post

def index(request):
    """Функция представления для главной страницы"""
    posts = Post.objects.all() # QuerySet
    categories = Category.objects.all()
    context = {
            "title": "Главная страница",
            "posts": posts,
            "categories": categories
            }
    return render(request, "cooking/index.html", context)

def category_list(request, pk):
    """Реакция на нажатие кнопки категории"""
    posts = Post.objects.filter(category_id=pk)
    categories = Category.objects.all()
    context = {
            "title": posts[0].category,
            "posts": posts,
            "categories": categories
            }
    return render(request, "cooking/index.html", context)

def post_detail(request, pk):
    """Детали поста - подробнее"""
    article = Post.objects.get(pk=pk)
    context = {
            "title": article.title,
            "post": article
            }
    return render(request, "cooking/article_detail.html", context)

