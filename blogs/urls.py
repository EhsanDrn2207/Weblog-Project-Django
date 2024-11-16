from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import views
from blogs.api.api_views import (
    BlogListAPIView,
    BlogDetailAPIView,
    CommentListAPIView,
    CommentDetailAPIView,
)


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
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
    
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
