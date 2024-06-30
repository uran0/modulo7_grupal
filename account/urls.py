from django.urls import path
from .views import CustomLoginView, welcome, register

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('welcome/', welcome, name='welcome'),
    path('register/', register, name='register'),
]
