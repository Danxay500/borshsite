from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('post/<int:post_id>', view_post, name='view_post')
]