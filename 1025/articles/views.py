from django.shortcuts import redirect, render
from articles.admin import PhotoInline
from .models import Article, Photo, Comment
from .forms import ArticleForm, PhotoForm, CommentForm
import os
from django.contrib import messages
from django.forms import modelformset_factory
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        photo_form = PhotoForm(request.POST, request.FILES)
        images = request.FILES.getlist('image')
        if article_form.is_valid() and photo_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
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
    if request.user.is_authenticated:
        comment_form = CommentForm()
    else:
        comment_form = CommentForm()
        comment_form.fields['content'].widget.attrs['readonly'] = True
        comment_form.fields['content'].widget.attrs['value'] = "로그인을 해주세요"
        comment_form.fields['content'].required = False

    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    photos = Photo.objects.filter(article_id=article.pk)
    if request.user == article.user:
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
    else:
        messages.warning(request, '작성자만 수정할 수 있습니다.')
        return redirect('articles:detail', article.pk)

@login_required
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

@login_required
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect('articles:detail', article.pk)

@login_required
def comments_update(request, article_pk, comment_pk):
    article = Article.objects.get(pk=article_pk)
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            return redirect('articles:detail', article_pk)
    else:
        c_form = CommentForm()
        comment_form = CommentForm(instance=comment)
    context = {
        'article': article,
        'comment_form': comment_form,
        'c_form': c_form,
        'article_pk': article_pk,
        'comment_pk': comment_pk,
    }
    return render(request, 'articles/comment_update.html', context)

@login_required
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)

@login_required
def likes(request, pk):
    article = Article.objects.get(pk=pk)
    if article.like_users.filter(pk=request.user.pk).exists():
    # if request.user in article.like_users.all():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:detail', pk)