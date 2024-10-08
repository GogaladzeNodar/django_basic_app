from django.shortcuts import render, get_object_or_404
from .models import Order

# Create your views here.


def OrderSummaryView(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, "order/order_summary.html", {"orders": orders})


def OrderDetailView(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, "order/order_detail.html", {"order": order})
