from django import forms
from book.models import Book


class OrderForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.all())
    plated_end_at = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
