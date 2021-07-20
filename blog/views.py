from django.db.models.fields import BigIntegerField
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView

from .models import *
from .forms import PostForm


class Home(ListView):
    model = Blog
    template_name = 'blog/home_blog_list.html'
    context_object_name = 'blog'
    # extra_context = {'title': 'Главная'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class ViewPost(DetailView):
    model = Blog
    template_name = 'blog/post_detail.html'
    context_object_name = 'blog_item'

    def get_context_data(self, **kwargs):

        try:
            views = Views.objects.get(id=self.kwargs['pk'])
            views.views += 1
        except:
            views = Views.objects.create(id=self.kwargs['pk'])
            views.views += 1

        views.save()

        views_watch = str(views.views)

        if len(str(views.views)) > 3 and len(str(views.views)) < 7:
            views_watch = views_watch[:-3]+"K"

        elif len(str(views.views)) > 6 and len(str(views.views)) < 10:
            views_watch = views_watch[:-6]+"M"

        elif len(str(views.views)) > 9:
            views_watch = views_watch[:-9]+"B"

        context = super().get_context_data(**kwargs)
        context['views'] = views_watch
        return context


# def index(request):
#     blog = Blog.objects.filter(is_published=True)
#     return render(request, 'blog/index.html', {'blog': blog, 'title': 'Список постов'})

# def view_post(request, post_id):
#     blog_item = get_object_or_404(Blog, pk=post_id)

#     try:
#         views = Views.objects.get(id=self.kwargs['pk'])
#         views.views += 1
#     except:
#         views = Views.objects.create(id=self.kwargs['pk'])
#         views.views += 1

#     if (blog_item.post_views == None):
#         blog_item.post_views_id = views.pk
        
#     views.save()
#     blog_item.save()

#     views_watch = str(views.views)

#     if len(str(views.views)) > 3 and len(str(views.views)) < 7:
#         views_watch = views_watch[:-3]+"K"

#     elif len(str(views.views)) > 6 and len(str(views.views)) < 10:
#         views_watch = views_watch[:-6]+"M"

#     elif len(str(views.views)) > 9:
#         views_watch = views_watch[:-9]+"B"

#     return render(request, 'blog/view_post.html', {'blog_item': blog_item, "views": views_watch})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = PostForm()

    return render(request, 'blog/add_post.html', {'form': form})