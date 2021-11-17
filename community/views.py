from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.views.decorators.http import require_safe
from rest_framework.decorators import api_view
from .models import Comment, Post
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def post_list_create(request):
    if request.method =="GET":
        posts = get_list_or_404(Post)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status= status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def post_detail_delete_update(request, post_pk):
    post = get_object_or_404(Post, pk = post_pk)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        post.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def comment_create(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        return Response(serializer.data, status= status.HTTP_201_CREATED)


@api_view(['PUT','DELETE'])
def comment_update_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk = comment_pk)
    if request.method == "PUT":
        serialzer = CommentSerializer(comment, data=request.data)
        if serialzer.is_valid(raise_exception=True):
            return Response(serialzer.data, status = status.HTTP_200_OK)
    elif request.method == "DELETE":
        comment.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)