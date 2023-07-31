from django.urls import path
from . import views as auth

urlpatterns = [
    path('main/', auth.main_view, name='main'),
    path('registrate/', auth.register, name='user-registrate'),
    path('login/', auth.login_view, name='user-login'),
    path('logout/', auth.logout_view, name='user-logout')

]
