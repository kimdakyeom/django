from django.urls import path
from . import views

app_name = 'reviews'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/comments/', views.comments, name='comments'),
    path('<int:pk>/posts/', views.posts, name='posts'),
    path('<int:review_pk>/comments/<int:comment_pk>/delete', views.comments_delete, name='comments_delete'),
    path('<int:pk>/recomments/', views.recomments, name='recomments'),
]