from django.urls import path
from .views import order_history, update_order_status, product_catalog, place_order

urlpatterns = [
    path('order-history/', order_history, name='order-history'),
    path('update-order-status/<int:order_id>/', update_order_status, name='update-order-status'),
    path('catalog/',product_catalog, name='product_catalog'),
    path('place_order/', place_order, name='place_order'),
]
