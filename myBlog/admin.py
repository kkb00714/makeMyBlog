from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostManageAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'writer', 'created_at', 'view_count', ]
    search_fields = ['title', 'content', 'writer']
    list_per_page = 20 

@admin.register(Comment)
class CommentManageAdmin(admin.ModelAdmin):
    list_display = ['post', 'writer', 'created_at']
    search_fields = ['writer']
    list_per_page = 30
