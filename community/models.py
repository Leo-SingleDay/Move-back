from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.DateTimeField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #유저 잠시 변경 ForeignKey -> DateTimeField
    review = models.ForeignKey(Post, on_delete=models.CASCADE)

    