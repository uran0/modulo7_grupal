from django.contrib import admin
from .models import CustomerInfo, Order

# Register your models here.
admin.site.register(CustomerInfo)
admin.site.register(Order)