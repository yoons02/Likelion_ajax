from django.urls import path
from . import views

app_name="items"
urlpatterns = [
    path('', views.main, name="main"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('show/<int:post_id>/', views.show, name="show"),
    path('delete/<int:post_id>/', views.delete, name="delete"),
    # 1. like_toggle url 연결하기
    path('like_toggle/<int:post_id>/', views.like_toggle, name="like_toggle"),
    # 1-1. my_like url 연결하기
    path('my_like/<int:user_id>', views.my_like, name='my_like'),
    # 2. dislike_toggle url 연결하기
    path('dislike_toggle/<int:post_id>/', views.dislike_toggle, name="dislike_toggle"),
    # 2-1. my_dislike url 연결하기
    path('my_dislike/<int:user_id>', views.my_dislike, name='my_dislike'),
]
