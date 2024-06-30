from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'status', 'total_amount']
        widgets = {
            'status': forms.Select(choices=Order.order_status),
            'total_amount': forms.HiddenInput(),
        }


class DeliveryForm(forms.Form):
    address = forms.CharField(max_length=255, label='Dirección de entrega')
    phone = forms.CharField(max_length=20, label='Teléfono de contacto')
    payment_method = forms.ChoiceField(choices=[
        ('credit_card', 'Tarjeta de crédito'),
        ('debit_card', 'Tarjeta de débito'),
        ('paypal', 'Paypal'),
    ], label='Forma de pago')