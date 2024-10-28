from django.shortcuts import render, get_object_or_404
from .models import Order, UserCart

# Create your views here.


def OrderSummaryView(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, "order/order_summary.html", {"orders": orders})


def OrderDetailView(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, "order/order_detail.html", {"order": order})


def usercart(request):
    cartitems = UserCart.objects.select_related("user").prefetch_related("product")

    return render(request, "order/usercart.html", {"cartitems": cartitems})
