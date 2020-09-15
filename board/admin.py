from django.contrib import admin

# Register your models here.
from .models import Content, Comment, Tag

admin.site.register(Content)
admin.site.register(Comment)
admin.site.register(Tag)