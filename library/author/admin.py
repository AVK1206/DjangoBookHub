from django.contrib import admin

from .models import Author


class AuthorInline(admin.TabularInline):
    model = Author.books.through


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'patronymic']
    search_fields = ['id', 'name', 'surname', 'patronymic']
    fieldsets = (
        (None, {
            'fields': ('name', 'surname', 'patronymic')
        }),
    )
    inlines = (AuthorInline, )
