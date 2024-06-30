from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('user', 'user'),
    )
    user_type=models.CharField(max_length=10, choices=USER_TYPES, default='user')
    
    @property
    def customer_info(self):
        return self.customerinfo if hasattr(self, 'customerinfo') else None

    def __str__(self):
        return self.username