from django.urls import path
from . import views
from api.api_views import (
    BlogListAPIView,
    BlogDetailAPIView,
    CommentListAPIView,
    CommentDetailAPIView,
)

urlpatterns = [
    path("", views.BlogListView.as_view(), name="blog_list"),
    path("blogs/<int:pk>/", views.blog_detail_view, name="blog_detail"),
    path("blogs/create/", views.BlogCreateView.as_view(), name="blog_create"),
    path("blogs/<int:pk>/edit/", views.BlogUpdateView.as_view(), name="blog_update"),
    path("blogs/<int:pk>/delete/", views.BlogDeleteView.as_view(), name="blog_delete"),
    
    # API views
    path('api/blogs/', BlogListAPIView.as_view(), name='api_blog_list'),
    path('api/blogs/<int:pk>/', BlogDetailAPIView.as_view(), name='api_blog_detail'),
    path('api/comments/', CommentListAPIView.as_view(), name='api_comment_list'),
    path('api/comments/<int:pk>/', CommentDetailAPIView.as_view(), name='api_comment_detail'),
]
