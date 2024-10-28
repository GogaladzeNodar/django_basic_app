from django.contrib import admin
from .models import Order, UserCart

# Register your models here.
# admin.site.register(Order)
admin.site.register(UserCart)


def mark_as_completed(modeladmin, request, queryset):
    updated = queryset.update(status=Order.OrderStatus.COMPLETED)


def mark_as_canceled(modeladmin, request, queryset):
    updated = queryset.update(status=Order.OrderStatus.CANCELED)


mark_as_completed.short_description = "Mark selected orders as Completed"
mark_as_canceled.short_description = "Mark selected orders as Canceled"


@admin.register(Order)
class Orderadmin(admin.ModelAdmin):
    list_display = ("user", "product", "quantity", "order_date", "status")

    search_fields = ("user", "product", "order_date", "status")

    ordering = ("user", "product")

    list_editable = (
        "product",
        "quantity",
        "status",
    )  #  "order_date", ავტომატურად გენერირებადი ველები list_editable-ში არ უნდა იყოს

    list_per_page = 20

    actions = [mark_as_completed, mark_as_canceled]


# class Order(models.Model):
#     class OrderStatus(models.TextChoices):
#         PENDING = "PE", "Pending"
#         COMPLETED = "CO", "Completed"
#         CANCELED = "CA", "Canceled"

#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     order_date = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(
#         max_length=2, choices=OrderStatus.choices, default=OrderStatus.PENDING
#     )

#     def __str__(self):
#         return f"{self.user} order {self.product}"
