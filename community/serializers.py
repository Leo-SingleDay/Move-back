from rest_framework import serializers
from .models import Post,Comment


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('content', 'created_at', 'updated_at', 'review')

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('title', 'content', 'created_at', 'updated_at',)
