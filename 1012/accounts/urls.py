from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.index, name="index"),
    path('accounts/signup', views.signup, name="signup"),
    path('accounts/login', views.login, name="login"),
    path('accounts/logout', views.logout, name="logout"),
    path('<int:pk>/accounts', views.profile, name="profile"),
    path('create', views.create, name="create"),
    path('<int:pk>/detail', views.detail, name="detail"),
    path('<int:pk>/update', views.update, name="update"),
    path('<int:pk>/delete', views.delete, name="delete"),
]