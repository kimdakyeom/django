from django.shortcuts import redirect, render
from .forms import ArticleForm, CommentForm
from .models import Article, Comment
from django.contrib.auth import get_user_model

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/forms.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user.is_authenticated:
        comment_form = CommentForm()
    else:
        comment_form = CommentForm()
        comment_form.fields['content'].widget.attrs['readonly'] = True
        comment_form.fields['content'].widget.attrs['value'] = "로그인을 해주세요"
        comment_form.fields['content'].required = False
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
    }
    return render(request, 'articles/forms.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    print("됨")
    if comment_form.is_valid():
        print("안됨")
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect('articles:detail', article.pk)

def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)

def userpage(request, pk):
    user = get_user_model().objects.get(pk=pk)
    article = Article.objects.all()
    context = {
        'user': user,
        'article': article,
    }
    return render(request, 'articles/userpage.html', context)