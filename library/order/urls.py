from django.urls import path
from . import views as or_v

urlpatterns = [
    path('main-page/', or_v.order_main_page, name='order-main'),
    path('create/', or_v.create_order_view, name='order-create'),
    path('orders/', or_v.visitor_orders, name='visitor-orders'),
]
