from django.test import TestCase
from .models import Blog
from django.urls import reverse
from django.contrib.auth import get_user_model


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = get_user_model().objects.create_user(username="username1",)
        cls.user2 = get_user_model().objects.create_user(username="username2")
        cls.blog1 = Blog.objects.create(
            title="title1",
            text="text1",
            author=cls.user1,
            status='pub',
        )
        cls.blog2 = Blog.objects.create(
            title="title2",
            text="text2",
            author=cls.user2,
            status='drf'
        )

    def test_blog_model_creation(self):
        self.assertEqual(self.blog1.title, 'title1')
        self.assertEqual(self.blog1.text, 'text1')
        self.assertEqual(self.blog1.author, self.user1)
        self.assertEqual(self.blog1.status, 'pub')

        self.assertEqual(self.blog2.title, 'title2')
        self.assertEqual(self.blog2.text, 'text2')
        self.assertEqual(self.blog2.author, self.user2)
        self.assertEqual(self.blog2.status, 'drf')

    def test_blog_list_url(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)

    def test_blog_list_name(self):
        response = self.client.get(reverse("blog_list"))
        self.assertEqual(response.status_code, 200)

    def test_blog_list_template_used(self):
        response = self.client.get(reverse("blog_list"))
        self.assertTemplateUsed(response, "blogs/blog_list_page.html")

    def test_blog_list_component_view(self):
        response = self.client.get(reverse("blog_list"))
        self.assertContains(response, self.blog1.title)
        self.assertContains(response, self.blog1.text)
        self.assertNotContains(response, self.blog2.title)
        self.assertNotContains(response, self.blog2.text)

