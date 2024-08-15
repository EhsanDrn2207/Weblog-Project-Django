from django.shortcuts import render
from django.views import generic
from .models import Blog
from django.urls import reverse


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


class BlogCreateView(generic.CreateView):
    model = Blog
    fields = ["title", "text", "author", "status"]
    template_name = "blogs/blog_create_page.html"
    context_object_name = "form"


class BlogUpdateView(generic.UpdateView):
    model = Blog
    fields = ["title", "text", "author", "status"]
    template_name = "blogs/blog_update_page.html"


class BlogDeleteView(generic.DeleteView):
    model = Blog
    template_name = "blogs/blog_delete_page.html"

    def get_success_url(self):
        return reverse("blog_list")
