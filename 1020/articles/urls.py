from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/comment/', views.comment_create, name='comment_create'),
    path('<int:article_pk>/comment/<int:comment_pk>/delete', views.comment_delete, name='comment_delete'),
    path('<int:pk>/userpage/', views.userpage, name='userpage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)