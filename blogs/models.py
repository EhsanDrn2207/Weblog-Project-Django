from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Blog(models.Model):
    STATUS_CHOICES = (
        ('drf', "draft"),
        ('pub', "published"),
    )
    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES)
    create_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", args=[self.id])
