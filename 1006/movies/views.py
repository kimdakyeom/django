from django.shortcuts import render, redirect

from movies.forms import MovieForm
from .models import Movie

def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

def create(request):
    if request.method == "POST":
        movies_form = MovieForm(request.POST)
        if movies_form.is_valid():
            movies_form.save()
            return redirect('movies:index')
    else:
        movies_form = MovieForm()
    context = {
        'movies_form': movies_form,
    }
    return render(request, 'movies/forms.html', context)

def detail(request, pk):
    movies = Movie.objects.get(pk=pk)
    if movies.running_time // 60 == 0:
        running_time = str(movies.running_time) + '분'
    else:
        running_time = str(movies.running_time // 60) + '시간 ' + str(movies.running_time % 60) + '분'
    context = {
        'movies': movies,
        'running_time': running_time,
    }
    return render(request, 'movies/detail.html', context)

def delete(request, pk):
    movies = Movie.objects.get(pk=pk)
    movies.delete()
    return redirect('movies:index')

def update(request, pk):
    movies = Movie.objects.get(pk=pk)
    if request.method == "POST":
        movies_form = MovieForm(request.POST, instance=movies)
        if movies_form.is_valid():
            movies_form.save()
            return redirect('movies:index')
    else:
        movies_form = MovieForm(instance=movies)
    context = {
        'movies_form': movies_form,
    }
    return render(request, 'movies/forms.html', context)