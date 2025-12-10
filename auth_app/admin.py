from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("username", "email", "institucion", "role", "is_staff", "is_active")
    list_filter = ("institucion", "role", "is_staff", "is_active")

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Información personal", {"fields": ("email", "first_name", "last_name")}),
        ("Institución", {"fields": ("institucion",)}),
        ("Rol", {"fields": ("role",)}),
        ("Permisos", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "institucion", "role", "password1", "password2", "is_staff", "is_active"),
        }),
    )

admin.site.register(User, CustomUserAdmin)