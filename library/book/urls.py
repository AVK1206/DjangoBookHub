from django.urls import path
from . import views as bk_v

urlpatterns = [
    path('main-page/', bk_v.book_main_page, name='book-main'),
    path('create/', bk_v.create_book_view, name='book-create'),
    path('list/', bk_v.book_list_view, name='book-list'),
    path('get-books-by-name/', bk_v.get_books_by_name, name='get-books-by-name'),
    path('get-books-by-author/', bk_v.get_books_by_author, name='get-books-by-author'),
    path('get-books-by-count/', bk_v.filter_books_by_count, name='filter-books-by-count'),
]
