from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/mypage/', views.mypage, name='mypage'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]