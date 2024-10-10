# urls.py in the 'store' app or your main urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.AllCategoryView, name="categorieslist"),
    path("products/", views.AllProductsView, name="productslist"),
]
