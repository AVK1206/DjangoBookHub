from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm, BookSearchNameForm, BookCountForm, BookSearchAuthorForm
from rest_framework import viewsets
from .serializers import BookSerializer


class BookView(viewsets.ModelViewSet):
    queryset = Book.get_all()
    serializer_class = BookSerializer


def create_book_view(request):
    if request.user.role == 0:
        return render(request, 'book/book_create.html', {'error': 'You must be an admin to add the book!'})

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            authors = form.cleaned_data.get('authors')
            if authors:
                for author in authors:
                    book.authors.add(author)

            book.save()

            return redirect('book-create')
    else:
        form = BookForm()

    return render(request, 'book/book_create.html', {'form': form})


def book_main_page(request):
    return render(request, 'book/book_main.html')


def run_welcome_page_view(request):
    return render(request, 'welcome/welcome.html')


def book_list_view(request):
    books = Book.get_all()
    context = {'books': books}
    return render(request, 'book/book_list.html', context)


def get_books_by_name(request):
    if request.method == 'POST':
        form = BookSearchNameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['book_name']
            books = Book.objects.filter(name__icontains=name)
            context = {'books': books, 'search_name': name}
            return render(request, 'book/get_books_by_name.html', context)
    else:
        form = BookSearchNameForm()

    context = {'form': form}
    return render(request, 'book/book_search.html', context)


def filter_books_by_count(request):
    form = BookCountForm()
    if request.method == "POST":
        form = BookCountForm(request.POST)
        if form.is_valid():
            count = form.cleaned_data['book_count']
            books = Book.objects.filter(count=count)
            context = {'form': form, 'books': books}
            return render(request, 'book/filter_books_by_count.html', context)

    context = {'form': form}
    return render(request, 'book/book_search_by_count.html', context)


def get_books_by_author(request):
    if request.method == 'POST':
        form = BookSearchAuthorForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['book_author']
            books = Book.objects.filter(authors__name__icontains=author)
            context = {'books': books, 'search_author': author}
            return render(request, 'book/get_books_by_author.html', context)
    else:
        form = BookSearchAuthorForm()

    context = {'form': form}
    return render(request, 'book/book_search_author.html', context)
