from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'user', 'end_at', 'plated_end_at']
    search_fields = ['id']
