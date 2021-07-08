from django.shortcuts import render
from django.http import HttpResponse

from .models import Blog

def index(request):
    blog = Blog.objects.all()
    return render(request, 'blog/index.html', {'blog': blog, 'title': 'Список постов'})

def view_post(request, post_id):
    blog_item = Blog.objects.get(pk=post_id)
    return render(request, 'blog/view_post.html', {'blog_item': blog_item})