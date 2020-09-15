from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.
class Content(models.Model):
    title=models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.TextField(default='')
    tags = models.ManyToManyField('Tag',blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Content', on_delete=models.CASCADE)
    text = models.TextField(default='')
    created_date = models.DateTimeField(default=timezone.now)

class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
