from django.db import models
from django.contrib.auth.models import User
from DjangoForever import settings
from store.models import Product


# Create your models here.


class Order(models.Model):
    class OrderStatus(models.TextChoices):
        PENDING = "PE", "Pending"
        COMPLETED = "CO", "Completed"
        CANCELED = "CA", "Canceled"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=2, choices=OrderStatus.choices, default=OrderStatus.PENDING
    )

    def __str__(self):
        return f"{self.user} order {self.product}"


"""
order app ში(ჯანგოს პირველ დავალებაში იყო შექმნა მოთხოვნილი) შექმენით ახალი მოდელი UserCart 
და დააკავშირეთ თქვენს მიერ შექმნილ იუზერის მოდელთან O2O კავშირით(OneToOne), კალათის სხვა ველები ამ ეტაპზე საჭირო არ არის.
"""


class UserCart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
