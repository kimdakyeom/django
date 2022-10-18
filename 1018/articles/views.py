from django.shortcuts import redirect, render
from articles.admin import PhotoInline
from .models import Article, Photo, Comment
from .forms import ArticleForm, PhotoForm, CommentForm
import os
from django.forms import modelformset_factory
from django.utils import timezone

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        photo_form = PhotoForm(request.POST, request.FILES)
        images = request.FILES.getlist('image')
        if article_form.is_valid() and photo_form.is_valid():
            print(1)
            article = article_form.save(commit=False)
            if len(images):
                for image in images:
                    image_instance = Photo(article=article, image=image)
                    article.save()
                    image_instance.save()
            else:
                article.save()
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
        photo_form = PhotoForm()
    context = {
        'article_form': article_form,
        'photo_form': photo_form,
    }
    return render(request, 'articles/forms.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        "comment_form": comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    photos = Photo.objects.filter(article_id=article.pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES, instance=article)
        photo_form = PhotoForm(request.POST, request.FILES)
        images = request.FILES.getlist('image')
        for photo in photos:
            if photo.image:
                os.remove(photo.image.path)
            photo.delete()
        if article.thumbnail:
            os.remove(article.thumbnail.path)
        if article_form.is_valid() and photo_form.is_valid():
            article = article_form.save(commit=False)
            if len(images):
                for image in images:
                    image_instance = Photo(article=article, image=image)
                    article.save()
                    image_instance.save()
            else:
                article.save()
            return redirect('articles:index')
    else:
        article_form = ArticleForm(instance=article)
        if photos:
            photo_form = PhotoForm(instance=photos[0])
        else:
            photo_form = PhotoForm()
    context = {
        'article_form': article_form,
        'photo_form': photo_form,
    }
    return render(request, 'articles/forms.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    photos = Photo.objects.filter(article_id=article.pk)
    for photo in photos:
        if photo.image:
            os.remove(photo.image.path)
    if article.thumbnail:
        os.remove(article.thumbnail.path)
    article.delete()
    return redirect('articles:index')

def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)

def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)