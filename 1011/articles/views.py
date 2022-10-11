from django.shortcuts import render
from django.contrib.auth import get_user_model

def index(request):
    return render(request, 'articles/index.html')

def member(request):
    users = get_user_model().objects.all()
    context = {
        "users": users,
    }
    return render(request, 'articles/member.html', context)

def profile(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        "user": user,
    }
    return render(request, 'articles/profile.html', context)