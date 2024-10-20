from django.shortcuts import render, redirect
from .models import Category, Post
from django.db.models import F
from .forms import PostAddForm

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
    Post.objects.filter(pk=pk).update(watched=F('watched') + 1)
    ext_post = Post.objects.all().order_by('-watched')[:5]
    context = {
            "title": article.title,
            "post": article,
            "ext_posts":ext_post
            }
    return render(request, "cooking/article_detail.html", context)

def add_post(request):
    """Добавление поста пользователем на сайте, в обход админки"""
    if request.method == "POST":
        form = PostAddForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post.objects.create(**form.cleaned_data)
            post.save()
            return redirect('post_detail', post.pk)
    else:
        form = PostAddForm()

    context = {
            "form": form,
            "title": "Добавить статью"
            }
    return render(request, "cooking/article_add_form.html", context)

        
    
