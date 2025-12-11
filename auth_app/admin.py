from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.contrib.auth.hashers import make_password
from .models import User

class CustomUserForm(forms.ModelForm):
    # Solo un campo de contraseña
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password", "role", "institucion")

    def save(self, commit=True):
        # Guardamos el objeto, pero con la contraseña hasheada
        user = super().save(commit=False)
        if self.cleaned_data["password"]:
            user.password = make_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserForm
    form = CustomUserForm
    model = User

    list_display = ("username", "email", "role", "institucion", "is_staff")
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Información adicional", {"fields": ("role", "institucion")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password", "role", "institucion"),
        }),
    )

admin.site.register(User, CustomUserAdmin)