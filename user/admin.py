from django.contrib import admin
from .models import CustomUser

# Register your models here.

# admin.site.register(CustomUser)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):

    list_display = ("email", "first_name", "last_name", "is_active", "is_staff")

    list_filter = ("email", "first_name", "last_name", "is_active")

    ordering = ("email", "last_name")

    search_fields = ("email", "first_name", "last_name")

    list_editable = ("first_name", "last_name")

    list_display_links = ("email",)

    list_per_page = 20
