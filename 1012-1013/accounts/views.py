from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from accounts.forms import ArticleForm
from .models import Article
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model



def index(request):
    articles = Article.objects.all()
    # if articles.author_id == get_user_model().pk:
    #     author = get_user_model.username
    context = {
        "articles": articles,
        # "author": author,
    }
    return render(request, 'accounts/index.html', context)

@login_required
def create(request):
    if request.method == "POST":
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            post = article_form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("accounts:index")
    else:
        article_form = ArticleForm()
    context = {
        "article_form": article_form,
    }
    return render(request, 'accounts/forms.html', context)

@login_required
def update(request, pk):
    articles = Article.objects.get(pk=pk)
    if request.method == "POST":
        article_form = ArticleForm(request.POST, instance=articles)
        if article_form.is_valid():
            article_form.save()
            print("3")
            return redirect("accounts:index")
    else:
        article_form = ArticleForm(instance=articles)
    context = {
        "article_form": article_form,
        "articles": articles,
    }
    return render(request, 'accounts/forms.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        "article": article,
    }
    return render(request, 'accounts/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('accounts:index')

def signup(request):
    form = CustomUserCreationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("accounts:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, 'accounts/login.html', context)

def profile(request, pk):
    user = get_user_model().objects.get(pk=pk)
    return render(request, 'accounts/profile.html', {'user': user,})

def userupdate(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/userupdate.html', context)

def userdelete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('accounts:index')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
    'form': form,
    }
    return render(request, 'accounts/change_password.html', context)

def userspage(request):
    users = get_user_model().objects.all()
    return render(request, 'accounts/userspage.html', {'users': users,})

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')