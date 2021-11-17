from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('reviews/', views.review_list),
    path('reviews/<int:review_pk>/', views.review_detail_update_delete, name='review'),
    path('<int:movie_pk>/reviews/', views.review_create)
]
