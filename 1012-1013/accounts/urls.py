from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.index, name="index"),
    path('accounts/signup/', views.signup, name="signup"),
    path('accounts/login/', views.login, name="login"),
    path('accounts/logout/', views.logout, name="logout"),
    path('<int:pk>/accounts', views.profile, name="profile"),
    path('userupdate/', views.userupdate, name='userupdate'),
    path('password/', views.change_password, name='change_password'),
    path('userdelete', views.userdelete, name="userdelete"),
    path('userspage', views.userspage, name="userspage"),
    path('create', views.create, name="create"),
    path('<int:pk>/detail', views.detail, name="detail"),
    path('<int:pk>/update', views.update, name="update"),
    path('<int:pk>/delete', views.delete, name="delete"),
]

# http://localhost:8000/accounts/signup/
# http://localhost:8000/accounts/signup