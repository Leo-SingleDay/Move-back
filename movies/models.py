from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre, related_name="movie")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

class EventMovie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    video_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre, related_name="eventmovie")

class Review(models.Model):
    content = models.CharField(max_length=100)
    rank = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
