from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth import login

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('welcome')

@login_required
def welcome(request):
    user = request.user
    if user.user_type == 'admin':
        return render(request, 'admin_welcome.html', {'user': user})
    elif user.user_type == 'staff':
        return render(request, 'staff_welcome.html', {'user': user})
    else:
        return render(request, 'user_welcome.html', {'user': user})
    
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/register.html', {'form': form})