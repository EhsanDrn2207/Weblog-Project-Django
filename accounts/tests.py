from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class HomePageTest(TestCase):
    def test_home_page_url(self):
        response = self.client.get("/home/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template_used(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home_page.html")

    def test_home_page_components(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Home Page")


