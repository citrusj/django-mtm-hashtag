from django import forms
from .models import Content, Comment, Tag

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title','body',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields=['name']