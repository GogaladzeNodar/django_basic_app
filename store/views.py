from django.shortcuts import render, get_list_or_404
from .models import Product


# Create your views here.
def ProductListView(request):
    products = Product.objects.all()
    return render(request, "store/product_list.html", {"products": products})


def ProductDetailView(request, pk):
    product = get_list_or_404(Product, pk=pk)
    return render(request, "store/product_detail.html", {"product": product})
