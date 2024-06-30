from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'account/login.html'

@login_required
def welcome(request):
    user = request.user
    if user.user_type == 'admin':
        return render(request, 'admin_welcome.html', {'user': user})
    elif user.user_type == 'staff':
        return render(request, 'staff_welcome.html', {'user': user})
    else:
        return render(request, 'user_welcome.html', {'user': user})