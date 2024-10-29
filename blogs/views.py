from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import Blog
from .forms import CommentForm


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blogs/blog_list_page.html'
    context_object_name = 'blogs'
    paginate_by = 4

    def get_queryset(self):
        return Blog.objects.filter(status='pub')


@login_required
def blog_detail_view(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog_comments = blog.comment.all()
    if request.method == 'POST':
        comment = CommentForm(request.POST)
        if comment.is_valid():
            new_comment = comment.save(commit=False)
            new_comment.user = request.user
            new_comment.blog = blog
            new_comment.save()
            comment = CommentForm()
    else:
        comment = CommentForm()
    return render(request, "blogs/blog_detail_page.html", context={
        "blog": blog,
        "blog_comments": blog_comments,
        "comment_form": comment,
    })


# class BlogDetailView(LoginRequiredMixin, generic.DetailView):
#     model = Blog
#     template_name = "blogs/blog_detail_page.html"
#     context_object_name = "blog"


class BlogCreateView(LoginRequiredMixin, generic.CreateView):
    model = Blog
    fields = ["title", "text", "author", "status"]
    template_name = "blogs/blog_create_page.html"
    context_object_name = "form"


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Blog
    fields = ["title", "text", "author", "status"]
    template_name = "blogs/blog_update_page.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user or self.request.user.username == "admin"


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Blog
    template_name = "blogs/blog_delete_page.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user or self.request.user.username == "admin"

    def get_success_url(self):
        return reverse("blog_list")
