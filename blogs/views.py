from django.shortcuts import render
from django.views import generic
from .models import Blog
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blogs/blog_list_page.html'
    context_object_name = 'blogs'
    paginate_by = 4

    def get_queryset(self):
        return Blog.objects.filter(status='pub')


class BlogDetailView(LoginRequiredMixin, generic.DetailView):
    model = Blog
    template_name = "blogs/blog_detail_page.html"
    context_object_name = "blog"


class BlogCreateView(LoginRequiredMixin, generic.CreateView):
    model = Blog
    fields = ["title", "text", "author", "status"]
    template_name = "blogs/blog_create_page.html"
    context_object_name = "form"


class BlogUpdateView(UserPassesTestMixin, LoginRequiredMixin, generic.UpdateView):
    model = Blog
    fields = ["title", "text", "author", "status"]
    template_name = "blogs/blog_update_page.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BlogDeleteView(UserPassesTestMixin, LoginRequiredMixin, generic.DeleteView):
    model = Blog
    template_name = "blogs/blog_delete_page.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def get_success_url(self):
        return reverse("blog_list")
