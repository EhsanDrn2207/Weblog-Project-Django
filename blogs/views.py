from django.shortcuts import render
from django.views import generic
from .models import Blog


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blogs/blog_list_page.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(status='pub')


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "blogs/blog_detail_page.html"
    context_object_name = "blog"
