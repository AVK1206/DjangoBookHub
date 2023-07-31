from django.urls import path
from . import views as ath_v

urlpatterns = [
    path('list/', ath_v.authors_list_view, name='author-list'),
    path('main-page/', ath_v.author_main_page, name='author-main'),
    path('create/', ath_v.create_author_view, name='author-create')
]
