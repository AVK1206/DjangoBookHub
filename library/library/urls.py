"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from book import views as bk_v
from authentication.views import CustomUserView
from author.views import AuthorView
from book.views import BookView
from order.views import OrderView

if settings.DEBUG:
    import debug_toolbar

router = DefaultRouter()
router.register(r'user', CustomUserView, basename='user')
router.register(r'author', AuthorView, basename='author')
router.register(r'book', BookView, basename='book')
router.register(r'order', OrderView, basename='order')

order_urls = [
    path('', OrderView.as_view({'get': 'list', 'post': 'create'}),
         name='order-list'),
    path('<int:pk>/', OrderView.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='order-detail'),
]

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/user/<int:user_pk>/order/', include(order_urls)),
    path('', bk_v.run_welcome_page_view, name='welcome'),
    path('book/', include('book.urls')),
    path('user/', include('authentication.urls')),
    path('order/', include('order.urls')),
    path('author/', include('author.urls'))
]
