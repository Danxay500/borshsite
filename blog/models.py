from typing import Text
from django.db import models
from django.db.models.deletion import PROTECT, SET_NULL
from django.db.models.fields import BigIntegerField
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def get_absolute_url(self):
        return reverse('view_post', kwargs={'pk': self.pk})
        
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']
    
class Views(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    views = models.BigIntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return str(self.views)

    class Meta:
        verbose_name = 'Просмотры'
        verbose_name_plural = 'Просмотры'
        ordering = ['-id']

class Comment(models.Model):
    pass
