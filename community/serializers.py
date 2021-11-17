from django.db.models.fields import DateTimeField
from rest_framework import serializers
from .models import Post,Comment

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('content', 'created_at', 'updated_at', 'review', 'user')

class PostSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    
    class Meta:
        model = Post
        fields = ('title', 'content', 'created_at', 'updated_at', 'user', 'username')
