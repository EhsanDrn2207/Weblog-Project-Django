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


class SignUpPageTest(TestCase):
    def setUp(self):
        self.username = "username"
        self.email = "newemail"

    def test_signup_page_url(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_page_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_template_used(self):
        response = self.client.get(reverse("signup"))
        self.assertTemplateUsed(response, "registration/signup_page.html")

    def test_signup_page_form(self):
        user = get_user_model().objects.create_user(username=self.username, email=self.email)
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "username")
        self.assertEqual(get_user_model().objects.all()[0].email, "newemail")
