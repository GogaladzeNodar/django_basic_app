from django.contrib import admin
from .models import Product, Category
from mptt.admin import MPTTModelAdmin

# Register your models here.
# admin.site.register(Product)
# admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        # "categories",
        # "description",
        "price",
        "image",
        "stock",
        "created_at",
        "updated_at",
    )

    list_filter = ("name", "categories", "price")

    search_fields = ("name", "categories", "price")

    ordering = ("-price", "name")

    fields = ("name", "description", "price", "categories", "stock")

    readonly_fields = ("created_at", "updated_at")

    list_editable = ("price", "stock", "image")

    list_display_links = ("name",)

    list_per_page = 20


def mark_as_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


def mark_as_deactive(modeladmin, request, queryset):
    queryset.update(is_active=False)


mark_as_deactive.short_description = "Mark selected products as deactive"
mark_as_active.short_description = "Mark selected products as active"


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = (
        "name",
        "parent",
        # "description",
        "is_active",
        "created_at",
        "updated_at",
    )
    list_filter = ("is_active", "name", "parent")

    search_fields = ("name", "parent")

    ordering = ("parent", "name")

    list_editable = ("parent", "is_active")

    list_display_links = ("name",)

    readonly_fields = ("created_at", "updated_at")

    fields = ("name", "parent", "description", "is_active")

    list_per_page = 20

    actions = [mark_as_active, mark_as_deactive]


#     name = models.CharField(max_length=255)
#     parent = TreeForeignKey(
#         "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
#     )
#     description = models.TextField(blank=True, null=True)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
