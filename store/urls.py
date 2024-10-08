# urls.py in the 'store' app or your main urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductListView, name="product_list"),
    path("products/<int:pk>/", views.ProductDetailView, name="product_detail"),
]
