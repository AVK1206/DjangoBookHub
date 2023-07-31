from django.contrib import admin
from .models import Book


class AuthorInline(admin.TabularInline):
    model = Book.authors.through


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'count']
    list_filter = ['id', 'name', 'authors__name']
    search_fields = ['name', 'description', 'count']

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(self.readonly_fields)
        if obj:  # Only apply readonly to existing objects
            readonly_fields += ['name', 'description', 'year_of_publication']
        return readonly_fields

    fieldsets = (
        ('General Information', {
            'fields': ('name', 'description', 'year_of_publication'),
        }),
        ('Release Information', {
            'fields': ('release_date', 'count')
        }),
    )
    inlines = (AuthorInline, )
