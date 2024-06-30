from django.shortcuts import render, redirect, get_object_or_404
from .models import Order

# Create your views here.

def order_history(request):
    orders = Order.objects.all()
    return render(request, 'orders/orders_history.html', {'orders': orders})

def update_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        order.status = new_status
        order.save()
        return redirect('order-history')
    return render(request, 'orders/update_order_status.html', {'order': order})