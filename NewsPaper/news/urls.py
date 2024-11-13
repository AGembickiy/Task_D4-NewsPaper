from django.urls import path
from .views import PostList, PostDetail, Posts, PostSearch, PostsForm

app_name = 'news'

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('posts/', Posts.as_view()),
    path('search/', PostSearch.as_view()),
    path('add/', PostsForm.as_view()),
]

