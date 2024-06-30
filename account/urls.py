from django.urls import path
from .views import CustomLoginView, welcome

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('welcome/', welcome, name='welcome'),
]
