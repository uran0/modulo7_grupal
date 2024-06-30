from django.db import models
from django.conf import settings
# Create your models here.


class CustomerInfo(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.user.username}'s Info"

class Order(models.Model):
    customer = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = (
        ('pending', 'Pending'),
        ('shipped', 'Shippoed'),
        ('delivered', 'Delivered'),
    )
    status = models.CharField(max_length=50, choices=order_status)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.customer.user.username}"
