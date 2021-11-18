from django.db.models.fields import DateTimeField
from rest_framework import serializers
from .models import Post,Comment

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('id','content', 'created_at', 'updated_at', 'review', 'user')

class PostSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('user',)
        
