from django.urls import path
from . import views

app_name = "community"

urlpatterns = [
    path('', views.post_list_create, name='post_list_create'),
    path('<int:post_pk>/', views.post_detail_delete_update, name='post_detail_delete_update'),
    path('<int:post_pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:post_pk>/comments/<int:comment_pk>/', views.comment_update_delete, name='comment_update_delete'),
]
