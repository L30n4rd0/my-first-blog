'''
Created on Oct 23, 2018

@author: leonardo
'''
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
        