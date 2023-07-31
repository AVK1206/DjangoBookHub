from django import forms
from .models import Book
from author.models import Author


class BookForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    class Meta:
        model = Book
        fields = ['name', 'description', 'count', 'authors']


class BookSearchNameForm(forms.Form):
    book_name = forms.CharField(label='Book Name', max_length=128)


class BookCountForm(forms.Form):
    book_count = forms.IntegerField(label='Book Count')


class BookSearchAuthorForm(forms.Form):
    book_author = forms.CharField(label='Book Author', max_length=128)
