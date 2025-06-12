from django.urls import path
from .views import (
    home, about,
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView,PostDeleteView,
    AuthorListView, AuthorDetailView, AuthorCreateView
)



urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('authors/create/', AuthorCreateView.as_view(), name='author_create'),

]
