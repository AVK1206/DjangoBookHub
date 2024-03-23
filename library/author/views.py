import logging

from django.shortcuts import render, redirect

from .forms import AuthorForm
from .models import Author
from rest_framework import viewsets
from .serializers import AuthorSerializer

logger = logging.getLogger('dev')


class AuthorView(viewsets.ModelViewSet):
    queryset = Author.get_all()
    serializer_class = AuthorSerializer


def authors_list_view(request):
    if request.user.role == 0:
        logger.warning(
            'Unauthorized access: Only admin is able to see all authors!')
        return render(request, 'author/author_main.html',
                      {'error': 'Only admin is able to see all authors!'})
    authors = Author.get_all()
    context = {'authors': authors}
    return render(request, 'author/author_list.html', context)


def author_main_page(request):
    return render(request, 'author/author_main.html')


def create_author_view(request):
    if request.user.role == 0:
        logger.warning(
            'Unauthorized access: Only admin is able to see all authors!')
        return render(request, 'author/author_main.html',
                      {'error': 'Only admin is able to add an author!'})
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author-list')
    else:
        form = AuthorForm()
    return render(request, 'author/author_create.html', {'form': form})
