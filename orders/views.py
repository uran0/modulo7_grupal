from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, CustomerInfo
from mgmt.models import Product
from .forms import OrderForm, DeliveryForm
from django.contrib.auth.decorators import login_required

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

@login_required
def product_catalog(request):
    products = Product.objects.all()
    return render(request, 'orders/catalog.html', {'products': products})

@login_required
def place_order(request):
    if request.method == 'POST':
        delivery_form = DeliveryForm(request.POST)
        order_form = OrderForm(request.POST)
        if delivery_form.is_valid() and order_form.is_valid():
            order = order_form.save(commit=False)
            order.customer = CustomerInfo.objects.get(user=request.user)
            order.total_amount = sum([product.price for product in order.products.all()])
            return redirect('order_success')
    else:
        delivery_form = DeliveryForm()
        order_form = OrderForm()
    
    return render(request, 'orders/place_order.html', {'delivery_form': delivery_form, 'order_form': order_form})
