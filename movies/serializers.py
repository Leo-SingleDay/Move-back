from rest_framework import serializers
from .models import Movie, Review, Genre


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
        )
    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview', 'genres', 'poster_path', 'release_date', 'popularity', 'like_users')

class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'user')