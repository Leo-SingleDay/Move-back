from django.db.models.fields import DateTimeField
from rest_framework import serializers
from .models import Post,Comment

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'post')

class PostSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('user',)
        
