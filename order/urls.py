from django.urls import path
from . import views

urlpatterns = [
    path("orders/", views.OrderSummaryView, name="order_summary"),
    path("orders/<int:pk>/", views.OrderDetailView, name="order_detail"),
]
