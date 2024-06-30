from django.urls import path
from .views import order_history, update_order_status

urlpatterns = [
    path('order-history/', order_history, name='order-history'),
    path('update-order-status/<int:order_id>/', update_order_status, name='update-order-status'),
]
