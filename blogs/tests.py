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

    def test_blog_list_component(self):
        response = self.client.get(reverse("blog_list"))
        self.assertContains(response, self.blog1.title)
        self.assertContains(response, self.blog1.text)
        self.assertNotContains(response, self.blog2.title)
        self.assertNotContains(response, self.blog2.text)

    def test_blog_detail_url(self):
        response = self.client.get(f"/blogs/{self.blog1.id}/")
        self.assertEqual(response.status_code, 200)

    def test_blog_detail_name(self):
        response = self.client.get(reverse("blog_detail", args=[self.blog1.id]))
        self.assertEqual(response.status_code, 200)

    def test_blog_detail_template_used(self):
        response = self.client.get(reverse("blog_detail", args=[self.blog1.id]))
        self.assertTemplateUsed(response, "blogs/blog_detail_page.html")

    def test_blog_detail_component(self):
        response = self.client.get(reverse("blog_detail", args=[self.blog1.id]))
        self.assertContains(response, self.blog1.title)
        self.assertContains(response, self.blog1.text)
        self.assertContains(response, self.blog1.author)

        response2 = self.client.get(reverse("blog_detail", args=[self.blog2.id]))
        self.assertContains(response2, self.blog2.title)
        self.assertContains(response2, self.blog2.text)
        self.assertContains(response2, self.blog2.author)

    def test_blog_create_url(self):
        response = self.client.get("/blogs/create/")
        self.assertEqual(response.status_code, 200)

    def test_blog_create_name(self):
        response = self.client.get(reverse("blog_create"))
        self.assertEqual(response.status_code, 200)

    def test_blog_create_template_used(self):
        response = self.client.get(reverse("blog_create"))
        self.assertTemplateUsed(response, "blogs/blog_create_page.html")

    def test_blog_create_form(self):
        response = self.client.post(path=reverse("blog_create"), data={
            "title": "title3",
            "text": "text3",
            "author": self.user1.id,
            "status": "pub",
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Blog.objects.last().title, "title3")
        self.assertEqual(Blog.objects.last().text, "text3")
        self.assertEqual(Blog.objects.last().author, self.user1)
        self.assertEqual(Blog.objects.last().status, "pub")

    def test_blog_update_url(self):
        response = self.client.get(f"/blogs/{self.blog1.id}/edit/")
        self.assertEqual(response.status_code, 200)

    def test_blog_update_name(self):
        response = self.client.get(reverse("blog_update", args=[self.blog1.id]))
        self.assertEqual(response.status_code, 200)

    def test_blog_update_template_used(self):
        response = self.client.get(reverse("blog_update", args=[self.blog1.id]))
        self.assertTemplateUsed(response, "blogs/blog_update_page.html")

    def test_blog_update_form(self):
        response = self.client.post(path=reverse("blog_update", args=[self.blog1.id]), data={
            "title": "title4",
            "text": "text4",
            "author": self.user2.id,
            "status": "drf",
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Blog.objects.first().title, "title4")
        self.assertEqual(Blog.objects.first().text, "text4")
        self.assertEqual(Blog.objects.first().author, self.user2)
        self.assertEqual(Blog.objects.first().status, "drf")
