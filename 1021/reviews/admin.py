from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'review', 
        'content',
        'user',
        'updated_at',
        'deleted',
    )
    search_fields = ('review__title', 'content', 'user__user_id',)

admin.site.register(Comment, CommentAdmin)