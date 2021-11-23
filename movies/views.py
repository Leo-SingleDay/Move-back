from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Movie, Review, EventMovie
from .serializers import MovieSerializer, ReviewSerializer, EventMovieSerializer

@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def event(request):
    if request.method == 'GET':
        movies = get_list_or_404(EventMovie)
        serializer = EventMovieSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def recommend_list(request):
    if request.method == 'GET':
        user = request.user
        like_movies = user.like_movies.all()
        context = {}
        for movie in like_movies:
            for genre in movie.genres.all():
                if genre.id not in context:
                    context[genre.id] = 1
                else:
                    context[genre.id] += 1
        context_sorted = sorted(context.items(), reverse=True, key=lambda item: item[1]) #[[28,4],[878,2],[12,1],[10752,1]]
        if len(context_sorted) > 4:
            movie1 = Movie.objects.all().filter(genres__in=[context_sorted[0][0]]).order_by('?')[:4]
            movie2 = Movie.objects.all().filter(genres__in=[context_sorted[1][0]]).order_by('?')[:3]
            movie3 = Movie.objects.all().filter(genres__in=[context_sorted[2][0]]).order_by('?')[:2]
            movie4 = Movie.objects.all().filter(genres__in=[context_sorted[3][0]]).order_by('?')[:1]
            movies = movie1 | movie2 | movie3 | movie4
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data)    
        elif len(context_sorted) > 2:
            movie1 = Movie.objects.all().filter(genres__in=[context_sorted[0][0]]).order_by('?')[:6]
            movie2 = Movie.objects.all().filter(genres__in=[context_sorted[1][0]]).order_by('?')[:4]
            movies = movie1 | movie2
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data)    
        elif len(context_sorted) == 1:
            movie1 = Movie.objects.all().filter(genres__in=[context_sorted[0][0]]).order_by('?')[:10]
            serializer = MovieSerializer(movie1, many=True)
            return Response(serializer.data)    
        else:
            movie1 = Movie.objects.all().order_by('?')[:10]
            serializer = MovieSerializer(movie1, many=True)
            return Response(serializer.data)    
        

@api_view(['GET'])
def popularity_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all().order_by('-popularity')[:10]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def latest_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all().order_by('-release_date')[:10]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET','PUT', 'DELETE'])
def review_detail_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        data = {
            'delete': f'댓글 {review_pk}번 {review.content}이 삭제되었습니다'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def review_get_create(request, movie_pk):
    if request.method == 'GET':
        reviews = Review.objects.all().filter(movie_id=movie_pk)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','POST'])
def like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        if movie.like_users.filter(pk=request.user.pk).exists():
            like = True
        else:
            like = False
    if request.method == 'POST':
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
            like = False
        else:
            movie.like_users.add(request.user)
            like = True
    context = {
        'like': like,
        'count': movie.like_users.count()
    }
    return Response(context)