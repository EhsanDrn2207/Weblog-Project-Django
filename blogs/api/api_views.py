from rest_framework import generics
from blogs.models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer


class BlogListAPIView(generics.ListAPIView):
    """
    API view to list published blogs.
    """
    queryset = Blog.objects.filter(status='pub').order_by("-modified_datetime")
    serializer_class = BlogSerializer


class BlogDetailAPIView(generics.RetrieveAPIView):
    """
    API view to retrieve a blog by its primary key.
    """
    queryset = Blog.objects.filter(status='pub')
    serializer_class = BlogSerializer


class CommentListAPIView(generics.ListCreateAPIView):
    """
    API view to list all comments or create a new comment.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        """
        Save the comment with the logged-in user.
        """
        serializer.save(user=self.request.user)


class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a comment.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer