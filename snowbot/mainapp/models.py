from django.db import models

# Create your models here.

class Jokes(models.Model):
    jokes = models.CharField(max_length=264)

    def __str__(self):
        return self.jokes

class Sing(models.Model):
    songs = models.CharField(max_length=264)

    def __str__(self):
        return self.songs

class Wisdom(models.Model):
    wisdom = models.CharField(max_length=264)

    def __str__(self):
        return self.wisdom
