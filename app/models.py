from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

class Catagory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Episode(models.Model):
    uid = models.UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    link = models.FilePathField(path='media\\series', match=None, recursive=True, null=True, blank=True)
    title = models.CharField(max_length=500, blank=True)
    thumbnail = models.FilePathField(path='media\\thumbnails', match=None, recursive=True, null=True, blank=True)
    size = models.IntegerField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, editable=True)

    class Meta:
        ordering = ['timestamp']
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        title = self.link
        if title:
            self.title = title.split('\\')[-1]
        return super().save(*args, **kwargs)

class Movie(models.Model):
    uid = models.UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    link = models.FilePathField(path='media\\movies', match=None, recursive=True, null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    thumbnail = models.FilePathField(path='media\\thumbnails', match=None, recursive=True, null=True, blank=True)

    size = models.IntegerField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, editable=True)
    tags = models.ManyToManyField(Catagory, blank=True)

    is_series = models.BooleanField(default=False, blank=True)
    episodes = models.ManyToManyField(Episode, blank=True)
    is_published = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        title = self.link
        if title:
            self.title = title.split('\\')[-1]
        return super().save(*args, **kwargs)
