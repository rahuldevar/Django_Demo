from django.forms import forms

from newproject.theapp.models import Book
from newproject.theapp.views import BookForm


class BookForm(forms.ModelForm):
    class Meta:
        model = BookForm
        fields = '__all__'