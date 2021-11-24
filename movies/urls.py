from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    # 영화전체리스트
    path('', views.all_list, name="all"),
    # 이벤트 영화리스트
    path('event/', views.event, name="event"),
    # 추천리스트
    path('recommend/', views.recommend_list, name="recommend"),
    # 최신리스트
    path('latest/', views.latest_list, name="latest"),
    # 인기리스트
    path('popularity/', views.popularity_list, name="popularity"),
    # 해당 영화 상세정보
    path('<int:movie_pk>/', views.detail, name='detail'),
    # 영화 좋아요
    path('<int:movie_pk>/like/', views.like, name='like'),
    # 영화 리뷰
    path('reviews/<int:review_pk>/', views.review_detail_update_delete, name='review'),
    path('<int:movie_pk>/reviews/', views.review_get_create),
    # 유저 영화 정보
    path('like-genres/', views.like_genres),
    path('like-movies/', views.like_movies),
]
