from django.contrib import admin
from .models import Article, Photo

class PhotoInline(admin.TabularInline):
    model = Photo

class ArticleAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]

admin.site.register(Article, ArticleAdmin)
