from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'middle_name', 'email',
                    'role', 'is_active']
    search_fields = ['first_name', 'last_name', 'email', 'role']
