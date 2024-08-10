from django.shortcuts import render
from django.views import generic
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


class SignUpView(generic.CreateView):
    model = get_user_model()
    form_class = CustomUserCreationForm
    template_name = "registration/signup_page.html"
    success_url = reverse_lazy("login")
