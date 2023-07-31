from django.db import transaction
from django.shortcuts import render, redirect
from order.forms import OrderForm
from order.models import Order
from rest_framework import viewsets
from .serializers import OrderSerializer


class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all()


def order_main_page(request):
    return render(request, 'order/order_main.html')


def visitor_orders(request):
    if request.user.role == 1:
        orders = Order.objects.select_related('user').all()
    else:
        orders = Order.objects.select_related('user').filter(user=request.user)
    context = {'orders': orders}
    return render(request, 'order/visitor_orders.html', context)


def create_order_view(request):
    if request.user.role == 1:
        return render(request, 'order/order_main.html', {'error': 'Only a user has ability to create an order!'})

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data['book']
            plated_end_at = form.cleaned_data['plated_end_at']

            if book.count == 0:
                return render(request, 'order/order_create.html',
                              {'form': form, 'error': 'The book is not available for ordering.'})
            try:
                with transaction.atomic():
                    order = Order(book=book, plated_end_at=plated_end_at, user=request.user)
                    order.save()
                    book.save()
            except Exception:
                return render(request, 'order/order_create.html',
                              {'form': form, 'error': 'An error occurred while creating the order.'})
            return redirect('order-main')
    else:
        form = OrderForm()

    context = {'form': form}
    return render(request, 'order/order_create.html', context)
