from django.contrib import admin
from .models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'create_datetime', 'status')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'recommend', 'is_active')


admin.site.register(Blog, BlogAdmin)

