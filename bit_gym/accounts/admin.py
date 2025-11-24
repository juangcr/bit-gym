from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """Users lists. Add groups separately (Admin, Staff, Customers)."""

    model = CustomUser
    list_display = (
        "customer_id",
        "username",
        "email",
        "is_basic",
        "is_premium",
        "is_staff",
        "is_superuser",
    )
    list_filter = (
        "is_basic",
        "is_premium",
        "is_staff",
        "is_superuser",
    )
    search_fields = (
        "username",
        "email",
    )
    ordering = ("username",)


admin.site.register(CustomUser, CustomUserAdmin)
