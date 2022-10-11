from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path('', views.index, name="index"),
    path('member/', views.member, name="member"),
    path('<int:pk>/profile/', views.profile, name="profile"),
]
