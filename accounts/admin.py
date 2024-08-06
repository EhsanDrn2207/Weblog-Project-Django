from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import *


class CustomUserAdmin(UserAdmin):
    model = CustomUserModel
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("age", "gender")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("age", "gender")}),
    )
    list_display = ("username", "email", "age", "gender")


admin.site.register(CustomUserModel, CustomUserAdmin)
