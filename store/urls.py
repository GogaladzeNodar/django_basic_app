# urls.py in the 'store' app or your main urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.AllCategoryView, name="categorieslist"),
    path("products/", views.AllProductsView, name="productslist"),
    path("category/", views.category_list, name="category_list"),
    path(
        "category/<int:category_id>/products/",
        views.category_products,
        name="category_products",
    ),
    path("product/<int:product_id>/", views.product_detail, name="product_detail"),
]
