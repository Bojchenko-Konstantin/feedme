from django import forms
from django.forms import widgets
from .models import Post
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class PostAddForm(forms.ModelForm):
    """Форма для добавления новой статьи"""
    class Meta:
        model = Post
        fields = ("title", "content",
                  "photo", "category")
        widgets = {"title": forms.TextInput(attrs={"class": "form-control"}),
                   "content": forms.Textarea(attrs={"class": "form-control"}),
                   "photo": forms.FileInput(attrs={"class": "form-control"}),
                   "category": forms.Select(attrs={"class": "form-control"}),
                   }

class LoginForm(AuthenticationForm):
    """Форма для аутентификации пользователя"""
    username = forms.CharField(label="Имя пользователя",
                               max_length=150,
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Пароль",
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))
