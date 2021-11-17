from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview', 'genres', 'poster_path', 'release_date', 'like_users')
