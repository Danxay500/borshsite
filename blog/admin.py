from django.contrib import admin

from .models import *


class BlogAdmin(admin.ModelAdmin):
    model = Blog
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published',)

class ViewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'views')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Views, ViewsAdmin)
