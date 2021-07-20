from django.urls import path

from .views import *

urlpatterns = [
    # path('', index, name='home'),
    path('', Home.as_view(), name='home'),
    # path('post/<int:post_id>', view_post, name='view_post'),
    path('post/<int:pk>', ViewPost.as_view(), name='view_post'),
    path('blog/add-post', add_post, name='add_post')
]