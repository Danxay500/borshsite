from django import forms
from django.db.models import fields
from django.forms import models, widgets
from .models import Blog
import re
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = '__all__'
        fields = ['title', 'content', 'photo', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title-form', 'placeholder': 'Название'}),
            'content': forms.Textarea(attrs={'class': 'content-form', 'placeholder': 'Текст'}),
            'photo': forms.FileInput(attrs={'class': 'photo-form'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'is-published-form'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title
