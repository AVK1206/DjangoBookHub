import logging

from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from rest_framework import viewsets

from .forms import CustomUserForm
from .models import CustomUser
from .serializers import CustomUserSerializer

logger = logging.getLogger('dev')


class CustomUserView(viewsets.ModelViewSet):
    queryset = CustomUser.get_all()
    serializer_class = CustomUserSerializer


def register(request):
    form = CustomUserForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            password = request.POST.get('password')
            new_user = form.save()
            new_user.set_password(password)
            new_user.save()
            logger.info('New user registered: %s', new_user.email)
            return redirect('user-login')
    return render(request, 'authentication/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            user.last_login = timezone.now()
            user.is_active = True
            user.save()
            logger.info('User logged in: %s', user.email)
            return redirect('main')
        else:
            logger.warning('Failed login attempt for email: %s', email)
            return render(request, 'authentication/login.html',
                          {'error': 'You must input valid credentials!'})

    return render(request, 'authentication/login.html')


def logout_view(request):
    request.user.is_active = False
    request.user.save()
    logout(request)
    logger.info('User logged out: %s', request.user.email)
    return redirect('user-login')


def main_view(request):
    return render(request, 'main/main.html')
