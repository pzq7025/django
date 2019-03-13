from django.contrib import admin

# Register your models here.

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    """
    take field to the web and display
    the secret of my name: because the secret has some requires so i use my name
    """
    list_display = ('title', 'content', 'pub_time')
    list_filter = ('pub_time',)


admin.site.register(Article, ArticleAdmin)
