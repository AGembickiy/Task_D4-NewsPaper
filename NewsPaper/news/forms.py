from django.forms import ModelForm
from django import forms
from .models import Post


class PostForm(ModelForm):
   class Meta:
       model = Post
       fields = ['author','post_status', 'heading', 'text_post']
       widgets = {
           'author': forms.TextInput(attrs={
               'class': 'form-control',
           }),
           'post_status': forms.Select(attrs={
               'class': 'form-control',
           },
           choices=Post.ARTICLE_OR_NEWS_SELECTION_FIELD,
           ),
       #     'heading': forms.Select(attrs={
       #         'class': 'form-control',
       #     }),
       #     'text_post': forms.Textarea(attrs={
       #         'class': 'form-control',
       #     }),
       }
